# import RPi.GPIO as GPIO

class InOut:
    def __init__(self):
        
        self.PINO_BUZZER = 12
        self.PINO_SAIDA_1 = 29
        self.PINO_SAIDA_2 = 31
        self.PINO_SAIDA_3 = 32
        self.PINO_SAIDA_4 = 33
        self.PINO_SAIDA_5 = 35
        self.PINO_SAIDA_6 = 36
        self.PINO_SAIDA_7 = 37
        self.PINO_SAIDA_8 = 38
        
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setwarnings(False)
        
        # GPIO.setup(self.PINO_BUZZER, GPIO.OUT)
        # GPIO.setup(self.PINO_SAIDA_1, GPIO.OUT)
        # GPIO.setup(self.PINO_SAIDA_2, GPIO.OUT)
        # GPIO.setup(self.PINO_SAIDA_3, GPIO.OUT)
        # GPIO.setup(self.PINO_SAIDA_4, GPIO.OUT)
        # GPIO.setup(self.PINO_SAIDA_5, GPIO.OUT)
        # GPIO.setup(self.PINO_SAIDA_6, GPIO.OUT)
        # GPIO.setup(self.PINO_SAIDA_7, GPIO.OUT)
        # GPIO.setup(self.PINO_SAIDA_8, GPIO.OUT)
        
        # GPIO.output(self.PINO_BUZZER, 0)
        # GPIO.output(self.PINO_SAIDA_1, 0)
        # GPIO.output(self.PINO_SAIDA_2, 0)
        # GPIO.output(self.PINO_SAIDA_3, 0)
        # GPIO.output(self.PINO_SAIDA_4, 0)
        # GPIO.output(self.PINO_SAIDA_5, 0)
        # GPIO.output(self.PINO_SAIDA_6, 0)
        # GPIO.output(self.PINO_SAIDA_7, 0)
        # GPIO.output(self.PINO_SAIDA_8, 0)
        
    def buzzer(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_BUZZER, 1)
            pass
        else:
            # GPIO.output(self.PINO_BUZZER, 0)
            pass
            
    def saida_1(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_SAIDA_1, 1)
            pass
        else:
            # GPIO.output(self.PINO_SAIDA_1, 0)
            pass

    def saida_2(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_SAIDA_2, 1)
            pass
        else:
            # GPIO.output(self.PINO_SAIDA_2, 0)
            pass

    def saida_3(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_SAIDA_3, 1)
            pass
        else:
            # GPIO.output(self.PINO_SAIDA_3, 0)
            pass

    def saida_4(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_SAIDA_4, 1)
            pass
        else:
            # GPIO.output(self.PINO_SAIDA_4, 0)
            pass

    def saida_5(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_SAIDA_5, 1)
            pass
        else:
            # GPIO.output(self.PINO_SAIDA_5, 0)
            pass

    def saida_6(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_SAIDA_6, 1)
            pass
        else:
            # GPIO.output(self.PINO_SAIDA_6, 0)
            pass

    def saida_7(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_SAIDA_7, 1)
            pass
        else:
            # GPIO.output(self.PINO_SAIDA_7, 0)
            pass

    def saida_8(self, estado):
        if estado == 1:
            # GPIO.output(self.PINO_SAIDA_8, 1)
            pass
        else:
            # GPIO.output(self.PINO_SAIDA_8, 0)
            pass