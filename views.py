from models.clientes import Cliente, Clientes
from models.servicos import Servico, Servicos
from models.horarios import Horario, Horarios
from datetime import datetime

def cliente_listar():
    return Clientes.listar()
def cliente_inserir(nome: str, email: str, fone: str):
    if nome and fone and email:
        c = Cliente(0, nome, email, fone)
        Clientes.inserir(c)
def cliente_atualizar(id: int, nome: str, email: str, fone: str):
    obj = Clientes.listar_id(id)
    novoObj = Cliente(obj.id, nome, email, fone)
    Clientes.atualizar(novoObj)
def cliente_excluir(id: int):
    obj = Clientes.listar_id(id)
    Clientes.excluir(obj)

def servico_listar():
    return Servicos.listar()
def servico_inserir(descricao: str, valor: float, duracao: int):
    if descricao and valor and duracao:
        s = Servico(0, descricao, valor, duracao)
        Servicos.inserir(s)
def servico_atualizar(id: int, descricao: str, valor: float, duracao: int):
    obj = Servicos.listar_id(id)
    novoObj = Servico(obj.id, descricao, valor, duracao)
    Servicos.atualizar(novoObj)
def servico_excluir(id: int):
    obj = Servicos.listar_id(id)
    Servicos.excluir(obj) 

def horario_listar():
    return Horarios.listar()
def horario_inserir(data: datetime, confirmado: bool, id_cliente: int, id_servico):
    if data:
        h = Horario(0, data, confirmado, id_cliente, id_servico)
        Horarios.inserir(h)
        print("horário inserido")
def horario_atualizar(id: int, data: datetime, confirmado: bool, id_cliente: int, id_servico):
    if data:
        h = Horarios.listar_id(id)
        novo_h = Horario(h.id, data, confirmado, id_cliente, id_servico)
        Horarios.atualizar(novo_h)
def horario_excluir(id: int):
    obj = Horarios.listar_id(id)
    if obj:
        Horarios.excluir(obj)