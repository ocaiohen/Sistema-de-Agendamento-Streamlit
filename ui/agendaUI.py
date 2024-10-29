import streamlit as st
from datetime import datetime, timedelta
import views
class AgendaUI:
    @staticmethod
    def main():
        st.header("Agenda do dia")

        data_str = st.text_input("Insira a data no formato dd/mm/aaaa: ")
        horario_inicial_str = st.text_input("Insira o horário inicial no formato HH:MM : ")
        horario_final_str = st.text_input("Insira o horário final no formato HH:MM : ")
        intervalo = st.number_input("Insira o intervalo entre cada horário em minutos: ", step = 1)

        if st.button("Inserir horários"):
            if data_str and horario_inicial_str and horario_final_str and intervalo:
                inicio = datetime.strptime(f"{data_str} {horario_inicial_str}", "%d/%m/%Y %H:%M")
                fim = datetime.strptime(f"{data_str} {horario_final_str}", "%d/%m/%Y %H:%M")

                horarios = []

                while inicio <= fim:
                    horarios.append(inicio)
                    inicio += timedelta(minutes=intervalo)

                for h in horarios:
                    views.horario_inserir(h, False, 0, 0)
            

        
        