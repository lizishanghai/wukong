export type World =
  | "flower_fruit_mountain"
  | "dragon_palace"
  | "heaven_palace"
  | "white_bone_cave"
  | "flaming_mountain"
  | "journey_road";

export type GameType =
  | "counting"
  | "addition"
  | "subtraction"
  | "comparison"
  | "ordering"
  | "pattern"
  | "classification"
  | "memory"
  | "find_difference"
  | "maze"
  | "clock_reading"
  | "shape_pattern";

export interface LevelQuestion {
  text: string;
  visual_objects: string[];
  options: (string | number)[];
  correct_answer: string | number | number[];
  pairs?: string[][];
  grid?: number[][];
  start?: number[];
  end?: number[];
  sequence?: (string | number)[];
  groups?: Record<string, string[]>;
  scene_a?: string[];
  scene_b?: string[];
  differences?: string[];
  clock_time?: { hour: number; minute: number };
}

export interface LevelReward {
  peaches: number;
  animation: string;
  dialogue: string;
  character: string;
}

export interface Level {
  id: string;
  world: World;
  level_number: number;
  name: string;
  story_intro: string;
  character: string;
  game_type: GameType;
  difficulty: number;
  question: LevelQuestion;
  reward: LevelReward;
  hints: string[];
  tags: string[];
}

export interface WorldInfo {
  id: World;
  name: string;
  name_cn: string;
  description: string;
  theme_color: string;
  characters: string[];
  level_count: number;
  unlock_requirement: string | null;
}

export interface PlayerProgress {
  player_id: string;
  total_peaches: number;
  current_world: World;
  current_costume: string;
  unlocked_costumes: string[];
  levels: Record<string, { completed: boolean; stars: number; attempts: number }>;
  streak_days: number;
}

export interface Costume {
  id: string;
  name: string;
  cost: number;
  owned: boolean;
}
