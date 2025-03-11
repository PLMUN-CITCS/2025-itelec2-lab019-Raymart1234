"""Enhanced Grade Calculator with Function Decomposition"""
 
 def get_student_score() -> float:
     """Gets a valid student score from user input."""
     """
     Handles user input to obtain the student's score.
     
     Returns:
         float: The numerical score entered by the user.
     """
     while True:
         try:
             score = float(input("Enter your score: "))
             if 0 <= score <= 100:
                 return score
             else:
                 print("Please enter a score between 0 and 100.")
             print("Please enter a valid score between 0 and 100.")
         except ValueError:
             print("Invalid input. Please enter a numerical value.")
             continue
 
 def calculate_grade(score: float) -> str:
     """Determines the grade based on the score."""
     """
     Determines the letter grade based on the given score.
 
     Parameters:
         score (float): The student's numerical score.
 
     Returns:
         str: The corresponding letter grade.
     """
     if score >= 90:
         return 'A'
     elif score > 80:
         return 'B'
     elif score > 70:
         return 'C'
     elif score > 60:
         return 'D'
     else:
         return 'F'
         return "A"
     if score >= 80:
         return "B"
     if score >= 70:
         return "C"
     if score >= 60:
         return "D"
     return "F"
 
 if __name__ == "__main__":
 def main():
     """Main program flow for grade calculation."""
     student_score = get_student_score()
     grade = calculate_grade(student_score)
     print(f"Your Grade is: {grade}")
     print(f"Your Grade is: {grade}")
 
 if __name__ == "__main__":
     main()