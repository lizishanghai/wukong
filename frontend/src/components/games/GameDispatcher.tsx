import type { Level } from "../../types/game";
import CountingGame from "./CountingGame";
import AdditionGame from "./AdditionGame";
import SubtractionGame from "./SubtractionGame";
import ComparisonGame from "./ComparisonGame";
import PatternGame from "./PatternGame";
import OrderingGame from "./OrderingGame";
import MemoryGame from "./MemoryGame";
import FindDifferenceGame from "./FindDifferenceGame";
import ClassificationGame from "./ClassificationGame";
import MazeGame from "./MazeGame";
import ClockGame from "./ClockGame";
import ShapePatternGame from "./ShapePatternGame";
import SightWordsGame from "./SightWordsGame";
import PhonicsGame from "./PhonicsGame";
import SudokuGame from "./SudokuGame";
import MakeTenGame from "./MakeTenGame";
import NumberSequenceGame from "./NumberSequenceGame";
import MirrorGame from "./MirrorGame";
import GeneralKnowledgeGame from "./GeneralKnowledgeGame";

interface Props {
  level: Level;
  onCorrect: () => void;
  onWrong: () => void;
}

/** Routes to the correct game component based on game_type. */
export default function GameDispatcher({ level, onCorrect, onWrong }: Props) {
  const q = level.question;

  switch (level.game_type) {
    case "counting":
      return <CountingGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "addition":
      return <AdditionGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "subtraction":
      return <SubtractionGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "comparison":
      return <ComparisonGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "pattern":
      return <PatternGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "ordering":
      return <OrderingGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "memory":
      return <MemoryGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "find_difference":
      return <FindDifferenceGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "classification":
      return <ClassificationGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "maze":
      return <MazeGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "clock_reading":
      return <ClockGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "shape_pattern":
      return <ShapePatternGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "sight_words":
      return <SightWordsGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "phonics":
      return <PhonicsGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "sudoku":
      return <SudokuGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "make_ten":
      return <MakeTenGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "number_sequence":
      return <NumberSequenceGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "mirror_symmetry":
      return <MirrorGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    case "general_knowledge":
      return <GeneralKnowledgeGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
    default:
      return <CountingGame question={q} onCorrect={onCorrect} onWrong={onWrong} />;
  }
}
