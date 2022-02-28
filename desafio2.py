import re


class AnalisaSenha():
    def __init__(self, senha_string):
        self.SENHA = senha_string

    # Regras de negócio

    def verifica_qntd_caracteres(self):
        '''Verifica se a senha possui no mínimo 6 caracteres'''
        if len(self.SENHA) >= 6:
            return True

    def verifica_min_digito(self):
        '''Verifica se a senha contém no mínimo 1 dígito'''
        if re.findall('[0-9]', self.SENHA):
            return True

    def verifica_letra_minuscula(self):
        '''Verifica se a senha contém no mínimo 1 letra em minúsculo'''
        if re.findall('[a-z]', self.SENHA):
            return True

    def verifica_letra_maiuscula(self):
        '''Verifica se a senha contém no mínimo 1 letra em maiúsculo'''
        if re.findall('[A-Z]', self.SENHA):
            return True

    def verifica_caract_especial(self):
        '''Verifica se a senha contém no mínimo 1 caractere especial'''
        if re.findall('[!@#$%^&*()-+]', self.SENHA):
            return True


if __name__ == '__main__':
    senha_string = 'Ya3'
    s = AnalisaSenha(senha_string)
    output = 0
    if not s.verifica_min_digito():
        output += 1
    if not s.verifica_letra_minuscula():
        output += 1
    if not s.verifica_letra_maiuscula():
        output += 1
    if not s.verifica_caract_especial():
        output += 1
    if not s.verifica_qntd_caracteres():
        if 6 - len(senha_string) > output:
            output += 6 - len(senha_string) - output

    print(output)
