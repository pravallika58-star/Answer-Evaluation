
# Case Study 31: String-Based Examination Answer Evaluation

print("==========================================")
print("    EXAMINATION ANSWER EVALUATION")
print("==========================================")

# Answer key
answer_key = ["python", "html", "cpu", "ram", "input"]

total_questions = len(answer_key)

# Marking scheme
correct_mark = 1
negative_mark = 0.25

# Number of students
n = int(input("Enter number of students: "))

if n <= 0:
    print("Invalid number of students!")

else:

    # Store student results
    student_results = []

    for i in range(n):

        print("\nStudent", i + 1)

        name = input("Enter student name: ")

        correct = 0
        incorrect = 0
        unanswered = 0

        # Read student answers
        for j in range(total_questions):

            answer = input(
                "Enter answer for Question " + str(j + 1) + ": "
            )

            # Compare answer strings
            if answer.strip() == "":
                unanswered += 1

            elif answer.strip().lower() == answer_key[j]:
                correct += 1

            else:
                incorrect += 1

        # Calculate final score
        score = (correct * correct_mark) - (
            incorrect * negative_mark
        )

        maximum_marks = total_questions * correct_mark

        # Store results
        student_results.append(
            (name, correct, incorrect, unanswered, score)
        )

    # Display student-wise results
    print("\n==========================================")
    print("          STUDENT RESULTS")
    print("==========================================")

    for result in student_results:

        name, correct, incorrect, unanswered, score = result

        print("\nStudent Name:", name)
        print("Correct Answers:", correct)
        print("Incorrect Answers:", incorrect)
        print("Unanswered Questions:", unanswered)
        print("Final Score:", round(score, 2), "/", maximum_marks)

        if score >= 4:
            print("Result: Excellent")
        elif score >= 2:
            print("Result: Good")
        elif score >= 0:
            print("Result: Needs Improvement")
        else:
            print("Result: Poor")

    print("\n==========================================")
    print("       EVALUATION COMPLETED")
    print("==========================================")
