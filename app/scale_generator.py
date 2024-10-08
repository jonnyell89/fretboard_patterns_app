from typing import List, Dict, Tuple

from config.config import CHROMATIC_SCALE
from app.library.intervals import scale_intervals
from app.library.enums import ScaleTypes
from app.utils import generate_sequence_from_intervals, generate_cache_key, get_or_generate

class ScaleGenerator:

    """
    A class to generate and store scale notes from scale intervals.

    Attributes:

        _chromatic_scale: The twelve note chromatic scale.
        _scale_notes_cache: A dictionary to store a tuple of scale key and scale type as keys and scale notes as values.
    
    """

    def __init__(self,
                 chromatic_scale: List[str] = CHROMATIC_SCALE
                 ) -> None:

        self._chromatic_scale: List[str] = chromatic_scale
        self._scale_notes_cache: Dict[Tuple[str, str], List[str]] = {}

    def get_or_generate_scale(self, 
                              scale_key: str,
                              scale_type: ScaleTypes
                              ) -> List[str]:
        
        """
        Generates a unique cache key, and then retrieves scale notes from the cache, based on the scale key and scale type.
        If unavailable, generates scale notes and stores them in the cache.

        Args:

            scale_key: The root note of the scale.
            scale_type: The name of the scale type.

        Returns:

            scale_notes: A list containing the scale notes.
        
        """

        cache_key: Tuple[str, str, str] = generate_cache_key("ScaleGenerator", scale_key, scale_type.value)

        scale_notes: List[str] = get_or_generate(cache=self._scale_notes_cache, 
                                                 cache_key=cache_key, 
                                                 generate_function=lambda: self._compute_scale_notes(scale_key=scale_key, 
                                                                                                     scale_type=scale_type))
    
        return scale_notes

    def _compute_scale_notes(self,
                             scale_key: str,
                             scale_type: ScaleTypes
                             ) -> List[str]:
        
        """
        Computes scale notes from scale intervals, based on the scale key and scale type.

        Args:

            scale_key: The root note of the scale.
            scale_type: The name of the scale type.

        Returns:

            scale_notes: A list containing the scale notes.
        
        """

        # Scale key index position in the chromatic scale
        scale_key_index: int = self._chromatic_scale.index(scale_key)

        # Accesses scale intervals dictionary
        intervals: List[int] = scale_intervals[scale_type.value]

        # Computes scale notes from scale intervals via the chromatic scale
        scale_notes: List[str] = generate_sequence_from_intervals(start_position=scale_key_index, 
                                                                  note_sequence=self._chromatic_scale, 
                                                                  intervals=intervals)

        return scale_notes



if __name__ == "__main__":

    print("--------------------")

    demo_scale_generator = ScaleGenerator()

    demo_scale_notes = demo_scale_generator.get_or_generate_scale(scale_key="C", scale_type=ScaleTypes.MAJOR_SCALE)

    print(demo_scale_notes)

    print("--------------------")

    print(demo_scale_generator._scale_notes_cache)

    print("--------------------")
