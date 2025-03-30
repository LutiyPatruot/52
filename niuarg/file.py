import csv

fieldnames = ["chat_id", "date", "type", "category", "amount"]
data = {
    'chat_id': 2144836254,
    'date': '30.03.2025',
    'type': 'доход',
    'category': 'gift_income',
    'amount': 123
}
#with open("database.csv", "w", ancoding="utf-8") as file:
#    writer = csv.DictWriter(file, fieldnames=fieldnames)
#    writer.writerow(data)i




with open("database.csv", "r", encoding="utf-8") as file:
    data = []
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

print(data)