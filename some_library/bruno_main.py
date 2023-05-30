from some_library.bruno_teste import *

def workspace():
    bruno = PessoaFisica(1000, 'Bruno', 'SHIS', '999761299', '123', '473829482', '123321')
    bruno.sacar(50)
    print(bruno.saldo)

if __name__ == '__main__':
    workspace()