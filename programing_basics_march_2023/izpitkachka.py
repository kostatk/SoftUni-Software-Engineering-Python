from random import randint

print("Това е ИЗПИТКАЧКАТА")
print("Тя ще те изпитва на таблицата за умножение докато нe достигнеш необходимите верни отговора или не напишеш stop "
      "вместо отговор")
answer_limit = int(input("До колко верни отговора ще играеш: "))

correct_answers_counter = 0
wrong_answers_counter = 0
HAS_QUITED = False
HAS_FAILED = False

while True:
    if correct_answers_counter == answer_limit:
        break
    if wrong_answers_counter == 3:
        HAS_FAILED = True
        break
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    multiply_correct = first_number * second_number
    input_command = input(f"Колко е {first_number} по {second_number}?    Отговор: ")
    if input_command == "stop":
        HAS_QUITED = True
        break
    multiply_answer = int(input_command)
    if multiply_answer == multiply_correct:
        print("Правилен отговор. БРАВО!")
        correct_answers_counter += 1
        if correct_answers_counter < answer_limit:
            print(f" Вече имаш {correct_answers_counter} верни отговора. Трябват ти "
                  f"още {answer_limit - correct_answers_counter} за да победиш.")
    else:
        print(f"ГРЕШКА! Правилният отговор е {multiply_correct}")
        wrong_answers_counter += 1
        print(f" Все още имаш {correct_answers_counter} верни отговора. Трябват ти "
              f"още {answer_limit - correct_answers_counter} за да победиш.")

print(f"Изпиткачката завърши")
if HAS_QUITED:
    print(f"Ах, ти мързел. Реши {correct_answers_counter + wrong_answers_counter} задачи и се отказа. Все пак имаш "
          f"{correct_answers_counter} верни и {wrong_answers_counter} грешни отговора.")
if HAS_FAILED:
    print(f"Съжалявам. Трябва да учиш повече. Вече имаш 3 грешки. А верните ти отговори са {correct_answers_counter}.")
else:
    if wrong_answers_counter == 0 and correct_answers_counter == answer_limit:
        print(f"ОТЛИЧЕН УЧЕНИК. ТИ ОТГОВОРИ НА {answer_limit} ВЪПРОСА БЕЗ ГРЕШКА")
    else:
        print(f"ЧУДЕСТНО. Ти позна {answer_limit} задачи и имаш само {wrong_answers_counter} грешни отговора.")
