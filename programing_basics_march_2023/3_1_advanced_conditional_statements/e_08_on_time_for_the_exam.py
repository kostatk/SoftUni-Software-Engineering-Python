hour_of_exam = int(input())
min_of_exam = int(input())
hour_of_arr = int(input())
min_of_arr = int(input())

# Представяме часа като общо минути след полунощ
time_exam_in_min = hour_of_exam * 60 + min_of_exam
time_arr_in_min = hour_of_arr * 60 + min_of_arr
how_early_in_min = time_exam_in_min - time_arr_in_min
final_hour = abs(how_early_in_min) // 60
final_minutes = abs(how_early_in_min) % 60

on_time = "On time"

# Цялата задача може да се направи като този вариант или като вложени конструкции, като се използва абсолютната стойност на разликата.
# Първата от 3 условия (разликата на двете времена == 0; > 0; < 0) и във всяка различните варианти. В първата има само 1 вариант,
# във втората има 3 варианта (до 30; до 60 и над 60)
# във третата има 2 вариант (до 60 и над 60)
if how_early_in_min > 30:
    on_time = "Early"
elif how_early_in_min < 0:
    on_time = "Late"

print(on_time)

if 0 < how_early_in_min < 60:
    print(f"{how_early_in_min} minutes before the start")
elif how_early_in_min >= 60:
    if final_minutes < 10:
        print(f"{final_hour}:0{final_minutes} hours before the start")
    else:
        print(f"{final_hour}:{final_minutes} hours before the start")
elif -60 < how_early_in_min < 0:
    print(f"{abs(how_early_in_min)} minutes after the start")
elif how_early_in_min <= -60:
    if final_minutes < 10:
        print(f"{final_hour}:0{final_minutes} hours after the start")
    else:
        print(f"{final_hour}:{final_minutes} hours after the start")
# Вместо условна проверка на минутите дали са над или под 10, можем да използваме форматиране, както следва:
# {final_minutes:02d} където 2d Показва колко цифри искаме да изпише (digits) а 0 показва с какъв символ да запълни,
# ако цифрата е само една.