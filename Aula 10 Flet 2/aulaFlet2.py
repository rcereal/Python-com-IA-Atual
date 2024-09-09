import flet

def main(page: flet.Page):
    
    page.title = 'Aula Flet II'

    texto = flet.Text('Ola mundo!')

    page.controls.append(texto)

    #inputs

    input_nome = flet.TextField(label= 'Digite seu nome: ')



    page.add(input_nome,
             flet.ElevatedButton(text= 'Cadastrar-se'))

    page.update()

flet.app(target =main) # " view = flet.WEB_BROWSER " CASO QUEIRA VER PELA WEB