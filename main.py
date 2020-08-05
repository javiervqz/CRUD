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
        print('{uid} | {name} | {company} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            position = client['position']
            ))

def update_client(idx, updated_name):
    global clients
    clients[idx].update({'name': updated_name})



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


def _get_client_index_by_name():
    client_name = _get_client_name()
    for key, client in enumerate(clients):
        if client['name'] == client_name:
            return key
        else:
            print('client not found')

def _print_welcome():
    print('Welcome to StuffVentas')
    print ('*'*20+'Hello Ppl'+'*'*20)
    print ('What ya want?')
    print ('[C]reate client\n')
    print ('[R]ead clients\n')
    print ('[U]pdate client\n')
    print ('[D]elete client\n')
    print ('[S]earch client\n')

if __name__ == '__main__':
    _print_welcome()

    command = input().upper()

    if command == 'C':
        client = {
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'position':_get_client_field('position')
            }
        create_client(client)
        list_clients()
    elif command == 'R':
        list_clients()
    elif command == 'U':
        idx = _get_client_index_by_name()
        updated_name = input('What is the new name?\n')
        update_client(idx,updated_name)

        list_clients()
        

        pass
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print ('Clients exists')
        else:
            print ('Client {} not in list'.format(client_name))
    else:
        print('Invalid comand')
