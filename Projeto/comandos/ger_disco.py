from database.db import conectar
from processo.sistema import SO
from Utils.data_hora import Agora
import subprocess  

sistema = SO()
class GerDiscoTeste:

    def __init__(self):
        self.saida = ""


    def teste(self):
     if sistema.testeSO() == "Windows":
        comando = ["powershell", "-Command", "Get-Volume"]
   
     else:
        comando = ["df", "-h"]
    
     try:
         resultado = subprocess.run(comando, capture_output=True, text=True)
         self.saida = resultado.stdout if resultado.stdout else resultado.stderr
         if resultado.returncode != 0 or not self.saida:
               return "Error"

         return "OK" 
     except Exception as e:
            print(f"Erro ao verificar disco: {e}")
            return "Erro"
     
    def resultadoGerDisco(self):
            status = self.teste()
            horario_atual = Agora()
            
            registro = f"Sistema: {sistema.testeSO()} | Data/Hora: {horario_atual.hoje()} | {status}\n"
            print(registro.strip())
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO disco_logs (sistema, data_hora, status, saida)
            VALUES (?, ?, ?, ?)
            """, (sistema.testeSO(), horario_atual.hoje(), status, self.saida))

            conn.commit()
            conn.close()


            print("Teste concluido. Log salvo no banco de dados")