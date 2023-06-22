length_in_meters = float(input())
width_in_meters = float(input())

workplace_length = 1.2
workplace_width = 0.7
corridor_width = 1

workplaces_per_width = (width_in_meters - corridor_width) // workplace_width
workplaces_per_length = length_in_meters // workplace_length

workplaces = workplaces_per_width * workplaces_per_length - 3

print(int(workplaces))