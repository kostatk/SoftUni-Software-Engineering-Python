
while True:
    destination = input()
    if destination == "End":
        break
    min_budget = float(input())
    saved = 0
    while saved < min_budget:
        amount = float(input())
        saved += amount
    print(f"Going to {destination}!")
