from arquivoNotificacao import Notificacao

class NotificacaoEmail(Notificacao):
    def __init__(self, mensagem, emailDestinatario):
        super().__init__(mensagem)
        self.emailDestinatario = emailDestinatario

    def enviar(self):
        return self.mensagem
    
