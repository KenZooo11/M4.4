import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
operator = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
a = float(input("Wprowadź pierwszą liczbę: "))
b = float(input("Wprowadź drugą liczbę: "))    

if operator == 1:
    logging.info(f"Dodaję {a} i {b}")
    print(f"Wynik wynosi ", a + b)
elif operator == 2:
    logging.info(f"Odejmuję {a} i {b}")
    print(f"Wynik wynosi ", a - b)
elif operator == 3:
    logging.info(f"Mnożę {a} i {b}")
    print(f"Wynik wynosi ", a * b)
elif operator == 4:
    logging.info(f"Dzielę {a} i {b}")
    if b == 0:
        logging.error("Nie można dzielić przez zero!")
    print(f"Wynik wynosi ", a / b)