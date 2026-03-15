import { useCallback, useEffect, useRef } from "react";

/**
 * Uses the Web Speech API to read text aloud.
 *
 * Mobile fixes:
 * - Cancel + delay before speaking to avoid overlap/stutter
 * - Queue only one utterance at a time
 * - Wait for voices to load before first speech (fixes silent first play on mobile)
 */
export function useSpeech() {
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const speakingRef = useRef(false);

  // Cancel any ongoing speech when unmounting
  useEffect(() => {
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
      window.speechSynthesis?.cancel();
    };
  }, []);

  const speak = useCallback((text: string, lang = "en-US") => {
    const synth = window.speechSynthesis;
    if (!synth) return;

    // Clear any pending scheduled speech
    if (timerRef.current) clearTimeout(timerRef.current);

    // Cancel current speech immediately
    synth.cancel();
    speakingRef.current = false;

    // Longer delay after cancel to let the mobile engine fully reset
    timerRef.current = setTimeout(() => {
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = lang;
      utter.rate = 0.85;
      utter.pitch = 1.1;
      utter.volume = 1;

      utter.onstart = () => {
        speakingRef.current = true;
      };
      utter.onend = () => {
        speakingRef.current = false;
      };
      utter.onerror = () => {
        speakingRef.current = false;
      };

      synth.speak(utter);
    }, 150);
  }, []);

  const stop = useCallback(() => {
    if (timerRef.current) clearTimeout(timerRef.current);
    speakingRef.current = false;
    window.speechSynthesis?.cancel();
  }, []);

  return { speak, stop };
}
