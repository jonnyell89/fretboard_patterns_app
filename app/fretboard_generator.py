from typing import List, Dict

from config.config import CHROMATIC_SCALE, FRETBOARD_LEN, FRETS, DEFAULT_TUNING
# from app.library.tunings import tunings
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
        num_strings: The number of guitar strings.
        frets: The frets on the guitar fretboard.

    """

    def __init__(self, 
                 fretboard_len: int = FRETBOARD_LEN, 
                 chromatic_scale: List[str] = CHROMATIC_SCALE, 
                 tuning: List[str] = DEFAULT_TUNING
                 ) -> None:
        
        self.fretboard_len: int = fretboard_len
        self.chromatic_scale: List[str] = chromatic_scale
        self.tuning: List[str] = tuning[::-1]
        self.string_dict: Dict[str, List[str]] = {}
        self.generate_strings()
        self.fretboard_dict: Dict[str, List[List[str]]] = {}
        self.num_strings = len(self.tuning)
        self.generate_fretboard_x()
        self.generate_fretboard_y()
        self.frets: List[str] = FRETS
    
    # Generates a list of notes representing a guitar string, starting from a specific point in the chromatic scale.
    def generate_string(self, root_note) -> List[str]:
                
        root_index = self.chromatic_scale.index(root_note)

        guitar_string = [self.chromatic_scale[(root_index + note) % len(self.chromatic_scale)] for note in range(self.fretboard_len)]

        return guitar_string

    # Instantiates a StringGenerator object for each unique root note in the tuning signature.
    def generate_strings(self) -> None:

        for root_note in self.tuning:

            if root_note not in self.string_dict:

                self.string_dict[root_note] = self.generate_string(root_note=root_note)

    # Generates a two-dimensional list of six guitar strings representing a chromatic guitar fretboard, in horizontal orientation.
    def generate_fretboard_x(self) -> None:

        horizontal_fretboard: List[List[str]] = [self.string_dict[root_note] for root_note in self.tuning]

        self.fretboard_dict["x"] = horizontal_fretboard

    # Generates a vertically orientated chromatic guitar fretboard by rotating the horizontally orientated chromatic guitar fretboard 90 degrees clockwise.
    def generate_fretboard_y(self) -> None:

        horizontal_fretboard: List[List[str]] = self.fretboard_dict["x"]

        vertical_fretboard: List[List[str]] = [["" for _ in range(self.num_strings)] for _ in range(self.fretboard_len)]

        for i in range(self.num_strings):

            for j in range(self.fretboard_len):

                vertical_fretboard[j][self.num_strings - 1 - i] = horizontal_fretboard[i][j]
                    
        self.fretboard_dict["y"] = vertical_fretboard



if __name__ == "__main__":

    print("--------------------")

    demo_fretboard = FretboardGenerator()

    demo_fretboard_dict = demo_fretboard.fretboard_dict

    apply_fret_marker(demo_fretboard_dict, orientation="x")

    print_fretboard(demo_fretboard_dict, orientation="x")
    print_fretboard(demo_fretboard_dict, orientation="y")


