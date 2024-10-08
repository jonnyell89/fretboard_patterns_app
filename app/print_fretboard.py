from typing import List, Dict, Optional

from config.config import FRETS
from app.scale_generator import ScaleGenerator
from app.scale_fretboard import ScaleFretboard
from app.chord_generator import ChordGenerator
from app.chord_fretboard import ChordFretboard
from app.library.enums import ScaleTypes, ChordTypes
from app.library.tunings import tunings
from app.library.degrees import chord_degrees

def print_fretboard(strings: Dict[str, List[str]], 
                    tuning: List[str], 
                    chord_degree: Optional[str] = None,
                    fret_marker: Optional[bool] = False
                    ) -> None:
    
    """
    A function to print either scale fretboards or chord fretboards to the terminal, in horizontal orientation.

    Args:

        strings: A dictionary containing scale notes mapped to guitar string representations, or a nested dictionary containing chord degrees.
        tuning: A list containing the root note of each open string.
        chord_degree: An optional parameter to access the nested dictionary containing chord notes mapped to guitar string representations.
        fret_marker: An optional list of numbers printed beneath the fretboard.
    
    """

    if chord_degree:

        fretboard = strings.get(chord_degree)

    else:

        fretboard = strings

    for root_note in tuning[::-1]:

        string = fretboard.get(root_note)

        print(string)
    
    if fret_marker:

        _print_fret_marker()

def _print_fret_marker() -> None:

    """
    A function to print a list of numbers representing the frets of the fretboard.
    
    """

    print(FRETS)

# generate_cache_key("ScaleGenerator", scale_key, scale_type.value)
scale_generator = ScaleGenerator()

scale_notes = scale_generator.get_or_generate_scale(scale_key="D", scale_type=ScaleTypes.NATURAL_MINOR)

print(f"scale_notes: {scale_notes}")

print("--------------------")

# generate_cache_key("ScaleFretboard", scale_notes[0], scale_type.value, tuning)
scale_fretboard = ScaleFretboard()

scale_strings = scale_fretboard.get_or_generate_scale_strings(scale_notes=scale_notes, scale_type=ScaleTypes.NATURAL_MINOR, tuning=tunings["e_standard"])

print(f"scale_strings: {scale_strings}")

print_fretboard(strings=scale_strings, chord_degree=None, tuning=tunings["e_standard"], fret_marker=True)

print("--------------------")

# generate_cache_key("ChordGenerator", scale_notes[0], scale_type.value, chord_type.value)
chord_generator = ChordGenerator()

chord_notes = chord_generator.get_or_generate_chord(scale_notes=scale_notes, scale_type=ScaleTypes.NATURAL_MINOR, chord_type=ChordTypes.SEVENTH)

print(f"chord_notes: {chord_notes}")

print("--------------------")

# generate_cache_key("ChordFretboard", scale_notes[0], scale_type.value, chord_type.value, tuning)
chord_fretboard = ChordFretboard()

chord_strings = chord_fretboard.get_or_generate_chord_strings(scale_notes=scale_notes, scale_type=ScaleTypes.NATURAL_MINOR, chord_notes=chord_notes, chord_type=ChordTypes.SEVENTH, tuning=tunings["e_standard"])

print(f"chord_strings: {chord_strings}")

print_fretboard(strings=chord_strings, chord_degree=chord_degrees["seventh"]["natural_minor"][0], tuning=tunings["e_standard"], fret_marker=True)

print("--------------------")
