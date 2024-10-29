from ui.clientesUI import ClientesUI
from ui.servicosUI import ServicosUI
from ui.horariosUI import HorariosUI
from ui.agendaUI import AgendaUI
import streamlit as st

# Configuração do título da aplicação
st.title("Sistema de Agendamento")

# Navegação entre as páginas
st.sidebar.title("Navegação")
paginas = {
    "Agenda do dia": "./pages/agendaUI.py",
    "Clientes": "./pages/clientesUI.py",
    "Horários": "./pages/horariosUI.py",
    "Serviços": "./pages/servicosUI.py"

}
selecionada = st.sidebar.selectbox("Página selecionada: ", (p for p in paginas.keys()))

# Carregar a página selecionada
if selecionada == "Agenda do dia":
    AgendaUI.main()
elif selecionada == "Clientes":
    ClientesUI.main()
elif selecionada == "Serviços":
    ServicosUI.main()
elif selecionada == "Horários":
    HorariosUI.main()