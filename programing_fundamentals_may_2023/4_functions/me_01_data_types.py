
def data_convert(type_of_data, data):
    if type_of_data == "int":
        print(int(data) * 2)
    elif type_of_data == "real":
        print(f"{float(data) * 1.5:.2f}")
    elif type_of_data == "string":
        print(f"${data}$")


user_data_type = input()
user_data = input()
data_convert(user_data_type, user_data)
