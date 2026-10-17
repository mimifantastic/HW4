# CS 1300 - Homework 4: Worked Answers

## Section 1: Multiple Choice

| Question | Answer | Explanation |
|---|---|---|
| 1 | **b) False** | `5 < 10` is true, but `10 < 3` is false; both must be true. |
| 2 | **b) not A or not B** | Negating an AND gives the OR of the negated conditions. |
| 3 | **d) Comparison operators** | Comparisons have higher precedence than `not`, `and`, and `or`. |
| 4 | **a) True** | `or` short-circuits after the true left operand, avoiding division by zero. |
| 5 | **b) False** | Seven is not less than or equal to five. |
| 6 | **a) x <= 5 and y >= 3** | Negate each comparison and change OR to AND. |
| 7 | **c) "hello"** | `or` returns its second operand when its first operand is falsy. |
| 8 | **a) 3 + 4 (addition)** | Addition has higher precedence than the comparison and Boolean operators. |
| 9 | **b) Any program can be written with sequence, selection, and iteration** | These are the three structured control-flow building blocks. |
| 10 | **c) A followed by B (on separate lines)** | The condition is true, and the unindented second print always executes. |
| 11 | **b) if x > 5:** | A Python `if` header ends with a colon. |
| 12 | **c) 4** | PEP 8 recommends four spaces per indentation level. |
| 13 | **c) C** | Seventy-five reaches the `score >= 70` branch. |
| 14 | **c) SyntaxError** | A missing colon makes the `if` statement invalid syntax. |
| 15 | **b) Exactly one** | With a final `else`, one branch always executes. See the clarification below. |
| 16 | **b) Program counter** | The program counter tracks the next instruction to execute. |
| 17 | **a) "" (empty string)** | `and` returns the falsy first operand. `print` displays a blank line, without quote marks. |
| 18 | **c) [] (empty list)** | Empty lists are falsy; all the other listed values are truthy. |
| 19 | **b) Warm** | Seventy-two satisfies `temperature > 70`, so later branches are skipped. |
| 20 | **a) True** | Negating `True` twice returns `True`. |

**Question 15 clarification:** The answer choices overlap: “at most one” and “at least one” are also true when exactly one branch runs. Because the question explicitly includes a final `else` and asks for the single best answer, **b) Exactly one** is the most precise choice. Without a final `else`, an `if-elif` chain may execute zero blocks.

## Section 2: True or False

| Question | Answer | Explanation |
|---|---|---|
| 1 | **T** | `1 < 2 > 3` is valid and means `1 < 2 and 2 > 3`, which is false. |
| 2 | **F** | The correct equivalent is `not A and not B`. |
| 3 | **T** | `and` has higher precedence than `or`. |
| 4 | **F** | `and` skips the right operand when the left operand is falsy. |
| 5 | **T** | Integer zero is falsy. |
| 6 | **F** | Dijkstra argued against unrestricted use of GOTO. |
| 7 | **F** | Indentation defines Python's code blocks and affects program behavior. |
| 8 | **T** | An `if-elif-else` chain never executes more than one branch per evaluation. |
| 9 | **T** | Integer `5` and floating-point `5.0` compare equal numerically. |
| 10 | **T** | The false left operand short-circuits `and`, so `print` is never called. |

## Section 3: Short Answer

### 1. De Morgan's Law

De Morgan's laws describe how negation changes a statement containing “and” or “or.” Saying “not both A and B” means “not A or not B,” while saying “neither A nor B” means “not A and not B.” For example, suppose a museum grants discounted admission only to visitors who have both a student ID and a discount coupon. A visitor fails to qualify if they lack a student ID or lack a coupon, including when they lack both.

### 2. Short-circuit evaluation

Short-circuit evaluation means Python stops evaluating a Boolean expression as soon as the left operand determines the result. For `and`, Python skips the right operand if the left operand is falsy; for `or`, it skips the right operand if the left operand is truthy. In this example, `x` is zero, so `x != 0` evaluates to `False`. Python therefore skips `10 / x > 2`, avoids dividing by zero, and assigns `False` to `result`.

### 3. Ordering conditions

An `if-elif-else` chain checks conditions from top to bottom and executes only the first matching branch. When assigning grades using lower-bound comparisons, the CS 1300 thresholds should be checked from highest to lowest, starting with `average >= 90` for A and then `average >= 87` for A-. If `average >= 60` for D were checked first, a student with a 95 average would incorrectly receive a D because that condition is already true. Checking the highest thresholds first ensures that the student receives the correct grade of A.

## Section 4: Python Programs

The three accompanying files contain complete solutions with explanatory comments:

1. `problem1_boolean_evaluator.py`
2. `problem2_weather_advisory.py`
3. `problem3_student_grade_report.py`

Run each file separately with Python 3 and enter the requested values.

### Interpretation of decimal inputs

The weather program accepts decimal temperatures and interprets the cold range as `32 <= temperature < 60`; this avoids an unintended gap between 59 and 60. The grade program uses the stated lower cutoffs without rounding the average before classification: for example, 89.5 earns A-, and 90 earns A. Only the displayed average is rounded to two decimal places. The assignment does not specify a different rounding policy.
