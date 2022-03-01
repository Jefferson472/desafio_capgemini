class CriaEscada():
    def desenha_escada(self, n):
        '''Recebe um número inteiro (n) e retorna uma escada desenhada em *'''
        base_escada = n
        for n in range(n, 0, -1):
            for j in range(0, base_escada, 1):
                if j+1 < n:
                    print(' ', end='')
                else:
                    print('*', end='')
            print()


if __name__ == '__main__':
    n = int(input('Digite um número inteiro: '))
    e = CriaEscada()
    e.desenha_escada(n)
