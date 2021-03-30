# Conexão ao postgre

import requests
import psycopg2
from psycopg2 import sql
import sys


class Crud():
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                dbname=self.dbname
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print(
                '------------------------------------------------------------'
                '\n-# PostgreSQL connection & transaction is ACTIVE\n'
            )
        except:
            print('Não foi possível conectar ao Banco de Dados! ')

    def close(self):
        try:
            self.cursor.close()
            print(
                '-# CLOSE connection\n'
                '------------------------------------------------------------\n'
            )
        except:
            print('Não existem conexões ativas! ')


# Função que cria tabela


    def create_table(self):
        try:
            create_table_command = '''CREATE TABLE organizing_to_care (
            ra INTEGER PRIMARY KEY,
            nome_aluno varchar(50),
            email_aluno varchar(50),
            logradouro varchar(50),
            numero varchar(5),
            cep varchar(10),
            complemento varchar(20))'''
            self.cursor.execute(create_table_command)
        except:
            print('A tabela já existe! Por isso não será criada! \n')

    def buscar_por_ra(self, ra):
        query = 'SELECT * FROM organizing_to_care WHERE ra = %s'
        self.cursor.execute(query, [ra])

        return self.cursor.fetchone()

    # Função que cadastra um aluno

    def insert_aluno(self):
        try:
            ra = int(input('Digite o RA do aluno: '))
            ra_existe = self.buscar_por_ra(ra)
            if (ra_existe):
                print('RA já cadastrado! ')
                return
        except ValueError:
            print('ERRO! Não digitar letras, apenas números! ')
        try:
            nome_aluno = str(input('Digite o nome do aluno: '))
        except ValueError:
            if nome_aluno != str:
                print('ERRO! Nome inválido, digite apenas letras! ')
        email_aluno = str(input('Digite o e-mail do aluno: '))
        try:
            cep = str(
                input('Digite o CEP do aluno [Digite apenas números]: '))
            if len(cep) < 8:
                print('CEP inválido, deve conter apenas 8 dígitos! ')
            if len(cep) == 8:
                cep = f'{cep[:5]}-{cep[5:8]}'
        except ValueError:
            print('Erro ao digitar o CEP! ')
        request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        address_data = request.json()
        logradouro = address_data['logradouro']
        try:
            numero = int(input('Digite o numero do logradouro do aluno: '))
        except ValueError:
            print('ERRO! Não digitar letras, apenas números! ')
        complemento = str(input('Digite o complemento do logradouro: '))
        insert_command = """INSERT INTO organizing_to_care (ra,nome_aluno,
        email_aluno, logradouro, numero, complemento,cep)
        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        self.cursor.execute(insert_command, [ra, nome_aluno,
                                             email_aluno, logradouro, numero, cep, complemento])
        print('\nAluno cadastrado com sucesso!')

    # Função que atualiza dados
    def update(self):
        ra = int(input('Digite o RA do aluno que deseja atualizar:  '))
        try:
            nome_aluno = str(input('Digite o novo nome do aluno: '))
        except ValueError:
            if nome_aluno != str:
                print('ERRO! Nome inválido, digite apenas letras! ')
        email_aluno = str(input('Digite o novo e-mail do aluno: '))
        try:
            cep = str(
                input('Digite novo o CEP do aluno [Digite apenas números]: '))
            if len(cep) < 8:
                print('CEP inválido, deve conter apenas 8 dígitos! ')
            if len(cep) == 8:
                cep = f'{cep[:5]}-{cep[5:8]}'
        except ValueError:
            print('Erro ao digitar o CEP! ')
        request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        address_data = request.json()
        logradouro = address_data['logradouro']
        try:
            numero = int(
                input('Digite o novo numero do logradouro do aluno: '))
        except ValueError:
            print('ERRO! Não digitar letras, apenas números! ')
        complemento = str(input('Digite o novo complemento do logradouro: '))
        update_command = """UPDATE organizing_to_care
        SET nome_aluno=%s ,email_aluno=%s,
        logradouro=%s, numero=%s,
        complemento=%s,cep=%s WHERE ra=%s"""
        self.cursor.execute(update_command, [nome_aluno,
                                             email_aluno, logradouro, numero, cep, complemento, ra])

    # Função que deleta o aluno cadastrado por RA
    def delete_aluno(self):
        ra = int(input('Digite o RA do aluno que deseja excluir:  '))
        delete = 'DELETE FROM organizing_to_care WHERE ra = %s' % ra
        self.cursor.execute(delete)
        print('DELETADO COM SUCESSO! ')

    # Função que consulta um aluno por vez e por número de RA
    def consultar(self):
        try:
            ra = int(input('Digite o RA do aluno que deseja consultar:  '))
            aluno = self.buscar_por_ra(ra)
            print("ra = ", aluno[0], )
            print("nome_aluno = ", aluno[1])
            print("email_aluno = ", aluno[2])
            print("logradouro  = ", aluno[3])
            print("numero = ", aluno[4])
            print("complemento = ", aluno[5])
            print("cep = ", aluno[6])
            print('*'*41)
        except (Exception, psycopg2.Error) as error:
            print("Erro ao consultar os dados! ", error)

    # Função que consulta TODOS ALUNOS cadastrados
    def consultar_todos(self):
        try:
            query = 'SELECT * FROM organizing_to_care'
            self.cursor.execute(query)
            organizing_to_care_rows = self.cursor.fetchall()
            for row in organizing_to_care_rows:
                print("ra = ", row[0], )
                print("nome_aluno = ", row[1])
                print("email_aluno = ", row[2])
                print("logradouro  = ", row[3])
                print("numero = ", row[4])
                print("complemento = ", row[5])
                print("cep = ", row[6])
                print('*'*41)
        except (Exception, psycopg2.Error) as error:
            print("Erro ao consultar os dados! ", error)
