from typing import List, Dict, Optional

from config.config import FRETS

# Prints a chromatic, scale or chord based guitar fretboard in a specific orientation.
def print_fretboard(fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], orientation: str, chord: Optional[int] = None) -> None:

    if not _is_valid_fretboard(fretboard_dict, orientation, chord):

        return

    if chord:

        fretboard = fretboard_dict[chord][orientation]

    else:

        fretboard = fretboard_dict[orientation]

    _print_fretboard(fretboard)

# Helper method -> Logic: Prints a series of lists representing guitar strings that together represent the guitar fretboard in both horizontal and vertical orientations.
def _print_fretboard(fretboard: List[List[str]]) -> None:

    for string in fretboard:

        print([f"{note:<2}" for note in string])

# Applies a list of numbers representing fret markers to a chromatic, scale or chord based guitar fretboard in a specific orientation.
def apply_fret_marker(fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], orientation: str, chord: Optional[int] = None) -> None:

    if not _is_valid_fretboard(fretboard_dict, orientation, chord):

        return

    if orientation == "x":

        _apply_fret_marker_x(fretboard_dict, chord)

    elif orientation == "y":

        _apply_fret_marker_y(fretboard_dict, chord)

# Helper method -> Logic: Applies a list of numbers representing fret markers to a specific horizontally orientated guitar fretboard.
def _apply_fret_marker_x(fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], chord: Optional[int] = None) -> None:

    if chord:

        fretboard_dict[chord]["x"].append(FRETS)

    else:

        fretboard_dict["x"].append(FRETS)

# Helper method -> Logic: Applies a list of numbers representing fret markers to a specific vertically orientated guitar fretboard.
def _apply_fret_marker_y(fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], chord: Optional[int] = None) -> None:

    if chord:

        for index, fret in enumerate(FRETS):

            fretboard_dict[chord]["y"][index].insert(0, fret)

    else:

        for index, fret in enumerate(FRETS):

            fretboard_dict["y"][index].insert(0, fret)

# Helper method -> Error handling: Checks if both the chord and orientation parameters are present in the fretboard dictionary.
def _is_valid_fretboard(fretboard_dict: Dict[Optional[int], Dict[str, List[List[str]]]], orientation: str, chord: Optional[int] = None) -> bool:

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


