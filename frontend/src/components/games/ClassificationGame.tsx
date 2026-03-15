import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import { objectToEmoji } from "../../utils/constants";
import { motion } from "framer-motion";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Classification game: drag/tap objects into correct categories. */
export default function ClassificationGame({ question, onCorrect, onWrong }: Props) {
  const groups = question.groups ?? {};
  const correctAnswer = question.correct_answer as unknown as Record<string, string[]>;
  const categories = Object.keys(groups);
  const items = [...question.visual_objects];

  const [remaining, setRemaining] = useState(items);
  const [selectedItem, setSelectedItem] = useState<string | null>(null);
  const [sorted, setSorted] = useState<Record<string, string[]>>(() =>
    Object.fromEntries(categories.map((c) => [c, []]))
  );

  const handleItemClick = (item: string) => {
    setSelectedItem(item);
  };

  const handleCategoryClick = (category: string) => {
    if (!selectedItem) return;

    // Check if this is the right category
    const correctCat = Object.entries(correctAnswer).find(([, vals]) =>
      vals.includes(selectedItem)
    );

    if (correctCat && correctCat[0] === category) {
      const newSorted = { ...sorted, [category]: [...sorted[category], selectedItem] };
      const newRemaining = remaining.filter((_, i) => i !== remaining.indexOf(selectedItem));
      setSorted(newSorted);
      setRemaining(newRemaining);
      setSelectedItem(null);

      if (newRemaining.length === 0) {
        setTimeout(onCorrect, 600);
      }
    } else {
      onWrong();
      setSelectedItem(null);
    }
  };

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>

      {/* Items to sort */}
      <div style={{ display: "flex", gap: 10, flexWrap: "wrap", justifyContent: "center" }}>
        {remaining.map((item, i) => (
          <motion.div
            key={`${item}-${i}`}
            whileTap={{ scale: 0.9 }}
            onClick={() => handleItemClick(item)}
            style={{
              width: 60,
              height: 60,
              borderRadius: 14,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 36,
              background: selectedItem === item ? "#FFD700" : "white",
              border: selectedItem === item ? "3px solid #FFA000" : "2px solid #ddd",
              cursor: "pointer",
              boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
            }}
          >
            {objectToEmoji(item)}
          </motion.div>
        ))}
      </div>

      {/* Category bins */}
      <div style={{ display: "flex", gap: 16, justifyContent: "center" }}>
        {categories.map((cat) => (
          <motion.div
            key={cat}
            whileHover={{ scale: 1.03 }}
            onClick={() => handleCategoryClick(cat)}
            style={{
              minWidth: 120,
              minHeight: 100,
              borderRadius: 16,
              padding: 12,
              background: selectedItem ? "rgba(255,215,0,0.2)" : "rgba(255,255,255,0.7)",
              border: "3px dashed #999",
              cursor: selectedItem ? "pointer" : "default",
              textAlign: "center",
            }}
          >
            <div style={{ fontSize: 16, fontWeight: "bold", marginBottom: 8, color: "#555" }}>
              {cat}
            </div>
            <div style={{ display: "flex", gap: 4, flexWrap: "wrap", justifyContent: "center" }}>
              {sorted[cat].map((item, i) => (
                <span key={i} style={{ fontSize: 28 }}>{objectToEmoji(item)}</span>
              ))}
            </div>
          </motion.div>
        ))}
      </div>
    </>
  );
}
