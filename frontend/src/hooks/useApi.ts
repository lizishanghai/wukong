/**
 * Standalone data hooks — no backend required.
 * Levels are bundled from JSON, progress is stored in localStorage.
 */
import { useCallback, useEffect, useMemo, useState } from "react";
import type { Level, WorldInfo, PlayerProgress, Costume, World, Story, StoryProgress } from "../types/game";
import allLevels from "../data/levels.json";
import allStories from "../data/stories.json";

// ---------------------------------------------------------------------------
// Static data
// ---------------------------------------------------------------------------

const WORLDS_META: Record<string, Omit<WorldInfo, "id" | "level_count">> = {
  flower_fruit_mountain: {
    name: "Flower Fruit Mountain",
    name_cn: "花果山",
    description: "Wukong's home! Learn to count with monkey friends.",
    theme_color: "#4CAF50",
    characters: ["wukong", "monkey_elder", "baby_monkeys"],
    unlock_requirement: null,
  },
  dragon_palace: {
    name: "Dragon Palace",
    name_cn: "龙宫",
    description: "Dive underwater to find patterns and treasures!",
    theme_color: "#2196F3",
    characters: ["wukong", "dragon_king", "shrimp_soldiers"],
    unlock_requirement: "flower_fruit_mountain",
  },
  heaven_palace: {
    name: "Heaven Palace",
    name_cn: "天宫",
    description: "Jump on clouds and learn to add numbers!",
    theme_color: "#FFC107",
    characters: ["wukong", "jade_emperor", "cloud_fairies"],
    unlock_requirement: "dragon_palace",
  },
  white_bone_cave: {
    name: "White Bone Cave",
    name_cn: "白骨洞",
    description: "Spot the disguises and sort the tricks!",
    theme_color: "#9C27B0",
    characters: ["wukong", "tang_monk", "white_bone_spirit"],
    unlock_requirement: "heaven_palace",
  },
  flaming_mountain: {
    name: "Flaming Mountain",
    name_cn: "火焰山",
    description: "Fan away the flames with subtraction!",
    theme_color: "#FF5722",
    characters: ["wukong", "princess_iron_fan", "fire_sprites"],
    unlock_requirement: "white_bone_cave",
  },
  journey_road: {
    name: "Journey Road",
    name_cn: "西行之路",
    description: "The final journey! Use everything you learned!",
    theme_color: "#FF9800",
    characters: ["wukong", "tang_monk", "bajie", "sha_wujing"],
    unlock_requirement: "flaming_mountain",
  },
};

const WORLD_ORDER: World[] = [
  "flower_fruit_mountain",
  "dragon_palace",
  "heaven_palace",
  "white_bone_cave",
  "flaming_mountain",
  "journey_road",
];

const levels = allLevels as Level[];
const stories = allStories as Story[];

// ---------------------------------------------------------------------------
// localStorage progress helpers
// ---------------------------------------------------------------------------

const PROGRESS_KEY = "wukong_progress";

function defaultProgress(): PlayerProgress {
  return {
    player_id: "default",
    total_peaches: 0,
    current_world: "flower_fruit_mountain",
    current_costume: "default",
    unlocked_costumes: ["default"],
    levels: {},
    stories: {},
    streak_days: 0,
  };
}

function loadProgress(): PlayerProgress {
  try {
    const raw = localStorage.getItem(PROGRESS_KEY);
    if (raw) return JSON.parse(raw);
  } catch { /* ignore */ }
  return defaultProgress();
}

function saveProgress(p: PlayerProgress) {
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(p));
}

// ---------------------------------------------------------------------------
// Daily challenge: pick 3 random levels seeded by date
// ---------------------------------------------------------------------------

function getDailyLevels(): Level[] {
  const today = new Date().toISOString().slice(0, 10);
  let seed = 0;
  for (let i = 0; i < today.length; i++) seed += today.charCodeAt(i);

  const picked: Level[] = [];
  const pool = [...levels];
  for (let i = 0; i < 3 && pool.length > 0; i++) {
    const idx = (seed * (i + 7)) % pool.length;
    const level = { ...pool[idx], id: `daily_${i + 1}` };
    picked.push(level);
    pool.splice(idx, 1);
  }
  return picked;
}

// ---------------------------------------------------------------------------
// Hooks (same interface as the API version)
// ---------------------------------------------------------------------------

