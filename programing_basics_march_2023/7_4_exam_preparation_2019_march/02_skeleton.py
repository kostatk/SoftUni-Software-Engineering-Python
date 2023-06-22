minutes_of_control = int(input())
seconds_of_control = int(input())
distance = float(input())
seconds_per_100 = int(input())

control_in_sec = minutes_of_control * 60 + seconds_of_control

our_time = (distance / 100 * seconds_per_100) - (distance / 120 * 2.5)

if our_time <= control_in_sec:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {our_time:.3f}.")
else:
    needed = our_time - control_in_sec
    print(f"No, Marin failed! He was {needed:.3f} second slower.")
