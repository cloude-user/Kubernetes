import sys

def main():
    # if len(sys.argv) < 2:
    #     print("No input received.")
    #     return
    
    user_input = sys.argv[1]
    
    print(f"Received user input: {user_input}")
    
    # Optional logic for number check
    try:
        number = int(user_input)
        if 1 <= number <= 10:
            print(f"Valid number: {number}")
        else:
            print("Invalid number! Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
