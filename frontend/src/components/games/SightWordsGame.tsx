import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import ObjectDisplay from "../ui/ObjectDisplay";
import OptionButton from "../ui/OptionButton";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Sight words game: see an image/emoji, pick the matching English word. */
export default function SightWordsGame({ question, onCorrect, onWrong }: Props) {
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<Record<number, boolean>>({});

  const handlePick = (opt: string | number, idx: number) => {
    if (selected !== null) return;
    const isCorrect = String(opt).toLowerCase() === String(question.correct_answer).toLowerCase();
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
      {question.visual_objects.length > 0 && (
        <ObjectDisplay objects={question.visual_objects} />
      )}
      <div style={{ display: "flex", gap: 12, flexWrap: "wrap", justifyContent: "center" }}>
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
