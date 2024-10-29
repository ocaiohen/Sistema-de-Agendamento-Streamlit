import json

class Servico:
    def __init__(self, id: int, descricao: str, valor: float, duracao: int):
        self.id = id 
        self.descricao = descricao
        self.valor = valor
        self.duracao = duracao
    def __str__(self):
        return f"ID: {self.id}; Descrição: {self.descricao}; Valor: {self.valor}; Duração: {self.duracao}"

class Servicos:
    servicos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()

        m = 0
        for c in cls.servicos:
            if c.id > m: m = c.id
        obj.id = m + 1
        cls.servicos.append(obj)
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        s = cls.listar_id(obj.id)
        if s != None:
            cls.servicos.remove(s)
            cls.salvar()
    @classmethod
    def atualizar(cls, obj):
        s = cls.listar_id(obj.id)
        if s != None:
            s.descricao = obj.descricao 
            s.valor = obj.valor
            s.duracao = obj.duracao
            cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.servicos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for s in cls.servicos:
            if s.id == id: return s
        return None  
    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo: 
            json.dump(cls.servicos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.servicos = []
        try:
            with open("servicos.json", mode="r") as arquivo:  
                texto = json.load(arquivo)
                for obj in texto:   
                    s = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
                    cls.servicos.append(s)
        except FileNotFoundError:
            with open("servicos.json", mode="w") as arquivo:
                json.dump([], arquivo)  # Cria um arquivo vazio