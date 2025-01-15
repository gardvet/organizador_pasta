import os
import shutil
import logging

def organizar_pasta(caminho_pasta):
    try:
        # Configuração básica do logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        if not os.path.exists(caminho_pasta):
            raise FileNotFoundError(f"O caminho '{caminho_pasta}' não existe.")
        if not os.path.isdir(caminho_pasta):
            raise NotADirectoryError(f"'{caminho_pasta}' não é um diretório.")

        file_extensions = set()
        for filename in os.listdir(caminho_pasta):
            caminho_arquivo = os.path.join(caminho_pasta, filename)
            if os.path.isfile(caminho_arquivo) and not filename.startswith("."):  # Ignora arquivos ocultos
                nome, extensao = os.path.splitext(filename)
                if extensao:
                    file_extensions.add(extensao[1:].lower())

        for extension in file_extensions:
            folder_name = f"Arquivos {extension.upper()}"
            folder_path = os.path.join(caminho_pasta, folder_name)
            os.makedirs(folder_path, exist_ok=True)

        for filename in os.listdir(caminho_pasta):
            caminho_arquivo = os.path.join(caminho_pasta, filename)
            if os.path.isfile(caminho_arquivo) and not filename.startswith("."):
                nome, extensao = os.path.splitext(filename)
                if extensao:
                    extensao = extensao[1:].lower()
                    folder_name = f"Arquivos {extensao.upper()}"
                    folder_path = os.path.join(caminho_pasta, folder_name)
                    try:
                        shutil.move(caminho_arquivo, folder_path)
                        logging.info(f"Arquivo '{filename}' movido para '{folder_name}'")
                    except shutil.Error as e:
                        logging.error(f"Erro ao mover '{filename}': {e}")

    except (FileNotFoundError, NotADirectoryError, OSError, PermissionError) as e:
        logging.error(f"Erro: {e}")
    except Exception as e:
        logging.error(f"Erro Inesperado: {e}")

if __name__ == "__main__":
    caminho_pasta = input("Digite o caminho da pasta que deseja organizar: ").strip()
    organizar_pasta(caminho_pasta)
