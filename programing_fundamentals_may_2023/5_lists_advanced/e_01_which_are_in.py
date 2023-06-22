
def is_substring(substring):
    for word in main_list:
        if substring in word:
            return True


list_with_checks = input().split(", ")
main_list = input().split(", ")

final_list = [element for element in list_with_checks if is_substring(element)]

print(final_list)
