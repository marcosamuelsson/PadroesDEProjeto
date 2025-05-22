from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    from cliente_app.models.models import Produto, produtos_bebidas, produtos_lanches

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua-chave-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafeteria.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from cliente_app.routes import cliente
    app.register_blueprint(cliente)

    # usar app.app_context para executar comandos com contexto da aplicação
    with app.app_context():
        db.create_all()

        for p in produtos_bebidas:
            if not Produto.query.filter_by(nome=p['nome']).first():
                db.session.add(Produto(nome=p['nome'], preco=p['preco'], tipo='bebida'))

        for p in produtos_lanches:
            if not Produto.query.filter_by(nome=p['nome']).first():
                db.session.add(Produto(nome=p['nome'], preco=p['preco'], tipo='lanche'))

        db.session.commit()

    return app
