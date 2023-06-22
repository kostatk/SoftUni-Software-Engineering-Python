from math import floor

record_in_sec = float(input())
distance_in_meters = float(input())
time_per_meter_in_sec = float(input())

slowing_in_sec = floor(distance_in_meters / 50) * 30

total_time_in_sec = (distance_in_meters * time_per_meter_in_sec) + slowing_in_sec

diff = abs(record_in_sec - total_time_in_sec)

if total_time_in_sec < record_in_sec:
    print(f"Yes! The new record is {total_time_in_sec:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")
