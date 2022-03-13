# API

API para buscar usuários de uma base externa

## Install

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requerimenst.txt.

```bash
virtualenv
```


```bash
pip install -r requirients.txt
```

# Banco de Dados

```
SQlite3
Para exemplo usei o banco local do Django.
```

# Execução

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserve
```

# Documentação

```
http://localhost:8000/swagger/
```

# Oberservações

é necessário usar o username e senha do usuário criado com o createsuperuser para obter o token e usar o refresh token
se preferir visualizar os logs de maneira melhor pode utilizar o django admin pelo link: 
[logs](http://localhost:8000/admin/drf_api_logger/apilogsmodel/)
Dentro do repositório a um collection do postman para auxiliar nos testes. (Framework.postman_collection.json)


## License
[MIT](https://choosealicense.com/licenses/mit/)