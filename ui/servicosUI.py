import streamlit as st
import pandas as pd
import views
class ServicosUI:
    @staticmethod
    def main():
        st.header("Serviços")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar:
            ServicosUI.listar()
        with inserir:
            ServicosUI.inserir()
        with atualizar:
            ServicosUI.atualizar()
        with excluir:
            ServicosUI.excluir()
    @staticmethod        
    def listar():
        # st.title("Listar Clientes")
        servicos = views.servico_listar() 

        if servicos:
            servicos_data = {
                "ID": [],
                "Descrição": [],
                "Valor": [],
                "Duracao": []
            }

            for s in servicos:
                servicos_data["ID"].append(s.id)
                servicos_data["Descrição"].append(s.descricao)
                servicos_data["Valor"].append(s.valor)
                servicos_data["Duração"].append(s.duracao)
            
                servicos_df = pd.DataFrame(servicos_data)
                st.dataframe(servicos_df)
        else:
            st.write("Não há serviços cadastrados")
        
        if st.button("Atualizar"):
            servicos = views.servico_listar()

    @staticmethod
    def inserir():
        descricao = st.text_input("Descrição: ")
        valor = st.number_input("Valor: ")
        duracao = st.number_input("Duração: ", step = 1)

        if st.button("Adicionar serviço"):
            if descricao and valor and duracao:
                views.servico_inserir(descricao, valor, duracao)
            else:
                st.error("Preencha todas as informações!")
    
    @staticmethod
    def atualizar():
        servicos = views.servico_listar() 

        if servicos:
            servico_selecionado = st.selectbox("Escolha o serviço a ser excluido: ", (s for s in servicos), index = None, placeholder="Selecione um serviço...")

            descricao = st.text_input("Nova descrição: ")
            valor = st.number_input("Novo valor: ")
            duracao = st.number_input("Nova duração: ", step = 1)

            if st.button("Atualizar cliente"):
                if descricao and valor and duracao and servico_selecionado:
                    views.cliente_atualizar(servico_selecionado.id, descricao, valor, duracao)
                else:
                    st.error("Insira todas as informações!")
        else:
            st.write("Não há serviços para atualizar")
    
    @staticmethod
    def excluir():
        servicos = views.servico_listar() 

        if servicos:
            servico_selecionado = st.selectbox("Escolha o serviço a ser excluido: ", (s for s in servicos), index = None, placeholder="Selecione um serviço...")

            if st.button("Excluir serviços"):
                if servico_selecionado:
                    views.servico_excluir(servico_selecionado.id)
                else:
                    st.error("Selecione um serviço")
        else:
            st.write("Não há serviços para excluir")
    