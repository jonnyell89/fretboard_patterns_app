from typing import List, Dict, Optional

from library.intervals import chromatic_scale
from library.tunings import tunings
from string_generator import StringGenerator



class FretboardGenerator:

    """
    A class to generate a chromatic guitar fretboard representation in both horizontal and vertical orientations.
    
    Attributes:

        length: The number of frets on the chromatic guitar fretboard.
        chromatic_scale: The twelve note chromatic scale.
        tuning: The root note of each guitar string, representing the tuning of the guitar.
        strings: The guitar strings as StringGenerator objects.
        fretboard_dict: The horizontal and vertical orientations of the chromatic guitar fretboard.
        frets: The frets on the guitar fretboard.

    """

    def __init__(self, length: int = 16, chromatic_scale: List[str] = chromatic_scale["chromatic_scale"], tuning: List[str] = tunings["e_standard"]) -> None:
        
        self.length: int = length
        self.chromatic_scale: List[str] = chromatic_scale
        self.tuning: List[str] = tuning[::-1]
        self.strings: List[StringGenerator] = [StringGenerator(root, self.length, self.chromatic_scale) for root in self.tuning]
        self.fretboard_dict: Dict[str, List[List[str]]] = {}
        self.generate_fretboard_x()
        self.generate_fretboard_y()
        self.frets: List[str] = [str(fret) for fret in range(self.length)]

    # Generates a two-dimensional list of six guitar strings representing a chromatic guitar fretboard, in horizontal orientation.
    def generate_fretboard_x(self) -> None:

        horizontal_fretboard: List[List[str]] = [string.generate_string() for string in self.strings]

        self.fretboard_dict["x"] = horizontal_fretboard

    # Generates a vertically orientated chromatic guitar fretboard by rotating the horizontally orientated chromatic guitar fretboard 90 degrees clockwise.
    def generate_fretboard_y(self) -> None:

        horizontal_fretboard: List[List[str]] = self.fretboard_dict["x"]

        number_of_strings: int = len(horizontal_fretboard)

        length_of_strings: int = len(horizontal_fretboard[0])

        vertical_fretboard: List[List[str]] = [[0 for _ in range(number_of_strings)] for _ in range(length_of_strings)]

        for i in range(number_of_strings):

            for j in range(length_of_strings):

                vertical_fretboard[j][number_of_strings - 1 - i] = horizontal_fretboard[i][j]
                    
        self.fretboard_dict["y"] = vertical_fretboard

    # Applies a list of numbers representing fret markers to a chromatic, scale or chord based guitar fretboard in a specific orientation.
    def apply_fret_marker(self, fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], orientation: str, chord: Optional[int] = None) -> None:

        if not self._is_valid_fretboard(fretboard_dict, orientation, chord):

            return

        if orientation == "x":

            self._apply_fret_marker_x(fretboard_dict, chord)

        elif orientation == "y":

            self._apply_fret_marker_y(fretboard_dict, chord)

    # Prints a chromatic, scale or chord based guitar fretboard in a specific orientation.
    def print_fretboard(self, fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], orientation: str, chord: Optional[int] = None) -> None:

        if not self._is_valid_fretboard(fretboard_dict, orientation, chord):

            return

        if chord:

            fretboard = fretboard_dict[chord][orientation]

        else:

            fretboard = fretboard_dict[orientation]

        self._print_fretboard(fretboard)

    # Helper method -> Error handling: Checks if both the chord and orientation parameters are present in the fretboard dictionary.
    def _is_valid_fretboard(self, fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], orientation: str, chord: Optional[int] = None) -> bool:

        if chord:

            if chord not in fretboard_dict:

                print(f"Error: {chord} chord not found in fretboard dictionary.")

                return False

            if orientation not in fretboard_dict[chord]:

                print(f"Error: {orientation} orientation not found in fretboard dictionary.")

                return False
            
        else:

            if orientation not in fretboard_dict:

                print(f"Error: {orientation} orientation not found in fretboard dictionary.")

                return False
            
        return True
    
    # Helper method -> Logic: Applies a list of numbers representing fret markers to a specific horizontally orientated guitar fretboard.
    def _apply_fret_marker_x(self, fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], chord: Optional[int] = None) -> None:

        if chord:

            fretboard_dict[chord]["x"].append(self.frets)

        else:

            fretboard_dict["x"].append(self.frets)

    # Helper method -> Logic: Applies a list of numbers representing fret markers to a specific vertically orientated guitar fretboard.
    def _apply_fret_marker_y(self, fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], chord: Optional[int] = None) -> None:

        if chord:

            for index, fret in enumerate(self.frets):
    
                fretboard_dict[chord]["y"][index].insert(0, fret)

        else:

            for index, fret in enumerate(self.frets):
    
                fretboard_dict["y"][index].insert(0, fret)

    # Helper method -> Logic: Prints a series of lists representing guitar strings that together represent the guitar fretboard in both horizontal and vertical orientations.
    def _print_fretboard(self, fretboard: List[List[str]]) -> None:

        for string in fretboard:

            print([f"{note:<2}" for note in string])



print("--------------------")

demo_fretboard = FretboardGenerator()

demo_fretboard_dict = demo_fretboard.fretboard_dict

demo_fretboard.apply_fret_marker(demo_fretboard_dict, orientation="x")

demo_fretboard.apply_fret_marker(demo_fretboard_dict, orientation="y")

demo_fretboard.print_fretboard(demo_fretboard_dict, orientation="x")

demo_fretboard.print_fretboard(demo_fretboard_dict, orientation="y")
