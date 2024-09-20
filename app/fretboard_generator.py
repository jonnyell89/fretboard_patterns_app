
"""
    This version contains:

        guitar_string(note, scale=scale_patterns["chromatic_scale"], length=16,)

        fret_marker(length=16)

        fretboard(tuning)

            guitar_string(note)

        scales(note, scale_pattern, scale=scale_patterns["chromatic_scale"])

        fretboard_scales(note, scale_pattern, tuning)

            scales(note, scale_pattern)

            fretboard(tuning)

        chords(note, scale_pattern, chord_pattern)

            scales(note, scale_pattern)

        fretboard_chords(note, scale_pattern, chord_pattern, tuning)

            chords(note, scale_pattern, chord_pattern)

            fretboard(tuning)

            fret_marker()

    Plus:

        user_display_1D(function)

        user_display_2D(function)

        user_display_3D(function)

        

    The user_display functions are not yet defined to format the lists returned by the main body of functions.

    The 'e_standard' tuning and the 'chromatic_scale' pattern still contain spaces.

"""



tunings = {
    
    "e_standard": ["E ", "A ", "D ", "G ", "B ", "E "]
    
}

scale_patterns = {

    "chromatic_scale": ["C ", "C#", "D ", "Eb", "E ", "F ", "F#", "G ", "Ab", "A ", "Bb", "B "],

    "major_scale": [0, 2, 4, 5, 7, 9, 11],

    "natural_minor": [0, 2, 3, 5, 7, 8, 10],

    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],

    "melodic_minor": [0, 2, 3, 5, 7, 9, 11]
    
}

chord_patterns = {

    "notes_3": [0, 2, 4],

    "notes_4": [0, 2, 4, 6]
    
}



"""
    Generate a guitar string, starting at a specific point in the scale.

    Call function once for every string on the fretboard, where the specific point is determined by the desired tuning.

    Generate a major scale from the chromatic scale.

    Generate a guitar string where only the specific notes in the major scale are displayed.

    Call function once for every string on the fretboard, where the specific point is determined by the desired tuning.

    Generate the standard chords for a specific scale.

    Generate the standard chords for a specific scale and display each chord, relative to the fretboard.

    Generate chord names to be displayed in tandem with the fretboard display.

"""



# This function uses a list comprehension to return a string of specific length, from a specific point in the scale.
def guitar_string(note, scale=scale_patterns["chromatic_scale"], length=16):

    start = scale.index(note)

    string = [scale[(start + index) % len(scale)] for index in range(length)]

    return string

# print(guitar_string("C "))



# This function uses a list comprehension to return a representation of the frets on a fretboard.
def fret_marker(length=16):

    frets = [str(fret) if fret >= 10 else str(fret) + " " for fret in range(length)]

    return frets

# print(fret_marker())



# This function applies the guitar_string function to every note in a specific tuning.
def fretboard(tuning):
    
    all_strings = [guitar_string(note) for note in tuning[::-1]]

    # This function returns the entire fretboard as a nested list.
    return all_strings

# fretboard(tunings["e_standard"])



# This function uses a list comprehension to return a specific scale, derived from the chromatic scale.
def scales(note, scale_pattern, scale=scale_patterns["chromatic_scale"]):

    start = scale.index(note)

    scale_notes = [scale[(start + scale_pattern[index % len(scale_pattern)]) % len(scale)] for index in range(len(scale_pattern))]

    # This function returns a specific scale, derived from the chromatic scale.
    return scale_notes

# print(scales("C ", scale_patterns["major_scale"]))



# This function applies the scales function and the guitar_string function to every note in a specific tuning.
def fretboard_scales(note, scale_pattern, tuning):

    scale_notes = scales(note, scale_pattern)

    all_strings = fretboard(tuning)

    string_notes = [[note if note in scale_notes else "  " for note in string] for string in all_strings]

    string_notes.append(fret_marker())

    # This function returns a scale in the context of the fretboard, as a nested list.
    return string_notes

# fretboard_scales("C ", scale_patterns["major_scale"], tunings["e_standard"])



# This function returns the chords derived from any scale.
def chords(note, scale_pattern, chord_pattern):

    scale_notes = scales(note, scale_pattern)

    chord_notes = [[scale_notes[(index + note) % len(scale_notes)] for note in chord_pattern] for index in range(len(scale_notes))]

    # This function returns the standard chords derived from a specific scale, as a nested list.
    return chord_notes

# chords("C ", scale_patterns["major_scale"], chord_patterns["notes_4"])



# This function returns the standard chords derived from a specific scale, in the context of the fretboard.
def fretboard_chords(note, scale_pattern, chord_pattern, tuning):

    chord_notes = chords(note, scale_pattern, chord_pattern)

    all_strings = fretboard(tuning)

    chord_fretboards = []

    for chord in chord_notes:

        string_chords = [[note if note in chord else "  " for note in string] for string in all_strings]

        string_chords.append(fret_marker())

        chord_fretboards.append(string_chords)
        
    # This function returns the standard chords in the context of the fretboard, as a nested list, contained in a list.
    return chord_fretboards

#fretboard_chords("C ", scale_patterns["major_scale"], chord_patterns["notes_4"], tunings["e_standard"])





# This function calls functions that return a 1D list.
def user_display_1D(function):

    print(function)

    print()



# This function calls functions that return a 2D list.
def user_display_2D(function):

    for index in function:

        print(index)
    
    print()



# This function calls functions that return a "3D" list.
def user_display_3D(function):

    for outer in function:

        for inner in outer:

            print(inner)

        print()





print("guitar_string: generates a guitar string representation\n")

user_display_1D(guitar_string("C "))



print("--------------------\n")

print("fret_marker: generates the fret marker representation\n")

user_display_1D(fret_marker())



print("--------------------\n")

print("fretboard: generates a chromatic fretboard representation\n")

user_display_2D(fretboard(tunings["e_standard"]))



print("--------------------\n")

print("scales: generates a scale\n")

user_display_1D(scales("C ", scale_patterns["major_scale"]))



print("--------------------\n")

print("fretboard_scales: generates a complete fretboard representation, including the fret marker and the scale mapped to the fretboard.\n")

user_display_2D(fretboard_scales("C ", scale_patterns["major_scale"], tunings["e_standard"]))



print("--------------------\n")

print("chords: generates the chords of a scale\n")

user_display_2D(chords("C ", scale_patterns["major_scale"], chord_patterns["notes_4"]))



print("--------------------\n")

print("fretboard_chords: generates a complete fretboard representation, including the fret marker and the chords mapped to the fretboard.\n")

user_display_3D(fretboard_chords("C ", scale_patterns["major_scale"], chord_patterns["notes_4"], tunings["e_standard"]))




