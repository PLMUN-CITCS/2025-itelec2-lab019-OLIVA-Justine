def get_student_score() -> int:
    """
    Prompt the user to enter a valid numerical score between 0 and 100.

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
    Determine the letter grade based on the numerical score.

    Args:
        score (int): The student's numerical score.

    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


if __name__ == "__main__":
    # Get user input and display the grade
    student_score = get_student_score()
    student_grade = calculate_grade(student_score)
    print(f"Your Grade is: {student_grade}")
