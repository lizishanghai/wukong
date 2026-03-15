import { motion } from "framer-motion";
import { objectToEmoji } from "../../utils/constants";

interface Props {
  objects: string[];
  /** If true, objects appear one by one with a bounce */
  animated?: boolean;
}

/** Renders a row of emoji objects (peaches, monkeys, etc.) */
export default function ObjectDisplay({ objects, animated = true }: Props) {
  return (
    <div
      style={{
        display: "flex",
        flexWrap: "wrap",
        gap: 8,
        justifyContent: "center",
        padding: "12px 8px",
      }}
    >
      {objects.map((obj, i) => {
        const emoji = objectToEmoji(obj);

        // Show separator differently
        if (obj === "|") {
          return (
            <div
              key={i}
              style={{
                width: 4,
                height: 60,
                background: "#999",
                borderRadius: 2,
                margin: "0 12px",
                alignSelf: "center",
              }}
            />
          );
        }

        return (
          <motion.span
            key={i}
            initial={animated ? { scale: 0, y: -20 } : {}}
            animate={{ scale: 1, y: 0 }}
            transition={{
              delay: animated ? i * 0.12 : 0,
              type: "spring",
              damping: 10,
            }}
            style={{
              fontSize: 44,
              cursor: "default",
              userSelect: "none",
            }}
          >
            {emoji}
          </motion.span>
        );
      })}
    </div>
  );
}
