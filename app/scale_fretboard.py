from typing import List, Dict, Tuple

from config.config import CHROMATIC_SCALE, FRETBOARD_LEN
from app.library.tunings import tunings
from app.library.enums import ScaleTypes
from app.scale_generator import ScaleGenerator
from app.utils import generate_string, generate_cache_key, get_or_generate

class ScaleFretboard:

    """
    A class to generate scale fretboards based on scale notes.

    Attributes:

        _fretboard_len: The length of the fretboard.
        _frets: A range object, representing the fret positions on the fretboard.
        _chromatic_scale: The twelve note chromatic scale.
        _scale_string_cache: A dictionary, keyed by a tuple of scale key, scale type and tuning, containing a nested dictionary with root notes as keys and scale note string representations as values.
    
    """

    def __init__(self):

        self._fretboard_len: int = FRETBOARD_LEN
        self._frets: range = range(FRETBOARD_LEN)
        self._chromatic_scale: List[str] = CHROMATIC_SCALE
        self._scale_string_cache: Dict[Tuple[str, str, str, Tuple[str, ...]], Dict[str, List[str]]] = {}

    def get_or_generate_scale_strings(self,
                                      scale_notes: List[str],
                                      scale_type: ScaleTypes,
                                      tuning: List[str]
                                      ) -> Dict[str, List[str]]:
        
        """ 
        Retrieves scale strings from the cache, based on the scale notes, scale type and tuning.
        If unavailable, generates scale strings and stores them in the cache.
        
        Args:

            scale_notes: A list containing the scale notes.
            scale_type: The name of the scale type.
            tuning: A list containing the root note of each open string.

        Returns:

            scale_strings: A dictionary containing root notes as keys and scale note string representations as values.

        """

        cache_key: Tuple[str, str, str, Tuple[str, ...]] = generate_cache_key("ScaleFretboard", scale_notes[0], scale_type.value, tuning)

        scale_strings: Dict[str, List[str]] = get_or_generate(cache=self._scale_string_cache, 
                                                              cache_key=cache_key, 
                                                              generate_function=lambda: self._compute_scale_strings(scale_notes=scale_notes, tuning=tuning))

        return scale_strings

    def _compute_scale_strings(self,
                               scale_notes: List[str],
                               tuning: List[str]
                               ) -> Dict[str, List[str]]:
        
        """
        Computes guitar string representations containing scale notes and blank spaces for notes that do not exist in the scale.

        Args:

            scale_notes: A list containing the scale notes.
            tuning: A list containing the root note of each open string.

        Returns:

            scale_string_dict: A dictionary containing root notes as keys and scale note string representations as values.
        
        """

        # Defines the dictionary to be returned
        scale_string_dict: Dict[str, List[str]] = {}

        # Generates a scale string for each root note in the tuning
        for root_note in tuning:
        
            # String root note index position in the chromatic scale
            root_index: int = self._chromatic_scale.index(root_note)

            # Computes scale string from the chromatic scale starting at the root index
            scale_string: List[str] = generate_string(start_position=root_index, 
                                                      note_sequence=self._chromatic_scale, 
                                                      scale_or_chord=scale_notes, 
                                                      frets=self._frets)

            # Stores scale string in the dictionary to be returned
            scale_string_dict[root_note] = scale_string

        return scale_string_dict



if __name__ == "__main__":

    print("--------------------")

    demo_scale_generator = ScaleGenerator()

    demo_scale_notes = demo_scale_generator.get_or_generate_scale(scale_key="C", scale_type=ScaleTypes.MAJOR_SCALE)

    print(demo_scale_notes)

    print("--------------------")

    demo_scale_fretboard = ScaleFretboard()

    demo_scale_strings = demo_scale_fretboard.get_or_generate_scale_strings(scale_notes=demo_scale_notes, scale_type=ScaleTypes.MAJOR_SCALE, tuning=tunings["e_standard"])

    print(demo_scale_strings)

    print("--------------------")

    print(demo_scale_fretboard._scale_string_cache)

    print("--------------------")
