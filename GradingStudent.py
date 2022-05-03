#GradingStudent

def gradingStudents(grades):
    for i in range(len(grades)):
        if(grades[i] >= 38):
            next_multiples = (grades[i] - (grades[i]%5)) + 5
            difference = next_multiples - grades[i]
            if difference < 3:
                grades[i] = next_multiples     
    return grades
