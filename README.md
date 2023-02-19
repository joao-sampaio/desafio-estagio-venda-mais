# Desafio estagio Venda Mais

Repositório dedicado a armazenas minha solução para o desafio

# Inicio

---

# Detalhes do sistema
 Framework: `Django`
 Banco de dados: `SQLite`

---

# Requisitos

1. python3 - https://www.python.org/
2. pip
3. venv - https://docs.python.org/3/library/venv.html (O uso de ambiente virtual não é obrigatorio, mas é altamente recomendado)

---

# Antes de Começar

<details>
  <summary><strong>Configurando o projeto na sua máquina</strong></summary><br />
  1. Clone o repositório

* Use o comando: `git clone git@github.com:joao-sampaio/desafio-estagio-venda-mais.git`
* Entre na pasta do repositório que você acabou de clonar:
  * `cd desafio-estagio-venda-mais`

  2. Crie um ambiente virtual para o projeto

* Linux: `python3 -m venv venv && source .venv/bin/activate`
* Windons: `py -m venv .venv && .venv\Scripts\activate.bat`
  
  3. Instale as dependências

* Linux: `python3 -m pip install -r dev-requirements.txt`
* Windons: `pip install -r dev-requirements.txt`

</details>

<details>
  <summary><strong>Rodando o Projeto localmente</strong></summary><br />
  1. Inicie o servidor local

* Linux: `python3 manage.py runserver`
* Windons: `py manage.py runserver`

  2. Acesse o link: http://localhost:8000/ no seu navegador de preferência
* Se tudo deu certo, você estará agora na página de login do cliente

</details>

---

# Entendendo o sistema

## Hierarquia de usuários
O sistema organisa os usuarios em uma hierarquia de permissões que vai de um a cinco, sendo 5 o administrador e 1 o cliente. Cada tipo de usuario possui permissões diferentes, exerto o administrador, que possui todas.

* Afim de facilitar a demonstração de seu funcionameto aplicação já possui usuarios cadastrados com dados ficticios e harbitrarios. Nesse sentido cada usuario é nomeado de acordo com seu tipo.
> Ex: admin, gerente2, atendente1, cliente1, helper4
* E suas senhas são a primeira letra do seu nome repetida quatro vezes seginda de 1234
> Ex: aaaa1234, gggg1234, aaaa1234, cccc1234, hhhh1234

A seguir uma explicação do fluxo de cada tipo de usuario:

### Admin
O usuario com maior nivel na hierarquia, pode ver e modificar toda a aplicação.
> Existe apenas um admin cadastrado.

### Gerente
Usuario de nivel 4, pode:
 * Gerenciar criar e definir a disponibilidate de serviços
 * Cadastrar novos atendentes
 * Gerar relatorio diario
> Existem 2 gerentes cadastrados

### Atendente
Usuario de nivel 3, pode:
 * Gerenciar Atendimentos
 * Gerar relatorio diario
> Existem 3 gerentes cadastrados

### Helpers
Usuario de nivel 2, não tem permições expeciais, mas pode acessar a area administratuva
> Existem 4 helpers cadastrados

### Cliente
Usuario de primeiro nivel, não tem permição de acessar a area administrativa, mas pode:
 * Cadastrar-se
 * Agendar novos atendimentos
> Existe apenas um cliente cadastrado

---

## Fluxo do Cliente

### Cadastro
Atraves do formulario disponivel em http://localhost:8000/cadastro

### Login
1. Atraves do formulario disponivel em http://localhost:8000/login
2. Ou http://localhost:8000 como visto no inicio

### Agendamento
Atraves do formulario disponivel em http://localhost:8000/agendamento

---

## Fluxo administrativo

### Cadastro
O cadastro de funcionarios deve ser feito por um admin ou gerente atraves da area administrativa

### Login
Atraves do formulario disponivel em http://localhost:8000/admin

#### Nesse momento o fluxo se divide em tipos de usuarios:

<details>
  <summary><strong>Gerentes</strong></summary><br />
* username: gerenteN sendo N o numero do funcionario(2 >= N >= 1) senha: gggg1234
  Gerentes  podem consultar e alterar serviços e cadastrar novos atendentes
> Ex: Mudar a disponibilidade de um serviço ou seu preço.
</details>

<details>
  <summary><strong>Atendentes</strong></summary><br />
* username: atendetenteN sendo N o numero do funcionario(3 >= N >= 1) senha: aaaa1234
  Atendentes apenas podem consultar e modificar atendimentos agendados por um cliente
> Ex: Definir um helper para executar o serviço ou reagendar para outra data
</details>

<details>
  <summary><strong>Helpers</strong></summary><br />
* username: helperN sendo N o numero do funcionario(4 >= N >= 1) senha: hhhh1234
  Helpers não podem fazer nada.
</details>

---

## Funções de relatorio

Funcionarios com acesso a lista de atendimentos podem filtrar os resultados com base em parametros arbitrários, por exemplo:

> Digamos que um gerente queira ver uma tela listando todos atendentes e seus serviços no dia usando uma cor para diferenciar cada STATUS do serviço e que ao clicar no serviço sejam listados os detalhes do mesmo(valor, horário do serviço, atendente e cliente).

* Bastaria acessa a plataforma, selecionar a opção "Atendimentos" no menu lateral esquero e em seguida usar o menu lateral direito para filtrar os atendimentos, Por Data e Hora do Serviço => Hoje, Por Situação => Realizado.

Funcionario de nivel maior ou igual a 3(atendentes, gerentes e admin) tem acesso a url http://localhost:8000/relatorio
que gera e exibe um relatorio diairo listando todos os atendimentos e o valor total de todos eles.

# Considerações finais

Apesar de não ter concluido todos os requisitos estou satisfeito com o resultado do projeto/desafio. Nos ultimos sete dias tive a oportinidade de adiquirir um conhecimento substancial do funcionamento do django. Apesar de muito extenso o framework é bem documentado e sua merecida popularidade possibilita que usuarios menos experientes tenham sempre onde procurar por referencias.
