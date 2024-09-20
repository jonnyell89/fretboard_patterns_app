
"""
    This version contains:

        guitar_string(note, length=16)

        fret_marker(length=16)

        fretboard(tuning)

            guitar_string(note)

        scales(note, scale_pattern)

        fretboard_scales(note, scale_pattern, tuning)

            scales(note, scale_pattern)

            fretboard(tuning)

        chords(note, scale_pattern, chord_pattern)

            scales(note, scale_pattern)

        fretboard_chords(note, scale_pattern, chord_pattern, tuning)

            chords(note, scale_pattern, chord_pattern)

            fretboard(tuning)

            fret_marker()

        chord_construction(note, scale_pattern, chord_pattern)

            chords(note, scale_pattern, chord_pattern)

            guitar_string(note, length=16)

        scientific_pitch_notation(tuning, pitch_notation)

            fretboard(tuning)

            fret_marker()

    Plus:

        user_display_1D(function)

        user_display_2D(function)

        user_display_3D(function)

"""



tunings = {
    
    "e_standard": ["E", "A", "D", "G", "B", "E"],

    "open_c": ["C", "G", "C", "G", "C", "E"]
    
}

pitch_notations = {

    "e_standard": [2, 2, 3, 3, 3, 4],

    "open_c": [2, 2, 3, 3, 4, 4]

}

scale_patterns = {

    "chromatic_scale": ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"],

    "major_scale": [0, 2, 4, 5, 7, 9, 11],

    "natural_minor": [0, 2, 3, 5, 7, 8, 10],

    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],

    "melodic_minor": [0, 2, 3, 5, 7, 9, 11],

    "ionian_mode": [0, 2, 4, 5, 7, 9, 11],

    "dorian_mode": [0, 2, 3, 5, 7, 9, 10],

    "phrygian_mode": [0, 1, 3, 5, 7, 8, 10],

    "lydian_mode": [0, 2, 4, 6, 7, 9, 11],

    "mixolydian_mode": [0, 2, 4, 5, 7, 9, 10],

    "aeolian_mode": [0, 2, 3, 5, 7, 8, 10],

    "locrian_mode": [0, 1, 3, 5, 6, 8, 10],

    "pentatonic_major": [0, 2, 4, 7, 9],

    "pentatonic_minor": [0, 3, 5, 7, 10]
    
}

chord_patterns = {

    "notes_3": [0, 2, 4],

    "notes_4": [0, 2, 4, 6]
    
}

note_intervals = {

    0: "R",
    1: "b2",
    2: "2",
    3: "3m",
    4: "3M",
    5: "4",
    6: "b5",
    7: "5",
    8: "#5",
    9: "6",
    10: "7",
    11: "7M",
    12: "8",
    13: "b9",
    14: "9",
    15: "#9",
    16: "b11",
    17: "11",
    18: "#11",
    19: "12",
    20: "b13",
    21: "13",
    22: "#13"

}

chord_names = {

    "": [0, 4, 7],
    "m": [0, 3, 7],
    
}

key_names = {

    0: ["C"],
    1: ["Db", "C#"],
    2: ["D"],
    3: ["Eb", "D#"],
    4: ["E"],
    5: ["F"],
    6: ["Gb", "F#"],
    7: ["G"],
    8: ["Ab", "G#"],
    9: ["A"],
    10: ["Bb", "A#"],
    11: ["B"]

}



"""
    Generate a guitar string, starting at a specific point in the scale.

    Call function once for every string on the fretboard, where the specific point is determined by the desired tuning.

    Generate a major scale from the chromatic scale.

    Generate a guitar string where only the specific notes in the major scale are displayed.

    Call function once for every string on the fretboard, where the specific point is determined by the desired tuning.

    Generate the chords for a specific scale.

    Generate the chords for a specific scale and display each chord, relative to the fretboard.

    Generate chord intervals to be displayed in tandem with the fretboard display.

"""



# This function uses a list comprehension to return a guitar string representation of specific length, from a specific point in the chromatic scale.
def guitar_string(note, length=16):

    # Defines the chromatic scale as the default scale pattern
    scale = scale_patterns["chromatic_scale"]

    # Returns the index position of the note in the chromatic scale
    start = scale.index(note)

    # This list comprehension returns a guitar string representation by iterating over the chromatic scale from the start index position
    # The modulus operator accounts for the difference between len(scale) and range(length) by wrapping the for loop around the length of the chromatic scale
    string = [scale[(start + index) % len(scale)] for index in range(length)]

    # This function returns the a guitar string representation as a list
    return string

