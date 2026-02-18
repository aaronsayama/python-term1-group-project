# Grade System - Question 2

def get_marks():
    marks = []
    for i in range(5):
<<<<<<< HEAD
        mark = float(input(f"Enter mark {i+1}: "))
        marks.append(mark)
=======
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
>>>>>>> f37a841 (addedvaridation)
    return marks

def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

def main():
    print("GRADE SYSTEM")
    print("------------")
    
    marks = get_marks()
    average = calculate_average(marks)
    
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()

