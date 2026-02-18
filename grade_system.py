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
                    print("Mark must be 0-100")
            except:
                print("Invalid input")
    return marks

def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

def get_grade(average):
    if average >= 80:
        return "A - Excellent"
    elif average >= 70:
        return "B - Good"
    elif average >= 60:
        return "C - Satisfactory"
    elif average >= 50:
        return "D - Pass"
    else:
        return "F - Fail"

def display_results(marks, average, grade):
    print("\n" + "="*30)
    print("RESULTS")
    print("="*30)
    for i, m in enumerate(marks):
        print(f"Subject {i+1}: {m}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print("="*30)

def main():
    while True:
        print("\nGRADE SYSTEM")
        print("------------")
        
        marks = get_marks()
        average = calculate_average(marks)
        grade = get_grade(average)
        
        display_results(marks, average, grade)
        
        again = input("\nTry again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

