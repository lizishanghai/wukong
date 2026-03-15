import { motion } from "framer-motion";
import { useState } from "react";

interface Props {
  label: string | number;
  onClick: () => void;
  correct?: boolean | null; // null = not answered yet, true/false = result
  disabled?: boolean;
  size?: "normal" | "large";
}

export default function OptionButton({ label, onClick, correct, disabled, size = "normal" }: Props) {
  const bg =
    correct === true ? "#4CAF50" :
    correct === false ? "#FF5252" :
    "linear-gradient(135deg, #FFD700, #FFA000)";

  const px = size === "large" ? 32 : 20;
  const py = size === "large" ? 20 : 14;
  const fs = size === "large" ? 28 : 22;

  return (
    <motion.button
      whileHover={disabled ? {} : { scale: 1.08 }}
      whileTap={disabled ? {} : { scale: 0.92 }}
      animate={
        correct === false
          ? { x: [0, -8, 8, -8, 8, 0] }
          : correct === true
          ? { scale: [1, 1.2, 1] }
          : {}
      }
      transition={{ duration: 0.4 }}
      onClick={disabled ? undefined : onClick}
      style={{
        padding: `${py}px ${px}px`,
        fontSize: fs,
        fontWeight: "bold",
        background: bg,
        color: correct != null ? "white" : "#5D4037",
        border: "3px solid rgba(255,255,255,0.5)",
        borderRadius: 20,
        cursor: disabled ? "default" : "pointer",
        minWidth: 80,
        boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
        opacity: disabled && correct == null ? 0.5 : 1,
      }}
    >
      {label}
    </motion.button>
  );
}
