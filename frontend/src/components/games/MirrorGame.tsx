import { useState } from "react";
import { motion } from "framer-motion";
import type { LevelQuestion } from "../../types/game";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

function MiniGrid({
  grid,
  cellSize = 36,
  highlight,
}: {
  grid: number[][];
  cellSize?: number;
  highlight?: "correct" | "wrong" | null;
}) {
  const size = grid.length;
  const borderColor =
    highlight === "correct"
      ? "#4CAF50"
      : highlight === "wrong"
      ? "#FF5252"
      : "#BDBDBD";

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: `repeat(${size}, ${cellSize}px)`,
        gap: 2,
        padding: 4,
        border: `3px solid ${borderColor}`,
        borderRadius: 10,
        background: "#F5F5F5",
      }}
    >
      {grid.flatMap((row, r) =>
        row.map((cell, c) => (
          <div
            key={`${r}-${c}`}
            style={{
              width: cellSize,
              height: cellSize,
              borderRadius: 4,
              background: cell === 1 ? "#FFB300" : "#FFFFFF",
              border: "1px solid #E0E0E0",
            }}
          />
        ))
      )}
    </div>
  );
}

/** Mirror symmetry game: pick the correct mirror reflection. */
export default function MirrorGame({ question, onCorrect, onWrong }: Props) {
  const [selected, setSelected] = useState<number | null>(null);
  const [resultIdx, setResultIdx] = useState<number | null>(null);
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);

  const reference = question.grid ?? [[0, 1], [1, 0]];
  const candidates = question.mirror_options ?? [];
  const correctAnswer = Number(question.correct_answer);

  const handlePick = (idx: number) => {
    if (selected !== null) return;
    const correct = idx === correctAnswer;
    setSelected(idx);
    setResultIdx(idx);
    setIsCorrect(correct);

    if (correct) {
      setTimeout(onCorrect, 800);
    } else {
      onWrong();
      setTimeout(() => {
        setSelected(null);
        setResultIdx(null);
        setIsCorrect(null);
      }, 1500);
    }
  };

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>

      {/* Reference grid */}
      <div style={{ textAlign: "center", margin: "16px 0" }}>
        <div style={{ fontSize: 14, color: "#666", marginBottom: 8 }}>Original:</div>
        <div style={{ display: "inline-block" }}>
          <MiniGrid grid={reference} cellSize={40} />
        </div>
      </div>

      <div style={{ textAlign: "center", fontSize: 28, margin: "8px 0" }}>🪞</div>
      <div style={{ fontSize: 14, color: "#666", textAlign: "center", marginBottom: 12 }}>
        Pick the mirror image:
      </div>

      {/* Candidate grids */}
      <div
        style={{
          display: "flex",
          gap: 12,
          justifyContent: "center",
          flexWrap: "wrap",
        }}
      >
        {candidates.map((grid, i) => (
          <motion.div
            key={i}
            whileHover={selected === null ? { scale: 1.08 } : {}}
            whileTap={selected === null ? { scale: 0.95 } : {}}
            onClick={() => handlePick(i)}
            style={{
              cursor: selected === null ? "pointer" : "default",
              opacity: selected !== null && resultIdx !== i ? 0.5 : 1,
            }}
          >
            <MiniGrid
              grid={grid}
              cellSize={32}
              highlight={
                resultIdx === i
                  ? isCorrect
                    ? "correct"
                    : "wrong"
                  : null
              }
            />
          </motion.div>
        ))}
      </div>
    </>
  );
}
