from typing import List, Dict, Tuple, Callable, Any

from config.config import CHROMATIC_SCALE
from app.library.intervals import scale_intervals

def generate_sequence_from_intervals(start_position: int, 
                                     note_sequence: List[str], 
                                     intervals: List[int]
                                     ) -> List[str]:
    
    """
    A function that uses a sequence of notes and an interval pattern to compute a new sequence of notes.
    
    Args:

        start_position: The index position in the sequence of notes where the new sequence begins.
        note_sequence: The sequence of notes that the new sequence is derived from.
        intervals: The interval pattern that determines the new sequence of notes.

    Return:

        A list of notes derived from the original sequence of notes.

    """
    
    return [note_sequence[(start_position + interval) % len(note_sequence)] for interval in intervals]

def generate_string(start_position: int, 
                    note_sequence: List[str], 
                    scale_or_chord: List[str], 
                    frets: range
                    ) -> List[str]:

    """
    A function that uses a sequence of notes and a separate sequence of scale notes or chord notes to compute a new sequence of notes.
    
    Args:

        start_position: The index position in the sequence of notes where the guitar string representation begins.
        note_sequence: The sequence of notes that must correspond with the scale notes or chord notes, in order to build the guitar string representation.
        scale_or_chord: The sequence of notes from either a scale or a chord.
        frets: A range object, representing the fret positions on the fretboard.

    Return:

        A list of formatted notes derived from the scale notes or chord notes that forms the guitar string representation. 

    """

    return [f"{note_sequence[(start_position + fret) % len(note_sequence)]:<2}" if note_sequence[(start_position + fret) % len(note_sequence)] in scale_or_chord else "__" for fret in frets]

def generate_cache_key(class_name: str, *args) -> Tuple[Any, ...]:

    """
    A function to generate a cache key, based on the name of the class and its own input arguments.
    
    Args:

        class_name: The name of the class.
        *args: The input arguments specific to the class.

    Return:

        A tuple representing the unique cache key.

    """

    return (class_name, *args)

def get_or_generate(cache: Dict[Tuple[Any, ...], Any], 
                    cache_key: Tuple[Any, ...], 
                    generate_function: Callable[[], Any]
                    ) -> Any:

    """
    A function that uses a cache key to retrieve data from the cache.
    If not available, generates the data and stores it in the cache.

    Args:

        cache: A dictionary structure for caching.
        cache_key: A unique tuple.
        generate_function: A function to generate the data, if not available in the cache.

    Return:

        return_value: The data output of the generator function.
    
    """

    if cache_key in cache:

        return cache[cache_key]
    
    return_value = generate_function()

    cache[cache_key] = return_value

    return return_value

def determine_pattern_type(note_sequence: List[str], 
                           interval_sequence: Dict[str, Tuple[int, ...]], 
                           chromatic_scale: List[str] = CHROMATIC_SCALE
                           ) -> str:

    """
    A function to match a sequence of notes to the correct interval pattern.

    Args:

        note_sequence: The scale notes or chord notes to be matched to the interval sequence.
        interval_sequence: The dictionary containing scale intervals and chord intervals.
        chromatic_scale: The twelve note chromatic scale.

    Return:

        pattern_type: The name of the sequence of notes.
    
    """

    root_index = chromatic_scale.index(note_sequence[0])

    note_intervals = [(index - root_index) % len(chromatic_scale) for index, note in enumerate(chromatic_scale) if note in note_sequence]

    intervals = tuple(note_intervals)

    for pattern_type, interval_pattern in interval_sequence.items():

        if interval_pattern == intervals:

            return pattern_type
        
    return None



if __name__ == "__main__":

    chromatic_scale = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

    scale_notes = ["C", "D", "E", "F", "G", "A", "B"]

    start_position = chromatic_scale.index("C")

    intervals = [0, 2, 4, 5, 7, 9, 11]

    frets = range(16)

    print(generate_sequence_from_intervals(start_position=start_position, note_sequence=chromatic_scale, intervals=intervals))

    print(generate_string(start_position=start_position, note_sequence=chromatic_scale, scale_or_chord=scale_notes, frets=frets))

    print(determine_pattern_type(note_sequence=scale_notes, interval_sequence=scale_intervals))
