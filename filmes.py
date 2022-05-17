import requests
import json

url = "http://177.101.203.139/edecio/filmes.json"

def titulo(msg, traco="-", tam=50):
    print()
    print(msg)
    print(traco*tam)

def listar_serv():
    titulo(msg="Listagem de filmes", tam=98)
    response = requests.get(url)
    filmes = json.loads(response.text)

    print("Cód. Nome do Filme.....................: Genero..............: Empresa.....: Ano Exib...: Publico.:")

    for i, filme in enumerate(filmes):
        print(
            f"{filme['id']:4d} {filme['titulo'][0:35]:35s} {filme['genero'][0:20]:20s} {filme['empresa_distribuidora'][0:20]:20s} {float(filme['ano_exibicao']):4.0f} {float(filme['publico_ano_exibicao']):10.0f} ")
        if i == 200:
            break
def filtro_pais_prod():
  titulo(msg="Filtro por Pais de Origem", tam=98)

  pais = input("Informe o Pais: ")
  response = requests.get(url)
  filmes = json.loads(response.text)
  print("Cód. Nome do Filme.....................: Pais............ Publico.:")

  contador = 0
  for filme in filmes:
        if filme["pais_produtor_obra"] == pais:
            print(
                f"{filme['id']:4d} {filme['titulo'][0:35]:35s} {filme['pais_produtor_obra']:20s}  {float(filme['publico_ano_exibicao']):10.0f}")
            contador += 1                

  if contador == 0:
        print("* Obs.: Não há Filmes produzidos neste Pais")

def salvar_local():
  titulo("Salvar Dados na Máquina Local")
  print("Aguarde...")
  response = requests.get(url)
  filmes = json.loads(response.text)
  dados = []

  for i, filme in enumerate(filmes):
    if filme['publico_ano_exibicao'] > 100000:
        novo = {"id": filme['id'], "ano": float(filme['ano_exibicao']), "titulo": filme['titulo'][0:35], "genero": filme['genero'], "pais_produtor_obra": filme['pais_produtor_obra'], "nacionalidade": filme['nacionalidade'], "empresa_distribuidora": filme['empresa_distribuidora'], "publico_ano_exibicao": float(filme['publico_ano_exibicao']), "renda_ano_exibicao": float(filme['renda_ano_exibicao'])}
        print(f"Salvando: {filme['titulo']}")
        dados.append(novo)
        if i == 200:
            break    
  with open("filmes.json", "w") as arq:
        json.dump(dados, arq, indent=4)

def listar_local():
    titulo(msg="Listagem de Filmes (máquina local)", tam=98)
    with open("filmes.json", "r") as arq:
        dados = json.load(arq)
    print("Cód. Nome do Filme.....................: Genero..............: Empresa.....: Ano Exib...: Publico.:")
    for filme in dados:
       print(
            f"{filme['id']:4d} {filme['titulo'][0:35]:35s} {filme['genero'][0:20]:20s} {filme['empresa_distribuidora'][0:20]:20s} {float(filme['ano']):4.0f} {float(filme['publico_ano_exibicao']):10.0f} ")
def estatistica():
   titulo(msg="Estatisticas dos Filmes", tam=98)
   response = requests.get(url)
   filmes = json.loads(response.text)
   n_filmes = 0
   n_filmes_18 = 0
   n_filmes_19 = 0
   pm_filmes = 0

   for i, filme in enumerate(filmes):
     n_filmes += 1
     pm_filmes += filme['publico_ano_exibicao']
     if filme['ano_exibicao'] == 2018:
       n_filmes_18 += 1
     if filme['ano_exibicao'] == 2019:
       n_filmes_19 += 1
     media = pm_filmes/n_filmes
   print(f"Nº de Filmes............: {n_filmes}")
   print(f"Nº de Filmes em 2018....: {n_filmes_18}")
   print(f"Nº de Filmes em 2019....: {n_filmes_19}")
   print(f"Média de Publico........: {media:9.2f}")

def genero():
   titulo(msg="Filmes por Genero", tam=98)
   response = requests.get(url)
   filmes = json.loads(response.text)
   fic = 0
   doc = 0
   ani = 0

   for i, filme in enumerate(filmes):
     if filme['genero'] == 'Ficção':
       fic += 1
     if filme['genero'] == 'Documentário':
       doc += 1
     if filme['genero'] == 'Animação':
       ani +=1
   
   print(f"Nº de Filmes Ficção............: {fic}")
   print(f"Nº de Filmes Documentário......: {doc}")
   print(f"Nº de Filmes Animação..........: {ani}")
   
def bonus():
  titulo("Salvar Dados na Máquina Local dos filmes BR")
  print("Aguarde...")
  response = requests.get(url)
  filmes = json.loads(response.text)
  dados = []
  for i, filme in enumerate(filmes):
    if filme['pais_produtor_obra'] == 'Brasil':
         novo = {"id": filme['id'], "ano": float(filme['ano_exibicao']), "titulo": filme['titulo'][0:35], "genero": filme['genero'], "pais_produtor_obra": filme['pais_produtor_obra'], "nacionalidade": filme['nacionalidade'], "empresa_distribuidora": filme['empresa_distribuidora'], "publico_ano_exibicao": float(filme['publico_ano_exibicao']), "renda_ano_exibicao": float(filme['renda_ano_exibicao'])}
         print(f"Salvando: {filme['titulo']}")
         dados.append(novo)
         if i == 200:
            break    
  with open("filmes_brasileiro.json", "w") as arq:
        json.dump(dados, arq, indent=4)

while True:
    titulo("Dados de Produtos de Estética", "=")
    print("1. Listar dados do servidor")
    print("2. Filtrar por Pais")
    print("3. Salvar dados na máquina local")
    print("4. Listar dados da máquina local")
    print("5. Estatística")
    print("6. Agrupar por Genero")
    print("7. Bonus")
    print("8. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listar_serv()
    elif opcao == 2:
        filtro_pais_prod()
    elif opcao == 3:
        salvar_local()
    elif opcao == 4:
        listar_local()
    elif opcao == 5:
        estatistica()
    elif opcao == 6:
        genero()
    elif opcao == 7:
        bonus()
    else:
        break