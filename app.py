import subprocess
import time
import requests
import os
import sys

# Obter o diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho relativo dos scripts
script_site_local = os.path.join(script_dir, "site_local.py")
script_app = os.path.join(script_dir, "automacao.py")

# Função para iniciar o servidor Flask
def start_flask_server():
    try:
        # Certifique-se de que o Python correto está sendo usado, por isso, caminho absoluto do Python
        python_path = sys.executable  # Usar o Python que está rodando este script
        flask_process = subprocess.Popen([python_path, script_site_local], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return flask_process
    except Exception as e:
        print(f"Erro ao iniciar o servidor Flask: {e}")
        return None

# Função para verificar se o servidor Flask está rodando
def wait_for_server(url, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Servidor Flask está pronto!")
                return True
        except requests.ConnectionError:
            pass
        time.sleep(1)
    print("O servidor Flask não respondeu a tempo.")
    return False

# Função para rodar o script de automação
def run_automation_script():
    try:
        # Usar o mesmo Python para rodar o script de automação
        python_path = sys.executable
        subprocess.run([python_path, script_app], check=True)
    except Exception as e:
        print(f"Erro ao rodar o script de automação: {e}")

# Função principal
if __name__ == "__main__":
    flask_url = "http://127.0.0.1:5000"  # URL do servidor Flask

    # Inicie o servidor Flask
    flask_process = start_flask_server()
    if not flask_process:
        sys.exit("Falha ao iniciar o servidor Flask.")

    print("Iniciando o servidor Flask...")

    # Aguarde o servidor ficar disponível
    if wait_for_server(flask_url):
        # Execute o script de automação
        print("Executando o script de automação...")
        run_automation_script()
    else:
        print("Falha ao iniciar o servidor Flask. Verifique o código do 'site_local.py'.")

    # Finalize o servidor Flask
    flask_process.terminate()
    print("Servidor Flask encerrado.")
