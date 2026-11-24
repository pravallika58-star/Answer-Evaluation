# Answer-Evaluation
# Case Study 31: String-Based Examination Answer Evaluation

## Python Activity-Based Learning

### Student Details
- **Name:**DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01A0383
- **Branch:**CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

String-Based Examination Answer Evaluation is a Python-based program that compares students' answers with a predefined answer key.

The program calculates the number of correct, incorrect and unanswered questions. It applies negative marking for incorrect answers and generates individual student performance reports.

## 2. Objectives

- To compare student answers with an answer key.
- To identify correct and incorrect answers.
- To count unanswered questions.
- To apply negative marking.
- To calculate the final examination score.
- To generate student-wise performance reports.
- To understand string comparison and list operations in Python.

## 3. Assumptions

1. The examination contains five questions.
2. A predefined answer key is available.
3. Each correct answer carries 1 mark.
4. Each incorrect answer carries a negative mark of 0.25.
5. Unanswered questions receive zero marks.
6. Answer comparison is case-insensitive.
7. Extra spaces before and after answers are ignored.
8. Each student answers the same set of questions.

### Marking Scheme

| Answer Type | Marks |
|---|---:|
| Correct Answer | +1 |
| Incorrect Answer | -0.25 |
| Unanswered | 0 |

## 4. Algorithm

1. Start the program.
2. Initialize the answer key.
3. Set the correct and negative marking values.
4. Enter the number of students.
5. Read each student's name.
6. Initialize correct, incorrect and unanswered counters.
7. Read answers for all questions.
8. Compare each answer with the answer key.
9. If the answer is blank, increase the unanswered counter.
10. If the answer matches the key, increase the correct counter.
11. Otherwise, increase the incorrect counter.
12. Calculate the final score using the marking scheme.
13. Store the student results in a list of tuples.
14. Display the individual student results.
15. Classify student performance.
16. Stop the program.

## 5. Pseudocode

```text
START

INITIALIZE answer_key

SET correct_mark = 1
SET negative_mark = 0.25

INPUT number_of_students

IF number_of_students <= 0
    DISPLAY Invalid input

ELSE

    FOR each student

        INPUT student_name

        SET correct = 0
        SET incorrect = 0
        SET unanswered = 0

        FOR each question

            INPUT student_answer

            IF answer is empty
                unanswered = unanswered + 1

            ELSE IF answer matches answer_key
                correct = correct + 1

            ELSE
                incorrect = incorrect + 1

            END IF

        END FOR

        CALCULATE final_score

        STORE student results

    END FOR

    FOR each student result

        DISPLAY student name
        DISPLAY correct answers
        DISPLAY incorrect answers
        DISPLAY unanswered questions
        DISPLAY final score

        CLASSIFY performance

    END FOR

END IF

STOP
```

## 6. Python Source Code

**File name:** `answer_evaluation.py`

The complete Python implementation is available in this folder.

## 7. Test Cases

| Test Case | Correct | Incorrect | Unanswered | Expected Score |
|---|---:|---:|---:|---:|
| 1 | 5 | 0 | 0 | 5.00 |
| 2 | 3 | 1 | 1 | 2.75 |
| 3 | 2 | 2 | 1 | 1.50 |
| 4 | 0 | 5 | 0 | -1.25 |
| 5 | 0 | 0 | 5 | 0.00 |

## 8. Expected Output

```text
EXAMINATION ANSWER EVALUATION

Student Name: Pravallika

Correct Answers: 3
Incorrect Answers: 1
Unanswered Questions: 1

Final Score: 2.75 / 5
Result: Good

EVALUATION COMPLETED
```

## 9. Conclusion

The String-Based Examination Answer Evaluation program successfully evaluates student answers by comparing them with a predefined answer key. It calculates correct, incorrect and unanswered responses and applies negative marking to determine the final score.

This project helps us understand Python variables, strings, operators, conditional statements, loops, lists and tuples. It also demonstrates how Python can be used to automate examination evaluation.

---

**Project:** Python Activity-Based Learning  
**Case Study Number:** 31  
**Topic:** String-Based Examination Answer Evaluation
