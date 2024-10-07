from enum import Enum

class ScaleTypes(Enum):

    MAJOR_SCALE = "major_scale"

    NATURAL_MINOR = "natural_minor"

    HARMONIC_MINOR = "harmonic_minor"

    MELODIC_MINOR = "melodic_minor"

    IONIAN_MODE = "ionian_mode"

    DORIAN_MODE = "dorian_mode"

    PHRYGIAN_MODE = "phrygian_mode"

    LYDIAN_MODE = "lydian_mode"

    MIXOLYDIAN_MODE = "mixolydian_mode"

    AEOLIAN_MODE = "aeolian_mode"

    LOCRIAN_MODE = "locrian_mode"

    PENTATONIC_MAJOR = "pentatonic_major"

    PENTATONIC_MINOR = "pentatonic_minor"

class ChordTypes(Enum):

    TRIAD = "triad"

    SEVENTH = "seventh"
