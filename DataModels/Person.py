from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Person:

    id: int
    firstname: str
    lastname: str
    age: int
