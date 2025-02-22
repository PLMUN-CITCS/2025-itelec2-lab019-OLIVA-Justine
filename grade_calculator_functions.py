def get_student_score():
	
    score = int(input("Enter your score: "))
    if 0 <= score <= 100:
        return score
    print("Please enter a valid score between 0 and 100.")
    return get_student_score() 

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

score = get_student_score()
grade = calculate_grade(score)
print(f"Your Grade is: {grade}")
