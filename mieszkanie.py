import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt


current_price = 120000  
annual_growth_rate = 0.05  
years = 5  
nominal_rate = 0.12  
monthly_rate = nominal_rate / 12 
months = years * 12  


future_price = current_price * (1 + annual_growth_rate) ** years

s
monthly_savings = npf.pmt(rate=monthly_rate, nper=months, pv=0, fv=-future_price, when='end')


monthly_prices = [current_price * (1 + annual_growth_rate) ** (month / 12) for month in range(months + 1)]
monthly_investment = np.zeros(months + 1)
balance = 0

for month in range(1, months + 1):
    balance = balance * (1 + monthly_rate) + monthly_savings
    monthly_investment[month] = balance


plt.figure(figsize=(10, 6))


plt.plot(range(months + 1), monthly_prices, label="Apartment Price", linestyle="--")


plt.plot(range(months + 1), monthly_investment, label="Investment Value", linestyle="-")


plt.title("Apartment Price vs Investment Growth Over 5 Years")
plt.xlabel("Months")
plt.ylabel("Value (PLN)")
plt.legend()
plt.grid()


plt.show()


print(f"Orientacyjna cena mieszkania za 5 lat: {future_price:.2f} zł")
print(f"Miesięczna wpłata do banku: {monthly_savings:.2f} zł")
