country = input()
tool = input()

hardness_grade = 0
implementation_grade = 0

if country == "Russia":
    if tool == "ribbon":
        hardness_grade = 9.100
        implementation_grade = 9.400
    elif tool == "hoop":
        hardness_grade = 9.300
        implementation_grade = 9.800
    elif tool == "rope":
        hardness_grade = 9.600
        implementation_grade = 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        hardness_grade = 9.600
        implementation_grade = 9.400
    elif tool == "hoop":
        hardness_grade = 9.550
        implementation_grade = 9.750
    elif tool == "rope":
        hardness_grade = 9.500
        implementation_grade = 9.400
elif country == "Italy":
    if tool == "ribbon":
        hardness_grade = 9.200
        implementation_grade = 9.500
    elif tool == "hoop":
        hardness_grade = 9.450
        implementation_grade = 9.350
    elif tool == "rope":
        hardness_grade = 9.700
        implementation_grade = 9.150

total_score = hardness_grade + implementation_grade
remaining_percent = (20 - total_score) / 20 * 100

print(f"The team of {country} get {total_score:.3f} on {tool}.")
print(f"{remaining_percent:.2f}%")
