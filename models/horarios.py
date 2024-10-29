import json
from datetime import datetime

class Horario:
    def __init__(self, id: int, data: datetime, confirmado: bool, id_c: int, id_s: int):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.id_cliente = id_c
        self.id_servico = id_s
    def __str__(self):
        return f"{self.id} - {self.data}"
    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["data"] = self.data.strftime("%d/%m/%Y %H:%M")
      dic["confirmado"] = self.confirmado
      dic["id_cliente"] = self.id_cliente
      dic["id_servico"] = self.id_servico
      return dic    

class Horarios:
  objetos = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    print("Arquivo aberto, inserindo")
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.data = obj.data
      c.confirmado = obj.confirmado
      c.id_cliente = obj.id_cliente
      c.id_servico = obj.id_servico
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Horario.to_json)
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"), obj["confirmado"], obj["id_cliente"], obj["id_servico"])
          cls.objetos.append(c)
    except FileNotFoundError:
      with open("horarios.json", mode="w") as arquivo:
        json.dump([], arquivo)  # Cria um arquivo vazio