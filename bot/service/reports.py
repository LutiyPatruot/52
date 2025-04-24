import matplotlib.pyplot as plt

def trend_line(data):
    aggregates = {}
    for d in data: 
        formatted_data = d["date"].strftime("%m.%Y")
        type_ = d["type"]
        amount  = d["amount"]
        if formatted_data not in aggregates:
            aggregates[formatted_data] = {"Доход": 0, "Расход": 0}
        aggregates[formatted_data] [type_] += amount

    print(aggregates)

    pre_data = []
    for d in aggregates:
        pre_data.append((d, aggregates[d]["Доход"],aggregates[d]["Расход"]))

    months = []
    incomes = []
    expences = []
    for row in pre_data:
        months.append(row[0])
        incomes.append(row[1])
        expences.append(row[2])

    plt.plot(months, incomes, label="Доходы")
    plt.plot(months, incomes, label="Расходы")
    plt.legend()
    plt.grid()
    plt.show()