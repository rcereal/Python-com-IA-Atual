from funcionario import Funcionario

primeiro_funcionario = Funcionario('Caio', 1400, 'TI', '44h Semanais')
segundo_funcionario = Funcionario('Ana Maria', 2500, 'Recursos Humanos','32h Semanais')
terceiro_funcionario = Funcionario('João', 1800, 'Marketing', '44h Semanais')

print(primeiro_funcionario.__dict__)
print(segundo_funcionario.__dict__)
print(terceiro_funcionario.__dict__)
