import math

print("Лабораторная работа 2. Часть 2. Вариант 6")
print("Расчёт компонентов технологической смеси")
print("1 — бетон: цемент 0.15, песок 0.35, щебень 0.50")
print("2 — керамика: глина 0.60, песок 0.25, добавка 0.15")
print("3 — сплав: Cu 0.70, Zn 0.25, Pb 0.05")

F = True
while F:
    try:
        choice = int(input("Выберите тип смеси (1, 2 или 3): ").strip())
        if choice in (1, 2, 3):
            F = False
        print("Ошибка: выберите 1, 2 или 3.")
    except ValueError:
        print("Ошибка: введите целое число 1, 2 или 3.")

match choice:
    case 1:
        name = "Бетон"
        fractions = {"цемент": 0.15, "песок": 0.35, "щебень": 0.50}
    case 2:
        name = "Керамика"
        fractions = {"глина": 0.60, "песок": 0.25, "добавка": 0.15}
    case 3:
        name = "Сплав"
        fractions = {"Cu": 0.70, "Zn": 0.25, "Pb": 0.05}

total_fraction = sum(fractions.values())

if not math.isclose(total_fraction, 1.0, rel_tol=0.0, abs_tol=1e-12):
    print(f"Ошибка: сумма долей не равна 1 (получено {total_fraction}).")
    raise SystemExit

print(f"\nПроверка суммы долей: {total_fraction:.2f} — сумма равна 1.")

F = True
while F:
    raw = input("Введите общую массу смеси M, кг (допустимо 1..10000): ").strip().replace(",", ".")
    try:
        M = float(raw)
        if not math.isfinite(M):
            print("Ошибка: число должно быть конечным.")
            continue
        if M < 1 or M > 10000:
            print("Ошибка: допустимый диапазон 1..10000 кг.")
            continue
        F = False
    except ValueError:
        print("Ошибка: введите число.")

if M < 100:
    party_class = "малая партия"
elif M <= 1000:
    party_class = "средняя партия"
else:
    party_class = "крупная партия"

print("\nРезультаты расчёта:")
print(f"Тип смеси: {name}")
print(f"Общая масса партии: {M:.3f} кг")
print()

for component, fraction in fractions.items():
    print(f"{component}: доля = {fraction:.2f}, масса = {M * fraction:.3f} кг")

print()
print(f"Сумма масс компонентов: {sum(M * f for f in fractions.values()):.3f} кг")
print(f"Класс партии: {party_class} (M = {M:.3f} кг)")