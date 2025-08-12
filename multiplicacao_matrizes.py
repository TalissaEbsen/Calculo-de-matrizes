class Operacoes:
    def soma(self, a, b):
        return a + b

    def multiplicacao(self, a, b):
        return a * b


class Matriz:
    def __init__(self, caminho_arquivo):
        self.dados = []
        with open(caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                numeros = list(map(float, linha.strip().split()))
                self.dados.append(numeros)

        self.tamanho = len(self.dados)

        # Verifica se é quadrada
        for linha in self.dados:
            if len(linha) != self.tamanho:
                raise ValueError("A matriz não é quadrada!")

    def get_tamanho(self):
        return self.tamanho

    def get_valor(self, i, j):
        return self.dados[i][j]

    def mostrar(self):
        for linha in self.dados:
            print("\t".join(map(str, linha)))

    @staticmethod
    def multiplicar(A, B, op):
        if A.get_tamanho() != B.get_tamanho():
            raise ValueError("Matrizes precisam ter o mesmo tamanho!")

        n = A.get_tamanho()
        resultado = Matriz.matriz_vazia(n)

        for i in range(n):
            for j in range(n):
                soma = 0
                print(f"\nCalculando elemento [{i}][{j}]:")
                for k in range(n):
                    mult = op.multiplicacao(A.get_valor(i, k), B.get_valor(k, j))
                    soma = op.soma(soma, mult)
                    print(f"{A.get_valor(i, k)} * {B.get_valor(k, j)} = {mult} | Soma parcial = {soma}")
                resultado.dados[i][j] = soma
        return resultado

    @staticmethod
    def matriz_vazia(tamanho):
        m = Matriz.__new__(Matriz)  # cria sem chamar __init__
        m.dados = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
        m.tamanho = tamanho
        return m


# ---------------- MAIN ----------------
if __name__ == "__main__":
    try:
        op = Operacoes()
        A = Matriz("matrizA.txt")
        B = Matriz("matrizB.txt")

        print("Matriz A:")
        A.mostrar()
        print("\nMatriz B:")
        B.mostrar()

        print("\n--- Multiplicação passo a passo ---")
        resultado = Matriz.multiplicar(A, B, op)

        print("\nMatriz Resultado:")
        resultado.mostrar()

    except Exception as e:
        print("Erro:", e)
