from typing import List, Dict, Tuple

from app.library.intervals import chord_intervals
from app.library.degrees import chord_degrees
from app.library.enums import ScaleTypes, ChordTypes
from app.scale_generator import ScaleGenerator
from app.utils import generate_sequence_from_intervals, generate_cache_key, get_or_generate

class ChordGenerator:

    """
    A class to generate and store chord notes from chord intervals.

    Attributes:

        _chord_notes_cache: A dictionary, keyed by a tuple of scale key, scale type and chord type, containing a nested dictionary with chord degrees as keys and chord notes as values.

    """

    def __init__(self,
                 ) -> None:
        
        self._chord_notes_cache: Dict[Tuple[str, str, str], Dict[str, List[str]]] = {}

    def get_or_generate_chord(self, 
                              scale_notes: List[str],
                              scale_type: ScaleTypes,
                              chord_type: ChordTypes
                              ) -> Dict[str, List[str]]:
        
        """
        Retrieves chord notes from the cache, based on their key, scale type and chord type.
        If unavailable, generates chord notes and stores them in the cache.

        Args:

            scale_notes: A list containing the scale notes.
            scale_type: The name of the scale type.
            chord_type: The name of the chord type.

        Returns:

            chord_notes: A dictionary containing chord degrees as keys and chord notes as values.
        
        """

        cache_key: Tuple[str, str, str, str] = generate_cache_key("ChordGenerator", scale_notes[0], scale_type.value, chord_type.value)

        chord_notes: Dict[str, List[str]] = get_or_generate(cache=self._chord_notes_cache, 
                                                            cache_key=cache_key, 
                                                            generate_function=lambda: self._compute_chord_notes(scale_notes=scale_notes, 
                                                                                                                scale_type=scale_type, 
                                                                                                                chord_type=chord_type))
        
        return chord_notes

    def _compute_chord_notes(self, 
                             scale_notes: List[str],
                             scale_type: ScaleTypes,
                             chord_type: ChordTypes
                             ) -> Dict[str, List[str]]:
        
        """
        Computes chords notes from chord intervals, based on their scale notes, scale type and chord type.

        Args:

            scale_notes: A list containing the scale notes.
            scale_type: The name of the scale type.
            chord_type: The name of the chord type.

        Returns:

            chord_notes_dict: A dictionary containing chord degrees as keys and chord notes as values.
        
        """
        
        # Defines the dictionary to be returned
        chord_notes_dict: Dict[str, List[str]] = {}

        # Accesses chord intervals dictionary
        intervals: List[int] = chord_intervals[chord_type.value]

        # Generates chord notes for each degree in the scale
        for chord_degree in range(len(chord_degrees[chord_type.value][scale_type.value])):

            # Defines the chord notes cache key
            chord_cache_key: str = (chord_degrees[chord_type.value][scale_type.value][chord_degree])

            # Computes chord notes from the chord intervals via the scale notes
            chord_notes: List[str] = generate_sequence_from_intervals(start_position=chord_degree, 
                                                                      note_sequence=scale_notes, 
                                                                      intervals=intervals)

            # Stores chord notes in the dictionary to be returned
            chord_notes_dict[chord_cache_key] = chord_notes

        return chord_notes_dict



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
