def generate_fibonacci_up_to(n):
    """Gera a sequência de Fibonacci até o número n."""
    fib_sequence = [0, 1]
    
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence

def is_fibonacci_number(n):
    """Verifica se o número informado pertence à sequência de Fibonacci."""
    if n < 0:
        return False
    
    fib_sequence = generate_fibonacci_up_to(n)
    return n in fib_sequence
