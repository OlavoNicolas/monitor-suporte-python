from comandos.ping import PingTeste
from comandos.tracer import TracerTeste
from comandos.dns import DnsTeste
from comandos.teste_porta import PortaTeste
from comandos.InterfaceRede import InterfaceRedeTeste
from comandos.portas_uso import PortasUsoTeste
from comandos.ger_disco import GerDiscoTeste
import time

class executar:
 
 def pingRun(self):
  self.ping = PingTeste()
  print("Iniciando monitoramento do Ping...")
  time.sleep(2.5)
  self.ping.resultadoPing()
 
 def tracerRun(self):
  self.tracer = TracerTeste()
  print("Iniciando monitoramento do Tracer...")
  time.sleep(2.5)
  self.tracer.resultadoTracer()
 
 def DnsRun(self):
  self.dns = DnsTeste()
  print("Iniciando monitoramento do DNS...")
  time.sleep(2.5)
  self.dns.resultadoDns()
 
 def PortatesteRun(self):
  self.Portatest = PortaTeste()
  print("Iniciando monitoramento para Testar porta...")
  time.sleep(5.0)
  self.Portatest.resultadoPortaTeste()
 
 def InterfaceRedeRun(self):
  self.interfaceRede = InterfaceRedeTeste()
  print("Iniciando monitoramento da interface de rede...")
  time.sleep(2.5)
  self.interfaceRede.resultadoInterface()
 
 def PortaUsoRun(self):
  portasUso = PortasUsoTeste()
  print("Iniciando monitoramento das portas em uso...")
  time.sleep(2.5)
  portasUso.resultadoPortasUso()
 
 def GerDiscoRun(self):
  gerDisco = GerDiscoTeste()
  print("Iniciando monitoramento do disco...")
  time.sleep(2.5)
  gerDisco.resultadoGerDisco()
