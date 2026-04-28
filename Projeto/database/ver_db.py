from database.db import conectar
from Utils.Limpar import limpar_tela
import time

class logs:
 
 def ver_pings(self,limit=10):
    conn = conectar()
    cursor = conn.cursor()
    print("Carregando...")
    time.sleep(1.5)
    limpar_tela()
    cursor.execute("""
    SELECT id, sistema, data_hora, host, status, saida
    FROM ping_logs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

 def ver_portaTeste(self,limit=10):
    conn = conectar()
    cursor = conn.cursor()
    print("Carregando...")
    time.sleep(1.5)
    limpar_tela()
    cursor.execute("""
    SELECT id, sistema, data_hora, host, porta, status, saida
    FROM porta_logs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

 def ver_dnsTeste(self,limit=10):
    conn = conectar()
    cursor = conn.cursor()
    print("Carregando...")
    time.sleep(1.5)
    limpar_tela()
    cursor.execute("""
    SELECT id, sistema, data_hora, host, status, saida
    FROM dns_logs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

 def ver_TracerTeste(self,limit=10):
    conn = conectar()
    cursor = conn.cursor()
    print("Carregando...")
    time.sleep(1.5)
    limpar_tela()
    cursor.execute("""
    SELECT id, sistema, data_hora, host, status, saida
    FROM tracer_logs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

 def ver_PortasUsoTeste(self,limit=10):
    conn = conectar()
    cursor = conn.cursor()
    print("Carregando...")
    time.sleep(1.5)
    limpar_tela()
    cursor.execute("""
    SELECT id, sistema, data_hora, status, saida
    FROM portas_uso_logs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

 def ver_RedeTeste(self,limit=10):
    conn = conectar()
    cursor = conn.cursor()
    print("Carregando...")
    time.sleep(1.5)
    limpar_tela()
    cursor.execute("""
    SELECT id, sistema, data_hora, status, saida
    FROM rede_logs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

 def ver_DiscoTeste(self,limit=10):
    conn = conectar()
    cursor = conn.cursor()
    print("Carregando...")
    time.sleep(1.5)
    limpar_tela()
    cursor.execute("""
    SELECT id, sistema, data_hora, status, saida
    FROM disco_logs
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados
