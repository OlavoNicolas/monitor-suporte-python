from Utils.Limpar import limpar_tela
import msvcrt
import time

def esperar_esc():
        print("Pressione ESC para voltar...")
        while True:
         if msvcrt.kbhit():  
            tecla = msvcrt.getch()
            
            if tecla == b'\x1b':  
                print("Voltando...")
                time.sleep(2.0)
                limpar_tela()
                break