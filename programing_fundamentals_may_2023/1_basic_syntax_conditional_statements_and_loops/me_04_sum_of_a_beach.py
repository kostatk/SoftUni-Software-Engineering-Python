# user_input = input().lower()
#
# print(user_input.count('sand') + user_input.count('water') + user_input.count('fish') + user_input.count('sun'))


user_input = input().lower()
word_counter = 0
words_to_search = ["water", "sun", "fish", "sand"]
for i in range(len(user_input)):
    if user_input[:3] in words_to_search:
        word_counter += 1
    elif user_input[:4] in words_to_search:
        word_counter += 1
    elif user_input[:5] in words_to_search:
        word_counter += 1
    user_input = user_input[1:]
print(word_counter)

