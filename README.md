# Card API

Projeto core da API CARD
 - Para acessar os dados (criar, update, excluir), utilizar http://127.0.0.1:8000/admin/
 - Usuário: user
 - Senha: senha123

## Getting started

Como pré-requisito é necessário que se tenha instalado a versão 3.6 do Python.
Instale também o gerenciador de pacotes (pip) para gerenciar as dependências do projeto.


As dependências do projeto estão listadas em requirements.txt.


#### Configurando o ambiente de desenvolvimento

Sempre procure configurar seus projetos em ambientes virtuais para evitar conflitos de bibliotecas com a versão do Python do seu sistema operacional ou de outros projetos que você eventualmente precisará configurar.


### Execução local

Para rodar o projeto em um servidor local, na raíz do projeto execute:

```
python manage.py makemigrations
```
```
python manage.py migrate
```
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


### Importação CSV
1 - Para importar os dados do CSV:
- Coloque os arquivos .CSV dentro da pasta core/utils/csv:

2 - Foram criados 2 comandos para preenchimento via CSV:
```
python manage.py insert_clients
```
```
python manage.py insert_cards
```

### Endpoint valid-thru
- Foi desenvolvido o endpoint valid-thru, que recebe dois parametros (year e month) e retorna os cartões ativos com vencimento nesta data:
```
http://127.0.0.1:8000/valid-thru/?month=4&year=2023
```
