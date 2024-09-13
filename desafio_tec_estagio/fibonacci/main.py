from fibonacci.fibonacci import is_fibonacci_number
from utils.input_handler import get_user_input

def main():
    
    number = get_user_input()
    
    if number is None:
        return

    if is_fibonacci_number(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
