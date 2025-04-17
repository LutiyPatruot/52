from config import database_path
import csv
from datetime import datetime

def write_database(data):
    with open(database_path, "a", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(data.values())

def beautify(rov):
    rov["date"] = datetime.strptime(rov["date"], "%d.%m.%Y")
    rov["amount"] = int(rov["amount"])
    rov["chat_id"] = int(rov["chat_id"])

def read_database(chat_id):
    with open(database_path, "r", encoding="utf8") as file:
        reader = csv.DictReader(file)
        my_data = []
        for rov in reader:
            if rov['chat_id'] == str(chat_id):
                beautify(rov)
                my_data.append(rov)
        return my_data
    