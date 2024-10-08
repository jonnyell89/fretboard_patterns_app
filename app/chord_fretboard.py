from typing import List, Dict, Tuple

from config.config import CHROMATIC_SCALE, FRETBOARD_LEN
from app.library.degrees import chord_degrees
from app.library.tunings import tunings
from app.library.enums import ScaleTypes, ChordTypes
from app.scale_generator import ScaleGenerator
from app.chord_generator import ChordGenerator
from app.utils import generate_string, generate_cache_key, get_or_generate

class ChordFretboard:

    """
    A class to generate chord fretboards based on chord notes.

    Attributes:

        _fretboard_len: The length of the fretboard.
        _frets: A range object, representing the fret positions on the fretboard.
        _chromatic_scale: The twelve note chromatic scale.
        _chord_string_cache: A dictionary, keyed by a tuple of scale key, scale type, chord type and tuning, containing a nested dictionary, keyed by chord degree, containing another nested dictionary with root notes as keys and chord note string representations as values.
    
    """

    def __init__(self):

        self._fretboard_len: int = FRETBOARD_LEN
        self._frets: range = range(FRETBOARD_LEN)
        self._chromatic_scale: List[str] = CHROMATIC_SCALE
        self._chord_string_cache: Dict[Tuple[str, str, str, str, Tuple[str, ...]], Dict[str, Dict[str, List[str]]]] = {}

    def get_or_generate_chord_strings(self,
                                      scale_notes: List[str],
                                      scale_type: ScaleTypes,
                                      chord_notes: Dict[str, List[str]],
                                      chord_type: ChordTypes,
                                      tuning: List[str]
                                      ) -> Dict[str, Dict[str, List[str]]]:
        
        """
        Retrieves chord note strings from the cache, based on the scale notes, scale type, chord notes, chord type and tuning.
        If unavailable, generates chord note strings and stores them in the cache.
        
        Args:

            scale_notes: A list containing the scale notes.
            scale_type: The name of the scale type.
            chord_notes: A dictionary containing chord degrees as keys and chord notes as values.
            chord_type: The name of the chord type.
            tuning: A list containing the root note of each open string.

        Returns:

            chord_strings: A dictionary, keyed by chord degrees, containing a nested dictionary with root notes as keys and chord note strings as values.
        
        """

        cache_key: Tuple[str, str, str, str, Tuple[str, ...]] = generate_cache_key("ChordFretboard", scale_notes[0], scale_type.value, chord_type.value, tuning)

        chord_strings: Dict[str, Dict[str, List[str]]] = get_or_generate(cache=self._chord_string_cache, 
                                                                         cache_key=cache_key, 
                                                                         generate_function=lambda: self._compute_chord_strings(chord_notes=chord_notes, 
                                                                                                                               scale_type=scale_type, 
                                                                                                                               chord_type=chord_type, 
                                                                                                                               tuning=tuning))

        return chord_strings

    def _compute_chord_strings(self,
                               chord_notes: Dict[str, List[str]],
                               scale_type: ScaleTypes,
                               chord_type: ChordTypes,
                               tuning: List[str]
                               ) -> Dict[str, Dict[str, List[str]]]:
        
        """
        Computes a guitar string representation containing chord notes and blank spaces for notes that do not exist in the chord.

        Args:

            chord_notes: A dictionary containing the chord degrees as keys and the chord notes as values.
            scale_type: The name of the scale type.
            chord_type: The name of the chord type.
            tuning: A list containing the root note of each open string.

        Returns:

            chord_degree_dict: A dictionary containing chord degrees as keys and a nested dictionary of root notes as keys and chord note strings as values.
        
        """

        # Defines the dictionary to be returned
        chord_degree_dict: Dict[str, Dict[str, List[str]]] = {}

        # Accesses chord notes for each degree in the scale
        for chord_notes_index, chord_notes_list in enumerate(chord_notes.values()):

            # Defines the chord degree cache key
            chord_degree_key = chord_degrees[chord_type.value][scale_type.value][chord_notes_index]

            # Defines the nested dictionary to store the chord note strings for each root note in the tuning
            chord_string_dict: Dict[str, List[str]] = {}
        
            # Generates a chord note string for each root note in the tuning
            for root_note in tuning:
            
                # String root note index position in the chromatic scale
                root_index: int = self._chromatic_scale.index(root_note)

                # Computes chord note string from the chromatic scale starting at the root index
                chord_string: List[str] = generate_string(start_position=root_index, 
                                                          note_sequence=self._chromatic_scale, 
                                                          scale_or_chord=chord_notes_list, 
                                                          frets=self._frets)

                # Stores chord note string in the nested dictionary
                chord_string_dict[root_note] = chord_string

            # Stores the nested dictionary inside the dictionary to be returned
            chord_degree_dict[chord_degree_key] = chord_string_dict

        return chord_degree_dict



if __name__ == "__main__":

    print("--------------------")

    demo_scale_generator = ScaleGenerator()

    demo_scale_notes = demo_scale_generator.get_or_generate_scale(scale_key="C", scale_type=ScaleTypes.MAJOR_SCALE)

    print(demo_scale_notes)

    print("--------------------")

    demo_chord_generator = ChordGenerator()

    demo_chord_notes = demo_chord_generator.get_or_generate_chord(scale_notes=demo_scale_notes, scale_type=ScaleTypes.MAJOR_SCALE, chord_type=ChordTypes.TRIAD)

    print(demo_chord_notes)

    print("--------------------")

    print(demo_chord_generator._chord_notes_cache)

    print("--------------------")

    demo_chord_fretboard = ChordFretboard()

    demo_chord_string_dict = demo_chord_fretboard.get_or_generate_chord_strings(scale_notes=demo_scale_notes, scale_type=ScaleTypes.MAJOR_SCALE, chord_notes=demo_chord_notes, chord_type=ChordTypes.TRIAD, tuning=tunings["e_standard"])

    print(demo_chord_string_dict)

    print("--------------------")

    print(demo_chord_fretboard._chord_string_cache)

    print("--------------------")
