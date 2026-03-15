import { useCallback, useEffect, useRef } from "react";

/**
 * Uses the Web Speech API to read text aloud.
 *
 * Mobile fixes:
 * - Cancel + small delay before speaking to avoid overlap/stutter
 * - Queue only one utterance at a time
 * - Handles the Chrome mobile bug where speechSynthesis pauses after ~15s
 */
export function useSpeech() {
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

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

    // Small delay after cancel to let the engine reset (fixes mobile stutter)
    timerRef.current = setTimeout(() => {
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = lang;
      utter.rate = 0.85;
      utter.pitch = 1.1;
      utter.volume = 1;

      // Chrome mobile bug: speech can pause. Resume workaround.
      utter.onstart = () => {
        // Keep-alive timer for long utterances on Chrome mobile
        const keepAlive = setInterval(() => {
          if (!synth.speaking) {
            clearInterval(keepAlive);
          } else {
            synth.pause();
            synth.resume();
          }
        }, 5000);
        utter.onend = () => clearInterval(keepAlive);
        utter.onerror = () => clearInterval(keepAlive);
      };

      synth.speak(utter);
    }, 80);
  }, []);

  const stop = useCallback(() => {
    if (timerRef.current) clearTimeout(timerRef.current);
    window.speechSynthesis?.cancel();
  }, []);

  return { speak, stop };
}
