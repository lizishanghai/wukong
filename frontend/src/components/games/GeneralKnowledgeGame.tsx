import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import OptionButton from "../ui/OptionButton";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** General knowledge game: text-based trivia (days, seasons, directions, etc.). */
export default function GeneralKnowledgeGame({ question, onCorrect, onWrong }: Props) {
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<Record<number, boolean>>({});

  const handlePick = (opt: string | number, idx: number) => {
    if (selected !== null) return;
    const isCorrect = String(opt) === String(question.correct_answer);
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
      <div
        style={{
          fontSize: 48,
          textAlign: "center",
          margin: "16px 0",
        }}
      >
        💡
      </div>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333", margin: "12px 16px" }}>
        {question.text}
      </h3>
      <div style={{ display: "flex", gap: 12, flexWrap: "wrap", justifyContent: "center", marginTop: 16 }}>
        {question.options.map((opt, i) => (
          <OptionButton
            key={i}
            label={opt}
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
