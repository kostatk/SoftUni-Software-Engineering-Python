from math import ceil

name_of_series = input()
episode_length = int(input())
break_time = int(input())

time_for_lunch = break_time / 8
time_for_relax = break_time / 4
remaining_time_for_movie = break_time - time_for_lunch - time_for_relax
remaining_from_break = abs(remaining_time_for_movie - episode_length)

if remaining_time_for_movie >= episode_length:
    print(f"You have enough time to watch {name_of_series} and left with {ceil(remaining_from_break)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(remaining_from_break)} more minutes.")