# Grade System - Question 2

def get_marks():
    marks = []
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter mark {i+1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Error: Mark must be between 0-100")
            except ValueError:
                print("Error: Please enter a valid number")
    return marks

def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def main():
    print("GRADE SYSTEM")
    print("------------")
    
    marks = get_marks()
    average = calculate_average(marks)
    grade = get_grade(average)
    
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
