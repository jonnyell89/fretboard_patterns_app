from typing import List

CHROMATIC_SCALE: List[str] = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

FRETBOARD_LEN = 16

NUM_FRETS: int = FRETBOARD_LEN
FRETS: List[str] = [str(FRET) for FRET in range(NUM_FRETS)]

DEFAULT_KEY = "C"
DEFAULT_TUNING = ["E", "A", "D", "G", "B", "E"]
DEFAULT_SCALE = [0, 2, 4, 5, 7, 9, 11]
DEFAULT_CHORD = [0, 2, 4]
