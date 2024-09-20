from typing import List

from library.intervals import chromatic_scale



class StringGenerator:

    """
    A class to generate a guitar string representation based on the chromatic scale.

    Attributes:

        root: The root note of the guitar string.
        length: The number of notes on the guitar string.
        chromatic_scale: The twelve note chromatic scale.
        root_index: The root note index of the guitar string, relative to the chromatic scale.
    
    """

    def __init__(self, root: str, length: int = 16, chromatic_scale: List[str] = chromatic_scale["chromatic_scale"]) -> None:

        self.root: str = root
        self.length: int = length
        self.chromatic_scale: List[str] = chromatic_scale
        self.root_index = self.chromatic_scale.index(self.root)

    # Generates a list of notes representing a guitar string, starting from a specific point in the chromatic scale.
    def generate_string(self) -> List[str]:

        return [self.chromatic_scale[(self.root_index + note) % len(self.chromatic_scale)] for note in range(self.length)]
    
    # Sets a new root note for the guitar string representation.
    def set_root(self, new_root: str) -> None:

        self.root: str = new_root

    # Sets a new length for the guitar string representation.
    def set_length(self, new_length: int) -> None:

        self.length: int = new_length



print("--------------------")

demo_string = StringGenerator("C")

print(demo_string.generate_string())