# print(guitar_string("E"))



# This function uses a list comprehension to return a representation of the frets on a fretboard.
def fret_marker(length=16):

    # This list comprehension returns a list of string format integers
    frets = [str(fret) for fret in range(length)]

    # This function returns the fretboard marker representation as a list
    return frets

# fret_marker()



# This function applies the guitar_string function to every note in a specific tuning.
def fretboard(tuning):
    
    # This list comprehension returns a two-dimensional list of guitar string representations
    all_strings = [guitar_string(note) for note in tuning[::-1]]

    # This function returns the entire fretboard representation as a two-dimensional list
    return all_strings

# fretboard(tunings["e_standard"])



# This function uses a list comprehension to return a specific scale, derived from the chromatic scale.
def scales(note, scale_pattern):

    # Defines the chromatic scale as the default scale pattern
    scale = scale_patterns["chromatic_scale"]

    # Returns the index position of the note in the chromatic scale
    start = scale.index(note)

    # This list comprehension returns a specific scale by iterating over the chromatic scale from the start index position
    # The modulus operator accounts for the difference between len(scale_pattern) and len(scale) by wrapping the for loop around the length of the scale_pattern
    # scale_notes = [scale[(start + scale_pattern[index % len(scale_pattern)]) % len(scale)] for index in range(len(scale_pattern))]
    
    # This list comprehension returns a specific scale by iterating over the chromatic scale from the start index position
    # The modulus operator accounts for the difference between len(scale) and the number of iterations in the scale_pattern for loop
    scale_notes = [scale[(start + interval) % len(scale)] for interval in scale_pattern]

    # This function returns a specific scale as a list, derived from the chromatic scale.
    return scale_notes

# scales("C", scale_patterns["major_scale"])



# This function calls the scales function and the guitar_string function to return a fretboard representation containing only the notes derived from a specific scale
def fretboard_scales(note, scale_pattern, tuning):

    # Returns a specific scale as a list, derived from the chromatic scale.
    scale_notes = scales(note, scale_pattern)

    # Returns the entire fretboard representation as a two-dimensional list
    all_strings = fretboard(tuning)

    # This two-dimensional list comprehension retains only the notes present in scale_notes from the all_strings two-dimensional list
    string_notes = [[note if note in scale_notes else "" for note in string] for string in all_strings]

    # Appends a fretboard marker representation to the end of the string_notes two-dimensional list
    string_notes.append(fret_marker())

    # This function returns a scale in the context of the fretboard, as a two-dimensional list.
    return string_notes

# fretboard_scales("C", scale_patterns["major_scale"], tunings["e_standard"])



# This function returns the chords derived from a specific scale.
def chords(note, scale_pattern, chord_pattern):

    # Returns a specific scale as a list, derived from the chromatic scale.
    scale_notes = scales(note, scale_pattern)

    # This two-dimensional list comprehension iterates over the chord_pattern list of intervals, relative to the scale_notes list of indices.
    # The modulus operator accounts for the difference between len(scale_notes) and the number of iterations in the chord_pattern two-dimensional for loop
    chord_notes = [[scale_notes[(index + interval) % len(scale_notes)] for interval in chord_pattern] for index in range(len(scale_notes))]

    # This function returns the chords derived from a specific scale, as a two-dimensional list.
    return chord_notes

# chords("C", scale_patterns["major_scale"], chord_patterns["notes_4"])



# This function returns the chords derived from a specific scale, in the context of the fretboard.
def fretboard_chords(note, scale_pattern, chord_pattern, tuning):

    # Returns the chords derived from a specific scale, as a two-dimensional list.
    chord_notes = chords(note, scale_pattern, chord_pattern)

    # Returns the entire fretboard representation as a two-dimensional list
    all_strings = fretboard(tuning)

    # Holds each complete chord fretboard representation as a three-dimensional list
    chord_fretboards = []

    # This for loop enables the following list comprehension to access each chord as a list of notes
    for chord in chord_notes:

        # This two-dimensional list comprehension retains only the notes present in chord from the all_strings two-dimensional list
        string_chords = [[note if note in chord else "" for note in string] for string in all_strings]

        # Appends a fretboard marker representation to the end of the string_chords two-dimensional list
        string_chords.append(fret_marker())

        # Appends the complete chord fretboard representation to the chord_fretboards three-dimensional list
        chord_fretboards.append(string_chords)
        
    # This function returns the chords in the context of the fretboard, as a three-dimensional.
    return chord_fretboards

