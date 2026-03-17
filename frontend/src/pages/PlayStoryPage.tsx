import { useState, useCallback, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useStory, useStoryProgress } from "../hooks/useApi";
import { useSpeech } from "../hooks/useSpeech";
import { WORLD_COLORS } from "../utils/constants";
import StorySceneView from "../components/story/StorySceneView";
import StoryProgress from "../components/story/StoryProgress";
import Celebration from "../components/ui/Celebration";
import { motion } from "framer-motion";

export default function PlayStoryPage() {
  const { storyId } = useParams<{ storyId: string }>();
  const navigate = useNavigate();
  const { story } = useStory(storyId ?? "");
  const { completeScene, completeStory } = useStoryProgress();
  const { speak, stop } = useSpeech();

  const [sceneIdx, setSceneIdx] = useState(0);
  const [showCelebration, setShowCelebration] = useState(false);

  useEffect(() => {
    return () => stop();
  }, [stop]);

  const handleSceneComplete = useCallback(() => {
    if (!story) return;
    completeScene(story.id, sceneIdx, story.scenes.length);

    if (sceneIdx < story.scenes.length - 1) {
      setSceneIdx((i) => i + 1);
    } else {
      // Story complete
      completeStory(story.id, 3, story.reward.peaches);
      setShowCelebration(true);
    }
  }, [story, sceneIdx, completeScene, completeStory]);

  const handleContinue = useCallback(() => {
    setShowCelebration(false);
    if (!story) {
      navigate("/stories");
      return;
    }
    // Navigate to next story or back to story list
    const nextNum = story.tribulation_number + 1;
    const nextId = `story_${String(nextNum).padStart(2, "0")}`;
    if (nextNum <= 81) {
      navigate(`/story/${nextId}`);
    } else {
      navigate("/stories");
    }
  }, [story, navigate]);

  if (!story) {
    return (
      <div style={{ width: "100%", height: "100%", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 16 }}>
        <div style={{ fontSize: 48 }}>📖</div>
        <h2>Story not found</h2>
        <button
          onClick={() => navigate("/stories")}
          style={{ padding: "12px 30px", fontSize: 18, background: "#FFD700", border: "none", borderRadius: 20, cursor: "pointer" }}
        >
          Back to Stories
        </button>
      </div>
    );
  }

  const bg = WORLD_COLORS[story.world] ?? "#4CAF50";
  const scene = story.scenes[sceneIdx];

  return (
    <div style={{ width: "100%", height: "100%", display: "flex", flexDirection: "column", position: "relative" }}>
      {/* Top bar */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "10px 16px",
          background: "rgba(255,255,255,0.9)",
          borderBottom: `3px solid ${bg}`,
          zIndex: 10,
        }}
      >
        <button
          onClick={() => navigate("/stories")}
          style={{ background: "none", border: "none", fontSize: 18, cursor: "pointer", padding: "4px 8px" }}
        >
          ← Back
        </button>
        <div style={{ textAlign: "center", flex: 1 }}>
          <div style={{ fontSize: 14, fontWeight: "bold", color: "#333" }}>
            Story {story.tribulation_number}: {story.title}
          </div>
          <StoryProgress current={sceneIdx} total={story.scenes.length} />
        </div>
        <div style={{ width: 60 }} />
      </div>

      {/* Scene */}
      <div style={{ flex: 1, position: "relative", overflow: "hidden" }}>
        <StorySceneView
          key={scene.scene_id}
          scene={scene}
          storyWorld={story.world}
          difficulty={story.difficulty}
          onSceneComplete={handleSceneComplete}
          speak={speak}
        />
      </div>

      {showCelebration && (
        <Celebration reward={story.reward} onContinue={handleContinue} />
      )}
    </div>
  );
}
