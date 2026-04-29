from database.db import conectar
from processo.sistema import SO
from Utils.data_hora import Agora
import subprocess  

sistema = SO()
class TracerTeste:

    def __init__(self):
        self.host = "8.8.8.8"
        self.saida = ""


    def teste(self):
     if sistema.testeSO() == "Windows":
        comando = ["tracert", "-d", self.host]
     else:
        comando = ["traceroute", "-n", self.host]
    
     try:
         resultado = subprocess.run(comando, capture_output=True, text=True)
         self.saida = resultado.stdout.lower()

         if resultado.returncode != 0:
            return False

         linhas = self.saida.strip().split("\n")
         if linhas and self.host in linhas[-1]:
             return True

         return True

     except Exception as e:
            self.saida = str(e)
            return False

    def resultadoTracer(self):
            sucesso = self.teste()
            status = "OK" if sucesso else "Não alcançado"
            horario_atual = Agora()
        
            
            registro = f"Sistema: {sistema.testeSO()} | Data/Hora: {horario_atual.hoje()} | Host: {self.host} -> {status}\n"
            print(registro.strip())
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO tracer_logs (sistema, data_hora, host, status, saida)
            VALUES (?, ?, ?, ?, ?)
            """, (sistema.testeSO(), horario_atual.hoje(), self.host, status, self.saida))

            conn.commit()
            conn.close()


            print("Teste concluido. Log salvo no banco de dados")
