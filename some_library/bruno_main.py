from bruno_teste import *

def workspace():
    bruno = PessoaFisica(1000, 'Bruno B', 'SHIS', '999761299', 'senha123', '12345678', 'tipo', '0000001')
    print(bruno.saldo)
    bruno.sacar(50)
    bruno.depositar(100)
    print(bruno.saldo)

if __name__ == '__main__':
    workspace()