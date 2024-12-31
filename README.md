# YouTube Downloader

Este projeto a função de baixar vídeos do YouTube. Ele utiliza o `yt-dlp` para gerenciar o download e o `ffmpeg` para combinar áudio e vídeo. Ele utiliza o yt-dlp para gerenciar o download e o ffmpeg para combinar áudio e vídeo. Além disso, o script inclui a verificação de instalação do ffmpeg no sistema, garantindo que o processo de combinação de formatos funcione corretamente.

## Funcionalidades

- Baixa vídeos e áudios do YouTube na melhor qualidade disponível.
- Exibe a velocidade de download em tempo real durante o processo.
- Cria um diretório único para cada download, baseado na data e hora atual, para evitar sobreposição de arquivos.
- Verifica automaticamente se o `ffmpeg` está instalado no sistema. Se não estiver, exibe uma mensagem de erro.
- Em caso de erro no processo de download, remove automaticamente a pasta criada durante o processo.

## Dependências

Este projeto requer as seguintes dependências para funcionar corretamente:

1. **Instalar as Bibliotecas Necessárias**

O código utiliza as seguintes bibliotecas externas:

- `yt-dlp`: Para realizar o download de vídeos do YouTube e de outros sites.
- `colorama`: Para adicionar cores ao terminal (útil para mostrar mensagens de erro e progresso).
- Você pode instalar todas as dependências de bibliotecas usando o arquivo `requirements.txt`.

2. **FFmpeg** Para baixar vídeos com áudio separado e mesclá-los

O FFmpeg é utilizado para mesclar vídeo e áudio, caso você baixe-os separadamente.

Instalação:

Baixe o FFmpeg [aqui](https://www.ffmpeg.org/download.html).

Extraia o arquivo em um diretório de sua escolha.
Adicione o diretório contendo o executável ffmpeg.exe ao PATH do sistema:

    Exemplo de diretório: C:\ffmpeg\bin\.

Verificação: Execute o comando abaixo no terminal para verificar se o FFmpeg foi configurado corretamente:

    ffmpeg -version

3. **Configuração do PATH (somente Windows)**

Adicionando o FFmpeg ao PATH:

  

No menu iniciar, pesquise por "Variáveis de Ambiente" e selecione "Editar variáveis de ambiente do sistema".

Na seção de variáveis do sistema, edite a variável Path e adicione o caminho onde o FFmpeg foi extraído 

    (ex: C:\ffmpeg\bin)


4. **Garantia de Funcionamento**

Se você seguir as instruções acima e tiver todos os requisitos instalados corretamente, o código deverá funcionar perfeitamente.

## Como Usar

1. Clone ou baixe o repositório para o seu computador.
2. Abra o terminal no diretório onde o projeto foi salvo.
3. Instale as dependências de bibliotecas utilizando o arquivo `requirements.txt`.

````
pip install -r requirements.txt
````
4. Certifique-se de que o ffmpeg esteja instalado e configurado corretamente no seu sistema
5. Execute o script e forneça a URL do vídeo do YouTube para iniciar o download

## Possíveis Erros

- **Erro no ffmpeg**: Se o `ffmpeg` não estiver instalado ou não estiver acessível no PATH do sistema, o script exibirá a seguinte mensagem de erro e não continuará o download:
- **Erro no download**: Se ocorrer algum erro durante o processo de download (por exemplo, erro na URL ou conexão), o script exibirá uma mensagem de erro e removerá o diretório criado durante o processo.
- **Problema com formatos múltiplos**: Se o `ffmpeg` não for encontrado e o download envolver a combinação de formatos de vídeo e áudio, o script exibirá uma mensagem de erro semelhante a:
> ERROR: You have requested merging of multiple formats but ffmpeg is
> not installed. Aborting due to --abort-on-error.
> ERROR: You have requested merging of multiple formats but ffmpeg is
> not installed. Aborting due to --abort-on-error

## Tecnologias Utilizadas

### **Python**

Descrição: Linguagem de programação de alto nível amplamente utilizada para automação, scripts e desenvolvimento de aplicativos.

### **yt-dlp**

Descrição: Biblioteca Python baseada no `youtube-dl`, usada para baixar vídeos e áudios de diversos sites, incluindo o YouTube. O script utiliza o `yt-dlp` para realizar os downloads.

Link: [yt-dlp no GitHub](https://github.com/yt-dlp/yt-dlp)

### **colorama**

Descrição: Biblioteca Python que facilita a utilização de cores no terminal, utilizada neste projeto para exibir mensagens de erro e progresso de forma mais visível.

Link: [colorama no GitHub](https://github.com/tartley/colorama)

### **ffmpeg**

Descrição: Software de código aberto utilizado para converter e manipular arquivos de áudio e vídeo. No projeto, ele é usado para combinar o áudio e o vídeo quando eles são baixados separadamente.

Link: [FFmpeg no site oficial](https://ffmpeg.org/)

### **os**

Descrição: Módulo padrão do Python usado para interagir com o sistema operacional, manipulando arquivos e diretórios.

Link: [os no Python Docs](https://docs.python.org/3/library/os.html)

### **shutil**

Descrição: Módulo padrão do Python utilizado para manipulação de arquivos e diretórios, incluindo operações de cópia, remoção e movimentação de arquivos.

Link: [shutil no Python Docs](https://docs.python.org/3/library/shutil.html)

### **datetime**

Descrição: Módulo padrão do Python que fornece classes para manipulação de datas e horas.

Link: [datetime no Python Docs](https://docs.python.org/3/library/datetime.html)



