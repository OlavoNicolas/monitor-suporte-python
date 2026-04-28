from Utils.Esperar_Esq import esperar_esc
class explicacao:
    def ExplicacaoComandos(self):
        print("\n===== COMANDOS DISPONÍVEIS =====\n")
        print("1) Conectividade (ping)")
        print("   - Testa se um host está acessível na rede.")
        print("   - Mede o tempo de resposta (latência).\n")

        print("2) Rota de Rede (traceroute / tracert)")
        print("   - Mostra o caminho que os pacotes percorrem até o destino.")
        print("   - Ajuda a identificar onde há falhas na rede.\n")

        print("3) Resolução DNS (nslookup / dig)")
        print("   - Converte nomes de domínio em endereços IP.")
        print("   - Útil para diagnosticar problemas de DNS.\n")

        print("4) Teste de Porta (nc / Test-NetConnection)")
        print("   - Verifica se uma porta específica está aberta em um host.")
        print("   - Muito usado para testar serviços (ex: web, banco de dados).\n")

        print("5) Interfaces de Rede (ip a / ipconfig)")
        print("   - Exibe informações das interfaces de rede do sistema.")
        print("   - Mostra IP, máscara, status da conexão, etc.\n")

        print("6) Portas em Uso (ss / netstat)")
        print("   - Lista portas abertas e conexões ativas.")
        print("   - Ajuda a identificar serviços rodando na máquina.\n")

        print("7) Uso de Disco (df / Get-Volume)")
        print("   - Mostra o espaço em disco disponível e utilizado.")
        print("   - Importante para evitar falta de armazenamento.\n")

        print("================================\n")

        esperar_esc()