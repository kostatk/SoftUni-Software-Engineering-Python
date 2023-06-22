num_tabs = int(input())
salary = int(input())

for _ in range(num_tabs):
    cur_web = input()
    if cur_web == "Facebook":
        salary -= 150
    elif cur_web == "Instagram":
        salary -= 100
    elif cur_web == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(int(salary))

