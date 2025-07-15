=======================
Saberes da Terra
=======================

Bem-vindo ao repositório do projeto "Saberes da Terra". Este arquivo fornece todas as instruções necessárias para instalar e executar a aplicação em um ambiente de desenvolvimento local.

-----------------------
📝 DESCRIÇÃO
-----------------------

(Sugestão: Adicione aqui uma ou duas frases que descrevam o objetivo principal do seu site. Por exemplo: "O 'Saberes da Terra' é uma plataforma para conectar produtores locais a consumidores, promovendo a agricultura sustentável e o comércio justo na nossa região.")

-----------------------
🛠️ TECNOLOGIAS UTILIZADAS
-----------------------

* Backend: Python, Flask
* Frontend: HTML, CSS, JavaScript
* Banco de Dados: SQLite (substitua se estiver usando outro, como PostgreSQL ou MySQL)

-----------------------
✅ PRÉ-REQUISITOS
-----------------------

Antes de começar, certifique-se de que você tem o Python 3.8 (ou superior) e o 'pip' instalados na sua máquina.

* Python 3: https://www.python.org/downloads/
* Pip: https://pip.pypa.io/en/stable/installation/

-----------------------
⚙️ INSTALAÇÃO
-----------------------

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Clone o repositório:
   git clone https://github.com/TaisTournier/site_saberesdaterra.git
   cd site_saberesdaterra

2. Crie e ative um ambiente virtual:
   É uma boa prática isolar as dependências do projeto.

   - No Windows:
     python -m venv venv
     .\venv\Scripts\activate

   - No macOS e Linux:
     python3 -m venv venv
     source venv/bin/activate

3. Instale as dependências:
   O arquivo `requirements.txt` contém todas as bibliotecas Python necessárias.
   (Importante: Certifique-se de que seu projeto tem um arquivo `requirements.txt`. Se não tiver, você pode gerá-lo com o comando `pip freeze > requirements.txt` depois de instalar as dependências manualmente).
   
   pip install -r requirements.txt

-----------------------
🚀 EXECUÇÃO
-----------------------

Com o ambiente configurado e as dependências instaladas, siga estes passos para iniciar a aplicação:

1. Inicie o servidor de desenvolvimento Flask:
   (Nota: Verifique se o arquivo principal do seu projeto se chama `app.py`. Se tiver outro nome, como `run.py` ou `main.py`, altere o comando abaixo de acordo).

   flask run

   Se o comando acima não funcionar, você pode tentar executá-lo diretamente com o Python:
   python app.py

2. Acesse a aplicação:
   Abra seu navegador e acesse o seguinte endereço:
   http://127.0.0.1:5000/

Pronto! A aplicação "Saberes da Terra" deve estar rodando localmente na sua máquina.