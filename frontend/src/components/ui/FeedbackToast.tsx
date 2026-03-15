import { motion, AnimatePresence } from "framer-motion";

interface Props {
  type: "correct" | "wrong" | null;
}

/**
 * Full-screen feedback overlay that shows 正确! or 错误! after answering.
 * Appears briefly then fades out.
 */
export default function FeedbackToast({ type }: Props) {
  return (
    <AnimatePresence>
      {type && (
        <motion.div
          key={type}
          initial={{ opacity: 0, scale: 0.5 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 0.8 }}
          transition={{ duration: 0.3 }}
          style={{
            position: "fixed",
            inset: 0,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            pointerEvents: "none",
            zIndex: 900,
          }}
        >
          <motion.div
            initial={{ y: 20 }}
            animate={{ y: 0 }}
            style={{
              padding: "20px 48px",
              borderRadius: 24,
              background: type === "correct"
                ? "linear-gradient(135deg, #4CAF50, #66BB6A)"
                : "linear-gradient(135deg, #FF5252, #FF8A80)",
              boxShadow: type === "correct"
                ? "0 8px 32px rgba(76,175,80,0.5)"
                : "0 8px 32px rgba(255,82,82,0.5)",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: 8,
            }}
          >
            <span style={{ fontSize: 48 }}>
              {type === "correct" ? "✅" : "❌"}
            </span>
            <span
              style={{
                fontSize: 32,
                fontWeight: "bold",
                color: "white",
                textShadow: "0 2px 4px rgba(0,0,0,0.2)",
              }}
            >
              {type === "correct" ? "正确!" : "错误，再试一次!"}
            </span>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
