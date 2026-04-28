from database.db import conectar
from processo.sistema import SO
from Utils.data_hora import Agora
import subprocess  

sistema = SO()
class PingTeste:

    def __init__(self):
        self.host = "8.8.8.8"
        self.saida = ""


    def teste(self):
        if sistema.testeSO() == "Windows":
            comando = ["ping", "-n", "4", self.host]
        else:
            comando = ["ping", "-c", "4", self.host]
        
        try:
            resultado = subprocess.run(comando, capture_output=True, text=True)
            self.saida = resultado.stdout
            return resultado.returncode == 0
        except Exception as e:
            self.saida = str(e)
            return False

    def resultadoPing(self):
            horario_atual = Agora()
            sucesso = self.teste()
            status = "Online" if sucesso else "Offline"
        
            registro = f"Sistema: {sistema.testeSO()} | Data/Hora: {horario_atual.hoje()} | Host: {self.host} -> {status}\n"
            print(registro.strip())

            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO ping_logs (sistema, data_hora, host, status, saida)
            VALUES (?, ?, ?, ?, ?)
            """, (sistema.testeSO(), horario_atual.hoje(), self.host, status, self.saida))

            conn.commit()
            conn.close()

            print("Teste concluído. Log salvo no banco de dados")