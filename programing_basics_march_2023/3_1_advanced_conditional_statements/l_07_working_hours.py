time = int(input())
day = input()

if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or
        day == "Saturday") and 10 <= time <= 18:
    print("open")
else:
    print("closed")


