import json

class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.id = id 
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"ID: {self.id}; Nome: {self.nome}; Email: {self.email}; Fone: {self.fone}"

class Clientes:
    clientes = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.clientes:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.clientes.append(obj)
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.clientes.remove(c)
            cls.salvar()
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome 
            c.email = obj.email
            c.fone = obj.fone
            cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.clientes
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.clientes:
            if c.id == id: return c
        return None  
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo: 
            json.dump(cls.clientes, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.clientes = []
        try:
            with open("clientes.json", mode="r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:   
                    b = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    cls.clientes.append(b)
        except FileNotFoundError:
            pass