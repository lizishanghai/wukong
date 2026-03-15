import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import { objectToEmoji } from "../../utils/constants";
import { motion } from "framer-motion";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Find the differences between two scenes. */
export default function FindDifferenceGame({ question, onCorrect, onWrong }: Props) {
  const sceneA = question.scene_a ?? [];
  const sceneB = question.scene_b ?? [];
  const diffs = question.differences ?? [];
  const [found, setFound] = useState<Set<number>>(new Set());

  // Find indices where scenes differ
  const diffIndices = sceneA
    .map((item, i) => (item !== sceneB[i] ? i : -1))
    .filter((i) => i >= 0);

  const handleTap = (idx: number, scene: "a" | "b") => {
    if (diffIndices.includes(idx) && !found.has(idx)) {
      const newFound = new Set(found);
      newFound.add(idx);
      setFound(newFound);

      if (newFound.size === diffIndices.length) {
        setTimeout(onCorrect, 600);
      }
    } else if (!found.has(idx)) {
      onWrong();
    }
  };

  const renderScene = (items: string[], scene: "a" | "b") => (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: `repeat(${Math.min(5, items.length)}, 56px)`,
        gap: 6,
        padding: 12,
        background: "rgba(255,255,255,0.7)",
        borderRadius: 16,
      }}
    >
      {items.map((item, i) => {
        const isDiff = diffIndices.includes(i);
        const isFound = found.has(i);
        return (
          <motion.div
            key={i}
            whileTap={{ scale: 0.9 }}
            animate={isFound ? { scale: [1, 1.2, 1] } : {}}
            onClick={() => handleTap(i, scene)}
            style={{
              width: 56,
              height: 56,
              borderRadius: 10,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 32,
              cursor: "pointer",
              background: isFound ? "#C8E6C9" : "white",
              border: isFound ? "3px solid #4CAF50" : "2px solid #eee",
            }}
          >
            {objectToEmoji(item)}
          </motion.div>
        );
      })}
    </div>
  );

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text || `Find ${diffIndices.length} differences!`}
      </h3>
      <p style={{ fontSize: 16, color: "#666" }}>
        Found: {found.size} / {diffIndices.length}
      </p>
      <div style={{ display: "flex", gap: 20, flexWrap: "wrap", justifyContent: "center" }}>
        {renderScene(sceneA, "a")}
        {renderScene(sceneB, "b")}
      </div>
    </>
  );
}
