def calculate_monthly_payment(principal, annual_rate, years):
    """Рассчитывает ежемесячный аннуитетный платёж по ипотеке.
    Обновлено после перезагрузки машины L.
    """
    # Пример калькулятора ипотеки для проекта tkpo3
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Все параметры должны быть положительными числами")

    monthly_rate = annual_rate / 100 / 12
    months = years * 12
    payment = (principal * monthly_rate * (1 + monthly_rate) ** months
               / ((1 + monthly_rate) ** months - 1))
    return round(payment, 2)
