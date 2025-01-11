import time
from datetime import date
from rich.progress import Progress
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Usuario(Base):
   __tablename__ = "usuarios"
   id = Column(Integer, primary_key=True)
   data = Column(String)
   nome = Column(String)
   cpf = Column(Integer)
   contato = Column(Integer)
   endereco = Column(String)

class Veiculo(Base):
   __tablename__ = "motos"
   id = Column(Integer, primary_key=True)
   data = Column(String)
   servico =Column(String)
   moto = Column(String)
   marca = Column(String)
   placa = Column(String)
   cor = Column(String)
   ano = Column(Integer)
   km = Column(Integer)
   valor_pecas = Column(String)
   mao_de_obra = Column(String)

def barra():
   with Progress() as progress:
      task = progress.add_task("[cyan]--> Por favor, aguarde ...", total=100)
      while not progress.finished:
        progress.update(task, advance=10)
        time.sleep(0.4)

def banco():
   engine = create_engine("sqlite:///my_clients.db")
   Base.metadata.create_all(engine)

   Session = sessionmaker(bind=engine)
   session = Session()

   datas= date.today()

   print(" >>> Seja Bem vindo!\n")
   barra()
   print(" --> Tudo pronto para iniciarmos nosso fluxo trabalho")
   time.sleep(1)
   while True:
      try:
         nomes= input(" Nome: ")
         cpfs= int(input(" CPF: "))
         contatos = int(input(" Contato: "))
         enderecos = input(" Endereço: ")

         novo_usuario = Usuario(data= datas, nome= nomes, cpf= cpfs, contato= contatos, endereco= enderecos)
         session.add(novo_usuario)
         session.commit()

         motos = input(" Moto/Modelo: ")
         marca1 = input(" Marca: ")
         cor1 = input(" Cor: ")
         anos = int(input(" Ano: "))
         placas = input(" Placa: ")
         kms = int(input(" KM: "))
         servicos = input(" Servico: ")
         valor_peca = float(input(" Valor Peças: R$ "))
         valor_m_obra = float(input(" Valor Mao-de-Obra: R$ "))

         nova_moto = Veiculo(moto= motos, marca= marca1, cor= cor1, ano= anos, placa= placas, km= kms, servico= servicos, valor_pecas= valor_peca, mao_de_obra= valor_m_obra, data= datas)
         session.add(nova_moto)
         session.commit()

         print("\n --> Novo registro ...\n")

         sair= int(input(" >>> DIGITE: \n --> 1: continuar (O) \n --> 2: encerrar conexao com o Banco (X) \n\n =  "))
         if sair == 1:
            pass
         elif sair == 2:
            print(" --> Finalizando")
            barra()
            break
      except ValueError:
         print(" --> valor incorreto!")

banco()