export function useWorlds() {
  const [worlds] = useState<WorldInfo[]>(() =>
    WORLD_ORDER.map((id) => {
      const meta = WORLDS_META[id]!;
      return {
        ...meta,
        id,
        level_count: levels.filter((lv) => lv.world === id).length,
      };
    })
  );
  return { worlds, loading: false };
}

export function useWorldLevels(worldId: string) {
  const worldLevels = useMemo(
    () => levels.filter((lv) => lv.world === worldId),
    [worldId]
  );
  return { levels: worldLevels, loading: false };
}

export function useLevel(levelId: string) {
  const level = useMemo(
    () => levels.find((lv) => lv.id === levelId) ?? null,
    [levelId]
  );
  return { level, loading: false };
}

export function useDailyChallenge() {
  const [daily] = useState<Level[]>(() => getDailyLevels());
  return { levels: daily, loading: false };
}

export function useProgress() {
  const [progress, setProgress] = useState<PlayerProgress>(loadProgress);

  const refresh = useCallback(() => {
    setProgress(loadProgress());
  }, []);

  const completeLevel = useCallback(
    async (levelId: string, stars: number, peaches: number) => {
      const p = loadProgress();
      const existing = p.levels[levelId] ?? {
        level_id: levelId,
        completed: false,
        stars: 0,
        attempts: 0,
      };
      existing.completed = true;
      existing.attempts += 1;
      existing.stars = Math.max(existing.stars, stars);
      p.levels[levelId] = existing;
      p.total_peaches += peaches;
      saveProgress(p);
      setProgress({ ...p });
      return p;
    },
    []
  );

  return { progress, refresh, completeLevel };
}

// ---------------------------------------------------------------------------
// Story hooks
// ---------------------------------------------------------------------------

export function useStories() {
  return { stories, loading: false };
}

export function useStory(storyId: string) {
  const story = useMemo(
    () => stories.find((s) => s.id === storyId) ?? null,
    [storyId]
  );
  return { story, loading: false };
}

export function useStoryProgress() {
  const [progress, setProgress] = useState<PlayerProgress>(loadProgress);

  const completeScene = useCallback(
    (storyId: string, sceneIndex: number, totalScenes: number) => {
      const p = loadProgress();
      if (!p.stories) p.stories = {};
      const existing: StoryProgress = p.stories[storyId] ?? {
        completed: false,
        scenes_completed: 0,
        stars: 0,
        attempts: 0,
      };
      existing.scenes_completed = Math.max(existing.scenes_completed, sceneIndex + 1);
      p.stories[storyId] = existing;
      saveProgress(p);
      setProgress({ ...p });
    },
    []
  );

  const completeStory = useCallback(
    (storyId: string, stars: number, peaches: number) => {
      const p = loadProgress();
      if (!p.stories) p.stories = {};
      const existing: StoryProgress = p.stories[storyId] ?? {
        completed: false,
        scenes_completed: 0,
        stars: 0,
        attempts: 0,
      };
      existing.completed = true;
      existing.attempts += 1;
      existing.stars = Math.max(existing.stars, stars);
      p.stories[storyId] = existing;
      p.total_peaches += peaches;
      saveProgress(p);
      setProgress({ ...p });
    },
    []
  );

  return { progress, completeScene, completeStory };
}

export function useCostumes() {
  const COSTUMES: Costume[] = [
    { id: "default", name: "Classic Wukong", cost: 0, owned: true },
    { id: "golden_armor", name: "Golden Armor", cost: 30, owned: false },
    { id: "cloud_rider", name: "Cloud Rider", cost: 30, owned: false },
    { id: "peach_farmer", name: "Peach Farmer", cost: 20, owned: false },
    { id: "dragon_warrior", name: "Dragon Warrior", cost: 50, owned: false },
    { id: "star_cape", name: "Star Cape", cost: 40, owned: false },
    { id: "fire_king", name: "Fire King", cost: 50, owned: false },
    { id: "journey_master", name: "Journey Master", cost: 100, owned: false },
  ];

  const [costumes] = useState(() => {
    const p = loadProgress();
    return COSTUMES.map((c) => ({
      ...c,
      owned: p.unlocked_costumes.includes(c.id),
    }));
  });
  return { costumes };
}
