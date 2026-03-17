import { useState, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import type { StoryScene, Level } from "../../types/game";
import NarrationOverlay from "./NarrationOverlay";
import GameDispatcher from "../games/GameDispatcher";
import FeedbackToast from "../ui/FeedbackToast";
import { resolveAssetPath } from "../../utils/constants";

interface Props {
  scene: StoryScene;
  storyWorld: string;
  difficulty: number;
  onSceneComplete: () => void;
  speak: (text: string, lang?: string) => void;
}

type Phase = "narration" | "game";

export default function StorySceneView({ scene, storyWorld, difficulty, onSceneComplete, speak }: Props) {
  const [phase, setPhase] = useState<Phase>("narration");
  const [feedback, setFeedback] = useState<"correct" | "wrong" | null>(null);
  const [attempts, setAttempts] = useState(0);
  const [showHint, setShowHint] = useState(false);

  const handleNarrationComplete = useCallback(() => {
    setPhase("game");
    // Read the question after a brief pause
    setTimeout(() => speak(scene.question.text), 400);
  }, [scene.question.text, speak]);

  const handleCorrect = useCallback(() => {
    setFeedback("correct");
    speak("正确! 太棒了!", "zh-CN");
    setTimeout(() => {
      setFeedback(null);
      onSceneComplete();
    }, 1200);
  }, [onSceneComplete, speak]);

  const handleWrong = useCallback(() => {
    setFeedback("wrong");
    speak("再试一次!", "zh-CN");
    setAttempts((a) => a + 1);
    if (attempts >= 1) setShowHint(true);
    setTimeout(() => setFeedback(null), 1500);
  }, [attempts, speak]);

  // Construct synthetic Level for GameDispatcher
  const syntheticLevel: Level = {
    id: scene.scene_id,
    world: storyWorld as Level["world"],
    level_number: 0,
    name: "",
    story_intro: scene.narration,
    character: "wukong",
    game_type: scene.game_type,
    difficulty,
    question: scene.question,
    reward: { peaches: 0, animation: "celebrate", dialogue: "", character: "wukong" },
    hints: scene.hints,
    tags: [],
  };

  const bgImage = resolveAssetPath(scene.background_image);

  return (
    <div style={{ width: "100%", height: "100%", position: "relative" }}>
      <AnimatePresence mode="wait">
        {phase === "narration" ? (
          <NarrationOverlay
            key="narration"
            narration={scene.narration}
            backgroundImage={bgImage}
            onComplete={handleNarrationComplete}
            speak={speak}
          />
        ) : (
          <motion.div
            key="game"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            style={{
              width: "100%",
              height: "100%",
              display: "flex",
              flexDirection: "column",
              backgroundImage: bgImage ? `url(${bgImage})` : undefined,
              backgroundSize: "cover",
              backgroundPosition: "center",
              backgroundColor: "#f5f0ff",
            }}
          >
            {/* Semi-transparent game area overlay */}
            <div
              style={{
                flex: 1,
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                padding: 16,
                gap: 16,
                background: "rgba(255,255,255,0.85)",
                margin: "10px",
                borderRadius: 16,
              }}
            >
              <GameDispatcher
                key={scene.scene_id}
                level={syntheticLevel}
                onCorrect={handleCorrect}
                onWrong={handleWrong}
              />

              {showHint && scene.hints.length > 0 && (
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  style={{
                    padding: "10px 20px",
                    background: "rgba(255,243,224,0.95)",
                    borderRadius: 12,
                    fontSize: 16,
                    color: "#E65100",
                    border: "2px solid #FFB74D",
                    maxWidth: 300,
                    textAlign: "center",
                  }}
                >
                  💡 {scene.hints[0]}
                </motion.div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <FeedbackToast type={feedback} />
    </div>
  );
}
