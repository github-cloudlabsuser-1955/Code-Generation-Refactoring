MAX = 100

def calculate_sum(arr):
    """
    Calculates the sum of elements in a list.

    Args:
        arr (list): List of integers.

    Returns:
        int: Sum of the integers in the list.
    """
    return sum(arr)

def get_integer_input(prompt):
    """
    Prompts the user for an integer input and handles invalid input.

    Args:
        prompt (str): The input prompt message.

    Returns:
        int: The valid integer input from the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """
    Main function to prompt the user for input, calculate the sum of integers, and display the result.
    """
    try:
        n = get_integer_input("Enter the number of elements (1-100): ")
        if not 1 <= n <= MAX:
            print(f"Invalid input. Please provide a number between 1 and {MAX}.")
            return

        arr = []
        print(f"Enter {n} integers:")
        for _ in range(n):
            arr.append(get_integer_input(""))

        total = calculate_sum(arr)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
