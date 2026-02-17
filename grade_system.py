# Grade System - Question 2

def get_marks():
    marks = []
    for i in range(5):
        mark = float(input(f"Enter mark {i+1}: "))
        marks.append(mark)
    return marks

def main():
    print("GRADE SYSTEM")
    print("------------")
    
    marks = get_marks()
    print(f"Marks entered: {marks}")

if __name__ == "__main__":
    main()
