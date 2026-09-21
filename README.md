# 🏥 Vitta+ — Sistema de Agendamento de Consultas

Sistema web para gerenciamento de uma clínica de saúde, desenvolvido como projeto acadêmico do curso de **Desenvolvimento Full-Stack em Python — Senac, turma 2026.2**.

O **Vitta+** foi desenvolvido utilizando Django e tem como objetivo centralizar o gerenciamento de médicos, pacientes e consultas, oferecendo uma interface web simples, organizada e responsiva.

---

## 📋 Sobre o Projeto

O Vitta+ é uma aplicação web desenvolvida para simular o funcionamento de um sistema de gerenciamento de uma clínica médica.

A aplicação permite o gerenciamento de informações relacionadas a:

* 👨‍⚕️ Médicos
* 🧑‍🤝‍🧑 Pacientes
* 📅 Consultas
* 🔐 Usuários e autenticação
* 🛡️ Permissões de acesso
* 🖼️ Fotos dos médicos
* ⭐ Avaliação dos médicos
* 🏥 Convênios médicos

O projeto foi desenvolvido com foco na aplicação prática dos conceitos estudados durante o curso de **Desenvolvimento Full-Stack em Python do Senac**.

---

## 🎯 Objetivos

### Objetivo geral

Desenvolver um sistema web utilizando Python e Django capaz de auxiliar no gerenciamento de uma clínica médica.

### Objetivos específicos

* Criar uma aplicação web utilizando Django;
* Implementar operações de cadastro, consulta, edição e exclusão de registros;
* Desenvolver modelos utilizando o ORM do Django;
* Implementar formulários e validações;
* Utilizar autenticação de usuários;
* Implementar controle de permissões;
* Trabalhar com relacionamentos entre modelos;
* Implementar upload de imagens;
* Desenvolver uma interface utilizando Bootstrap;
* Organizar o projeto seguindo a estrutura padrão do Django;
* Aplicar conceitos de desenvolvimento Back-End e Front-End.

---

## ⚙️ Tecnologias utilizadas

### Back-End

* **Python**
* **Django 6.1.1**
* **SQLite**
* Django ORM
* Sistema de autenticação e permissões do Django

### Front-End

* **HTML5**
* **CSS3**
* **Bootstrap 5**
* JavaScript

### Ferramentas

* Git
* GitHub
* Visual Studio Code
* Ambiente virtual Python (`venv`)

---

## 🏗️ Estrutura do Projeto

A estrutura principal do projeto está organizada da seguinte forma:

```text
agenda_consulta/
│
├── agenda/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── consulta/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── doctors/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

### Principais componentes

#### `agenda/`

Contém as configurações principais do projeto Django.

Entre os arquivos estão:

* `settings.py` — configurações da aplicação;
* `urls.py` — URLs principais do projeto;
* `asgi.py` — configuração para servidores ASGI;
* `wsgi.py` — configuração para servidores WSGI.

#### `consulta/`

É a aplicação responsável pelas principais funcionalidades do sistema.

Nela estão localizados:

* Modelos;
* Views;
* Forms;
* URLs;
* Templates;
* Arquivos estáticos;
* Migrations;
* Configurações do Django Admin.

#### `media/doctors/`

Diretório utilizado para armazenar as imagens cadastradas para os médicos.

#### `db.sqlite3`

Banco de dados SQLite utilizado durante o desenvolvimento da aplicação.

#### `manage.py`

Arquivo responsável pela execução dos principais comandos administrativos do Django.

---

## 👨‍⚕️ Médicos

O sistema permite cadastrar e administrar médicos da clínica.

Entre as informações utilizadas estão:

* Nome;
* Data de nascimento;
* CRM;
* Sexo;
* Especialidade;
* Avaliação;
* Local de atendimento;
* Preço da consulta;
* Foto.

Também é possível visualizar os médicos cadastrados e suas respectivas informações.

A avaliação dos médicos utiliza uma escala de **0 a 5 estrelas**.

---

## 🧑‍🤝‍🧑 Pacientes

O sistema possui gerenciamento de pacientes.

Os registros podem conter informações como:

* Nome;
* Data de nascimento;
* CPF;
* Sexo;
* Convênio médico.

O CPF é armazenado no banco de dados sem formatação, enquanto a interface pode apresentá-lo de forma formatada.

Exemplo:

```text
Armazenado:
12345678900

