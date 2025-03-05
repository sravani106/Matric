
def process_list(lst):
    unique_list = sorted(set(lst))  # Remove duplicates and sort
    return unique_list, unique_list[-2] if len(unique_list) > 1 else None

def swap_tuples(t1, t2):
    return t2, t1  # Swap without extra variables

def set_operations(set1, set2):
    return set1 | set2, set1 & set2, set1 - set2  # Union, Intersection, Difference

def top_student(students):
    return max(students, key=students.get), max(students.values())

def menu():
    while True:
        print("\nChoose an operation:")
        print("1. Process List")
        print("2. Swap Tuples")
        print("3. Set Operations")
        print("4. Find Top Student")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            lst = list(map(int, input("Enter list elements separated by space: ").split()))
            print("Sorted unique list:", *(res := process_list(lst)))
        elif choice == "2":
            t1 = tuple(map(int, input("Enter first tuple elements separated by space: ").split()))
            t2 = tuple(map(int, input("Enter second tuple elements separated by space: ").split()))
            print("Swapped Tuples:", *(swap_tuples(t1, t2)))
        elif choice == "3":
            set1 = set(map(int, input("Enter first set elements separated by space: ").split()))
            set2 = set(map(int, input("Enter second set elements separated by space: ").split()))
            print("Union, Intersection, Difference:", *(set_operations(set1, set2)))
        elif choice == "4":
            students = {}
            n = int(input("Enter number of students: "))
            for _ in range(n):
                name, marks = input("Enter student name and marks separated by space: ").split()
                students[name] = int(marks)
            print("Top Student:", *(top_student(students)))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

menu()