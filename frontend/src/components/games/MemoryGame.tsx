import { useState, useCallback } from "react";
import type { LevelQuestion } from "../../types/game";
import { objectToEmoji } from "../../utils/constants";
import { motion } from "framer-motion";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

interface Card {
  id: number;
  value: string;
  flipped: boolean;
  matched: boolean;
}

/** Memory matching: flip cards to find pairs. */
export default function MemoryGame({ question, onCorrect, onWrong }: Props) {
  const pairs = question.pairs ?? [];

  const [cards] = useState<Card[]>(() => {
    const all: Card[] = [];
    pairs.forEach((pair, pi) => {
      pair.forEach((val, vi) => {
        all.push({ id: pi * 2 + vi, value: val, flipped: false, matched: false });
      });
    });
    // Shuffle
    for (let i = all.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [all[i], all[j]] = [all[j], all[i]];
    }
    return all;
  });

  const [flippedIds, setFlippedIds] = useState<number[]>([]);
  const [matchedValues, setMatchedValues] = useState<Set<string>>(new Set());
  const [busy, setBusy] = useState(false);

  const handleFlip = useCallback((card: Card) => {
    if (busy || card.flipped || card.matched || flippedIds.length >= 2) return;

    const newFlipped = [...flippedIds, card.id];
    setFlippedIds(newFlipped);

    if (newFlipped.length === 2) {
      setBusy(true);
      const [a, b] = newFlipped.map((id) => cards.find((c) => c.id === id)!);

      if (a.value === b.value) {
        // Match!
        setTimeout(() => {
          const newMatched = new Set(matchedValues);
          newMatched.add(a.value);
          setMatchedValues(newMatched);
          setFlippedIds([]);
          setBusy(false);

          if (newMatched.size === pairs.length) {
            setTimeout(onCorrect, 500);
          }
        }, 600);
      } else {
        // No match
        onWrong();
        setTimeout(() => {
          setFlippedIds([]);
          setBusy(false);
        }, 1500);
      }
    }
  }, [busy, flippedIds, cards, matchedValues, pairs.length, onCorrect, onWrong]);

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: `repeat(${Math.min(4, cards.length)}, 72px)`,
          gap: 10,
          justifyContent: "center",
        }}
      >
        {cards.map((card) => {
          const isFlipped = flippedIds.includes(card.id);
          const isMatched = matchedValues.has(card.value);
          const showFace = isFlipped || isMatched;

          return (
            <motion.div
              key={card.id}
              whileTap={showFace ? {} : { scale: 0.9 }}
              animate={isMatched ? { scale: [1, 1.1, 1] } : {}}
              onClick={() => handleFlip(card)}
              style={{
                width: 72,
                height: 72,
                borderRadius: 14,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: showFace ? 36 : 28,
                background: isMatched
                  ? "#C8E6C9"
                  : showFace
                  ? "white"
                  : "linear-gradient(135deg, #FFD700, #FFA000)",
                border: "2px solid #ddd",
                cursor: showFace ? "default" : "pointer",
                boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
              }}
            >
              {showFace ? objectToEmoji(card.value) : "?"}
            </motion.div>
          );
        })}
      </div>
    </>
  );
}
