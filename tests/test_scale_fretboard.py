import pytest

from config.config import CHROMATIC_SCALE
from app.library.intervals import scale_patterns
from app.scale_fretboard import ScaleFretboard

def test_scale_fretboard_init():

    fretboard = ScaleFretboard()
    
    assert "x" in fretboard.scale_fretboard_dict

    assert "y" in fretboard.scale_fretboard_dict

@pytest.mark.parametrize("scale_name, expected_scale", [
    ("major_scale", scale_patterns["major_scale"]), 
    ("natural_minor", scale_patterns["natural_minor"]),
    ("harmonic_minor", scale_patterns["harmonic_minor"]),
    ("melodic_minor", scale_patterns["melodic_minor"]),
    ("ionian_mode", scale_patterns["ionian_mode"]),
    ("dorian_mode", scale_patterns["dorian_mode"]),
    ("phrygian_mode", scale_patterns["phrygian_mode"]),
    ("lydian_mode", scale_patterns["lydian_mode"]),
    ("mixolydian_mode", scale_patterns["mixolydian_mode"]),
    ("aeolian_mode", scale_patterns["aeolian_mode"]),
    ("locrian_mode", scale_patterns["locrian_mode"]),
    ("pentatonic_major", scale_patterns["pentatonic_major"]),
    ("pentatonic_minor", scale_patterns["pentatonic_minor"])
    ])

def test_scale_pattern(scale_name, expected_scale):

    fretboard = ScaleFretboard(scale_pattern=scale_patterns[scale_name])

    assert fretboard.scale_pattern == expected_scale

def test_calculate_scale_notes():

    fretboard = ScaleFretboard()

    assert len(fretboard.scale_notes) == len(fretboard.scale_pattern)

    assert all(note in CHROMATIC_SCALE for note in fretboard.scale_notes)

def test_generate_scale_fretboard():

    fretboard = ScaleFretboard()

def test__apply_scale_to_fretboard():

    fretboard = ScaleFretboard()