# fretboard_chords("C", scale_patterns["major_scale"], chord_patterns["notes_4"], tunings["e_standard"])



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





# This function calls functions that return a 1D list.
def user_display_1D(input_function):

    # If input_function is a list of strings
    if all(isinstance(element, str) for element in input_function):

        # This line returns a list of strings, formatted to contain a space to the right of a single digit number.
        items = [f"{str(item):<2}" for item in input_function]

        print(items)

    # # If input_function is a list of integers
    # elif all(isinstance(element, int) for element in input_function):
        
    #     # This line returns a list of integers, formatted to contain a space to the left of a single digit number.
    #     items = [f"{item:2d}" for item in input_function]

    #     print(items)

    # If input_function is a list of both strings and integers
    else:

        raise ValueError("This list contains both strings and integers")

    # This print statement adds a line in between calls and can be written out in the final script
    print()



# This function calls functions that return a two-dimensional list.
def user_display_2D(input_function):

    for element in input_function:

        # If element is a list of strings
        if all(isinstance(item, str) for item in element):

            # This line returns a list of strings, formatted to contain a space to the right of a single digit number.
            items = [f"{item:<2}" for item in element]

            print(items)

        # # If element is a list of integers
        # elif all(isinstance(item, int) for item in element):

        #     # This line returns a list of integers, formatted to contain a space to the left of a single digit number.
        #     items = [f"{item:2d}" for item in element]

        #     print(items)

        # If element is a list of both strings and integers
        else:

            raise ValueError("This list contains both strings and integers")

    # This print statement adds a line in between calls and can be written out in the final script
    print()



# This function calls functions that return a three-dimensional list.
def user_display_3D(input_function):

    for outer in input_function:

        for inner in outer:

            # If inner is a list of strings
            if all(isinstance(item, str) for item in inner):

                # This line returns a list of strings, formatted to contain a space to the right of a single digit number.
                items = [f"{item:<2}" for item in inner]

                print(items)

            # # If inner is a list of integers
            # elif all(isinstance(item, int) for item in inner):

            #     # This line returns a list of integers, formatted to contain a space to the left of a single digit number.
            #     items = [f"{item:2d}" for item in inner]

            #     print(items)

            # If inner is a list of both strings and integers
            else:

                raise ValueError("This list contains both strings and integers")

        # This print statement adds a line in between calls and can be written out in the final script
        print()





print("guitar_string: generates a guitar string representation\n")

user_display_1D(guitar_string("C"))



print("--------------------\n")

print("fret_marker: generates the fret marker representation\n")

user_display_1D(fret_marker())



print("--------------------\n")

print("fretboard: generates a chromatic fretboard representation\n")

user_display_2D(fretboard(tunings["e_standard"]))



print("--------------------\n")

print("scales: generates a scale\n")

user_display_1D(scales("C", scale_patterns["major_scale"]))



print("--------------------\n")

print("fretboard_scales: generates a complete fretboard representation, including the fret marker and the scale mapped to the fretboard.\n")

user_display_2D(fretboard_scales("C", scale_patterns["major_scale"], tunings["e_standard"]))



print("--------------------\n")

print("chords: generates the chords of a scale, derived from three notes.\n")

user_display_2D(chords("C", scale_patterns["major_scale"], chord_patterns["notes_3"]))



print("--------------------\n")

print("chord_construction: generates the interval pattern of the chords from a scale, derived from three notes.\n")

user_display_2D(chord_construction("C", scale_patterns["major_scale"], chord_patterns["notes_3"]))



print("--------------------\n")

print("chords: generates the chords of a scale, derived from four notes.\n")

user_display_2D(chords("C", scale_patterns["major_scale"], chord_patterns["notes_4"]))



print("--------------------\n")

print("chord_construction: generates the interval pattern of the chords from a scale, derived from four notes.\n")

user_display_2D(chord_construction("C", scale_patterns["major_scale"], chord_patterns["notes_4"]))



print("--------------------\n")

print("fretboard_chords: generates a complete fretboard representation, including the fret marker and the chords mapped to the fretboard.\n")

user_display_3D(fretboard_chords("C", scale_patterns["major_scale"], chord_patterns["notes_4"], tunings["e_standard"]))



print("--------------------\n")

print("scientific_pitch_notation: generates a complete fretboard representation, including the fret marker and the scientific pitch notation mapped to the fretboard.\n")

user_display_2D(scientific_pitch_notation(tunings["e_standard"], pitch_notations["e_standard"]))




