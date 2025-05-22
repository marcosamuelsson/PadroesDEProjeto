1.1. Factory Method

Onde: create_app() em cliente_app/__init__.py
Explicação:
A função create_app() é um clássico exemplo do padrão Factory Method, onde a criação da 
instância de Flask é encapsulada em uma função para que a aplicação possa ser instanciada 
de forma flexível e reutilizável.
Esse padrão é útil para testes, múltiplas configurações, ou extensão da aplicação.

python
def create_app():
    app = Flask(__name__)
    ...
    return app


---

1.2. Template Method

Onde: Nos arquivos HTML (index.html, pagamento.html, confirmacao.html) com uso do Jinja2
Explicação:
O uso de templates com blocos que podem ser preenchidos dinamicamente é um exemplo do padrão 
Template Method, onde a estrutura principal da interface é definida e partes variáveis são 
"preenchidas" no processo de renderização.

---

1.3. DAO (Data Access Object)

Onde: Produto, Pedido, ItemPedido em models.py
Explicação:
Essas classes são mapeamentos diretos entre as entidades do sistema e o banco de dados (via SQLAlchemy). 
Elas encapsulam o acesso à base de dados, escondendo detalhes da SQL, o que é a definição do padrão DAO.

python
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ...


---

1.4. MVC (Model-View-Controller)

Onde:

 Model -> models.py (classes Produto, Pedido, etc.)
 View -> templates HTML (index.html, pagamento.html, etc.)
 Controller -> routes.py com as rotas Flask
  Explicação:
  A separação entre dados (Model), lógica de controle (Controller) e apresentação (View) segue o padrão 
  arquitetural MVC, que ajuda na organização e escalabilidade do projeto.

---

1.5. Singleton (indiretamente aplicado)

Onde: db = SQLAlchemy() em __init__.py
Explicação:
A instância db é criada uma única vez e inicializada com app em create_app(). Isso garante que só uma conexão 
com o banco seja usada por instância da aplicação. É uma forma controlada de aplicar o padrão Singleton para 
gerenciar acesso global ao banco.

---

1.6. Command Pattern (com Blueprint do Flask)

Onde: Uso de Blueprint em routes.py
Explicação:
O Blueprint encapsula comandos (rotas) em objetos reutilizáveis e independentes, como no Command Pattern, onde 
comandos são encapsulados como objetos para serem registrados e executados.

python
cliente = Blueprint('cliente', __name__, template_folder='templates')
...
@cliente.route('/')
def index():
    ...


---

2. Padrões GRASP (General Responsibility Assignment Software Patterns)

2.1. Controller

Onde: routes.py (funções index, pagamento, confirmacao)
Explicação:
As funções do Flask atuam como Controllers, recebendo eventos da interface e orquestrando ações de acordo com 
a regra de negócio. São responsáveis por coordenar o fluxo entre as camadas (View ↔ Model).

---

2.2. Creator

Onde:

 confirmacao() cria objetos Pedido e ItemPedido
  Explicação:
  A função que precisa de um objeto (Pedido, ItemPedido) é também quem o cria, seguindo o GRASP Creator.

python
novo_pedido = Pedido(...)
item_pedido = ItemPedido(...)


---

2.3. Information Expert

Onde: models.py + Lógica de negócio em routes.py
Explicação:
A responsabilidade por lidar com dados de produtos, pedidos e cálculos de totais está nas classes que 
possuem essa informação — como Produto, Pedido, ItemPedido, ou nas funções que operam diretamente com elas (como pagamento()).

---

2.4. Low Coupling

Onde: Separação de arquivos (models.py, routes.py, templates/, __init__.py)
Explicação:
Cada parte do sistema conhece apenas o necessário para funcionar, o que reduz o acoplamento. Por exemplo, 
routes.py importa os modelos, mas não acessa o banco diretamente.

---

2.5. High Cohesion

Onde: Cada arquivo tem responsabilidades bem definidas.
Explicação:

 models.py -> apenas modelos de dados
 routes.py -> lógica de controle
 templates/ -> apresentação
 __init__.py -> configuração e inicialização

---

3. Orientação a Objetos no Projeto

Características da OO presentes:

- Classes e Objetos

 As classes Produto, Pedido, ItemPedido representam entidades reais da cafeteria.

- Encapsulamento

 A lógica e os atributos de banco de dados estão dentro das classes, evitando que o resto do sistema precise 
 conhecer detalhes da implementação.

- Associação entre Objetos

 Pedido se relaciona com ItemPedido (via db.relationship), demonstrando relações entre objetos.

python
itens = db.relationship('ItemPedido', backref='pedido', lazy=True)


- Modularização e Reuso

 Ao separar a lógica em classes e funções, o projeto favorece reuso e testes.

- Herança

 Todas as classes de modelo herdam de db.Model, que fornece funcionalidades ORM (mapa objeto-relacional).

python
class Produto(db.Model): ...

---

Resumo Geral das Funções do Projeto

| Parte            | Função                                                                |
| -----------------| --------------------------------------------------------------------- |
| index.html       | Exibe os produtos (bebidas e lanches) e permite seleção de quantidade |
| pagamento.html   | Mostra o resumo do pedido e permite escolher método de pagamento      |
| confirmacao.html | Confirma o pedido, mostra o número de senha e detalhes                |
| routes.py        | Controla as rotas da aplicação e lógica de fluxo                      |
| models.py        | Define as entidades e suas relações com o banco                       |
| __init__.py      | Inicializa a aplicação e popula o banco com os produtos               |
| cafeteria.db     | Armazena pedidos e produtos usando SQLite                             |
