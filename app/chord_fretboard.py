from typing import List, Dict

from config.config import DEFAULT_TUNING, DEFAULT_KEY, DEFAULT_SCALE, DEFAULT_CHORD
# from app.library.tunings import tunings
# from app.library.intervals import scale_patterns, chord_patterns
from app.fretboard_generator import FretboardGenerator
from app.scale_fretboard import ScaleFretboard
from app.utils import print_fretboard, apply_fret_marker

class ChordFretboard:

    """
    A class to generate a guitar fretboard representation containing the notes of a specific chord derived from the inherited scale, in both horizontal and vertical orientations.

    Attributes:

        scale_fretboard: A ScaleFretboard object.
        chord_pattern: The series of intervals that make up the chord.
        chord_notes_dict: The series of notes that make up the chord, derived from the inherited scale.
        chord_fretboard_dict: The horizontal and vertical orientations of the guitar fretboard containing the notes from the chord, derived from the inherited scale.
    
    """

    def __init__(self, 
                 scale_fretboard: ScaleFretboard,
                 chord_pattern: List[int] = DEFAULT_CHORD
                 ) -> None:

        self.scale_fretboard = scale_fretboard
        self.chord_pattern: List[int] = chord_pattern
        self.chord_notes_dict: Dict[int, List[str]] = {}
        self.calculate_chord_notes()
        self.chord_fretboard_dict: Dict[int, Dict[str, List[List[str]]]] = {}
        self.generate_chord_fretboards()

    # Generates a list of notes representing the chords for each scale degree, based on the chord pattern and derived from the inherited scale.
    def calculate_chord_notes(self) -> None:

        scale_degrees: int = len(self.scale_fretboard.scale_notes)

        for degree_index in range(scale_degrees):

            chord_notes: List[str] = [self.scale_fretboard.scale_notes[(degree_index + note) % scale_degrees] for note in self.chord_pattern]

            self.chord_notes_dict[degree_index + 1] = chord_notes

    # Generates a chord orientated guitar fretboard in both horizontal and vertical orientations.
    def generate_chord_fretboards(self) -> None:

        for chord_index, chord in self.chord_notes_dict.items():

            self.chord_fretboard_dict[chord_index] = {

                "x": self._apply_chords_to_fretboard_x(chord),
                "y": self._apply_chords_to_fretboard_y(chord)

            }
    
    # Helper method -> Logic: Applies the chord notes to the scale orientated horizontal guitar fretboard.
    def _apply_chords_to_fretboard_x(self, chord: List[str]) -> List[List[str]]:

        horizontal_fretboard = self.scale_fretboard.scale_fretboard_dict["x"]

        chord_fretboard_x: List[List[str]] = [[note if note in chord else "__" for note in string] for string in horizontal_fretboard]

        return chord_fretboard_x

    # Helper method -> Logic: Applies the chord notes to the scale orientated vertical guitar fretboard.
    def _apply_chords_to_fretboard_y(self, chord: List[str]) -> List[List[str]]:

        vertical_fretboard = self.scale_fretboard.scale_fretboard_dict["y"]

        chord_fretboard_y: List[List[str]] = [[note if note in chord else "__" for note in string] for string in vertical_fretboard]

        return chord_fretboard_y



if __name__ == "__main__":

    print("--------------------")

    demo_fretboard_generator = FretboardGenerator(tuning=DEFAULT_TUNING)

    demo_scale_fretboard = ScaleFretboard(fretboard_generator=demo_fretboard_generator, key=DEFAULT_KEY, scale_pattern=DEFAULT_SCALE)

    demo_chord_fretboard = ChordFretboard(scale_fretboard=demo_scale_fretboard, chord_pattern=DEFAULT_CHORD)

    demo_chord_fretboard_dict = demo_chord_fretboard.chord_fretboard_dict

    apply_fret_marker(demo_chord_fretboard_dict, orientation="x", chord=1)

    print_fretboard(demo_chord_fretboard_dict, orientation="x", chord=1)
    print_fretboard(demo_chord_fretboard_dict, orientation="y", chord=1)


