import sqlite3

def conectar():
    return sqlite3.connect("monitor.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    # PING
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ping_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sistema TEXT,
        data_hora TEXT,
        host TEXT,
        status TEXT,
        saida TEXT
    )
    """)

    # TRACEROUTE
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tracer_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sistema TEXT,
        data_hora TEXT,
        host TEXT,
        status TEXT,
        saida TEXT
    )
    """)

    # DNS
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dns_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sistema TEXT,
        data_hora TEXT,
        host TEXT,
        status TEXT,
        saida TEXT
    )
    """)

    # TESTE DE PORTA
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS porta_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sistema TEXT,
        data_hora TEXT,
        host TEXT,
        porta TEXT,
        status TEXT,
        saida TEXT

    )
    """)

    # INTERFACE DE REDE
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rede_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sistema TEXT,
        data_hora TEXT,
        status TEXT,
        saida TEXT
    )
    """)

    # PORTAS EM USO
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS portas_uso_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sistema TEXT,
        data_hora TEXT,
        status TEXT,
        saida TEXT
    )
    """)

    # DISCO
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS disco_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sistema TEXT,
        data_hora TEXT,
        status TEXT,
        saida TEXT
    )
    """)


    conn.commit()
    conn.close()