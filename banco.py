import sqlite3

NOME_BANCO = "painel.db"

def conectar():
    """Cria a conexão com o banco e a tabela se não existir."""
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def adicionar_tarefa(titulo, status="Pendente"):
    """Insere um novo registro no banco (Create)."""
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo, status) VALUES (?, ?)", (titulo, status))
    conn.commit()
    conn.close()

def listar_tarefas():
    """Busca todos os registros salvos no banco (Read)."""
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, status FROM tarefas ORDER BY id DESC")
    dados = cursor.fetchall()
    conn.close()
    return dados

def atualizar_status(id_tarefa, novo_status):
    """Atualiza o status de um registro existente (Update)."""
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET status = ? WHERE id = ?", (novo_status, id_tarefa))
    conn.commit()
    conn.close()

def deletar_tarefa(id_tarefa):
    """Remove um registro do banco de dados (Delete)."""
    conn = sqlite3.connect(NOME_BANCO)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()