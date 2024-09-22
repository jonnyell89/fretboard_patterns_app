from typing import List, Dict

from app.library.intervals import chord_patterns
from app.scale_fretboard import ScaleFretboard
from app.utils import print_fretboard, apply_fret_marker

class ChordFretboard(ScaleFretboard):

    """
    A class to generate a guitar fretboard representation containing the notes of a specific chord derived from the inherited scale, in both horizontal and vertical orientations.

    Attributes:

        chord_pattern: The series of intervals that make up the chord.
        chord_notes_dict: The series of notes that make up the chord, derived from the inherited scale.
        chord_fretboard_dict: The horizontal and vertical orientations of the guitar fretboard containing the notes from the chord, derived from the inherited scale.
    
    """

    def __init__(self, 
                 chord_pattern: List[int] = chord_patterns["notes_3"]
                 ) -> None:

        # Refers to the ScaleFretboard constructor.
        super().__init__()

        self.chord_pattern: List[int] = chord_pattern
        self.chord_notes_dict: Dict[int, List[str]] = {}
        self.calculate_chord_notes()
        self.chord_fretboard_dict: Dict[int, Dict[str, List[List[str]]]] = {}
        self.generate_chord_fretboards()

    # Generates a list of notes representing the chords for each scale degree, based on the chord pattern and derived from the inherited scale.
    def calculate_chord_notes(self) -> None:

        scale_degrees: int = len(self.scale_notes)

        for degree_index in range(scale_degrees):

            chord_notes: List[str] = [self.scale_notes[(degree_index + note) % scale_degrees] for note in self.chord_pattern]

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

        horizontal_fretboard = self.scale_fretboard_dict["x"]

        chord_fretboard_x: List[List[str]] = [[note if note in chord else "__" for note in string] for string in horizontal_fretboard]

        return chord_fretboard_x

    # Helper method -> Logic: Applies the chord notes to the scale orientated vertical guitar fretboard.
    def _apply_chords_to_fretboard_y(self, chord: List[str]) -> List[List[str]]:

        vertical_fretboard = self.scale_fretboard_dict["y"]

        chord_fretboard_y: List[List[str]] = [[note if note in chord else "__" for note in string] for string in vertical_fretboard]

        return chord_fretboard_y



if __name__ == "__main__":

    print("--------------------")

    demo_chord_fretboard = ChordFretboard()

    demo_chord_fretboard_dict = demo_chord_fretboard.chord_fretboard_dict

    apply_fret_marker(demo_chord_fretboard_dict, orientation="x", chord=1)

    print_fretboard(demo_chord_fretboard_dict, orientation="x", chord=1)
    print_fretboard(demo_chord_fretboard_dict, orientation="y", chord=1)


