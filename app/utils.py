from typing import List

def generate_sequence_from_intervals(start_position: int, 
                                     note_sequence: List[str], 
                                     intervals: List[int]
                                     ) -> List[str]:
    
    """
    A function to wrap around a sequence of notes in steps of intervals to compute a new sequence of notes.
    
    Args:

        start_position: The index position in the sequence of notes where the new sequence begins.
        note_sequence: The sequence of notes that the new sequence is derived from.
        intervals: The sequence of intervals that determine the new sequence of notes.

    Returns:

        A list of notes derived from the original sequence of notes.

    """
    
    return [note_sequence[(start_position + interval) % len(note_sequence)] for interval in intervals]

def generate_string(start_position: int, 
                    note_sequence: List[str], 
                    scale_or_chord: List[str], 
                    frets: range
                    ) -> List[str]:

    """
    A function to wrap around a sequence of notes with reference to a sequence of scale notes or chord notes, in steps of intervals, to compute a guitar string representation.
    
    Args:

        start_position: The index position in the sequence of notes where the guitar string representation begins.
        note_sequence: The sequence of notes that must correspond with the scale notes or chord notes, in order to build the guitar string representation.
        scale_or_chord: The sequence of notes from either a scale or a chord.
        frets: A range object, representing the fret positions on the fretboard.

    Returns:

        A list of notes derived from the scale notes or chord notes that forms the guitar string representation. 

    """

    return [note_sequence[(start_position + fret) % len(note_sequence)] if note_sequence[(start_position + fret) % len(note_sequence)] in scale_or_chord else "__" for fret in frets]



if __name__ == "__main__":

    chromatic_scale = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

    scale_notes = ["C", "D", "E", "F", "G", "A", "B"]

    start_position = chromatic_scale.index("C")

    intervals = [0, 2, 4, 5, 7, 9, 11]

    frets = range(16)

    print(generate_sequence_from_intervals(start_position=start_position, note_sequence=chromatic_scale, intervals=intervals))

    print(generate_string(start_position=start_position, note_sequence=chromatic_scale, scale_or_chord=scale_notes, frets=frets))
