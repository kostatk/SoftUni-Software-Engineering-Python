pool_volume = int(input())
pipe_one_l_per_hour = int(input())
pipe_two_l_per_hour = int(input())
hours_missing = float(input())

filled_volume_from_one = hours_missing * pipe_one_l_per_hour
filled_volume_from_two = hours_missing * pipe_two_l_per_hour

total_filled = filled_volume_from_two + filled_volume_from_one

if total_filled <= pool_volume:
    print(f"The pool is {total_filled/pool_volume*100:.2f}% full. Pipe 1: {filled_volume_from_one/total_filled*100:.2f}%. "
          f"Pipe 2: {filled_volume_from_two/total_filled*100:.2f}%.")
else:
    diff = total_filled - pool_volume
    print(f"For {hours_missing} hours the pool overflows with {diff:.2f} liters.")