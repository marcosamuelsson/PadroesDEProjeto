from datetime import datetime
from cliente_app import db

produtos_bebidas = [
    {'id': 'cafe', 'nome': 'Café', 'preco': 4.0},
    {'id': 'capuccino', 'nome': 'Capuccino', 'preco': 6.0},
    {'id': 'suco', 'nome': 'Suco Natural', 'preco': 5.5},
    {'id': 'mochaccino', 'nome': 'Mochaccino', 'preco': 7.0},
    {'id': 'chagelado', 'nome': 'Chá gelado', 'preco': 5.0},
    {'id': 'refri', 'nome': 'Refrigerante (lata)', 'preco': 5.0}
]

produtos_lanches = [
    {'id': 'pao_queijo', 'nome': 'Pão de Queijo', 'preco': 3.0},
    {'id': 'sanduiche', 'nome': 'Sanduíche Natural', 'preco': 7.5},
    {'id': 'bolo', 'nome': 'Bolo de Cenoura', 'preco': 4.5},
    {'id': 'coxinha', 'nome': 'Coxinha', 'preco': 5.0},
    {'id': 'croassaint', 'nome': 'Croassaint', 'preco': 8.0},
    {'id': 'enrolado', 'nome': 'Enroladinho de salsicha', 'preco': 4.5}
]

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # bebida ou lanche
    
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pendente')
    metodo_pagamento = db.Column(db.String(20))
    senha = db.Column(db.String(10))
    total = db.Column(db.Float, nullable=False)  # NOVO CAMPO ADICIONADO
    itens = db.relationship('ItemPedido', backref='pedido', lazy=True)

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    quantidade = db.Column(db.Integer)
