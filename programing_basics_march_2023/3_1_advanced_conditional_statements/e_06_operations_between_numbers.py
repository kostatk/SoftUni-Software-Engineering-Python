n_one = int(input())
n_two = int(input())
operator = input()

result = 0
even_or_odd = "odd"

if n_two != 0:
    if operator == "+":
        result += n_one + n_two
        if result % 2 == 0:
            even_or_odd = "even"
        print(f"{n_one} {operator} {n_two} = {result} - {even_or_odd}")
    elif operator == "-":
        result += n_one - n_two
        if result % 2 == 0:
            even_or_odd = "even"
        print(f"{n_one} {operator} {n_two} = {result} - {even_or_odd}")
    elif operator == "*":
        result += n_one * n_two
        if result % 2 == 0:
            even_or_odd = "even"
        print(f"{n_one} {operator} {n_two} = {result} - {even_or_odd}")
    elif operator == "/":
        result += n_one / n_two
        print(f"{n_one} / {n_two} = {result:.2f}")
    elif operator == "%":
        result += n_one % n_two
        print(f"{n_one} % {n_two} = {result}")
else:
    print(f"Cannot divide {n_one} by zero")