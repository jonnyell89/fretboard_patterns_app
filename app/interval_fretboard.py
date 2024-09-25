
class IntervalFretboard:

    def __init__(self):

        pass

    # This function returns the interval names, relative to the root note of the chords derived from a specific scale.
    def chord_construction(note, scale_pattern, chord_pattern):

        # Returns the chords derived from a specific scale, as a two-dimensional list.
        chord_notes = chords(note, scale_pattern, chord_pattern)

        # Holds each complete chord construction as a two-dimensional list
        chord_intervals = []

        # This for loop enables the following list comprehension to access each chord as a list of notes
        for chord in chord_notes:

            # Returns a two octave guitar string representation, relative to the root note of each chord.
            octaves = guitar_string(chord[0], length=23)

            # This list comprehension returns the index positions of each note in the chord
            # intervals = [octaves.index(note) for note in chord]

            intervals = []

            chord_index = 0

            # This for loop ensures that the chord_notes index positions are appended to intervals in ascending order
            for index, note in enumerate(octaves):

                if note == chord[chord_index]:

                    intervals.append(index)

                    chord_index += 1

                    if chord_index >= len(chord):

                        break

            # This list comprehension accesses the note_intervals dictionary to return a list of note interval names
            interval_names = [note_intervals.get(interval) for interval in intervals]

            # Appends each list of note interval names to the chord_intervals two-dimensional list.
            chord_intervals.append(interval_names)  
        
        # This function returns the note interval names for each chord, as a two-dimensional list.
        return chord_intervals

# print(chord_construction("C", scale_patterns["major_scale"], chord_patterns["notes_4"]))
