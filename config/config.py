from typing import List

CHROMATIC_SCALE: List[str] = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

NUM_STRINGS: int = 6
STRING_LEN: int = 16

FRETBOARD_LEN = STRING_LEN

NUM_FRETS: int = FRETBOARD_LEN
FRETS: List[str] = [str(FRET) for FRET in range(NUM_FRETS)]
