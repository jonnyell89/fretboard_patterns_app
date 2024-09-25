import pytest

from config.config import CHROMATIC_SCALE, FRETBOARD_LEN
from archive.string_generator import StringGenerator

@pytest.mark.parametrize("root_note", CHROMATIC_SCALE)
def test_string_generator_init(root_note):

    string = StringGenerator(root_note=root_note)

    assert string.string_len == FRETBOARD_LEN


