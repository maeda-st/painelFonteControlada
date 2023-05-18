class Dado:
    def __init__(self):
        self.TELA_PRINCIPAL = 0
        self.TELA_TESTE_TENSAO = 1
        self.TELA_CONFIGURAR = 2
        self.TELA_OUTA = 3
        self.TELA_OUTB = 4
        self.TELA_OUT4_A = 5
        self.TELA_OUT4_B = 6
        self.TELA_QTDCICLOS_A = 7
        self.TELA_QTDCICLOS_B = 8
        self.TELA_TEMPOCICLO_A = 9
        self.TELA_TEMPOCICLO_B = 10
        self.TELA_EXECUTAR = 11
        self.TELA_EXECUTANDO = 12

        self.tela_ativa = self.TELA_PRINCIPAL
        self.aciona_buzzer = True
        
        self._cursor = 'cross'
        #self._cursor = 'none'
        self._nome_programa = 'Fonte controlada'
        self.t_on_off_canalA = []
        self.t_on_off_canalA.append([10,10])#on off saida 1
        self.t_on_off_canalA.append([10,10])#on off saida 2
        self.t_on_off_canalA.append([10,10])#on off saida 3
        self.t_on_off_canalA.append([87])#ciclos on off por minuto
        self.t_on_off_canalA.append([1])# quantidade de ciclos
        self.t_on_off_canalA.append([1,1])# ton toff dos ciclos
        self.t_on_off_canalB = []
        self.t_on_off_canalB.append([10,10])
        self.t_on_off_canalB.append([10,10])
        self.t_on_off_canalB.append([10,10])
        self.t_on_off_canalB.append([87])
        self.t_on_off_canalB.append([1])
        self.t_on_off_canalB.append([1,1])
        self.ton_ou_toff = True
        self.indice_saidaA = 1
        self.indice_saidaB = 1
        self.inicia_ou_paraA = False
        self.inicia_ou_paraB = False
        self.qtd_ciclos_canalA = 1
        self.qtd_ciclos_canalB = 1

        self.fim_ciclo_A = False
        self.fim_ciclo_B = False

        self.ton_canal1_A = 0
        self.toff_canal1_A = 0
        self.ton_canal2_A = 0
        self.toff_canal2_A = 0
        self.ton_canal3_A = 0
        self.toff_canal3_A = 0
        self.ton_canal4_A = 0
        self.toff_canal4_A = 0

        self.ton_canal1_B = 0
        self.toff_canal1_B = 0
        self.ton_canal2_B = 0
        self.toff_canal2_B = 0
        self.ton_canal3_B = 0
        self.toff_canal3_B = 0
        self.ton_canal4_B = 0
        self.toff_canal4_B = 0

        self.eh_segundo_ou_minuto_A = True
        self.eh_segundo_ou_minuto_B = True

        self.fator_tempoA = 1
        self.fator_tempoB = 1

        self.ton_ciclos_canalA = 0
        self.toff_ciclos_canalA = 0
        self.ton_ciclos_canalB = 0
        self.toff_ciclos_canalB = 0

        self.frequencia_onA = 0
        self.frequencia_offA = 0
        self.frequencia_onB = 0
        self.frequencia_offB = 0
        
        self._black = '#000000'
        self._white = '#FFFFFF'
        self._brighted = '#C4C4C4'
        self._grey = '#E5E5E5'
        self._grey_dark = "#505050"
        self._red = '#FF0000'
        self._green = '#2CCA28'
        self._blue = '#31455B'

        self._window_w = 480
        self._window_h = 320
        
    @property
    def cursor(self):
        return self._cursor
    
    @property
    def nome_programa(self):
        return self._nome_programa

    
    @property
    def black(self):
        return self._black
    
    @property
    def white(self):
        return self._white
    
    @property
    def brighted(self):
        return self._brighted
    
    @property
    def grey(self):
        return self._grey
    
    @property
    def red(self):
        return self._red
    
    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue
    
    @property
    def window_w(self):
        return self._window_w
    
    @property
    def window_h(self):
        return self._window_h