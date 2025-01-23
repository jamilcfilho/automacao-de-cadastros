from flask import Flask, redirect, request, url_for

app = Flask(__name__)

# Alunos cadastrados (armazenados em memória para simular um banco de dados)
alunos_cadastrados = []

# Página inicial de login


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # Não há validação; qualquer email/senha é aceito
        return redirect(url_for("formulario"))
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: auto;
            }
            .login-container {
                background-color: #fff;
                padding: 50px;
                border-radius: 8px;
                box-shadow: 0 0 50px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }
            .login-container h1 {
                margin-bottom: 50px;
            }
            .login-container input {
                width: 92%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 10px;
                border-align: center;
            }
            .login-container button {
                width: 100%;
                padding: 10px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
            }
            .login-container button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h1>Login</h1>
            <form method="POST">
                <input type="email" name="email" placeholder="Email" required><br>
                <input type="password" name="password" placeholder="Senha" required><br>
                <button type="submit">Entrar</button>
            </form>
        </div>
    </body>
    </html>
    '''

# Página do formulário


@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        # Coleta os dados do formulário
        nome = request.form.get("nome")
        ra = request.form.get("ra")
        data_nascimento = request.form.get("data_nascimento")
        curso = request.form.get("curso")
        valor_curso = float(request.form.get("valor_curso"))
        bolsa_100 = request.form.get("bolsa_100") == "on"
        bolsa_50 = request.form.get("bolsa_50") == "on"

        # Calcula o valor final
        if bolsa_100:
            valor_final = 0
        elif bolsa_50:
            valor_final = valor_curso * 0.5
        else:
            valor_final = valor_curso

        # Salva os dados do aluno
        aluno = {
            "nome": nome,
            "ra": ra,
            "data_nascimento": data_nascimento,
            "curso": curso,
            "valor_curso": valor_curso,
            "bolsa_100": bolsa_100,
            "bolsa_50": bolsa_50,
            "valor_final": valor_final
        }
        alunos_cadastrados.append(aluno)

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulário</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                padding: 50px;
            }
            .form-container {
                background-color: #fff;
                padding: 50px;
                border-radius: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-width: 900px;
                margin: auto;
            }
            .form-container h1 {
                text-align: center;
            }
            .form-container input, .form-container button {
                width: calc(100% - 20px);
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            .form-container button {
                background-color: #28a745;
                color: white;
                border: none;
                cursor: pointer;
            }
            .form-container button:hover {
                background-color: #218838;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            table, th, td {
                border: 1px solid #ddd;
            }
            th, td {
                padding: 8px;
                text-align: center;
            }
            th {
                background-color: #f4f4f4;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>Cadastro de Aluno</h1>
            <form method="POST">
                <input type="text" name="nome" placeholder="Nome do Aluno" required><br>
                <input type="text" name="ra" placeholder="RA do Aluno" required><br>
                <input type="date" name="data_nascimento" required><br>
                <input type="text" name="curso" placeholder="Curso" required><br>
                <input type="number" name="valor_curso" placeholder="Valor do Curso (R$)" step="0.01" required><br>
                <label><input type="checkbox" name="bolsa_100"> Bolsa Integral</label><br>
                <label><input type="checkbox" name="bolsa_50"> Bolsa Parcial</label><br>
                <button type="submit">Enviar</button>
                <button type="reset">Limpar</button>
            </form>
            <table>
                <tr>
                    <th>Nome</th>
                    <th>RA</th>
                    <th>Data de Nascimento</th>
                    <th>Curso</th>
                    <th>Valor do Curso (R$)</th>
                    <th>Bolsa 100%</th>
                    <th>Bolsa 50%</th>
                    <th>Valor Final (R$)</th>
                </tr>
                ''' + ''.join(f'''
                <tr>
                    <td>{aluno['nome']}</td>
                    <td>{aluno['ra']}</td>
                    <td>{aluno['data_nascimento']}</td>
                    <td>{aluno['curso']}</td>
                    <td>{aluno['valor_curso']:.2f}</td>
                    <td>{"Sim" if aluno['bolsa_100'] else "Não"}</td>
                    <td>{"Sim" if aluno['bolsa_50'] else "Não"}</td>
                    <td>{aluno['valor_final']:.2f}</td>
                </tr>
                ''' for aluno in alunos_cadastrados) + '''
            </table>
        </div>
    </body>
    </html>
    '''


if __name__ == "__main__":
    app.run(debug=True)
