from clientes import Cliente, Clientes

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
