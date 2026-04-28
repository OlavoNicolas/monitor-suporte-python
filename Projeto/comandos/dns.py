from database.db import conectar
from processo.sistema import SO
from Utils.data_hora import Agora
import subprocess  

sistema = SO()
class DnsTeste:

    def __init__(self):
        self.host = "google.com"
        self.saida = ""
        

    def teste(self):
     comando = ["nslookup", self.host]
    
     try:
            resultado = subprocess.run(comando, capture_output=True, text=True)
            self.saida = resultado.stdout.lower()

            if resultado.returncode == 0:
                return "Online"
            return "Offline"
     except Exception as e:
            print(f"Erro ao executar nslookup: {e}")
            return "Erro"
    
    def resultadoDns(self):
            status = self.teste()
            horario_atual = Agora()
            
            registro = f"Sistema: {sistema.testeSO()} | Data/Hora: {horario_atual.hoje()} | Host: {self.host} -> {status}\n"
            print(registro.strip())
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO dns_logs (sistema, data_hora, host, status, saida)
            VALUES (?, ?, ?, ?, ?)
            """, (sistema.testeSO(), horario_atual.hoje(), self.host, status, self.saida))

            conn.commit()
            conn.close()


            print("Teste concluido. Log salvo no banco de dados")