import csv


from dataclasses import dataclass
from statistics import mean


with open("messy_people (1).csv", "r") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    data = list(csv_reader)


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




class Dataset:
    def __init__(self,filename):
        with open(filename, "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            data = list(csv_reader)
            records= []

            for i in data:
                obj = Record(
                    i["id"],
                    i["name"],
                    i["age"],
                    i["city"],
                    i["score"]
                )
                records.append(obj)
            self.records = records


    def clean(self):

        # Remove completely blank rows
        valid_records = []

        for i in self.records:
            if i.age == "" and i.score == "" and i.id == "" and i.name == "" and i.city == "":
                continue

            valid_records.append(i)

        # Convert age to int and remove records with invalid age
        valid_age_records = []

        for i in valid_records:
            try:
                i.age = int(i.age)
                valid_age_records.append(i)
            except ValueError:
                continue

        # Find the mean of valid scores
        scores = []

        for i in valid_age_records:
            try:
                scores.append(float(i.score))
            except ValueError:
                continue

        mean_number = mean(scores)

        # Convert scores and replace missing/invalid scores with mean
        valid_score_records = []

        for i in valid_age_records:
            try:
                i.score = float(i.score)
            except ValueError:
                i.score = mean_number

            valid_score_records.append(i)

        # Convert IDs, remove duplicate IDs, and fix missing name/city
        seen_ids = set()
        cleaned_records = []

        for i in valid_score_records:

            try:
                i.id = int(i.id)
            except ValueError:
                continue

            if i.id in seen_ids:
                continue

            seen_ids.add(i.id)

            if i.name == "":
                i.name = "Unknown"

            if i.city == "":
                i.city = "Unknown"

            cleaned_records.append(i)

        self.records =  cleaned_records



    def stream(self):
        for i in self.records:
            yield i

# Create Record objects
recordObjList = []

dataset = Dataset("messy_people (1).csv")

dataset.clean()

for record in dataset.stream():
    print(record)