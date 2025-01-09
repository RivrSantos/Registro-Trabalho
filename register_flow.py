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

   print(">>> Seja Bem vindo!\n")
   barra()
   print("--> Tudo pronto para iniciarmos nosso fluxo trabalho")
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

         print("\n -> Novo registro ...\n")

         sair= int(input("DIGITE: \n--> 1: continuar\n--> 2: encerrar conexao com o Banco\n\n"))
         if sair == 1:
            pass
         elif sair == 2:
            print("Finalizando")
            barra()
            break
      except ValueError:
         print("--> valor incorreto!")

banco()
















# while True:
#     try:
#         # Para ler registros, podemos usar o método query() da sessão. Podemos filtrar, ordenar e executar várias outras operações:
#         cons= int(input("Consultar no Banco de Dados:\n\n --> 1: sim\n --> 2: nao\n\n > "))
#         if cons == 1:
#             cons1= input("Informe COLUNA/filtro:")
#             usuarios = session.query(Usuario).filter_by(cons1).all()
#             for usuario in usuarios:
#                 print(usuario.nome)

#         elif cons == 2:
#             pass

#         #Para atualizar, basta modificar os atributos do objeto e então chamar session.commit():
#         atualizar= int(input("Deseja fazer atualizaçao no Banco de Dados:\n\n --> 1: sim\n --> 2: nao\n\n > "))
#         if atualizar == 1:
#             cons2= input("Informe Colmn/atualizaçao:")
#             usuario = session.query(Usuario).first()
#             usuario.nome = atualizar
#             session.commit()

#         elif atualizar == 2:
#             pass

#         # Para deletar, use o método delete() e então session.commit():
#         deletar= int(input("Deletar usuario:\n\n --> 1: sim\n --> 2: nao\n\n > "))
#         if deletar == 1:
#             cons3= input("Informe ID:")
#             usuario = session.query(Usuario).get(cons3)
#             session.delete(usuario)
#             session.commit()

#         elif deletar == 2:
#             pass
#         saindo= int(input("DIGITE: \n--> 1: continuar\n--> 2: sair\n\n"))
#         if sair == 1:
#             pass
#         elif saindo == 2:
#             print("--> The looping entry program finish...")
#             time.sleep(2)
#             break
#     except ValueError:
#         print("valor incorreto")


# Além do simples filter_by, podemos usar o método filter para construir critérios de filtragem mais complexos, utilizando operadores como ==, !=, <, >, entre outros:
# usuarios = session.query(Usuario).filter(Usuario.idade > 25).all()
# SQLAlchemy nos permite também usar funções SQL nativas, como COUNT, MAX, MIN, diretamente em nossas consultas:
# from sqlalchemy import func

# numero_de_usuarios = session.query(func.count(Usuario.id)).scalar()
# setup.py 
# colocar as dependencias do projeto
# from distutils.core import setup
# setup(console=["workflow.py"])

# lossário Quit() Função nativa do Python para parar a execução do software do Python

# hift + botão direito do mouse Atalho do Windows para abrir o terminal dentro de uma pasta

# ath Módulo do pacote Os com uma função chamada “exist” que verifica se um arquivo existe