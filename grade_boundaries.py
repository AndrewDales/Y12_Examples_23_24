def calc_grade(raw_score: int) -> str:
    # Program will calculate and return a grade based on a raw score.
    if raw_score >= 264:
        grade = "A*"
    elif raw_score >= 229:
        grade = "A"
    elif raw_score >= 189:
        grade = "B"
    elif raw_score >= 150:
        grade = "C"
    elif raw_score >= 111:
        grade = "D"
    elif raw_score >= 72:
        grade = "E"
    else:
        grade = "U"
    return grade


if __name__ == "__main__":
    my_grade = calc_grade(259)
    print(my_grade)
