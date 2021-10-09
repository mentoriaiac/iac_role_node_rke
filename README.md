IaC Role RKE
=========

Essa role é responsável por instalar tudo necessário para ter no nó de RKE(Rancher Kubernetes Engine).

## Dependências

Para realizar os teste localmente é necessário a instalação das seguintes dependências:

    Python
    Molecule

## Preparando o ambiente

### Primeiro Passo:

Clone este repositório, ele é a base da role do nomad.
> git clone https://github.com/mentoriaiac/iac-role-node-rke


Ao final um diretório com a sua role será criado e você precisa agora entrar neste novo diretório. Para fazer isto use o comando a seguir:
> cd iac-role-node-rke


### Segundo Passo

Para a criação do ambiente virtual do python utilizamos o pipenv.

<https://pipenv.pypa.io/en/latest/>

Será necessária a instalação do pacote seguindo o seguinte procedimento.

```bash

 pip install pipenv

```

Crie um ambiente virtual para o python3. Como o ansible e o molecule são escritos em python, vamos precisar muito de uma estrutura de isolamento. Para criar um ambiente python isolado use o comando a seguir com pipenv:

```bash

python3 -m pipenv install


```

Esse comando irá instalar os requiriments localizados no Pipfile, ele funciona de forma parecida com o requirements do python pip.
### Terceiro Passo

O pipenv aceita dois comandos de interação

pipenv run -> Executa um comando dentro do ambiente virtual

pipenv shell -> Acessa o ambiente virtual

Para os comandos diretos do molecule vamos utilizar o pipenv run.

### Quarto Passo

Para realizar teste rápido após alguma modificação execute a seguinte sequência de comandos:

```bash

pipenv run molecule create

pipenv run molecule converge

pipenv run molecule verify

```

Ao termino do teste, destrua o ambiente

```bash

pipenv run molecule destroy

pipenv run molecule test

```
