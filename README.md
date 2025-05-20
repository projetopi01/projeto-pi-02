<h1 align="center">
  <img alt="Gerenciador de Cadastro de Gestantes" title="GestantesApp" src=".github/logo.png" width="200px" />
</h1>

<h3 align="center">Gerenciador de Cadastro de Gestantes: API, Frontend e Banco de Dados</h3>

<blockquote align="center">“Cuidar do início da vida é construir um futuro saudável e promissor.”</blockquote>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-instalação-e-execução">Instalação e Execução</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-api">API</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-licença">Licença</a>
</p>

<br>

<p align="center">
  <img alt="PROJETO DO GERENCIADOR" src=".github/gestantes_app.png" width="100%">
</p>

---

## 🧪 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias e ferramentas:

### Backend
- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Gunicorn](https://gunicorn.org/)
- [Pytest](https://docs.pytest.org/)

### Frontend
- **HTML5, CSS3, JavaScript**
- Scripts interativos com JavaScript para cálculo de idade, semanas, edição de exames e busca de CEP.

### Banco de Dados
- [SQLite](https://www.sqlite.org/) (ambiente local)
> Observação: em produção recomenda-se PostgreSQL para persistência de dados na nuvem.

### Integrações e API
- [ViaCEP](https://viacep.com.br/) — Busca automática de endereço por CEP.
- API REST interna com endpoints para consultar gestantes e exames via JSON.

### Deploy e CI/CD
- [Render](https://render.com/) — Hospedagem da aplicação web.
- [GitHub](https://github.com/) + [GitHub Actions](https://github.com/features/actions) — Versionamento e Integração Contínua.

### Acessibilidade
- Implementação de boas práticas como `aria-label`, foco via teclado, contraste e semântica HTML.

---

## 💻 Projeto

O **Gerenciador de Gestantes** é uma aplicação voltada para o acompanhamento pré-natal de gestantes. Ele permite:

- Cadastro de gestantes com dados completos
- Cálculo automático de idade e semanas de gestação
- Tabela cronológica interativa de exames
- Status coloridos editáveis nos exames
- Busca por CPF
- Visualização de dados e exames já preenchidos
- Fornecimento de API REST com os dados cadastrados

---

## ⚙️ Instalação e Execução

### Clone o repositório:
```bash
git clone https://github.com/seuusuario/gerenciador-gestantes.git
cd gerenciador-gestantes
```

### Backend
```bash
cd backend
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
.env\Scriptsctivate

pip install -r requirements.txt
```

### Executar localmente:
```bash
python app.py
# O servidor estará disponível em http://127.0.0.1:5000
```

### Frontend
```bash
cd frontend
# Abra o arquivo index.html no navegador
```

---

## 🔬 Testes Automatizados

### Para rodar testes com Pytest:
```bash
cd backend
pytest
```

> Os testes são executados automaticamente também via GitHub Actions a cada push na branch `main`.

---

## 📡 API

### Endpoints disponíveis:

#### GET `/api/gestante`
Retorna uma lista com todos os cadastros de gestantes.

#### GET `/api/gestante/<cpf>`
Retorna os dados de uma gestante específica, com base no CPF informado.

#### POST `/api/exames_status`
Recebe dados atualizados da tabela de exames para salvar no banco.

---

## 📂 Estrutura do Projeto

```bash
gerenciador-gestantes/
├── backend/
│   ├── app.py
│   ├── api.py
│   ├── models.py
│   ├── templates/
│   │   ├── cadastro_gestante.html
│   │   ├── login_page.html
│   │   ├── success_page.html
│   ├── static/
│   │   └── styles.css
│   ├── requirements.txt
│   └── Procfile
│
├── frontend/
│   ├── index.html
│   ├── cadastro_gestante.html
│   ├── login_page.html
│   └── static/
│       └── styles.css
│
├── docs/
│   └── documentação.md
└── .github/
    └── workflows/
        └── python-tests.yml
```

---

## 📝 Licença

Esse projeto está sob a licença MIT.  
Veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
