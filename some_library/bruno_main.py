from some_library.bruno_teste import *

def workspace():
    bruno = Cliente(1000, 'Bruno', 'endereço', 'telefone', 'senha123', '432423423')
    bruno.sacar(50)
    print(bruno.saldo())

if __name__ == '__main__':
    workspace