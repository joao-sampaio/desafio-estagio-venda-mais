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
  * Entre na pasta do repositório que você acabou de clonar: `cd desafio-estagio-venda-mais`
2. Crie um ambiente virtual para o projeto

  * Linux: `python3 -m venv venv && source .venv/bin/activate`
  * Windons: `py -m venv .venv && .venv\Scripts\activate.bat`
3. Instale as dependências

  * Linux: `python3 -m pip install -r requirements.txt`
  * Windons: `pip install -r requirements.txt`
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
O sistema organiza os usuários em uma hierarquia de permissões que vai de um a cinco, sendo 5 o administrador e 1 o cliente. Cada tipo de usuário possui permissões diferentes, excerto o administrador, que possui todas.

* Para facilitar a demonstração de seu funcionamento a aplicação já possui usuários cadastrados com dados fictícios e arbitrários. Nesse sentido, cada usuário é nomeado de acordo com seu tipo.
> Ex: admin, gerente2, atendente1, cliente1, helper4
* E suas senhas são a primeira letra do seu nome repetida quatro vezes seguida de 1234
> Ex: aaaa1234, gggg1234, aaaa1234, cccc1234, hhhh1234

## A seguir uma explicação do fluxo de cada tipo de usuário:

### Admin
O usuário com maior nível na hierarquia, pode ver e modificar toda a aplicação.
> Existe apenas um admin cadastrado.

### Gerente
Usuário de nível 4, pode:

* Gerenciar, criar e definir a disponibilidade de serviços
* Cadastrar novos atendentes
* Gerar relatório diário

> Existem 2 gerentes cadastrados

### Atendente
Usuário de nível 3, pode:

* Gerenciar Atendimentos
* Gerar relatório diário
 
> Existem 3 gerentes cadastrados

### Helpers
Usuário de nível 2, não tem permissões especiais, mas pode acessar a área administrativa
> Existem 4 helpers cadastrados

### Cliente
Usuário de primeiro nível, não tem permissão de acessar a área administrativa, mas pode:

* Cadastrar-se
* Agendar novos atendimentos
 
> Existe apenas um cliente cadastrado

---

## Fluxo do Cliente

### Cadastro
Através do formulário disponível em http://localhost:8000/cadastro

### Login
1. Através do formulário disponível em http://localhost:8000/login
2. Ou http://localhost:8000 como visto no início

### Agendamento
Através do formulário disponível em http://localhost:8000/agendamento

---

## Fluxo administrativo

### Cadastro
O cadastro de funcionários deve ser feito por um admin ou gerente através da área administrativa

### Login
Através do formulário disponível em http://localhost:8000/admin

#### Nesse momento o fluxo se divide em tipos de usuários:

<details>
  <summary><strong>Gerentes</strong></summary><br />

* username: gerenteN sendo N o número do funcionários(2 >= N >= 1) senha: gggg1234

  Gerentes  podem consultar e alterar serviços e cadastrar novos atendentes
> Ex: Mudar a disponibilidade de um serviço ou seu preço.
</details>

<details>
  <summary><strong>Atendentes</strong></summary><br />

* username: atendetenteN sendo N o número do funcionário(3 >= N >= 1) senha: aaaa1234

  Atendentes apenas podem consultar e modificar atendimentos agendados por um cliente
> Ex: Definir um helper para executar o serviço ou reagendar para outra data
</details>

<details>
  <summary><strong>Helpers</strong></summary><br />

* username: helperN sendo N o numero do funcionário(4 >= N >= 1) senha: hhhh1234

  Helpers não podem fazer nada.
</details>

---

## Funções de relatorio

1. Funcionários com acesso à lista de atendimentos podem filtrar os resultados com base em parâmetros arbitrários, por exemplo:

 Digamos que um gerente queira ver uma tela listando todos atendentes e seus serviços no dia usando uma cor para diferenciar cada STATUS do serviço e que ao clicar no serviço sejam listados os detalhes do mesmo(valor, horário do serviço, atendente e cliente).

* Bastaria acessa a plataforma, selecionar a opção "Atendimentos" no menu lateral esquerdo e em seguida usar o menu lateral direito para filtrar os atendimentos, Por Data e Hora do Serviço => Hoje, Por Situação => Realizado.

2. Funcionário de nível maior ou igual a 3(atendentes, gerentes e admin) tem acesso a url http://localhost:8000/relatorio
que gera e exibe um relatório diário listando todos os atendimentos e o valor total de todos eles.

---

# Considerações finais

Apesar de não ter concluído todos os requisitos, estou satisfeito com o resultado do projeto/desafio. Nos últimos sete dias tive a oportunidade de adquirir um conhecimento substancial do funcionamento do django. Apesar de muito extenso, o framework é bem documentado e sua merecida popularidade possibilita que usuários menos experientes tenham sempre onde procurar por referências.
