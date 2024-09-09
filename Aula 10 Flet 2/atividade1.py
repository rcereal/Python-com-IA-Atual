import flet

def main(page: flet.Page):

    def exibir_ao_usuario_apos_clicar_no_botao(e):
        page.clean()
        mensagem = flet.Text(f'''Seja bem vindo {input_nome.value}! 
        Vimos que mora no estado {input_estado.value}.''')
        
        page.controls.append(mensagem)

        page.update()

    page.title = 'Pagina de Cadastro'

    texto = flet.Text('Digite as informações abaixo para se cadastrar.')
    
    page.controls.append(texto)

    #inputs
    input_nome = flet.TextField(label= 'Digite seu nome: ')
    input_cep = flet.TextField(label= 'Digite seu CEP: ')
    input_estado = flet.TextField(label= 'Digite o estado da sua residencia: ')


    #add widgets
    page.add(input_nome,
             input_cep,
             input_estado,
             flet.ElevatedButton('Cadastrar-se',on_click=exibir_ao_usuario_apos_clicar_no_botao))
    page.update()

flet.app(target= main)