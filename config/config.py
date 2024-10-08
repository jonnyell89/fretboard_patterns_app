from typing import List

CHROMATIC_SCALE: List[str] = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

FRETBOARD_LEN = 16

NUM_FRETS: int = FRETBOARD_LEN
FRETS: List[str] = [f"{FRET:<2}" for FRET in range(NUM_FRETS)]
