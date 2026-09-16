import csv
import time

from finalToolkit.word_to_number import word_to_number
from dataclasses import dataclass
from statistics import mean








def log_time(func):

    def wrapping_function(*args):
        timer_start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        time_taken = end-timer_start

        print(f"{func.__name__} took {time_taken} seconds")

        return result
    return wrapping_function



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
            self.rows_loaded = 0
            self.rows_dropped = 0
            self.invalid_ages = 0
            self.invalid_ids = 0
            self.duplicate_ids = 0
            self.word_ages = 0
            self.missing_scores = 0
            self.missing_names = 0
            self.missing_cities = 0

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
                self.rows_dropped += 1
                continue

            valid_records.append(i)

        # Convert age to int and remove records with invalid age
        valid_age_records = []

        for i in valid_records:
            try:
                i.age = int(i.age)
                valid_age_records.append(i)
            except ValueError:
                age = i.age.strip().lower()
                if age in word_to_number:
                    i.age = word_to_number[age]
                    self.word_ages += 1
                    valid_age_records.append(i)
                else:
                    self.invalid_ages += 1 
                    self.rows_dropped += 1
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
                self.missing_scores += 1

            valid_score_records.append(i)

        # Convert IDs, remove duplicate IDs, and fix missing name/city
        seen_ids = set()
        cleaned_records = []

        for i in valid_score_records:

            try:
                i.id = int(i.id)
            except ValueError:
                self.invalid_ids += 1 
                self.rows_dropped += 1
                continue

            if i.id in seen_ids:
                self.duplicate_ids += 1 
                self.rows_dropped += 1
                continue

            seen_ids.add(i.id)

            if i.name == "":
                i.name = "Unknown"
                self.missing_names += 1

            if i.city == "":
                i.city = "Unknown"
                self.missing_cities += 1

            cleaned_records.append(i)

        self.records =  cleaned_records



    def stream(self):
        for i in self.records:
            yield i


    @log_time
    def average_score(self):
        score = []
        for i in self.records:
            score.append(i.score)
        return mean(score)

    @log_time
    def people_per_city(self):
        cities = {}
        for i in self.records:
            if i.city not in cities:
                cities[i.city] = 0
            cities[i.city]+=1

        return cities

    # def oldest(self):
    #     age =[]
    #     for i in self.records:
    #         age.append(i.age)
    #     return max(age)
    # def youngest(self):
    #     age =[]
    #     for i in self.records:
    #         age.append(i.age)
    #     return min(age)

    # if in case user wants to later acces the info of oldest or youngest
    @log_time
    def oldest(self):
        return max(self.records,key = lambda i:i.age)

    @log_time
    def youngest(self):
        return min(self.records,key = lambda i:i.age)









dataset = Dataset("messy_people (1).csv")
dataset.clean()



for record in dataset.stream():
    print(record)
print(dataset.people_per_city())
print(dataset.average_score())
print(dataset.oldest())
print(dataset.youngest())