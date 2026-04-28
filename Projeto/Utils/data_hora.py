import datetime

class Agora:
 def hoje(self):
  return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")