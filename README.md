# Automação de "Cadastros"

Este projeto tem como objetivo automatizar o preenchimento de formulário em um site fictício desenvolvido em Flask.

A automação é realizada utilizando a biblioteca PyAutoGUI, que simula interações com a interface gráfica do site, como clicar, digitar, selecionar campos de formulários entre outras funcionalidades.

A parte de leitura da base de dados será realizada pela biblioteca Pandas, na qual servirá para realizar a leitura e interação das informações contidas em um arquivo .csv.

O processo é alimentado pelo arquivo "alunos_informacoes.csv" na qual contém informações fictícias de alunos, como nome, registro acadêmico (RA), data de nascimento, curso, valor do curso, se o aluno paga o valor integral ou se ele é bolsista em 100% ou 50%. 

Através dessas informações o site revelará, após o preenchimento do formulário o valor que o aluno pagará do curso.

## Objetivo

Este projeto foi desenvolvido com o objetivo de consolidar e demonstrar os conhecimentos adquiridos em diversos cursos que realizei. Durante o processo, explorei ferramentas essenciais de desenvolvimento web, como Flask, técnicas avançadas de automação com PyAutoGUI, e manipulação eficiente de bases de dados utilizando Pandas. O resultado final é um projeto integrado, que une essas tecnologias para resolver problemas de forma prática e inovadora, reforçando minha capacidade de aprendizado contínuo e aplicação de múltiplas ferramentas em um único contexto.


## Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/stable/)
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
* [Pandas](https://pandas.pydata.org/)

## Dependências e Versões Necessárias

* Python - Versão: 3.12.2
* Flask - Versão: 3.0.3
* PyAutoGUI - Versão: 0.9.54
* Pandas - Versão: 2.2.3

## Como rodar o projeto ✅

1. Realize o processo de clone do repositório para adquirir todos os arquivos do projeto.
2. Para a correta utilização da automação, tenha em sua máquina o navegador web "Google Chrome", se já possui pule essa etapa, porém caso não possua, pode-se realizar o download em: 

```
https://www.google.com/chrome/dr/download/?brand=YTUH&ds_kid=43700077650614087&gad_source=1&gclid=EAIaIQobChMI0-jH1oWKiwMVDl9IAB1Q5ghfEAAYASAAEgJSSvD_BwE&gclsrc=aw.ds#gad_source_1
```

3. Utilizando uma IDE, na qual aconselho o "Visual Studio Code - VSCode", execute o arquivo "app.py", isso fará com que sejá ativado um site fictício localmente em sua máquina e a automação comece.
Pode-se utilizar uma outra opção após adquirir o repositório, que é de utilizar diretamente o terminal da sua máquina (lembrando que precisa acessar o diretório correto de onde salvou o arquivo pelo próprio terminal) executando o seguinte comando:

```
python app.py
```

4. Logo após essas etapas a automação iniciará e ao término do preenchimento dos dados, ela termina.

OBS: Lembrando que durante a execução da automação, não pode utilizar a máquina. E caso precise finalizá-la antes do término, somente é necessário arrastar o mouse até o canto superior direito do seu monitor e ela se encerrará automaticamente deixando a máquina livre para o uso.


## 📌 Informações importantes sobre a aplicação 📌

Todos os dados de informações de alunos foram adquiridos de forma fictícia através do ChatGPT, utilizando o seguinte prompt de comando para ele:

"Crie um arquivo em formato .csv na qual contenha informações fictícias de 50 alunos com os seguintes campos em sua coluna: Nome do aluno, RA do aluno, Data de nascimento, Curso, Valor do curso (entre 1200 até 2500, utilizando casas decimais), Integral (sim ou não) ,Bolsa 100% (sim ou não), Bolsa 50% (sim ou não)"

O site elaborado em Flask, também é fictício e não possui vinvulo com nenhuma empresa ou órgão, somente foi produzido para fins de estudos.