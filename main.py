import sys

clients = [
    {
        'name':"Diana",
        'company':"Casa Inc",
        'position':"La boss"
    },
    {
        'name':"Max",
        'company':"Casa Inc",
        'position': "El chiki baiby"
    }

]

def create_client(client):
  #  global clientsUnboundLocalError: local variable 'clients' referenced before assignment
    global clients #It needs to take the variable from "outside" or error above occurs 
    if client not in clients:
        clients.append(client)
    else:
        print ('Client already in client\'s list')

def list_clients():
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx,client['name']))

def update_client(client_name, updated_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = client_name
    else:
        print ('Client not in list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in client list')


def search_client(client_name):
    for client in clients :
        if client != client_name:
            continue
        else:
            return True

def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}?\n'.format(field_name))
        if field == 'exit':
            field = None
            break

    if not field:
        sys.exit()

    return field



def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name\n')
        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

def _print_welcome():
    print('Welcome to StuffVentas')
    print ('*'*20+'Hello Ppl'+'*'*20)
    print ('What ya want?')
    print ('[C]reate client\n')
    print ('[L]ist clients\n')
    print ('[U]pdate client\n')
    print ('[D]elete client\n')
    print ('[S]earch client\n')

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'position':_get_client_field('position')
            }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name')
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print ('Clients exists')
        else:
            print ('Client {} not in list'.format(client_name))
    else:
        print('Invalid comand')