Exibido:
123.456.789-00
```

---

## 📅 Consultas

O módulo de consultas permite controlar os agendamentos realizados na clínica.

Uma consulta relaciona:

```text
Médico
   │
   └── Consulta
          │
          └── Paciente
```

Cada consulta possui informações como:

* Médico;
* Paciente;
* Data e horário.

O sistema também possui validação para evitar que um mesmo médico seja agendado para duas consultas no mesmo horário.

---

## 🔐 Autenticação

O sistema utiliza o sistema de autenticação nativo do Django.

Usuários podem realizar login e acessar as funcionalidades disponíveis de acordo com suas permissões.

As áreas protegidas utilizam o mecanismo de autenticação do Django para impedir o acesso de usuários não autenticados.

---

## 🛡️ Sistema de Permissões

O Vitta+ utiliza o sistema de permissões do Django para controlar o acesso às funcionalidades da aplicação.

As permissões podem ser atribuídas diretamente a um usuário ou por meio de grupos.

Isso permite controlar quais funcionalidades cada usuário pode visualizar e utilizar.

Exemplos de permissões:

```text
Adicionar
Visualizar
Alterar
Excluir
```

O sistema também utiliza as permissões para controlar a exibição de determinadas opções de navegação.

Dessa forma, o usuário visualiza apenas as funcionalidades para as quais possui autorização.

---

## 🖥️ Interface

A interface do sistema foi desenvolvida utilizando **Bootstrap**, permitindo a criação de uma interface responsiva e adaptável a diferentes tamanhos de tela.

O projeto utiliza componentes como:

* Navbar;
* Cards;
* Tabelas;
* Formulários;
* Botões;
* Alertas;
* Modais;
* Sistema de grid responsivo.

A identidade visual da aplicação utiliza a marca **Vitta+**, com foco em uma aparência relacionada à área da saúde.

---

## 📸 Upload de imagens

O sistema permite cadastrar imagens dos médicos.

As imagens são armazenadas no diretório:

```text
media/doctors/
```

O Django utiliza a configuração de arquivos de mídia para gerenciar esses arquivos durante o desenvolvimento.

---

## 🗄️ Banco de Dados

Durante o desenvolvimento, o projeto utiliza **SQLite**.

O arquivo do banco de dados está localizado em:

```text
db.sqlite3
```

O acesso ao banco é realizado através do **Django ORM**, permitindo trabalhar com os dados utilizando os modelos Python em vez de escrever consultas SQL diretamente.

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/DeLemosCoding/agenda_consulta.git
```

Entrar no diretório:

```bash
cd agenda_consulta
```

---

### 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv .venv
```

Ativar o ambiente virtual:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

O projeto atualmente utiliza Django **6.1.1**, além das demais dependências especificadas no arquivo `requirements.txt`.

---

### 4. Executar as migrações

```bash
python manage.py migrate
```

Caso sejam realizadas alterações nos modelos:

```bash
python manage.py makemigrations
```

e depois:

```bash
python manage.py migrate
```

---

### 5. Criar um superusuário

Para acessar o Django Admin:

```bash
python manage.py createsuperuser
```

Informe:

```text
Username:
Email:
Password:
```

---

### 6. Executar o servidor

```bash
python manage.py runserver
```

Por padrão, o Django disponibilizará a aplicação em:

```text
http://127.0.0.1:8000/
```

Caso seja necessário utilizar outra porta:

```bash
python manage.py runserver 8080
```

---

## 🔑 Django Admin

O projeto utiliza o painel administrativo do Django para gerenciamento dos dados.

Após criar um superusuário, o painel pode ser acessado em:

```text
/admin/
```

Exemplo:

```text
http://127.0.0.1:8000/admin/
```

Por meio do Django Admin é possível administrar usuários, grupos, permissões e os registros disponibilizados pela aplicação.

---

## 🔄 Fluxo básico do sistema

O funcionamento geral da aplicação pode ser representado pelo seguinte fluxo:

```text
                    ┌─────────────────┐
                    │      Vitta+     │
                    │   Página Inicial│
                    └────────┬────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
           ┌─────────┐ ┌──────────┐ ┌───────────┐
           │ Médicos │ │ Pacientes│ │ Consultas │
           └────┬────┘ └─────┬────┘ └─────┬─────┘
                │            │            │
                └────────────┼────────────┘
                             ▼
                       ┌─────────────┐
                       │   Banco de  │
                       │    Dados    │
                       └─────────────┘
