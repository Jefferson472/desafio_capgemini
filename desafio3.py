class AnalisaAnagramas():
    def __init__(self, palavra):
        self.palavra = palavra
        self.tamanho = len(palavra)

    def verifica_anagrama(self):
        '''Recebe uma string qualquer e retorna as combinações de anagramas possíveis'''
        len_anagrama = 0
        anagrama_dict = {}
        for i in range(self.tamanho):
            for j in range(i, self.tamanho):
                sub_string = ''.join(sorted(self.palavra[i:j+1]))
                if sub_string not in anagrama_dict:
                    anagrama_dict[sub_string] = 1
                else:
                    anagrama_dict[sub_string] += 1
                len_anagrama += anagrama_dict[sub_string]-1
        return len_anagrama


if __name__ == '__main__':
    a = AnalisaAnagramas('ovo')
    output = a.verifica_anagrama()
    print(output)
