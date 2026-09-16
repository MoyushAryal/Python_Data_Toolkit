from Logic.dataset import Dataset
from Report.report import generate_report


dataset = Dataset("data/messy_people (1).csv")

dataset.clean()

generate_report(dataset)