#обработчики: перегружаются перед каждым вызовом

def message1():
    print('smapSpamSPAM')

def message2(self):
    print('Ni! Ni!')
    self.method1()          #Обращение к экземпляру 'Hello'