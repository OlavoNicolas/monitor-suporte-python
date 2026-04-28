from processo.sistema import SO
import os
sistema = SO()

def limpar_tela():
    os.system('cls' if sistema.testeSO() == "Windows" else 'clear')