from arquivoNotificacao import Notificacao

class NotificacaoSMS(Notificacao):
    def __init__(self, mensagem,numeroDestinatario):
        super().__init__(mensagem)
        self.numeroDestinatario = numeroDestinatario

    def enviar(self):
        return self.mensagem
    