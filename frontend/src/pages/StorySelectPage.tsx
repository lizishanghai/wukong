import { useMemo } from "react";
import { useNavigate } from "react-router-dom";
import { useStories, useStoryProgress } from "../hooks/useApi";
import { WORLD_COLORS } from "../utils/constants";
import type { World } from "../types/game";
import { motion } from "framer-motion";
import type { Story, StoryProgress as StoryProgressType } from "../types/game";

const WORLD_NAMES: Record<string, string> = {
  flower_fruit_mountain: "🌺 Flower Fruit Mountain",
  dragon_palace: "🐉 Dragon Palace",
  heaven_palace: "☁️ Heaven Palace",
  white_bone_cave: "🦴 White Bone Cave",
  flaming_mountain: "🔥 Flaming Mountain",
  journey_road: "🛤️ Journey Road",
};

const WORLD_ORDER = [
  "flower_fruit_mountain",
  "dragon_palace",
  "heaven_palace",
  "white_bone_cave",
  "flaming_mountain",
  "journey_road",
];

export default function StorySelectPage() {
  const navigate = useNavigate();
  const { stories } = useStories();
  const { progress } = useStoryProgress();

  const grouped = useMemo(() => {
    const groups: Record<string, Story[]> = {};
    for (const s of stories) {
      if (!groups[s.world]) groups[s.world] = [];
      groups[s.world].push(s);
    }
    // Sort stories within each world by tribulation number
    for (const w of Object.keys(groups)) {
      groups[w].sort((a, b) => a.tribulation_number - b.tribulation_number);
    }
    return groups;
  }, [stories]);

  // Determine which stories are unlocked (sequential)
  const completedStories = progress?.stories ?? {};
  const completedSet = new Set(
    Object.entries(completedStories)
      .filter(([, sp]) => sp.completed)
      .map(([id]) => id)
  );

  // First uncompleted story is the next one to play; all before it are unlocked
  let nextStoryFound = false;
  const unlockedSet = new Set<string>();
  for (const world of WORLD_ORDER) {
    for (const story of grouped[world] ?? []) {
      if (completedSet.has(story.id)) {
        unlockedSet.add(story.id);
      } else if (!nextStoryFound) {
        unlockedSet.add(story.id);
        nextStoryFound = true;
      }
    }
  }

  return (
    <div
      style={{
        width: "100%",
        minHeight: "100%",
        background: "linear-gradient(180deg, #1a0533 0%, #2d1b69 50%, #1a0533 100%)",
        padding: "20px 16px 40px",
        overflowY: "auto",
      }}
    >
      {/* Header */}
      <div style={{ display: "flex", alignItems: "center", marginBottom: 20 }}>
        <button
          onClick={() => navigate("/")}
          style={{ background: "none", border: "none", fontSize: 20, cursor: "pointer", color: "white", padding: "4px 8px" }}
        >
          ← Home
        </button>
        <h1 style={{ flex: 1, textAlign: "center", color: "white", fontSize: 24, margin: 0 }}>
          📖 Story Adventure
        </h1>
        <div style={{ width: 60 }} />
      </div>

      <p style={{ textAlign: "center", color: "rgba(255,255,255,0.7)", fontSize: 14, marginBottom: 24 }}>
        81 Tribulations of Journey to the West
      </p>

      {/* Story groups by world */}
      {WORLD_ORDER.map((worldId) => {
        const worldStories = grouped[worldId];
        if (!worldStories?.length) return null;
        const color = WORLD_COLORS[worldId as World] ?? "#4CAF50";

        return (
          <div key={worldId} style={{ marginBottom: 28 }}>
            <h2 style={{ color, fontSize: 18, marginBottom: 12, paddingLeft: 4 }}>
              {WORLD_NAMES[worldId]}
            </h2>
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(150px, 1fr))",
                gap: 12,
              }}
            >
              {worldStories.map((story) => {
                const sp = completedStories[story.id];
                const unlocked = unlockedSet.has(story.id);
                const completed = completedSet.has(story.id);

                return (
                  <StoryCard
                    key={story.id}
                    story={story}
                    progress={sp}
                    unlocked={unlocked}
                    completed={completed}
                    color={color}
                    onClick={() => unlocked && navigate(`/story/${story.id}`)}
                  />
                );
              })}
            </div>
          </div>
        );
      })}
    </div>
  );
}

function StoryCard({
  story,
  progress,
  unlocked,
  completed,
  color,
  onClick,
}: {
  story: Story;
  progress?: StoryProgressType;
  unlocked: boolean;
  completed: boolean;
  color: string;
  onClick: () => void;
}) {
  return (
    <motion.div
      whileHover={unlocked ? { scale: 1.05 } : undefined}
      whileTap={unlocked ? { scale: 0.95 } : undefined}
      onClick={onClick}
      style={{
        padding: "14px 12px",
        background: unlocked
          ? completed
            ? `linear-gradient(135deg, ${color}33, ${color}55)`
            : "rgba(255,255,255,0.1)"
          : "rgba(255,255,255,0.03)",
        borderRadius: 14,
        cursor: unlocked ? "pointer" : "default",
        border: `2px solid ${unlocked ? color + "88" : "rgba(255,255,255,0.1)"}`,
        opacity: unlocked ? 1 : 0.4,
        textAlign: "center",
      }}
    >
      <div style={{ fontSize: 13, color: "rgba(255,255,255,0.5)", marginBottom: 4 }}>
        #{story.tribulation_number}
      </div>
      <div style={{ fontSize: 14, fontWeight: "bold", color: "white", marginBottom: 4 }}>
        {unlocked ? story.title : "🔒"}
      </div>
      <div style={{ fontSize: 12, color: "rgba(255,255,255,0.6)" }}>
        {story.title_cn}
      </div>
      {completed && (
        <div style={{ marginTop: 6, fontSize: 12, color: "#4CAF50" }}>
          ⭐ Complete
        </div>
      )}
      {!completed && progress && progress.scenes_completed > 0 && (
        <div style={{ marginTop: 6, fontSize: 12, color: "#FFD700" }}>
          {progress.scenes_completed}/{story.scenes.length} scenes
        </div>
      )}
    </motion.div>
  );
}