```

---

## 🧩 Arquitetura

O projeto segue a arquitetura baseada no padrão **MVT (Model-View-Template)** utilizado pelo Django.

### Model

Responsável pela representação e persistência dos dados.

```text
models.py
```

### View

Responsável pela lógica das requisições e pelo processamento das informações.

```text
views.py
```

### Template

Responsável pela apresentação das informações ao usuário.

```text
templates/
```

Fluxo simplificado:

```text
Usuário
   │
   ▼
URL
   │
   ▼
View
   │
   ├──────► Model ──────► Banco de Dados
   │
   ▼
Template
   │
   ▼
Usuário
```

---

## 🔒 Segurança

O projeto utiliza recursos nativos do Django relacionados à segurança da aplicação, incluindo:

* Autenticação de usuários;
* Controle de permissões;
* Proteção CSRF;
* Validação de formulários;
* ORM para interação com o banco de dados;
* Restrição de acesso a determinadas views.

Em um ambiente de produção, recomenda-se realizar configurações adicionais de segurança, como:

* `DEBUG = False`;
* Configuração adequada de `ALLOWED_HOSTS`;
* Uso de variáveis de ambiente para informações sensíveis;
* Configuração de HTTPS;
* Configuração adequada de arquivos estáticos e de mídia;
* Banco de dados apropriado para produção.

---

## 📚 Conceitos aplicados

Durante o desenvolvimento foram utilizados diversos conceitos de programação e desenvolvimento web, incluindo:

* Python;
* Programação orientada a objetos;
* Django;
* MVT;
* HTTP;
* URLs e rotas;
* Views;
* Templates;
* Formulários;
* Validação de dados;
* Django ORM;
* Banco de dados;
* CRUD;
* Autenticação;
* Autorização;
* Grupos e permissões;
* Upload de arquivos;
* HTML;
* CSS;
* Bootstrap;
* Git;
* GitHub.

---

## 📝 CRUD

O sistema trabalha com operações fundamentais de gerenciamento de dados:

| Operação   | Descrição                      |
| ---------- | ------------------------------ |
| **Create** | Cadastro de novos registros    |
| **Read**   | Visualização dos registros     |
| **Update** | Edição de registros existentes |
| **Delete** | Exclusão de registros          |

Essas operações são utilizadas principalmente no gerenciamento de médicos, pacientes e consultas.

---

## 👥 Público-alvo

O sistema foi desenvolvido como uma aplicação acadêmica para simular uma solução de gerenciamento de uma clínica médica.

Entre os possíveis usuários estão:

* Administradores;
* Funcionários da clínica;
* Profissionais responsáveis pelo atendimento;
* Usuários autorizados pelo administrador.

---

## 🎓 Projeto acadêmico

Este projeto foi desenvolvido como parte do curso:

**Desenvolvimento Full-Stack em Python — Senac**

**Turma:** 2026.2

O objetivo é aplicar, em um projeto prático, os conhecimentos adquiridos durante o curso nas áreas de desenvolvimento Back-End, Front-End, banco de dados e desenvolvimento de aplicações web.

---

## 👨‍💻 Autores

Projeto desenvolvido por alunos do curso de **Desenvolvimento Full-Stack em Python — Senac 2026.2**.

### Repositório

[DeLemosCoding/agenda_consulta](https://github.com/DeLemosCoding/agenda_consulta)

---

## 📄 Licença

Este projeto foi desenvolvido para fins **acadêmicos e educacionais**.

Seu código pode ser utilizado como referência para estudos relacionados a Python, Django e desenvolvimento Full-Stack.