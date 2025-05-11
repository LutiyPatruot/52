import matplotlib.pyplot as plt
from service.datadase import read_database

data = read_database(2144836254)

#data1 = [35, 25, 20, 20]
#label1 = ["A", "B", "C", "D"]

#data2 = [50, 35, 15]
#label2 = ["E", "F", "G"]

#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

#ax1.pie(data1, labels=label1, autopct="%1.1f%%")
#ax1.set_title("Диограмма доходов")
#ax2.pie(data2, labels=label2, autopct="%1.1f%%")
#ax2.set_title("Диограмма расходов")

#fig.suptitle("Доходы и Расходы в категориях")
#plt.show()

from service.getter_categories import attrs_lexicon

expeces  = []
incomes = []
for obj in attrs_lexicon:
    if obj [0].endswith('expences'):
        expeces.append(obj)
    elif obj[0].endswith('incomes'):
        incomes.append(obj)

expeces_tmp_titles = []
incomes_tmp_titles = []
for e in expeces:
    expeces_tmp_titles.append(e[1].text)
for i in incomes:
    incomes_tmp_titles.append(e[1].text)

to_pie = {"income": {"sum": 0}, "expence": {"sum": 0}}
for d in data:
    category = d["category"]
    amount = d["amount"]

    if d["type"] == "Доход":
        type_="income"
    elif d["type"] == "Расход":
        type_= "expence"

    if category not in to_pie[type_]:
        to_pie[type_][category] = 0
        to_pie[type_][category] += amount
        to_pie[type_]["sum"] += amount

expeces_titles = []
expeces_values = []

incomes_titles = []
incomes_values = []

for e in expeces_tmp_titles:
    if e in to_pie ("expence"):
        value = to_pie["expence"][e] / to_pie["expence"]["sum"] * 100
        expeces_titles.append(e)
        expeces_values.append(value)

for i in incomes_tmp_titles:
    if i in to_pie ("incomes"):
        value = to_pie["incomes"][i] / to_pie["incomes"]["sum"] * 100
        incomes_titles.append(i)
        incomes_values.append(value)

print(incomes_titles)
print(incomes_values,sum (incomes_values))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.pie(incomes_values, labels=incomes_titles, autopct="%1.1f%%")
ax1.set_title("Диограмма доходов")
ax2.pie(incomes_values, labels=expeces_titles, autopct="%1.1f%%")
ax2.set_title("Диограмма расходов")

fig.suptitle("Доходы и Расходы в категориях")
plt.show()
