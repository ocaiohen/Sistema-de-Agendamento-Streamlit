import streamlit as st
import pandas as pd
import views
from datetime import datetime

class HorariosUI:
    @staticmethod
    def main():
        st.header("Horários")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar:
            HorariosUI.listar()
        with inserir:
            HorariosUI.inserir()
        with atualizar:
            HorariosUI.atualizar()
        with excluir:
            HorariosUI.excluir()
    @staticmethod        
    def listar():
        horarios = views.horario_listar() 

        if horarios:
            horarios_data = {
                "ID": [],
                "Data": [],
                "Confirmado": [],
                "ID Cliente": [],
                "ID Serviço": []
            }

            for s in horarios:
                horarios_data["ID"].append(s.id)
                horarios_data["Data"].append(s.data)
                horarios_data["Confirmado"].append(s.confirmado)
                horarios_data["ID Cliente"].append(s.id_cliente)
                horarios_data["ID Serviço"].append(s.id_servico)
            
                horarios_df = pd.DataFrame(horarios_data)
                st.dataframe(horarios_df)
        else:
            st.write("Não há horários cadastrados")
        
        if st.button("Atualizar"):
            horarios = views.horario_listar()
        pass
    @staticmethod
    def inserir():
        data_str = st.text_input("Insira a data no formato (dd/mm/aaaa HH:MM): ")
        confirmado = st.selectbox("O horário está confirmado? ", (False, True), key = "confirmado_inserir")
        id_cliente = st.number_input("Insira o ID do cliente: ", step = 1, placeholder="ID...", value = 0, min_value = 0)
        id_servico = st.number_input("Insira o ID do serviço: ", step = 1, placeholder="ID...", value = 0, min_value = 0)

        if st.button("Inserir horário: "):
            if data_str:
                data_dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
                st.warning("Inserindo horário")
                views.horario_inserir(data_dt, confirmado, id_cliente, id_servico)
                print("Horário inserido st, em tese")
    
    @staticmethod
    def atualizar():
        horarios = views.horario_listar()

        if horarios:
            selecionado = st.selectbox("Selecione o horário a ser atualizado: ", (h for h in horarios))

            data_str = st.text_input("Insira a nova data no formato (dd/mm/aaaa HH:MM): ")
            confirmado = st.selectbox("O horário está confirmado? ", (False, True), key = "confirmado_atualizar", index = None, placeholder="Selecionado o estado da confirmação...")
            id_cliente = st.number_input("Insira o novo ID do cliente: ", step = 1, placeholder="ID...", value = 0, min_value = 0)
            id_servico = st.number_input("Insira o novo ID do serviço: ", step = 1, placeholder="ID...", value = 0, min_value = 0)

            if st.button("Atualizar horário"):
                if data_str and confirmado and id_cliente and id_servico:
                    data_dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M")

                    views.horario_atualizar(selecionado.id ,data_dt, confirmado, id_cliente, id_servico)
                    horarios = views.horario_listar()
        else:
            st.write("Não há horários para atualizar")

    @staticmethod
    def excluir():
        horarios = views.horario_listar()
        selecionado = st.selectbox("Insira o horário a ser excluido: ", (h for h in horarios), index = None, placeholder="Selecione o horário...")

        if selecionado and st.button("Excluir horário"):
            views.horario_excluir(selecionado.id)
            horarios = views.horario_listar()

    