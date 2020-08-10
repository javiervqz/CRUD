import sys, csv, os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name','company','position']
clients = []

def _initialize_clients_from_storage():
    #Context Manager
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row) 

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name,CLIENT_TABLE)


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



def delete_client(idx):
    global clients
    clients.pop(idx)



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
    idx = None
    for key, client in enumerate(clients):
        if client['name'] == client_name:
            idx = key
    if idx:
        return idx
    else :
        return client_name

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
    _initialize_clients_from_storage()
    _print_welcome()

    command = input().upper()

    if command == 'C':
        client = {
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'position':_get_client_field('position')
            }
        create_client(client)

    elif command == 'R':
        list_clients()
    elif command == 'U':
        idx = _get_client_index_by_name()
        updated_name = input('What is the new name?\n')
        update_client(idx,updated_name)
       
    elif command == 'D':
        idx = _get_client_index_by_name()
        delete_client(idx)
    elif command == 'S':
        Found = str(_get_client_index_by_name())

        if Found.isdigit():
            print ('Clients exists, index {}'.format(Found))
        else:
            print ('Client "{}" not in list'.format(Found))
    else:
        print('Invalid comand')
    _save_clients_to_storage()
