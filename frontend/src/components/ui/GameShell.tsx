import { type ReactNode } from "react";
import type { Level } from "../../types/game";
import { WORLD_COLORS, WORLD_EMOJIS } from "../../utils/constants";

interface Props {
  level: Level;
  peaches: number;
  onBack: () => void;
  children: ReactNode;
}

/** Wraps every game screen with a top bar, story intro, and consistent styling. */
export default function GameShell({ level, peaches, onBack, children }: Props) {
  const bg = WORLD_COLORS[level.world] ?? "#4CAF50";

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        background: `linear-gradient(135deg, ${bg}22, ${bg}44)`,
        position: "relative",
        overflow: "hidden",
      }}
    >
      {/* Top bar */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "12px 20px",
          background: "rgba(255,255,255,0.85)",
          borderBottom: `3px solid ${bg}`,
        }}
      >
        <button onClick={onBack} style={backBtnStyle}>
          ← Back
        </button>
        <span style={{ fontSize: 18, fontWeight: "bold" }}>
          {WORLD_EMOJIS[level.world]} {level.name}
        </span>
        <span style={{ fontSize: 18 }}>🍑 {peaches}</span>
      </div>

      {/* Story intro */}
      <div
        style={{
          padding: "14px 24px",
          background: "rgba(255,255,255,0.7)",
          margin: "10px 16px 0",
          borderRadius: 16,
          fontSize: 17,
          lineHeight: 1.5,
          textAlign: "center",
        }}
      >
        <strong>{level.character === "wukong" ? "🐵" : level.character === "bajie" ? "🐷" : level.character === "sha_wujing" ? "🧔" : "🧙"}</strong>{" "}
        "{level.story_intro}"
      </div>

      {/* Game area */}
      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: "16px",
          gap: 16,
        }}
      >
        {children}
      </div>
    </div>
  );
}

const backBtnStyle: React.CSSProperties = {
  background: "none",
  border: "none",
  fontSize: 20,
  cursor: "pointer",
  padding: "4px 8px",
};
