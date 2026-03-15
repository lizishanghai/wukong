import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import { motion } from "framer-motion";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Ordering game: tap numbers in order (smallest to biggest). */
export default function OrderingGame({ question, onCorrect, onWrong }: Props) {
  const sequence = (question.sequence ?? []) as number[];
  const correctOrder = [...sequence].sort((a, b) => a - b);
  const [tapped, setTapped] = useState<number[]>([]);
  const [shaking, setShaking] = useState(false);

  const handleTap = (num: number) => {
    if (tapped.includes(num) || shaking) return;

    const nextExpected = correctOrder[tapped.length];
    if (num === nextExpected) {
      const newTapped = [...tapped, num];
      setTapped(newTapped);
      if (newTapped.length === correctOrder.length) {
        setTimeout(onCorrect, 600);
      }
    } else {
      setShaking(true);
      onWrong();
      setTimeout(() => {
        setTapped([]);
        setShaking(false);
      }, 1500);
    }
  };

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>

      {/* Progress: show what's been tapped */}
      <div style={{ display: "flex", gap: 8, justifyContent: "center", minHeight: 50 }}>
        {tapped.map((n, i) => (
          <motion.div
            key={i}
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            style={{
              width: 48,
              height: 48,
              borderRadius: 12,
              background: "#4CAF50",
              color: "white",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 24,
              fontWeight: "bold",
            }}
          >
            {n}
          </motion.div>
        ))}
        {Array.from({ length: correctOrder.length - tapped.length }).map((_, i) => (
          <div
            key={`empty-${i}`}
            style={{
              width: 48,
              height: 48,
              borderRadius: 12,
              border: "3px dashed #ccc",
            }}
          />
        ))}
      </div>

      {/* Number buttons (scrambled) */}
      <motion.div
        animate={shaking ? { x: [0, -10, 10, -10, 10, 0] } : {}}
        style={{ display: "flex", gap: 12, flexWrap: "wrap", justifyContent: "center" }}
      >
        {sequence.map((num) => {
          const used = tapped.includes(num);
          return (
            <motion.button
              key={num}
              whileHover={used ? {} : { scale: 1.1 }}
              whileTap={used ? {} : { scale: 0.9 }}
              onClick={() => handleTap(num)}
              style={{
                width: 64,
                height: 64,
                borderRadius: 16,
                fontSize: 28,
                fontWeight: "bold",
                background: used ? "#E0E0E0" : "linear-gradient(135deg, #FFD700, #FFA000)",
                color: used ? "#999" : "#5D4037",
                border: "none",
                cursor: used ? "default" : "pointer",
                boxShadow: used ? "none" : "0 4px 12px rgba(0,0,0,0.15)",
              }}
            >
              {num}
            </motion.button>
          );
        })}
      </motion.div>
    </>
  );
}
