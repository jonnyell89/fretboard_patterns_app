
class PitchFretboard:

    def __init__(self):

        pass

    # This function returns the scientific pitch notation in the context of the fretboard, relative to a specific tuning.
    def scientific_pitch_notation(tuning, pitch_notation):

        # Returns the entire fretboard representation as a two-dimensional list
        fretboard_notes = fretboard(tuning)

        # Holds each scientific pitch notation fretboard representation as a two-dimensional list
        fretboard_pitch = []

        # This for loop enables the following for loop to access each guitar string representation of the fretboard_notes two-dimensional list
        for index, string in enumerate(fretboard_notes[::-1]):

            # Returns the open string pitch notation for each guitar string representation
            pitch = pitch_notation[index]

            # Holds the pitch notation of each note for each guitar string representation
            note_pitch = []

            # This for loop accesses each note in the guitar string representation, incrementing the pitch with each octave threshold.
            for index, note in enumerate(string):

                # This if statement prevents pitch incrementation if the 'C' note occurs as the first note in a guitar string representation
                if note == "C" and index != 0:

                    pitch += 1

                else:

                    pass

                # Appends the pitch notation to the note_pitch list with each iteration
                note_pitch.append(str(pitch))

            # Inserts each pitch notation guitar string representation at the front of the fretboard_pitch two-dimensional list
            fretboard_pitch.insert(0, note_pitch)
        
        # Appends a fretboard marker representation to the end of the fretboard_pitch two-dimensional list
        fretboard_pitch.append(fret_marker())

        # This function returns a pitch notation fretboard representation as a two-dimensional list.
        return fretboard_pitch

# scientific_pitch_notation(tunings["e_standard"], pitch_notations["e_standard"])
