# ATV09 - Portal em Django

## Identificação da dupla

- José Kayky Barros Dantas
- Antonio [SOBRENOME COMPLETO]
- Turma 523 - Instituto Federal de Alagoas (IFAL)

## Descrição do projeto

Migração do portal da ATV06 (HTML, CSS, Grid/Flexbox e responsividade) para uma aplicação Django.
O menu e os conteúdos do portal são cadastrados no Django Admin (Models `Menu` e `Conteudo`),
e a navegação usa as URLs e Views do Django.

- `Conteudo`: título, slug, conteúdo HTML e ativo.
- `Menu`: título, tipo de destino (conteúdo interno ou link externo), ordem, ativo, relação com `Conteudo` e URL externa.

## Tecnologias utilizadas

- Python 3
- Django
- SQLite
- HTML5 e CSS3 (Grid, Flexbox e Media Queries)

## Como executar

### 1. Criar e ativar o ambiente virtual

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Executar as migrations

```bash
python manage.py migrate
```

### 4. Carregar os dados iniciais (menu e conteúdos)

```bash
python manage.py carregar_portal
```

### 5. Criar o superusuário

```bash
python manage.py createsuperuser
```

### 6. Executar o servidor

```bash
python manage.py runserver
```

## Acesso

- Aplicação: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/

## Estrutura

```
portal/
├── models.py          (Menu e Conteudo)
├── admin.py
├── views.py
├── urls.py
├── migrations/
├── templates/portal/  (base.html e conteudo.html)
└── static/portal/
    ├── css/style.css
    └── img/
```
