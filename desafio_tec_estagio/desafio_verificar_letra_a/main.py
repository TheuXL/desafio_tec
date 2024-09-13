def contar_letra_a(string):

    quantidade_a = string.lower().count('a')
    
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

entrada = input("Digite uma string: ")
contar_letra_a(entrada)
