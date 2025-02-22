def get_student_score() -> int:
    """
    Prompts the user to enter a valid numerical score between 0 and 100.

    Returns:
        int: The validated score input by the user.
    """
    while True:
        try:
            score = int(input("Enter your score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Error: Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def calculate_grade(score: int) -> str:
    """
    Determines the letter grade based on the numerical score.

    Parameters:
        score (int): The student's numerical score.

    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    return 'F'

# Get user input and display the grade
student_score = get_student_score()
student_grade = calculate_grade(student_score)
print(f"Your Grade is: {student_grade}")  # Final output
