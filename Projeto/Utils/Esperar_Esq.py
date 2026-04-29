import time
from processo.sistema import SO
from Utils.Limpar import limpar_tela

sistema = SO()
if sistema.testeSO() == "Windows":
    try:
        import msvcrt
    except ImportError:
        msvcrt = None
else:
    msvcrt = None


def esperar_esc():
    print("Pressione ESC para voltar...")

    if msvcrt:
        while True:
            if msvcrt.kbhit():
                tecla = msvcrt.getch()

                if tecla == b'\x1b':
                    print("Voltando...")
                    time.sleep(2.0)
                    limpar_tela()
                    break

    else:
        input("Pressione Enter para voltar...")
        print("Voltando...")
        time.sleep(2.0)
        limpar_tela()
