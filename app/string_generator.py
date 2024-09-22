from typing import List

from config.config import CHROMATIC_SCALE, STRING_LEN

class StringGenerator:

    """
    A class to generate a guitar string representation based on the chromatic scale.

    Attributes:

        root_note: The root note of the guitar string.
        string_len: The number of notes on the guitar string.
        chromatic_scale: The twelve note chromatic scale.
        root_index: The root note index of the guitar string, relative to the chromatic scale.
    
    """

    def __init__(self, 
                 root_note: str, 
                 string_len: int = STRING_LEN, 
                 chromatic_scale: List[str] = CHROMATIC_SCALE
                 ) -> None:

        self.root_note: str = root_note
        self.string_len: int = string_len
        self.chromatic_scale: List[str] = chromatic_scale
        self.root_index = self.chromatic_scale.index(self.root_note)

    # Generates a list of notes representing a guitar string, starting from a specific point in the chromatic scale.
    def generate_string(self) -> List[str]:

        return [self.chromatic_scale[(self.root_index + note) % len(self.chromatic_scale)] for note in range(self.string_len)]
    
    # Sets a new root note for the guitar string representation.
    def set_root(self, new_root_note: str) -> None:

        self.root_note: str = new_root_note

    # Sets a new length for the guitar string representation.
    def set_length(self, new_string_len: int) -> None:

        self.string_len: int = new_string_len



if __name__ == "__main__":

    print("--------------------")

    demo_string = StringGenerator("C")

    print(demo_string.generate_string())


