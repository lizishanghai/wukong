import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import { resolveAssetPath } from "../../utils/constants";
import OptionButton from "../ui/OptionButton";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Make Ten game: find the number that completes 10. */
export default function MakeTenGame({ question, onCorrect, onWrong }: Props) {
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<Record<number, boolean>>({});

  const handlePick = (opt: string | number, idx: number) => {
    if (selected !== null) return;
    const isCorrect = Number(opt) === Number(question.correct_answer);
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
      <h3 style={{ fontSize: 26, textAlign: "center", color: "#333", margin: "16px 0" }}>
        {question.text}
      </h3>
      {question.image ? (
        <div style={{ textAlign: "center", margin: "16px 0" }}>
          <img
            src={resolveAssetPath(question.image)}
            alt=""
            style={{ width: 80, height: 80, objectFit: "contain" }}
          />
        </div>
      ) : (
        <div
          style={{
            fontSize: 48,
            textAlign: "center",
            margin: "24px 0",
            fontWeight: "bold",
            color: "#E65100",
          }}
        >
          🔟
        </div>
      )}
      <div style={{ display: "flex", gap: 16, flexWrap: "wrap", justifyContent: "center" }}>
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
