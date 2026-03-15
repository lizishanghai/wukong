import { useState, useCallback } from "react";
import type { LevelQuestion } from "../../types/game";
import { motion } from "framer-motion";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Simple grid maze: tap arrow buttons to move Wukong to the goal. */
export default function MazeGame({ question, onCorrect, onWrong }: Props) {
  const grid = question.grid ?? [[0]];
  const start = question.start ?? [0, 0];
  const end = question.end ?? [grid.length - 1, (grid[0]?.length ?? 1) - 1];

  const [pos, setPos] = useState(start);
  const rows = grid.length;
  const cols = grid[0]?.length ?? 1;

  const move = useCallback(
    (dr: number, dc: number) => {
      const nr = pos[0] + dr;
      const nc = pos[1] + dc;

      if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) return;
      if (grid[nr][nc] === 1) {
        onWrong();
        return;
      }

      setPos([nr, nc]);

      if (nr === end[0] && nc === end[1]) {
        setTimeout(onCorrect, 400);
      }
    },
    [pos, grid, rows, cols, end, onCorrect, onWrong]
  );

  const cellSize = Math.min(60, Math.floor(300 / Math.max(rows, cols)));

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text || "Guide Wukong through the maze!"}
      </h3>

      {/* Grid */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: `repeat(${cols}, ${cellSize}px)`,
          gap: 3,
          justifyContent: "center",
        }}
      >
        {grid.map((row, r) =>
          row.map((cell, c) => {
            const isPlayer = r === pos[0] && c === pos[1];
            const isEnd = r === end[0] && c === end[1];
            const isWall = cell === 1;

            return (
              <motion.div
                key={`${r}-${c}`}
                animate={isPlayer ? { scale: [1, 1.1, 1] } : {}}
                transition={{ repeat: isPlayer ? Infinity : 0, duration: 1 }}
                style={{
                  width: cellSize,
                  height: cellSize,
                  borderRadius: 8,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: cellSize * 0.55,
                  background: isWall
                    ? "#795548"
                    : isEnd
                    ? "#FFD700"
                    : isPlayer
                    ? "#4CAF50"
                    : "#E8F5E9",
                  border: "1px solid #ddd",
                }}
              >
                {isPlayer ? "🐵" : isEnd ? "⭐" : isWall ? "🪨" : ""}
              </motion.div>
            );
          })
        )}
      </div>

      {/* Arrow controls */}
      <div style={{ display: "grid", gridTemplateColumns: "60px 60px 60px", gap: 6, justifyContent: "center" }}>
        <div />
        <ArrowBtn label="↑" onClick={() => move(-1, 0)} />
        <div />
        <ArrowBtn label="←" onClick={() => move(0, -1)} />
        <ArrowBtn label="↓" onClick={() => move(1, 0)} />
        <ArrowBtn label="→" onClick={() => move(0, 1)} />
      </div>
    </>
  );
}

function ArrowBtn({ label, onClick }: { label: string; onClick: () => void }) {
  return (
    <motion.button
      whileTap={{ scale: 0.85 }}
      onClick={onClick}
      style={{
        width: 60,
        height: 60,
        borderRadius: 14,
        fontSize: 28,
        background: "linear-gradient(135deg, #FFD700, #FFA000)",
        color: "#5D4037",
        border: "none",
        cursor: "pointer",
        boxShadow: "0 3px 8px rgba(0,0,0,0.15)",
        fontWeight: "bold",
      }}
    >
      {label}
    </motion.button>
  );
}
