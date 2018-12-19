# Configurando o ambiente

```shell
docker-compose build
```

# Criar um novo projeto

```shell
docker-compose run web create-react-app myapp
```

## Permição para edição do projeto (linux)

```shell
sudo chmod 777 -R myapp
```

## Rodando a aplicação

Abra o arquivo `dockerfile` e adicione os seguintes comandos no final do arquivo caso não exista.

```
WORKDIR /usr/app/myapp
CMD [ "yarn", "start" ]
```

Para iniciar a aplicação.

```shell
docker-compose up
```

# Instalando dependência

Instalando pacotes declarados no `package.json`.

```shell
docker-compose run web yarn install
```

Instalando pacotes explicitamente como por exemplo:

```shell
docker-compose run web yarn add redux react-redux moment
```

<br/><br/>

> *Caso queira mudar o nome do projeto, substituia todas as ocorrencias de "myapp" para o nome do projeto desejado.