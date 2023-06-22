from math import floor

record_time_in_sec = float(input())
distance_in_m = float(input())
ivan_time_per_m = float(input())

slowing_in_sec = floor(distance_in_m / 15) * 12.5
ivan_total_time_in_sec = ivan_time_per_m * distance_in_m + slowing_in_sec
not_enough_time = ivan_total_time_in_sec - record_time_in_sec

if ivan_total_time_in_sec < record_time_in_sec:
    print(f"Yes, he succeeded! The new world record is {ivan_total_time_in_sec:.2f} seconds.")
else:
    print(f"No, he failed! He was {not_enough_time:.2f} seconds slower.")