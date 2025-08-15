class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        resultado = []

        for i in range(numRows):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                elif j == 1 or j == i - 1:
                    temp.append(i)
                else:
                    temp.append(resultado[i - 1][j] + resultado[i - 1][j - 1])
            resultado.append(temp)
        return resultado


s = Solution()
i = int(input("Digite a coluna do triangulo de pascal: "))
print(s.generate(i))
