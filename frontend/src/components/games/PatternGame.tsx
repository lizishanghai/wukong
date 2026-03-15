import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import { objectToEmoji } from "../../utils/constants";
import OptionButton from "../ui/OptionButton";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Pattern completion: show a sequence with a "?" and pick what fills it. */
export default function PatternGame({ question, onCorrect, onWrong }: Props) {
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<Record<number, boolean>>({});
  const sequence = question.sequence ?? [];

  const handlePick = (opt: string | number, idx: number) => {
    if (selected !== null) return;
    const isCorrect = opt === question.correct_answer;
    setResult({ [idx]: isCorrect });
    setSelected(idx);
    if (isCorrect) {
      setTimeout(onCorrect, 800);
    } else {
      onWrong();
      setTimeout(() => { setSelected(null); setResult({}); }, 1500);
    }
  };

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>

      {/* Sequence display */}
      <div style={{ display: "flex", gap: 10, flexWrap: "wrap", justifyContent: "center", padding: 12 }}>
        {sequence.map((item, i) => (
          <div
            key={i}
            style={{
              width: 60,
              height: 60,
              borderRadius: 12,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: item === "?" ? 32 : 36,
              background: item === "?" ? "#FFD700" : "rgba(255,255,255,0.8)",
              border: item === "?" ? "3px dashed #FF9800" : "2px solid #ddd",
              fontWeight: "bold",
              color: item === "?" ? "#FF9800" : "#333",
            }}
          >
            {item === "?" ? "?" : objectToEmoji(String(item))}
          </div>
        ))}
      </div>

      {/* Options */}
      <div style={{ display: "flex", gap: 16, flexWrap: "wrap", justifyContent: "center" }}>
        {question.options.map((opt, i) => (
          <OptionButton
            key={i}
            label={typeof opt === "string" ? objectToEmoji(opt) : opt}
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
