from dataclasses import dataclass

@dataclass
class Record:
    id: int
    name: str
    age: int
    city: str
    score: float

    def Validity(self):
        values = [self.id, self.name, self.age, self.city, self.score]
        return not any(value == "" for value in values)