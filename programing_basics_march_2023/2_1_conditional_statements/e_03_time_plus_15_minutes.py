hour = int(input())
minutes= int(input())

total_minutes = hour * 60 + minutes + 15

_hour = total_minutes // 60
_minutes = total_minutes % 60

if _hour > 23:
    _hour = 0

if _minutes < 10:
    print(f"{_hour}:0{_minutes}")
else:
    print(f"{_hour}:{_minutes}")