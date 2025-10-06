conversion = {
    1.0 :   (97,100),
    1.25 :  (94,96.99),
    1.5 :   (91,93.99),
    1.75 :  (88,90.99),
    2.0 :   (85,87.99),
    2.25 :  (82,84.99),
    2.5 :   (79,81.99),
    2.75 :  (76,78.99),
    3.0 :   (75,75.99),
}

non_number_error = "Please enter a valid number."
over_range_error = "Please enter number between 1-100."


def calculate_grade(score:float) -> float:
    for grade, (min_score, max_score) in conversion.items():
        if min_score <= round(score,2) <= max_score:
            return grade
    return 5.0 

while True:
    try:
        user_input = float(input("Enter Raw Grade: "))
        if user_input > 100 or user_input < 1:
            print(over_range_error)
            continue 
        print(f"Final Grade: {calculate_grade(user_input)}")
        break
    except ValueError:
        print(non_number_error)