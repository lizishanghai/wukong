import { create } from "zustand";

interface GameState {
  /** Sound effects enabled */
  soundOn: boolean;
  toggleSound: () => void;

  /** Current attempt count for active level */
  attempts: number;
  resetAttempts: () => void;
  addAttempt: () => void;

  /** Show celebration overlay */
  celebrating: boolean;
  setCelebrating: (v: boolean) => void;
}

export const useGameStore = create<GameState>((set) => ({
  soundOn: true,
  toggleSound: () => set((s) => ({ soundOn: !s.soundOn })),

  attempts: 0,
  resetAttempts: () => set({ attempts: 0 }),
  addAttempt: () => set((s) => ({ attempts: s.attempts + 1 })),

  celebrating: false,
  setCelebrating: (v) => set({ celebrating: v }),
}));
