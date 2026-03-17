interface Props {
  current: number;
  total: number;
}

export default function StoryProgress({ current, total }: Props) {
  return (
    <div style={{ display: "flex", gap: 8, justifyContent: "center" }}>
      {Array.from({ length: total }, (_, i) => (
        <div
          key={i}
          style={{
            width: 12,
            height: 12,
            borderRadius: "50%",
            background: i < current ? "#4CAF50" : i === current ? "#FFD700" : "#ddd",
            border: i === current ? "2px solid #FFA000" : "2px solid transparent",
            transition: "all 0.3s",
          }}
        />
      ))}
    </div>
  );
}
