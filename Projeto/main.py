from database.db import criar_tabelas
from processo.menu import menu
from Utils.Limpar import limpar_tela
import time

def main():
    
    limpar_tela()
    
    print("=" * 36)
    print("ENTRANDO...")
    print("=" * 36)
    time.sleep(2.5)
    
    limpar_tela()

    criar_tabelas()  
    m = menu()
    m.MenuPrincipal()

if __name__ == "__main__":
    main()