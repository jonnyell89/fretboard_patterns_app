from typing import List, Dict

from config.config import CHROMATIC_SCALE, NUM_STRINGS, STRING_LEN, FRETBOARD_LEN, FRETS
from app.library.tunings import tunings
from app.string_generator import StringGenerator
from app.utils import print_fretboard, apply_fret_marker

class FretboardGenerator:

    """
    A class to generate a chromatic guitar fretboard representation in both horizontal and vertical orientations.
    
    Attributes:

        fretboard_len: The length of the guitar fretboard.
        chromatic_scale: The twelve note chromatic scale.
        tuning: The root note of each guitar string, representing the tuning of the guitar.
        string_dict: The guitar strings as instantiated StringGenerator objects.
        fretboard_dict: The horizontal and vertical orientations of the chromatic guitar fretboard.
        frets: The frets on the guitar fretboard.

    """

    def __init__(self, 
                 fretboard_len: int = FRETBOARD_LEN, 
                 chromatic_scale: List[str] = CHROMATIC_SCALE, 
                 tuning: List[str] = tunings["e_standard"]
                 ) -> None:
        
        self.fretboard_len: int = fretboard_len
        self.chromatic_scale: List[str] = chromatic_scale
        self.tuning: List[str] = tuning[::-1]
        self.string_dict: Dict[str, List[str]] = {}
        self.generate_strings()
        self.fretboard_dict: Dict[str, List[List[str]]] = {}
        self.generate_fretboard_x()
        self.generate_fretboard_y()
        self.frets: List[str] = FRETS

    # Instantiates a StringGenerator object for each unique root note in the tuning signature.
    def generate_strings(self) -> None:

        for root_note in self.tuning:

            if root_note not in self.string_dict:

                self.string_dict[root_note] = StringGenerator(root_note, self.fretboard_len, self.chromatic_scale).generate_string()

    # Generates a two-dimensional list of six guitar strings representing a chromatic guitar fretboard, in horizontal orientation.
    def generate_fretboard_x(self) -> None:

        horizontal_fretboard: List[List[str]] = [self.string_dict[root_note] for root_note in self.tuning]

        self.fretboard_dict["x"] = horizontal_fretboard

    # Generates a vertically orientated chromatic guitar fretboard by rotating the horizontally orientated chromatic guitar fretboard 90 degrees clockwise.
    def generate_fretboard_y(self) -> None:

        horizontal_fretboard: List[List[str]] = self.fretboard_dict["x"]

        vertical_fretboard: List[List[str]] = [["" for _ in range(NUM_STRINGS)] for _ in range(STRING_LEN)]

        for i in range(NUM_STRINGS):

            for j in range(STRING_LEN):

                vertical_fretboard[j][NUM_STRINGS - 1 - i] = horizontal_fretboard[i][j]
                    
        self.fretboard_dict["y"] = vertical_fretboard



if __name__ == "__main__":

    print("--------------------")

    demo_fretboard = FretboardGenerator()

    demo_fretboard_dict = demo_fretboard.fretboard_dict

    apply_fret_marker(demo_fretboard_dict, orientation="x")

    print_fretboard(demo_fretboard_dict, orientation="x")
    print_fretboard(demo_fretboard_dict, orientation="y")


