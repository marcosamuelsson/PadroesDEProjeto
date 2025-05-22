from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import random
from cliente_app.models.models import produtos_bebidas, produtos_lanches, Pedido, ItemPedido, Produto, db

cliente = Blueprint('cliente', __name__, template_folder='templates')

@cliente.route('/')
def index():
    return render_template('index.html', bebidas=produtos_bebidas, lanches=produtos_lanches)

@cliente.route('/pagamento', methods=['POST'])
def pagamento():
    itens = []
    total = 0

    for produto in produtos_bebidas + produtos_lanches:
        valor = request.form.get(produto['id'], '').strip()
        if valor.isdigit():
            quantidade = int(valor)
            if quantidade > 0:
                subtotal = quantidade * produto['preco']
                total += subtotal
                itens.append({
                    'nome': produto['nome'],
                    'quantidade': quantidade,
                    'preco': produto['preco'],
                    'subtotal': subtotal
                })

    if not itens:
        flash('Você deve selecionar pelo menos um item para prosseguir com o pedido.', 'error')
        return redirect(url_for('cliente.index'))

    session['itens'] = itens
    session['total'] = total
    return render_template('pagamento.html', itens=itens, total=total)

@cliente.route('/confirmacao', methods=['POST'])
def confirmacao():
    itens = session.get('itens', [])
    total = session.get('total', 0)

    if not itens:
        flash('Pedido vazio não pode ser finalizado.', 'error')
        return redirect(url_for('cliente.index'))

    metodo_pagamento = request.form.get('metodo')
    senha = random.randint(1000, 9999)

    novo_pedido = Pedido(
        metodo_pagamento=metodo_pagamento,
        senha=str(senha),
        status='pendente',
        total=total  # NOVO CAMPO
    )
    db.session.add(novo_pedido)
    db.session.flush()  # garante novo_pedido.id para os itens

    for item in itens:
        produto = Produto.query.filter_by(nome=item['nome']).first()
        if produto:
            item_pedido = ItemPedido(
                pedido_id=novo_pedido.id,
                produto_id=produto.id,
                quantidade=item['quantidade']
            )
            db.session.add(item_pedido)

    db.session.commit()

    session.pop('itens', None)
    session.pop('total', None)

    return render_template('confirmacao.html', senha=senha, itens=itens, total=total, metodo=metodo_pagamento)