import streamlit as st

class ClientesUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        
        with listar:
            ClientesUI.listar()
        with inserir:
            ClientesUI.inserir()
        with atualizar:
            ClientesUI.atualizar()
        with excluir:
            ClientesUI.excluir()

    @staticmethod        
    def listar():
        pass
        # st.title("Listar Clientes")
    
    @staticmethod
    def inserir():
        pass
        # st.title("Inserir Cliente")
    
    @staticmethod
    def atualizar():
        pass
        # st.title("Atualizar Cliente")
    
    @staticmethod
    def excluir():
        pass
        # st.title("Excluir Cliente")