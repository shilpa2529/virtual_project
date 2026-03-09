
def totalMarks(marks):
    total=sum(marks)
    return total

def averageMarks(marks):
    average= sum(marks) / len(marks)
    return average


def gradeAssignment(average):
    if average >= 80:
        return "A Grade"
    elif average >= 60:
        return "B Grade"
    elif average >= 40:
        return "C Grade"
    else:
        return "Fail"