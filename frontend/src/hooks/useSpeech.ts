import { useCallback, useEffect, useRef } from "react";

/**
 * Uses the Web Speech API to read text aloud.
 * Automatically reads the question when a level loads.
 */
export function useSpeech() {
  const utterRef = useRef<SpeechSynthesisUtterance | null>(null);

  // Cancel any ongoing speech when unmounting
  useEffect(() => {
    return () => {
      window.speechSynthesis?.cancel();
    };
  }, []);

  const speak = useCallback((text: string, lang = "en-US") => {
    if (!window.speechSynthesis) return;

    // Cancel previous utterance
    window.speechSynthesis.cancel();

    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = lang;
    utter.rate = 0.85; // Slightly slower for children
    utter.pitch = 1.1; // Slightly higher pitch, friendlier
    utter.volume = 1;

    utterRef.current = utter;
    window.speechSynthesis.speak(utter);
  }, []);

  const stop = useCallback(() => {
    window.speechSynthesis?.cancel();
  }, []);

  return { speak, stop };
}
