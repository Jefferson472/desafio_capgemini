# Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.

class AnalisaAnagramas():
    def __init__(self, palavra):
        self.palavra = palavra
        self.anagramas = []

    def analisa(self):
        self.anagramas = []
        for i in range(len(self.palavra)):
            for j in range(i+1, len(self.palavra)):
                self.anagramas.append(self.palavra[i:j+1])
        return self.anagramas

    def ordena_anagramas(self, anagramas):
        for anagrama in anagramas:
            anagrama.sort()
            print(anagrama)
        return self.anagramas

    def conta_anagramas(self):
        return len(self.anagramas)


if __name__ == '__main__':
    a = AnalisaAnagramas('abba')
    resultado = a.analisa()
    # resultado = a.ordena_anagramas(resultado)
    print(resultado)
