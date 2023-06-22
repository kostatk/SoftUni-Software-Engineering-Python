list_of_words = input().split()
palindrome_word = input()

# palindrome_list = []
#
# for element in list_of_words:
#     if element == element[::-1]:
#         palindrome_list.append(element)

palindrome_list = [element for element in list_of_words if element == element[::-1]]
palindrome_word_counter = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {palindrome_word_counter} times")
