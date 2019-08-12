# Card API

Projeto core da API CARD

### API's


## Getting started

Como pré-requisito é necessário que se tenha instalado a versão 3.6 do Python.
Instale também o gerenciador de pacotes (pip) para gerenciar as dependências do projeto.


As dependências do projeto estão listadas em requirements.txt.




#### Configurando o ambiente de desenvolvimento

Sempre procure configurar seus projetos em ambientes virtuais para evitar conflitos de bibliotecas com a versão do Python do seu sistema operacional ou de outros projetos que você eventualmente precisará configurar.

Seguem algumas opções de configuração do ambiente virtual:

##### PyEnv

Para bibliotecas exclusivas de desenvolvimento, execute a seguinte sequência para instalar os pré-requisitos:

 1. pyenv (https://github.com/pyenv/pyenv)
    - Instalação (debian / ubuntu):
    ```bash
    $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    $ exec "$SHELL"
    ```
 2. pyenv-virtualenv (https://github.com/pyenv/pyenv-virtualenv)
    - Instalação como plugin do pyenv:
    ```bash
    $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
    $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    $ exec "$SHELL"
    ```

 3. Instalação de bibliotecas necessárias para executar o passo 4:
    ```bash
    $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev
    ```

 4. Python 3.6.3
    - Instalação via pyenv:
    ```bash
    $ pyenv install 3.6.3
    ```


### Execução local

Para rodar o projeto em um servidor local, na raíz do projeto execute:


```
python manage.py runserver
```

O sistema será executado no endereço local, na porta padrão (8000).

### Execução local em docker

1 - Instalar docker:
```
sudo apt-get install docker.io
```

2 - Instalar docker-compose:
```
sudo apt-get install docker-compose
```

3 - Restart no docker:
```
systemctl restart docker
```

Para subir o conteiner com build do zero:
```
sudo docker-compose up --build
```

Para somente subir a api com o build já construído:
```
sudo docker-compose up
```

Acessar o swagger: ```http://localhost:8000/swagger```
