# Monitor de Suporte (Python)

Ferramenta de diagnóstico de rede e sistema desenvolvida em Python, com execução multiplataforma <b>(Linux/Windows)<b/> e persistência de logs em <b>SQLite.<b/>
> Projeto focado em simular cenários reais de suporte técnico, automatizando verificações essenciais e organizando os resultados para análise.

## Proposta

Em ambientes de suporte, muitos problemas são repetitivos: rede lenta, DNS falhando, portas bloqueadas, disco cheio.
Este projeto centraliza esses diagnósticos em uma única ferramenta, permitindo:

* Execução rápida de testes
* Padronização de análises
* Registro histórico dos resultados

## Funcionalidades

* Menu interativo (modo manual e automático)
* Execução de comandos nativos do sistema
* Compatibilidade com Linux e Windows
* Registro de logs estruturados em banco de dados
* Organização modular do código

## Demonstração

<p align="center">
<video src="https://github.com/user-attachments/assets/8d102a73-fcf7-416c-bc24-eed64d98997a" width="600" autoplay loop muted playsinline></video>
</p>

## Comandos implementados

### 1. Conectividade (ping)

* Verifica se um host está acessível
* Mede latência da rede

### 2. Rota de rede (traceroute / tracert)

* Identifica o caminho até o destino
* Ajuda a localizar falhas na rede

### 3. Resolução DNS (nslookup / dig)

* Converte domínio em IP
* Diagnostica problemas de DNS

### 4. Teste de porta (nc / Test-NetConnection)

* Verifica se uma porta está aberta
* Útil para serviços como APIs, bancos, etc.

### 5. Interfaces de rede (ip a / ipconfig)

* Mostra configuração da rede local
* IP, máscara, status da conexão

### 6. Portas em uso (ss / netstat)

* Lista conexões ativas
* Identifica serviços rodando

### 7. Uso de disco (df / Get-Volume)

* Espaço disponível e utilizado
* Prevenção de falhas por falta de armazenamento

## Diferenciais técnicos

* Integração direta com comandos do sistema via `subprocess`
* Persistência estruturada com SQLite
* Criação automática de tabelas
* Separação por camadas (menu, execução, comandos, banco)
* Base pronta para evoluir para monitoramento contínuo

## Tecnologias utilizadas

* Python
* SQLite
* subprocess
* os
* sys
* platform
* datetime
* time
* sqlite3
* msvcrt

## Estrutura do projeto

```bash
monitor-suporte-python/
├── main.py
├── database/
├── comandos/
├── processo/
├── utils/
└── README.md
```

## Como executar
- git clone https://github.com/OlavoNicolas/monitor-suporte-python.git
- cd monitor-suporte-python
- python main.py

## Banco de dados

O sistema utiliza SQLite para armazenar logs dos testes.
As tabelas são criadas automaticamente na inicialização.

Exemplo de dados armazenados:
- Sistema operacional
- Data e hora
- Host/serviço testado
- Status (Online/Offline)
- Saída completa do comando

## Valor para o portfólio

Este projeto demonstra:

- Conhecimento prático de redes
- Automação com Python
- Integração com sistema operacional
- Organização de código
- Persistência de dados

## Autor
Olavo Nicolas

## Observação
Projeto em evolução contínua com foco em aprendizado e aplicação prática de conceitos reais de suporte e infraestrutura.

