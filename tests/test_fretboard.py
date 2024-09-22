import pytest

from config.config import NUM_STRINGS, STRING_LEN
from app.library.tunings import tunings
from app.fretboard_generator import FretboardGenerator

def test_fretboard_generator_init():

    fretboard = FretboardGenerator()

    assert fretboard.fretboard_len == STRING_LEN

    assert len(fretboard.tuning) == NUM_STRINGS

    assert "x" in fretboard.fretboard_dict

    assert "y" in fretboard.fretboard_dict

@pytest.mark.parametrize("tuning_name, expected_tuning", [
    ("e_standard", tunings["e_standard"][::-1]), 
    ("open_c", tunings["open_c"][::-1])
    ])

def test_fretboard_tuning(tuning_name, expected_tuning):

    fretboard = FretboardGenerator(tuning=tunings[tuning_name])

    assert fretboard.tuning == expected_tuning

def test_generate_fretboard_x():

    fretboard = FretboardGenerator()

    horizontal_fretboard = fretboard.fretboard_dict["x"]

    assert len(horizontal_fretboard) == NUM_STRINGS

    assert all(len(string) == STRING_LEN for string in horizontal_fretboard)

def test_generate_fretboard_y():

    fretboard = FretboardGenerator()

    vertical_fretboard = fretboard.fretboard_dict["y"]

    assert len(vertical_fretboard) == STRING_LEN

    assert all(len(fret_width) == NUM_STRINGS for fret_width in vertical_fretboard)

    horizontal_fretboard = fretboard.fretboard_dict["x"]

    for i in range(NUM_STRINGS):

        for j in range(STRING_LEN):

            assert vertical_fretboard[j][NUM_STRINGS - 1 - i] == horizontal_fretboard[i][j]
