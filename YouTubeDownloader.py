import os
import shutil
from datetime import datetime
from yt_dlp import YoutubeDL
from colorama import Fore, init
import subprocess

# Inicializa o colorama
init(autoreset=True)

# Função para exibir mensagens de erro em vermelho
def erro(msg):
    print(Fore.RED + msg)

# Função para verificar se o ffmpeg está instalado no sistema
def verificar_ffmpeg():
    try:
        # Executa o comando 'ffmpeg' para verificar se está no PATH
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

# Função para converter a velocidade de bits para MB/s ou KB/s
def formatar_velocidade(velocidade):
    if velocidade is None or velocidade == 0:
        return "N/A"
    
    # Converter de bits para bytes (1 byte = 8 bits)
    velocidade_bytes = velocidade / 8
    
    if velocidade_bytes >= 1024 * 1024:  # MB/s
        return f"{velocidade_bytes / (1024 * 1024):.2f}MB/s"
    elif velocidade_bytes >= 1024:  # KB/s
        return f"{velocidade_bytes / 1024:.2f}KB/s"
    else:  # bytes/s
        return f"{velocidade_bytes:.2f}B/s"

def baixar_video(url):
    caminho_destino = None  # Inicializa a variável para o caminho do diretório

    # Verifica se o ffmpeg está instalado
    if not verificar_ffmpeg():
        erro("Ocorreu um erro: ffmpeg não está instalado ou não está acessível no PATH do sistema.")
        return

    try:
        # Cria uma pasta com data e horário do download
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        caminho_destino = os.path.join(os.getcwd(), timestamp)
        os.makedirs(caminho_destino, exist_ok=True)

        # Configurações do yt-dlp para baixar vídeo e áudio
        ydl_opts = {
            'outtmpl': os.path.join(caminho_destino, '%(title)s.%(ext)s'),
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Baixa o melhor vídeo e áudio em MP4
            'merge_output_format': 'mp4',  # Garante que a saída será um arquivo .mp4
            'quiet': True,  # Minimiza a quantidade de informações no terminal
            'progress_hooks': [  # Definindo um gancho de progresso personalizado
                lambda d: print(f"\r[download] Velocidade de transferência: {formatar_velocidade(d.get('speed', 0))}", end="") 
                if d['status'] == 'downloading' else None
            ]
        }

        # Baixa o vídeo e áudio
        print("Baixando vídeo e áudio na melhor qualidade disponível em MP4...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("\nDownload concluído!")
        print(f"Arquivos salvos em: {caminho_destino}")

    except Exception as e:
        erro(f"Ocorreu um erro: {e}")
    
        # Se o caminho destino foi criado e o download falhou, remove o diretório
        if caminho_destino and os.path.exists(caminho_destino):
            try:
                shutil.rmtree(caminho_destino)  # Remove o diretório e seu conteúdo
            except Exception as remove_error:
                pass  # Se falhar na remoção, não exibe nada

if __name__ == "__main__":
    url_video = input("Digite a URL do vídeo do YouTube: ")
    baixar_video(url_video)
