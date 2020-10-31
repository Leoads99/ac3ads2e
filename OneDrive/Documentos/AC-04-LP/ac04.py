# Definição da Classe Mãe Pessoa

class Pessoa:
    # Construtor
    def __init__(self, nome, rg, cpf,
                 telefone):
        # Atributos
        self.nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.telefone = telefone

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def set_rg(self, rg):
        self.__rg = rg
        return self.__rg

"""
class Especialidade:
   def __init__(self, especialidade):
        self.especialidade = especialidade
    
    def exibir_especialidade(self):
        print(especialidade)    
"""

class Medico(Pessoa):
    def __init__(self, nome, rg, cpf, 
                 telefone, crm, salario, especialidade):
        super().__init__(nome, rg, cpf, telefone)
        self.crm = crm
        self.salario = salario
        self.especialidade = especialidade

    def info_medico(self):
        print("NOME:", self.nome)
        #print("RG:", self.__rg)
        #print("CPF:", self.__cpf)
        print("TELEFONE:", self.telefone)
        print("CRM:", self.crm)
        print("SALÁRIO:", self.salario)
        # super().exibir_especialidade()

    def visitar_paciente(self):
        print('O MÉDICO VISITOU O PACIENTE: ', Paciente.nome)

    def registrar_obs(self):
        print("""O MÉDICO REGISTROU AS OBSERVAÇÕES
        REALIZADAS DO PACIENTE: """, Paciente.nome)

    def historico_paciente(self):
        historico = []
        historico.append(str(registrar_obs))
    
    #def get_crm(self):
    #    return self.__crm

    #def set_crm(self, crm):
    #    self.__crm = crm
    #    return self.__crm

        
class Paciente(Pessoa):
    def __init__(self, nome, rg, cpf,
                telefone, endereco, data_nasc):
        super().__init__(nome, rg, cpf, telefone)
        self.enderco = endereco
        self.data_nasc = data_nasc
        
    def info_paciente(self):
        print("NOME:", self.nome)
        #print("RG:", self.__rg)
        #print("CPF:", self.__cpf)
        print("TELEFONE:", self.telefone)
        print("CRM:", self.crm)
        print("SALÁRIO:", self.salario)

    #def ficar_internado(self):
    #    print("PACIENTE DE NOME: ", self.nome)
    #    Quarto.info_quarto(self)

    def medico_responsavel(self):
        Medico.info_medico(self)

        
class Quarto:
    def __init__(self, numero_quarto, numero_andar):
        self.numero_quarto = numero_quarto
        self.numero_andar = numero_andar

    def info_quarto(self):
        print("LOCALIZADO NO QUARTO DE NÚMERO: ", self.numero_quarto)
        print("LOCALIZADO NO ANDAR: ", self.numero_andar)

medico = Medico('João', 23122312, 12231223,
                 11923423453,13811, 10000, 'Cardiologia')
medico.info_medico()

paciente = Paciente('Filipe',1231231,220390121,
                    11957483940,'Rua Guarani 320','11/08/1976')
# paciente.ficar_internado()

quarto = Quarto(54, '5° andar')

quarto.info_quarto()
