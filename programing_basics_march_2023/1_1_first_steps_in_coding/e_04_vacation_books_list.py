num_of_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())

total_hours_for_reading = num_of_pages // pages_per_hour
hours_needed_per_day = total_hours_for_reading // days_for_reading

print(hours_needed_per_day)

