from sequencias.sequencia_a import proximo_elemento_a
from sequencias.sequencia_b import proximo_elemento_b
from sequencias.sequencia_c import proximo_elemento_c
from sequencias.sequencia_d import proximo_elemento_d
from sequencias.sequencia_e import proximo_elemento_e
from sequencias.sequencia_f import proximo_elemento_f

def main():
    sequencia_a = [1, 3, 5, 7]
    sequencia_b = [2, 4, 8, 16, 32, 64]
    sequencia_c = [0, 1, 4, 9, 16, 25, 36]
    sequencia_d = [4, 16, 36, 64]
    sequencia_e = [1, 1, 2, 3, 5, 8]
    sequencia_f = [2, 10, 12, 16, 17, 18, 19]

    print(f"Próximo elemento da sequência a: {proximo_elemento_a(sequencia_a)}")
    print(f"Próximo elemento da sequência b: {proximo_elemento_b(sequencia_b)}")
    print(f"Próximo elemento da sequência c: {proximo_elemento_c(sequencia_c)}")
    print(f"Próximo elemento da sequência d: {proximo_elemento_d(sequencia_d)}")
    print(f"Próximo elemento da sequência e: {proximo_elemento_e(sequencia_e)}")
    print(f"Próximo elemento da sequência f: {proximo_elemento_f(sequencia_f)}")

if __name__ == "__main__":
    main()
