import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import { objectToEmoji } from "../../utils/constants";
import OptionButton from "../ui/OptionButton";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Shape pattern game: complete a colored shape sequence. */
export default function ShapePatternGame({ question, onCorrect, onWrong }: Props) {
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<Record<number, boolean>>({});

  const seq = question.sequence ?? [];

  const handlePick = (opt: string | number, idx: number) => {
    if (selected !== null) return;
    const isCorrect = String(opt) === String(question.correct_answer);
    setResult({ [idx]: isCorrect });
    setSelected(idx);

    if (isCorrect) {
      setTimeout(onCorrect, 800);
    } else {
      onWrong();
      setTimeout(() => {
        setSelected(null);
        setResult({});
      }, 1500);
    }
  };

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>

      {/* Shape sequence */}
      <div
        style={{
          display: "flex",
          gap: 10,
          justifyContent: "center",
          flexWrap: "wrap",
          margin: "16px 0",
        }}
      >
        {seq.map((item, i) => {
          const isBlank = item === "?";
          return (
            <div
              key={i}
              style={{
                width: 56,
                height: 56,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: isBlank ? 28 : 36,
                background: isBlank ? "#FFF3E0" : "#F5F5F5",
                border: isBlank ? "3px dashed #FF9800" : "2px solid #E0E0E0",
                borderRadius: 12,
                fontWeight: "bold",
                color: isBlank ? "#FF9800" : undefined,
              }}
            >
              {isBlank ? "?" : objectToEmoji(String(item))}
            </div>
          );
        })}
      </div>

      {/* Options */}
      <div style={{ display: "flex", gap: 16, flexWrap: "wrap", justifyContent: "center" }}>
        {question.options.map((opt, i) => (
          <OptionButton
            key={i}
            label={objectToEmoji(String(opt))}
            size="large"
            correct={result[i] ?? null}
            disabled={selected !== null}
            onClick={() => handlePick(opt, i)}
          />
        ))}
      </div>
    </>
  );
}
