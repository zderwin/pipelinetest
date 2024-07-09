# app.py

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def main():
    print("Welcome to the Python test application!")
    print(f"2 + 5 = {add_numbers(2, 5)}")
    print(f"8 - 2 = {subtract_numbers(8, 2)}")

if __name__ == "__main__":
    main()
