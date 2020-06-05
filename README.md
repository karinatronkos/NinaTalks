# NinaTalks

**Integrantes:**
- Alexandre Abrahão
- Fernanda Castro
- Karina Tronkos
- Matheus Leal

**Objetivo:**
O objetivo deste trabalho é criar um web site voltado ao mundo UI/UX, tecnologia e desenvolvimento de software. Esse site irá possuir as seguintes páginas:
- Home
- About
- Parcerias
- Palestras/Eventos
- Blog (ter um admin)
- Contato (redirect para o e-mail) - Freebies para download

## Como Usar

### Usando Localmente

- Para utilizar a versão correta do python precisamos instalar o pyenv

- Vamos instalar a versão 3.7 com o seguinte comando:

```pyenv install 3.7.0```

- Instale os pacotes utilizados:

```make setup-python```

- Execute o site localmente:

```make run```

### Usando via Docker

- Para utilizar a docker precisamos instalar o docker-compose

- Execute o site localmente via docker:

```make up```

## Dependencias Necessárias

### Pyenv

Basta executar o seguinte comando no seu terminal:

```curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash ```

- Aguarde a instalação e então será necessário colocar o seguinte trecho de código no seu .bashrc ou .zshrc:

```
export PATH=”~/.pyenv/bin:$PATH”
eval “$(pyenv init -)”
eval “$(pyenv virtualenv-init -)”
```

### Docker 

Você pode verificar as instruções de instalação do Docker [aqui](https://docs.docker.com/install/)
