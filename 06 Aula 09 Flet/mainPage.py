#importacao do flet
import flet

def main(page:flet.Page):

    def exibir_usuario(e):
        if not input_senha.value:
            input_senha.error_text = 'Campo Obrigatorio!'
            page.update()

        elif not input_idade.value:
            input_idade.error_text = 'Campo Obrigatorio!'
            page.update()

        elif not input_nome.value:
            input_nome.error_text = 'Campo Obrigatorio!'
            page.update()
        
        else:
            nome = input_nome.value
            idade = input_idade.value

            texto = flet.Text(f'Ola seja bem vindo! {nome} sua idade é {idade}!')

            page.clean()

            page.add(texto)

        


    input_nome = flet.TextField(label = 'Digite seu nome')

    input_idade = flet.TextField(label = 'Digite sua idade')

    input_senha = flet.TextField(label = 'Digite sua senhas')

    layout = flet.Row(
        [
            flet.ElevatedButton('Cadastre-se',on_click = exibir_usuario), 
            flet.ElevatedButton('Esqueci minha senha')
        ]
    )

    page.add(
        input_nome,
        input_idade,
        input_senha,
        layout
    )

    # ola = flet.Text('Ola Mundo!')
    
    # page.controls.append(ola)

    # page.update()

#usado para dizer qual vai ser a funcao principal que ira rodar o sistem
#flet

flet.app(target = main)