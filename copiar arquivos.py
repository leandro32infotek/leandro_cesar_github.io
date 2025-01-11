import os
import shutil

def copiar_arquivos(origem, destino):
    try:
        # Verifica se a pasta de origem existe
        if not os.path.exists(origem):
            print(f"A pasta de origem '{origem}' não existe.")
            return

        # Cria a pasta de destino, se não existir
        if not os.path.exists(destino):
            os.makedirs(destino)

        # Lista os arquivos na pasta de origem
        arquivos = os.listdir(origem)
        if not arquivos:
            print("A pasta de origem está vazia.")
            return

        # Copia os arquivos para a pasta de destino
        for arquivo in arquivos:
            caminho_origem = os.path.join(origem, arquivo)
            caminho_destino = os.path.join(destino, arquivo)

            # Ignora arquivos protegidos como desktop.ini
            if not os.path.isfile(caminho_origem) or arquivo == "desktop.ini":
                continue

            shutil.copy2(caminho_origem, caminho_destino)
            print(f"Arquivo '{arquivo}' copiado para '{destino}'.")

        print("Cópia concluída!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Caminhos das pastas (substitua pelos seus caminhos)
pasta_origem = "C:/Users/Desktop/Music"
pasta_destino = "C:/Users/Desktop/OneDrive/Área de Trabalho"

# Chama a função
copiar_arquivos(pasta_origem, pasta_destino)
