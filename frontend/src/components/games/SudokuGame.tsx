import { useState, useCallback } from "react";
import { motion } from "framer-motion";
import type { LevelQuestion } from "../../types/game";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** 4×4 Mini Sudoku: tap empty cells to cycle 1-4, then check. */
export default function SudokuGame({ question, onCorrect, onWrong }: Props) {
  const puzzle = question.grid ?? [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]];
  const solution = question.sudoku_solution ?? puzzle;
  const size = puzzle.length;

  const [board, setBoard] = useState<number[][]>(() =>
    puzzle.map((row) => [...row])
  );
  const [errors, setErrors] = useState<boolean[][]>(() =>
    Array.from({ length: size }, () => Array(size).fill(false))
  );
  const [checked, setChecked] = useState(false);

  const isLocked = useCallback(
    (r: number, c: number) => puzzle[r][c] !== 0,
    [puzzle]
  );

  const handleCellTap = (r: number, c: number) => {
    if (isLocked(r, c) || checked) return;
    setBoard((prev) => {
      const next = prev.map((row) => [...row]);
      next[r][c] = (next[r][c] % size) + 1; // cycle 1→2→3→4→1
      return next;
    });
    setErrors(Array.from({ length: size }, () => Array(size).fill(false)));
  };

  const handleCheck = () => {
    // Check if all cells are filled
    const allFilled = board.every((row) => row.every((cell) => cell !== 0));
    if (!allFilled) return;

    // Compare with solution
    const newErrors = board.map((row, r) =>
      row.map((cell, c) => !isLocked(r, c) && cell !== solution[r][c])
    );
    const hasErrors = newErrors.some((row) => row.some(Boolean));

    setErrors(newErrors);
    setChecked(true);

    if (!hasErrors) {
      setTimeout(onCorrect, 800);
    } else {
      onWrong();
      setTimeout(() => {
        setChecked(false);
        setErrors(Array.from({ length: size }, () => Array(size).fill(false)));
      }, 1500);
    }
  };

  const cellSize = 60;

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>

      {/* Grid */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: `repeat(${size}, ${cellSize}px)`,
          gap: 3,
          justifyContent: "center",
          margin: "16px auto",
          padding: 8,
          background: "#5D4037",
          borderRadius: 12,
          width: "fit-content",
        }}
      >
        {board.flatMap((row, r) =>
          row.map((cell, c) => {
            const locked = isLocked(r, c);
            const hasError = errors[r][c];
            const bg = hasError
              ? "#FFCDD2"
              : locked
              ? "#D7CCC8"
              : cell === 0
              ? "#FFFDE7"
              : "#E8F5E9";

            return (
              <motion.div
                key={`${r}-${c}`}
                whileTap={locked ? {} : { scale: 0.9 }}
                onClick={() => handleCellTap(r, c)}
                style={{
                  width: cellSize,
                  height: cellSize,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: cell === 0 ? 18 : 28,
                  fontWeight: "bold",
                  background: bg,
                  borderRadius: 8,
                  cursor: locked ? "default" : "pointer",
                  color: locked ? "#5D4037" : hasError ? "#D32F2F" : "#1B5E20",
                  border:
                    (r === 2 && c < size ? "2px solid #5D4037" : "") ||
                    undefined,
                  // 2x2 box borders
                  borderTop: r % 2 === 0 && r > 0 ? "3px solid #3E2723" : undefined,
                  borderLeft: c % 2 === 0 && c > 0 ? "3px solid #3E2723" : undefined,
                }}
              >
                {cell === 0 ? "·" : cell}
              </motion.div>
            );
          })
        )}
      </div>

      {/* Check button */}
      <div style={{ textAlign: "center", marginTop: 16 }}>
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={handleCheck}
          style={{
            padding: "14px 40px",
            fontSize: 22,
            fontWeight: "bold",
            background: "linear-gradient(135deg, #4CAF50, #2E7D32)",
            color: "white",
            border: "none",
            borderRadius: 16,
            cursor: "pointer",
            boxShadow: "0 4px 12px rgba(0,0,0,0.2)",
          }}
        >
          ✅ Check
        </motion.button>
      </div>
    </>
  );
}
