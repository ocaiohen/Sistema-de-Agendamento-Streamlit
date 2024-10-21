import streamlit as st
import pandas as pd
import views
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
        # st.title("Listar Clientes")
        clientes = views.cliente_listar() 

        if clientes:
            clientes_data = {
                "ID": [],
                "Nome": [],
                "Email": [],
                "Fone": []
            }

            for c in clientes:
                clientes_data["ID"].append(c.id)
                clientes_data["Nome"].append(c.nome)
                clientes_data["Email"].append(c.email)
                clientes_data["Fone"].append(c.fone)
            
            clientes_df = pd.DataFrame(clientes_data)
            st.dataframe(clientes_df)
        else:
            st.write("Não há clientes cadastrados")

    @staticmethod
    def inserir():
        nome = st.text_input("Nome: ")
        email = st.text_input("Email: ")
        fone = st.text_input("Fone: ")

        if st.button("Adicionar cliente"):
            if nome and email and fone:
                views.cliente_inserir(nome, email, fone)
            else:
                st.error("Preencha todas as informações!")
    
    @staticmethod
    def atualizar():
        clientes = views.cliente_listar() 

        cliente_selecionado = st.selectbox("Escolha o cliente a ter as informações atualizadas: ", (c for c in clientes), index = None, placeholder="Selecione um cliente...")

        nome = st.text_input("Novo nome: ")
        email = st.text_input("Novo email: ")
        fone = st.text_input("Novo fone: ")

        if st.button("Atualizar cliente"):
            if nome and email and fone and cliente_selecionado:
                views.cliente_atualizar(cliente_selecionado.id, nome, email, fone)
            else:
                st.error("Insira todas as informações!")
    
    @staticmethod
    def excluir():
        clientes = views.cliente_listar() 

        cliente_selecionado = st.selectbox("Escolha o cliente a ser excluido: ", (c for c in clientes), index = None, placeholder="Selecione um cliente...")

        if st.button("Excluir clientes"):
            if cliente_selecionado:
                views.cliente_excluir(cliente_selecionado.id)
            else:
                st.error("Selecione um cliente!")