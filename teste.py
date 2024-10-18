class Teste:
    def __init__(self):
        self.dado = 10
        self.descricao = "É uma descrição de exemplo que o objeto tem"
    def __str__(self) -> str:
        return f"{self.descricao} | {self.dado}"

variavel = Teste()
variavel.dado = 50
print(variavel)
