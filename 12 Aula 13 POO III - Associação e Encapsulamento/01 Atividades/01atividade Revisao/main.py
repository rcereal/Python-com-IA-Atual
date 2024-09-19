from notificacaoEmail import NotificacaoEmail
from notificacaoSMS import NotificacaoSMS

lista_Email = {
    'mensagem': [],
    'email': []
}

lista_SMS = {
    'mensagem': [],
    'numero do destinatario': []
}

print('Ola bem  vindo ao painel de mensagens.')

while True:
    print('1. Email')
    print('2. SMS')

    pergunta_painel = int(input('Qual opção deseja ? '))

    if pergunta_painel == 1:
        msg_email = input('Digite a mensagem que deseja enviar: ')
        destinatario_email = input('Agora digite o email do destinatario: ')
        objetoNotificacaoEmail = NotificacaoEmail(msg_email, destinatario_email)

        lista_Email['mensagem'].append(objetoNotificacaoEmail.enviar())
        lista_Email['email'].append(objetoNotificacaoEmail.emailDestinatario)

        continuar = input('Deseja continuar ? S/N. ').upper()
        if continuar == 'S':
            continue
        else:
            break

    else:
        msg_sms = input('Digite a mensagem que deseja enviar: ')
        numero_destinatario = input('Agora digite o numero do destinatario: ')
        objetoNotificacaoSMS = NotificacaoSMS(msg_sms, numero_destinatario)
        

        lista_SMS['mensagem'].append(objetoNotificacaoSMS.mensagem)
        lista_SMS['numero do destinatario'].append(objetoNotificacaoSMS.numeroDestinatario)
        
        continuar = input('Deseja continuar ? S/N. ').upper()
        if continuar == 'N':
            break

print(lista_Email)