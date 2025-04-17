import matplotlib.pyplot as plt
from service.datadase import read_database

data = read_database(2144836254)

#создаем данные для оси OX и OY
aggregates = {}
for d in data: 
    formatted_data = d["date"].strftime("%m.%Y")
    type_ = d["type"]
    amount  = d["amount"]
    if formatted_data not in aggregates:
        aggregates[formatted_data] = {"Доход": 0, "Расход": 0}
    aggregates[formatted_data] [type_] += amount

print(aggregates)