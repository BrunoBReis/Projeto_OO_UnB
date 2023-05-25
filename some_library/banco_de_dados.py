class DataBank_Gerente():

    def get_data (self, name = "Gerentes.txt"):
        data = open(name, "r", encoding="utf-8")
        gerentes = data.readlines()
        print (gerentes)
        data.close


class DataBank_Clientes():

    def get_data (self, name = "Clientes.txt"):
        data = open(name, "r", encoding="utf-8")
        clientes = data.readlines()
        print (clientes)
        data.close

class DataBank_Historico():

    def get_data (self, name = "Historico.txt"):
        data = open(name, "r", encoding="utf-8")
        historico = data.readlines()
        print (historico)
        data.close