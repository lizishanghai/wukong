import { useState, useEffect, useCallback } from "react";
import { motion } from "framer-motion";

interface Props {
  narration: string;
  backgroundImage: string;
  onComplete: () => void;
  speak: (text: string, lang?: string) => void;
}

export default function NarrationOverlay({ narration, backgroundImage, onComplete, speak }: Props) {
  const [displayText, setDisplayText] = useState("");
  const [done, setDone] = useState(false);

  // Typewriter effect
  useEffect(() => {
    setDisplayText("");
    setDone(false);
    let idx = 0;
    const interval = setInterval(() => {
      idx++;
      if (idx >= narration.length) {
        setDisplayText(narration);
        setDone(true);
        clearInterval(interval);
      } else {
        setDisplayText(narration.slice(0, idx));
      }
    }, 35);
    return () => clearInterval(interval);
  }, [narration]);

  // TTS reads narration
  useEffect(() => {
    const timer = setTimeout(() => speak(narration), 300);
    return () => clearTimeout(timer);
  }, [narration, speak]);

  const handleTap = useCallback(() => {
    if (!done) {
      // Skip to end
      setDisplayText(narration);
      setDone(true);
    } else {
      onComplete();
    }
  }, [done, narration, onComplete]);

  // Determine if image exists (fallback to gradient)
  const bgStyle: React.CSSProperties = {
    width: "100%",
    height: "100%",
    display: "flex",
    flexDirection: "column",
    justifyContent: "flex-end",
    position: "relative",
    cursor: "pointer",
    backgroundImage: backgroundImage
      ? `url(${backgroundImage})`
      : "linear-gradient(135deg, #667eea, #764ba2)",
    backgroundSize: "cover",
    backgroundPosition: "center",
    backgroundColor: "#2c1e5b",
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      style={bgStyle}
      onClick={handleTap}
    >
      {/* Dark overlay for readability */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: "linear-gradient(transparent 40%, rgba(0,0,0,0.7) 100%)",
        }}
      />

      {/* Narration text */}
      <div
        style={{
          position: "relative",
          padding: "20px 24px 24px",
          minHeight: 120,
        }}
      >
        <motion.p
          initial={{ y: 10 }}
          animate={{ y: 0 }}
          style={{
            fontSize: 20,
            lineHeight: 1.6,
            color: "white",
            textShadow: "1px 1px 4px rgba(0,0,0,0.8)",
            margin: 0,
          }}
        >
          {displayText}
          {!done && (
            <motion.span
              animate={{ opacity: [1, 0] }}
              transition={{ repeat: Infinity, duration: 0.8 }}
            >
              |
            </motion.span>
          )}
        </motion.p>

        {done && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            style={{
              marginTop: 12,
              fontSize: 14,
              color: "rgba(255,255,255,0.7)",
              textAlign: "center",
            }}
          >
            Tap to continue...
          </motion.div>
        )}
      </div>
    </motion.div>
  );
}
