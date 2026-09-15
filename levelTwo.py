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


class LevelTwo:

    def __init__(self, records):
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

        return cleaned_records


# Create Record objects
recordObjList = []

for i in data:
    obj = Record(i["id"], i["name"], i["age"], i["city"], i["score"]
    )
    recordObjList.append(obj)


# Level 2 cleaning
level_two = LevelTwo(recordObjList)
cleaned_records = level_two.clean()


# Check validity
for i in cleaned_records:
    print(i.Validity())



# valid_record =[]

# for i in range(len(recordObjList)):
#     if recordObjList[i].age == "" and recordObjList[i].score == "" and recordObjList[i].id == "" and recordObjList[i].name == "" and recordObjList[i].city == "": 
#         continue
#     else:
#         valid_record.append(recordObjList[i])




# super_valid_record =[]
# for i in valid_record:
#         try:
#             i.age = int(i.age)
#             super_valid_record.append(i)
#         except ValueError:
#             continue


# valid_score_record=[]
# for i in super_valid_record:
#     try:
#         i.score = float(i.score)
#         valid_score_record.append(i)
#     except ValueError:
#         continue

# for_mean =[]
# for i in valid_score_record:
#     for_mean.append(i.score)


# mean_number = mean(for_mean)

# print(mean_number)

# updated_with_mean_score = []
# for i in super_valid_record:
#     try:
#         i.score = float(i.score)

#         updated_with_mean_score.append(i)
#     except ValueError:
#         i.score = mean_number
#         updated_with_mean_score.append(i)
        



# valid_id_record=[]
# for i in updated_with_mean_score:
#     try:
#         i.id = int(i.id)
#         valid_id_record.append(i)
#     except ValueError:
#         continue


# seen_ids = set()
# non_duplicate_id=[]
# for i in valid_id_record:
#     if i.id in seen_ids:
#         continue
#     else:
#         seen_ids.add(i.id)
#         non_duplicate_id.append(i)



# for i in non_duplicate_id:
#     if i.name == "":
#         i.name = "Unknown"
# for i in non_duplicate_id:
#     if i.city == "":
#         i.city = "Unknown"


# validity_check=[]
# for i in non_duplicate_id:
#    print(i.Validity())


