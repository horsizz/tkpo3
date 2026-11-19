import tkinter as tk
from calculator import calculate_monthly_payment


def calculate():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        years = float(years_entry.get())
        monthly = calculate_monthly_payment(principal, rate, years)
        result_label.config(text=f"Ежемесячный платёж: {monthly:.2f}")
    except ValueError:
        result_label.config(text="Ошибка: введите корректные числа")


root = tk.Tk()
root.title("Калькулятор ипотеки")

tk.Label(root, text="Сумма кредита:").grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)
principal_entry.insert(0, "1000000")

tk.Label(root, text="Годовая ставка (%):").grid(row=1, column=0, padx=10, pady=10)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=10)
rate_entry.insert(0, "10")

tk.Label(root, text="Срок (лет):").grid(row=2, column=0, padx=10, pady=10)
years_entry = tk.Entry(root)
years_entry.grid(row=2, column=1, padx=10, pady=10)
years_entry.insert(0, "10")

calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

calculate()
root.mainloop()
