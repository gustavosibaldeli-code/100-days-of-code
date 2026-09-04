import streamlit as st
import banco

# Configuração da página
st.set_page_config(page_title="Painel de Controle - Dia 10", layout="centered")

# Inicializa o banco de dados
banco.conectar()

st.title("📊 Painel de Controle com Banco de Dados")
st.caption("Dia 10 do #100DiasDeCode - CRUD com Python + SQLite + Streamlit")

# --- FORMULÁRIO DE CADASTRO ---
st.subheader("➕ Adicionar Nova Tarefa/Projeto")
with st.form("form_nova_tarefa", clear_on_submit=True):
    col_input, col_status = st.columns([3, 2])
    with col_input:
        titulo = st.text_input("Título / Descrição", placeholder="Ex: Criar API de Autenticação")
    with col_status:
        status = st.selectbox("Status Inicial", ["Pendente", "Em Andamento", "Concluído"])
    
    btn_salvar = st.form_submit_button("Salvar no Banco", use_container_width=True)

    if btn_salvar:
        if titulo.strip():
            banco.adicionar_tarefa(titulo, status)
            st.success(f"✅ '{titulo}' salvo com sucesso!")
            st.rerun()
        else:
            st.warning("⚠️ Digite um título válido antes de salvar.")

st.divider()

# --- LISTAGEM E GERENCIAMENTO ---
st.subheader("📋 Gerenciar Registros no Banco")
registros = banco.listar_tarefas()

if not registros:
    st.info("Nenhum registro encontrado no banco de dados. Adicione o primeiro no formulário acima!")
else:
    # Cabeçalho da tabela
    header1, header2, header3 = st.columns([3, 2, 1])
    header1.markdown("**Título / Projeto**")
    header2.markdown("**Status**")
    header3.markdown("**Ação**")

    for id_t, titulo_t, status_t in registros:
        col1, col2, col3 = st.columns([3, 2, 1])
        
        with col1:
            st.write(f"**#{id_t}** - {titulo_t}")
        
        with col2:
            opcoes = ["Pendente", "Em Andamento", "Concluído"]
            idx_atual = opcoes.index(status_t) if status_t in opcoes else 0
            novo_st = st.selectbox(
                "Mudar status", 
                opcoes, 
                index=idx_atual, 
                key=f"sel_{id_t}", 
                label_visibility="collapsed"
            )
            if novo_st != status_t:
                banco.atualizar_status(id_t, novo_st)
                st.toast(f"Status do item #{id_t} atualizado!")
                st.rerun()
                
        with col3:
            if st.button("🗑️ Excluir", key=f"btn_del_{id_t}", use_container_width=True):
                banco.deletar_tarefa(id_t)
                st.toast(f"Item #{id_t} removido!")
                st.rerun()