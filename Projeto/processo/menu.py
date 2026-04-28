from database.ver_db import logs
from processo.executar import executar 
from Utils.Explicacao import explicacao
from Utils.Limpar import limpar_tela
from Utils.Esperar_Esq import esperar_esc
import sys
import time

class menu:
    def MenuPrincipal(self):
      ExpComandos = explicacao()
      loop = True
      while(loop == True):
       print("=" * 36)
       print("   MONITOR DE SUPORTE - v1.0")
       print("=" * 36)
       print("Bem vindo ao monitor de suporte!")
       print("Escolha abaixo um comando:")
       print("[1] Iniciar diagnóstico")
       print("[2] Comandos disponíveis")
       print("[3] Ver logs do banco")
       print("[4] Sair")
  
       try:
          escolhaInicial = int(input("Digite a sua escolha: "))
       except ValueError:
          print("Entrada inválida! Digite um número.")
          time.sleep(1.5)
          limpar_tela()
          continue
       match escolhaInicial:
          case 1:
            print("Carregando...")
            time.sleep(2.0)
            limpar_tela()
            self.autoManual()
          case 2:
            print("Carregando...")
            time.sleep(2.0)
            limpar_tela()
            ExpComandos.ExplicacaoComandos()
          case 3:
            print("Carregando...")
            time.sleep(2.0)
            limpar_tela()
            self.menuLogs()
          case 4:
            limpar_tela()
            print("Fechando programa...")
            time.sleep(2.0)
            limpar_tela()
            sys.exit()
          case _:
            print("ERROR")
            print("Tente novamente!")
            time.sleep(1.5)
            limpar_tela()

    def autoManual(self):
     loop = True
     while(loop == True):   
      print("Você deseja realizar os comados de maneira:")
      print("[1]-Manual")
      print("[2]-Automatico")
      print("[3]-Voltar ao menu principal")
      try:
        escolha = int(input("Digite a sua escolha: "))
      except ValueError:
         print("Entrada inválida! Digite um número.")
         time.sleep(1.5)
         limpar_tela()
         continue
    
      match escolha:
       case 1:
        print("Carregando...")
        time.sleep(2.0)
        limpar_tela()
        self.menuManual()
       case 2:
        print("Carregando...")
        time.sleep(2.0)
        limpar_tela()
        self.menuAuto()
       case 3:
        print("Carregando...")
        time.sleep(2.0)
        limpar_tela()    
        break
       case _:
        print("ERROR")
        print("Tente novamente!")
        time.sleep(1.5)
        limpar_tela()

    def menuManual(self):
     exe = executar()
     loop = True
     while(loop == True):   
      print("Escolha abaixo um comando:")
      print("[1]-Ping [2]-Tracer [3]-Dns [4]-Porta [5]-Rede [6]-Portas em uso [7]-Disco [8]-Menu Principal")
 
      try:
        escolha = int(input("Digite a sua escolha: "))
      except ValueError:
         print("Entrada inválida! Digite um número.")
         time.sleep(1.5)
         limpar_tela()
         continue
    
      match escolha:
       case 1:
        exe.pingRun()
        time.sleep(2.8)
        limpar_tela()
       case 2:
        exe.tracerRun()
        time.sleep(2.8)
        limpar_tela()
       case 3:
        exe.DnsRun()
        time.sleep(2.8)
        limpar_tela()
       case 4:
        exe.PortatesteRun()
        time.sleep(2.8)
        limpar_tela()
       case 5:
        exe.InterfaceRedeRun()
        time.sleep(2.8)
        limpar_tela()
       case 6:
        exe.PortaUsoRun()
        time.sleep(2.8)
        limpar_tela()
       case 7:
        exe.GerDiscoRun()
        time.sleep(2.8)
        limpar_tela()
       case 8:
        print("Carregando...")
        time.sleep(2.8)
        limpar_tela()
        self.MenuPrincipal()
       case _:
        print("ERROR")
        print("Tente novamente!")
        time.sleep(1.5)
        limpar_tela()
    def menuAuto(self):
     while True:
        print("Executando comandos...")
        exe = executar()   
        exe.pingRun()
        exe.tracerRun()
        exe.DnsRun()
        exe.PortatesteRun()
        exe.InterfaceRedeRun()
        exe.PortaUsoRun()
        exe.GerDiscoRun()
        print("Todos Logs foram salvos no banco de dados")
        esperar_esc()
        self.MenuPrincipal()
    
    def menuLogs(self):
     log = logs()
     loop = True
     while(loop == True):   
      print("Escolha abaixo um comando:")
      print("[1]-Log Ping [2]-Log Tracer [3]-Log Dns [4]-Log Porta [5]-Log Rede") 
      print("[6]-Log Portas em uso [7]-Disco [8]-Menu Principal")
      try:
        escolha = int(input("Digite a sua escolha: "))
      except ValueError:
         print("Entrada inválida! Digite um número.")
         time.sleep(1.5)
         limpar_tela()
         continue
    
      match escolha:
       case 1:
        resultados = log.ver_pings()
        if not resultados:
            print("Nenhum log encontrado.")
        else:
          for r in resultados:
            print(f"""
            ID: {r[0]}
            Sistema: {r[1]}
            Data: {r[2]}
            Host: {r[3]}
            Status: {r[4]}
            Saída: {r[5]}
            -------------------------
            """)
        esperar_esc()
       case 2:
        resultados = log.ver_TracerTeste()
        if not resultados:
            print("Nenhum log encontrado.")
        else:
          for r in resultados:
            print(f"""
            ID: {r[0]}
            Sistema: {r[1]}
            Data: {r[2]}
            Host: {r[3]}
            Status: {r[4]}
            Saída: {r[5]}
            -------------------------
            """)
        esperar_esc()
       case 3:
        resultados = log.ver_dnsTeste()
        if not resultados:
            print("Nenhum log encontrado.")
        else:
          for r in resultados:
            print(f"""
            ID: {r[0]}
            Sistema: {r[1]}
            Data: {r[2]}
            Host: {r[3]}
            Status: {r[4]}
            Saída: {r[5]}
            -------------------------
            """)
        esperar_esc()
       case 4:
        resultados = log.ver_portaTeste()
        if not resultados:
            print("Nenhum log encontrado.")
        else:
          for r in resultados:
            print(f"""
            ID: {r[0]}
            Sistema: {r[1]}
            Data: {r[2]}
            Host: {r[3]}
            Porta: {r[4]}
            Status: {r[5]}
            Saída: {r[6]}
            -------------------------
            """)
        esperar_esc()
       case 5:
        resultados = log.ver_RedeTeste()
        if not resultados:
            print("Nenhum log encontrado.")
        else:
          for r in resultados:
            print(f"""
            ID: {r[0]}
            Sistema: {r[1]}
            Data: {r[2]}
            Status: {r[3]}
            Saída: {r[4]}
            -------------------------
            """)
        esperar_esc()
       case 6:
        resultados = log.ver_PortasUsoTeste()
        if not resultados:
            print("Nenhum log encontrado.")
        else:
          for r in resultados:
            print(f"""
            ID: {r[0]}
            Sistema: {r[1]}
            Data: {r[2]}
            Status: {r[3]}
            Saída: {r[4]}
            -------------------------
            """)
        esperar_esc()
       case 7:
        resultados = log.ver_DiscoTeste()
        if not resultados:
            print("Nenhum log encontrado.")
        else:
          for r in resultados:
            print(f"""
            ID: {r[0]}
            Sistema: {r[1]}
            Data: {r[2]}
            Status: {r[3]}
            Saída: {r[4]}
            -------------------------
            """)
        esperar_esc()
       case 8:
        print("Carregando...")
        time.sleep(2.0)
        limpar_tela()
        self.MenuPrincipal()
       case _:
        print("ERROR")
        print("Tente novamente!")
        time.sleep(1.5)
        limpar_tela()