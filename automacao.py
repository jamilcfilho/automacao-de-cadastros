import pyautogui
import pandas
import time

# Passo a passo
# Passo 1: Abrir o navegador web -> Google Chrome
pyautogui.PAUSE = 0.8
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 2: Acessar o link do site local -> http://127.0.0.1:5000/
link = "http://127.0.0.1:5000/"
pyautogui.write(link)
pyautogui.press("enter")

# Tempo para o computador carregar o site
time.sleep(1)

# Passo 3: Digitar email e senha e clicar em "Entrar"
email = "exemplo@gmail.com"
senha = "exemplo"
pyautogui.click(x=584, y=415)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 4: Confirmar em "Ok" no verificador de senha
pyautogui.press("enter")

time.sleep(1.5)


# Passo 5: Importar a base de dados
tabela = pandas.read_csv("alunos_informacoes.csv")

time.sleep(1.5)
print(tabela)

# Passo 6: Cadastrar os alunos
for linha in tabela.index:
    pyautogui.click(x=273, y=301)

    nome_aluno = tabela.loc[linha, "Nome do aluno"]
    pyautogui.write(str(nome_aluno))
    pyautogui.press("tab")

    RA_aluno = tabela.loc[linha, "RA do aluno"]
    pyautogui.write(str(RA_aluno))
    pyautogui.press("tab")

    data_nascimento = tabela.loc[linha, "Data de nascimento"]
    # Substitui os traços "-" por uma string vazia, removendo-os
    data_formatada = data_nascimento[8:10] + \
        data_nascimento[5:7] + data_nascimento[0:4]
    pyautogui.write(str(data_formatada))
    pyautogui.press("tab")
    pyautogui.press("tab")

    curso = tabela.loc[linha, "Curso"]
    pyautogui.write(str(curso))
    pyautogui.press("tab")

    valor_curso = tabela.loc[linha, "Valor do curso"]
    pyautogui.write(str(valor_curso))
    pyautogui.press("tab")

    bolsa_100 = tabela.loc[linha, "Bolsa 100%"]
    if bolsa_100 == "Sim":
        pyautogui.press("space")
        pyautogui.press("tab")
    else:
        pyautogui.press("tab")

    bolsa_50 = tabela.loc[linha, "Bolsa 50%"]
    if bolsa_50 == "Sim":
        pyautogui.press("space")
        pyautogui.press("tab")
    else:
        pyautogui.press("tab")

    # Acionar o botão "Enviar"
    pyautogui.press("enter")


# Passo 7: Rolar a página para o final afim de indicar as informações
pyautogui.scroll(-10000)
