contatos = []

def adicionar_contato(nome, email, telefone, favorito):
    contatos.append({
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "favorito": favorito,
    })

def IsOrNotFavorito(mensagem):
    while True:
        resposta = input(mensagem + ' (s/n): ').strip().lower()
        if resposta in ('s', 'sim'):
            return True
        if resposta in ('n', 'nao', 'não'):
            return False
        print("Responda com 's' ou 'n'.")

def visualizar_contatos(lista=None):
    if lista is None:
        lista = contatos
    if not lista:
        print("Nenhum contato encontrado.")
        return
    for i, c in enumerate(lista, start=1):
        estrela = "★" if c["favorito"] else "☆"
        print(f"{i}. {estrela} {c['nome']} | {c['email']} | {c['telefone']}")


def visualizar_contatos_favoritos():
    favoritos = [c for c in contatos if c["favorito"]]
    visualizar_contatos(favoritos)

def marcar_favorito(indice):
    if 0 <= indice <= len(contatos):
        if contatos[indice]['favorito'] == True:
            contatos[indice]['favorito'] = False
            print(f'Contato {contatos[indice]['nome']} foi marcado como favorito!')
        else:
            contatos[indice]['favorito'] = True
            print(f'Contato {contatos[indice]['nome']} foi desmarcado como favorito!')
    else:
        print('Índice inválido. Por favor, escolha um índice válido.')

def editar_contato(indice):
    contato = contatos[indice]
    campo = input("Qual campo editar (nome/email/telefone)? ").strip().lower()

    if campo not in ("nome", "email", "telefone"):
        print("Campo inválido.")
        return

    novo = input(f"Novo {campo}: ").strip()
    if novo:
        contato[campo] = novo
        print("Contato atualizado!")
    else:
        print("Valor vazio, nada foi alterado.")

def remover_contato(indice):
    if 0 <= indice <= len(contatos):
        contato_removido = contatos.pop(indice)
        print(f'Contato {contato_removido['nome']} foi removido com sucesso!')

while True:
    print('\nMenu do Gerenciamento de Tarefas:')
    print('1. Adicionar Contato')
    print('2. Visualizar Contatos')
    print('3. Visualizar Contatos favoritos')
    print('4. Marcar/desmarcar contato como favorito')
    print('5. Editar contato existente')
    print('6. Remover contato')
    print('7. Sair')

    escolha = input('Digite o número que corresponde a opção desejada: ')

    if escolha == '1':
        nome = input('Digite o nome: ').strip()
        email = input('Digite o email: ').strip()
        telefone = input('Digite o telefone: ').strip()
        favorito = IsOrNotFavorito('Marcar como favorito?')
        adicionar_contato(nome, email, telefone, favorito)
        print("Contato adicionado!")

    elif escolha == '2':
        visualizar_contatos()

    elif escolha == '3':
        visualizar_contatos_favoritos()

    elif escolha == '4':
        visualizar_contatos()
        try:
            indice = int(input('Digite o número do contato que deseja marcar/desmarcar como favorito: ')) - 1
            marcar_favorito(indice)
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido.')
    
    elif escolha == '5':
        try:
            visualizar_contatos()
            indice = int(input('Digite o número do contato que deseja editar como favorito: ')) - 1
            editar_contato(indice)
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido.')

    elif escolha == '6':
        visualizar_contatos()
        try:
            indice = int(input('Digite o número do contato que deseja remover: ')) - 1
            remover_contato(indice)
        except ValueError:
            print('Entrada inválida. Por favor, digite um número válido.')

    elif escolha == '7':
        print('Saindo do Sistema')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida')




