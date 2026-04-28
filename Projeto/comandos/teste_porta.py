from database.db import conectar
from processo.sistema import SO
from Utils.data_hora import Agora
import subprocess  

sistema = SO()
class PortaTeste:

    def __init__(self):
        self.host = "google.com"
        self.port = "80"
        self.saida = ""


    def teste(self):
     if sistema.testeSO() == "Windows":
        comando = [
         "powershell",
         "-Command",
         f"Test-NetConnection -ComputerName {self.host} -Port {self.port}"]     
     else:
        comando = ["nc", "-zv", self.host, self.port]
    
     try:
            resultado = subprocess.run(comando, capture_output=True, text=True, timeout=10)
            self.saida = resultado.stdout + resultado.stderr
            saida_lower = self.saida.lower()

            if sistema.testeSO() == "Windows":
                return "tcptestsucceeded : true" in saida_lower
            else:
                return resultado.returncode == 0

     except Exception as e:
            self.saida = str(e)
            return False
    
    def resultadoPortaTeste(self):
        sucesso = self.teste()
        status = "OK" if sucesso else "Offline"
        horario_atual = Agora()
            
       
        registro = f"Sistema: {sistema.testeSO()} | Data/Hora: {horario_atual.hoje()} | Host: {self.host} Port: {self.port} -> {status}\n"
        print(registro.strip())

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO porta_logs (sistema, data_hora, host, porta, status, saida)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (sistema.testeSO(), horario_atual.hoje(), self.host, self.port, status, self.saida))

        conn.commit()
        conn.close()


        print("Teste concluido. Log salvo no banco de dados")