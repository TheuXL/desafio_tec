def get_user_input():
    """Obtém um número do usuário via input."""
    try:
        user_input = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
        return user_input
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return None
