import pytest

from config.config import FRETBOARD_LEN
from app.string_generator import StringGenerator

def test_string_generator_init():

    string = StringGenerator("E")

    assert string.string_len == FRETBOARD_LEN


