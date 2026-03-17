import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import { objectToEmoji } from "../../utils/constants";
import { motion } from "framer-motion";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Comparison game: two groups side by side, pick which has more. */
export default function ComparisonGame({ question, onCorrect, onWrong }: Props) {
  const [selected, setSelected] = useState<string | null>(null);

  // Split visual_objects by "|"
  const sepIdx = question.visual_objects.indexOf("|");
  const leftGroup = sepIdx >= 0 ? question.visual_objects.slice(0, sepIdx) : question.visual_objects;
  const rightGroup = sepIdx >= 0 ? question.visual_objects.slice(sepIdx + 1) : [];

  const handlePick = (side: "left" | "right") => {
    if (selected) return;
    setSelected(side);
    if (side === correctSide) {
      setTimeout(onCorrect, 800);
    } else {
      onWrong();
      setTimeout(() => setSelected(null), 1500);
    }
  };

  const leftCount = leftGroup.length;
  const rightCount = rightGroup.length;
  const correctSide = leftCount >= rightCount ? "left" : "right";

  const groupStyle = (side: "left" | "right"): React.CSSProperties => ({
    display: "flex",
    flexWrap: "wrap",
    gap: 6,
    justifyContent: "center",
    padding: 16,
    borderRadius: 20,
    border: selected === side
      ? `4px solid ${side === correctSide ? "#4CAF50" : "#FF5252"}`
      : "4px solid transparent",
    background: "rgba(255,255,255,0.6)",
    cursor: selected ? "default" : "pointer",
    minWidth: 120,
    minHeight: 80,
  });

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>
      <div style={{ display: "flex", gap: 24, alignItems: "center" }}>
        <motion.div
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          style={groupStyle("left")}
          onClick={() => handlePick("left")}
        >
          {leftGroup.map((obj, i) => (
            <span key={i} style={{ fontSize: 40 }}>{objectToEmoji(obj)}</span>
          ))}
        </motion.div>

        <span style={{ fontSize: 28, fontWeight: "bold", color: "#666" }}>VS</span>

        <motion.div
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          style={groupStyle("right")}
          onClick={() => handlePick("right")}
        >
          {rightGroup.map((obj, i) => (
            <span key={i} style={{ fontSize: 40 }}>{objectToEmoji(obj)}</span>
          ))}
        </motion.div>
      </div>
    </>
  );
}
