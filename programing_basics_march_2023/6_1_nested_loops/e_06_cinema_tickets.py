
student_counter = 0
standard_counter = 0
kid_counter = 0
seat_count = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    cur_empty_seats = int(input())
    for seat in range(cur_empty_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1
        seat_count += 1
    print(f"{movie_name} - {seat_count / cur_empty_seats * 100:.2f}% full.")
    seat_count = 0

print(f"Total tickets: {student_counter + standard_counter + kid_counter}")
print(f"{student_counter / (student_counter + standard_counter + kid_counter) * 100:.2f}% student tickets.")
print(f"{standard_counter / (student_counter + standard_counter + kid_counter) * 100:.2f}% standard tickets.")
print(f"{kid_counter / (student_counter + standard_counter + kid_counter) * 100:.2f}% kids tickets.")

