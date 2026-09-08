import csv
from dataclasses import dataclass
with open("messy_people (1).csv",'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    data = list(csv_reader)
    # print(data)


# Mero normal Record Class

# class Record:
#     def __init__(self,id,name,age,city,score):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.city = city
#         self.score = score


@dataclass
class Record:
    id:int
    name:str
    age:int
    city:str
    score: float

    def Validity(self):
        if(self.id == "" or self.name == "" or self.age == "" or self.city == "" or self.score == ""):
            return False
        else:
            return True


recordObjList = []
# obj1 = record(data[])
for i in data:
    obj = Record(i["id"],i["name"],i["age"],i["city"],i["score"])
    recordObjList.append(obj)
    print( obj.Validity())

