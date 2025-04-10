import matplotlib.pyplot as plt

#данные графиков
x = ["Март","апрель","май","июнь","июль","август"]
incomes = [5000, 4000, 3300, 13000, 15000, 17000]
expences = [7000, 6000, 1200, 10000, 16000, 19000]

plt.plot(x, incomes, label="Доходы")
plt.plot(x, expences, label="Расходы")
plt.legend()
plt.grid()

plt.show()