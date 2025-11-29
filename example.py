from dataclasses import dataclass
from typing import Generator


@dataclass
class StringSplitter:
    string: str

    def get_chars(self) -> Generator[str]:
        for char in self.string:
            yield char


a_generator = StringSplitter("somestring")
for idx, char in enumerate(a_generator.get_chars()):
    if idx > 5:
        break
    print(char)
