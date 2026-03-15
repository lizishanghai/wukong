import { useState } from "react";
import type { LevelQuestion } from "../../types/game";
import OptionButton from "../ui/OptionButton";

interface Props {
  question: LevelQuestion;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Render an SVG analog clock face. */
function ClockFace({ hour, minute }: { hour: number; minute: number }) {
  const cx = 100;
  const cy = 100;
  const r = 85;

  // Hour hand: 360/12 = 30 deg per hour, + fraction for minutes
  const hourAngle = ((hour % 12) + minute / 60) * 30 - 90;
  const hourRad = (hourAngle * Math.PI) / 180;
  const hx = cx + Math.cos(hourRad) * 50;
  const hy = cy + Math.sin(hourRad) * 50;

  // Minute hand
  const minAngle = minute * 6 - 90;
  const minRad = (minAngle * Math.PI) / 180;
  const mx = cx + Math.cos(minRad) * 70;
  const my = cy + Math.sin(minRad) * 70;

  // Hour markers
  const markers = Array.from({ length: 12 }, (_, i) => {
    const angle = ((i + 1) * 30 - 90) * (Math.PI / 180);
    const x = cx + Math.cos(angle) * 72;
    const y = cy + Math.sin(angle) * 72;
    return { x, y, label: i + 1 };
  });

  return (
    <svg
      viewBox="0 0 200 200"
      width={200}
      height={200}
      style={{ margin: "0 auto", display: "block" }}
    >
      {/* Clock face */}
      <circle cx={cx} cy={cy} r={r} fill="#FFFDE7" stroke="#5D4037" strokeWidth={4} />
      {/* Hour markers */}
      {markers.map((m) => (
        <text
          key={m.label}
          x={m.x}
          y={m.y}
          textAnchor="middle"
          dominantBaseline="central"
          fontSize={16}
          fontWeight="bold"
          fill="#5D4037"
        >
          {m.label}
        </text>
      ))}
      {/* Minute ticks */}
      {Array.from({ length: 60 }, (_, i) => {
        const a = (i * 6 - 90) * (Math.PI / 180);
        const inner = i % 5 === 0 ? 78 : 82;
        return (
          <line
            key={i}
            x1={cx + Math.cos(a) * inner}
            y1={cy + Math.sin(a) * inner}
            x2={cx + Math.cos(a) * 85}
            y2={cy + Math.sin(a) * 85}
            stroke="#5D4037"
            strokeWidth={i % 5 === 0 ? 2 : 1}
          />
        );
      })}
      {/* Hour hand */}
      <line x1={cx} y1={cy} x2={hx} y2={hy} stroke="#D32F2F" strokeWidth={6} strokeLinecap="round" />
      {/* Minute hand */}
      <line x1={cx} y1={cy} x2={mx} y2={my} stroke="#1976D2" strokeWidth={4} strokeLinecap="round" />
      {/* Center dot */}
      <circle cx={cx} cy={cy} r={5} fill="#5D4037" />
    </svg>
  );
}

/** Clock reading game: show an analog clock, pick the correct time. */
export default function ClockGame({ question, onCorrect, onWrong }: Props) {
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<Record<number, boolean>>({});

  const clock = question.clock_time ?? { hour: 12, minute: 0 };

  const handlePick = (opt: string | number, idx: number) => {
    if (selected !== null) return;
    const isCorrect = String(opt) === String(question.correct_answer);
    setResult({ [idx]: isCorrect });
    setSelected(idx);

    if (isCorrect) {
      setTimeout(onCorrect, 800);
    } else {
      onWrong();
      setTimeout(() => {
        setSelected(null);
        setResult({});
      }, 1500);
    }
  };

  return (
    <>
      <h3 style={{ fontSize: 22, textAlign: "center", color: "#333" }}>
        {question.text}
      </h3>
      <ClockFace hour={clock.hour} minute={clock.minute} />
      <div style={{ display: "flex", gap: 16, flexWrap: "wrap", justifyContent: "center", marginTop: 16 }}>
        {question.options.map((opt, i) => (
          <OptionButton
            key={i}
            label={opt}
            size="large"
            correct={result[i] ?? null}
            disabled={selected !== null}
            onClick={() => handlePick(opt, i)}
          />
        ))}
      </div>
    </>
  );
}
