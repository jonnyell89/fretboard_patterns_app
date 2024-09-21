from typing import List, Dict

from app.library.intervals import scale_patterns
from app.fretboard_generator import FretboardGenerator
from app.utils import print_fretboard, apply_fret_marker

class ScaleFretboard(FretboardGenerator):

    """
    A class to generate a guitar fretboard representation containing the notes of a specific scale, in both horizontal and vertical orientations.

    Attributes:

        key: The first note in the scale.
        scale_pattern: The series of intervals that make up the scale.
        key_index: The first note in the scale, relative to the chromatic scale.
        scale_notes: The series of notes that make up the scale, derived from the chromatic scale.
        scale_fretboard_dict: The horizontal and vertical orientations of the guitar fretboard containing the notes from the scale.
    
    """

    def __init__(self, 
                 key: str = "C", 
                 scale_pattern: List[int] = scale_patterns["major_scale"]
                 ) -> None:

        # Refers to the FretboardGenerator class constructor.
        super().__init__()

        self.key: str = key
        self.scale_pattern: List[int] = scale_pattern        
        self.key_index: int = self.chromatic_scale.index(self.key)
        self.scale_notes: List[str] = self.calculate_scale_notes()
        self.scale_fretboard_dict: Dict[str, List[List[str]]] = {}
        self.generate_scale_fretboard()

    # Generates a list of notes representing the scale, derived from the chromatic scale.
    def calculate_scale_notes(self) -> List[str]:

        scale_notes: List[str] = [self.chromatic_scale[(self.key_index + note) % len(self.chromatic_scale)] for note in self.scale_pattern]

        return scale_notes

    # Generates a scale orientated guitar fretboard in both horizontal and vertical orientations.
    def generate_scale_fretboard(self) -> None:

        self.scale_fretboard_dict["x"] = self._apply_scale_to_fretboard(self.fretboard_dict["x"])

        self.scale_fretboard_dict["y"] = self._apply_scale_to_fretboard(self.fretboard_dict["y"])
    
    # Helper method -> Logic: Applies the scale to the standard chromatic guitar fretboard.
    def _apply_scale_to_fretboard(self, fretboard: List[List[str]]) -> List[List[str]]:

        scale_fretboard: List[List[str]] = [[note if note in self.scale_notes else "__" for note in string] for string in fretboard]

        return scale_fretboard



if __name__ == "__main__":

    print("--------------------")

    demo_scale_fretboard = ScaleFretboard()

    demo_scale_fretboard_dict = demo_scale_fretboard.scale_fretboard_dict

    apply_fret_marker(demo_scale_fretboard_dict, orientation="x")

    print_fretboard(demo_scale_fretboard_dict, orientation="x")
    print_fretboard(demo_scale_fretboard_dict, orientation="y")


