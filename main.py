import sys



def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('This client already exists')

def update_client(client_index):
    global clients
    if client_index != -1:
        client = {
            'name' : _get_client_field('name'),
            'company' : _get_client_field('company'),
            'email' : _get_client_field('email'),
            'position' : _get_client_field('position'),
        }
        clients[client_index] = client
    else:
        print(f'Client {client_name} is not in client list')

def delete_client(client_index):
    global clients
    if client_index != -1:
        clients.pop(client_index)


def search_client(client_index):
    global clients
    if client_index != -1:
        print('{} is in the client name!'.format(clients[client_index]['name']))
    else:
        print(f'Client {clients[client_index]["name"]} is not in client list')

def list_clients():
    global clients
    for idx,client in enumerate(clients):
         print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position'])
            )

def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What do you like to do today?')
    print('[C]reate clients')
    print('[U]pdate client')
    print('[D]elete clients')
    print('[S]earch client')

def _get_client_name():
    global clients
    client_name = None
    while not client_name:
        client_name = input('what is your client name? ')
        for idx,client in enumerate(clients):
            if client['name'] == client_name:
                return idx


    if client_name == 'exit':
        sys.exit()

    print(f'Client {client_name} is not in client list')
    return -1

def _get_client_field(field_name):
    field = None
    while not field:
        field = input(f'what is the client {field_name}? ')
    if field_name == 'exit':
        sys.exit()
    return field
        
def run():
    _print_welcome()

    command = input()
    command = command.upper()
    
    list_clients()
    if command == 'C':
        client = {
            'name' : _get_client_field('name'),
            'company' : _get_client_field('company'),
            'email' : _get_client_field('email'),
            'position' : _get_client_field('position'),
        }
        create_client(client)
    elif command == 'U':
        client_name = _get_client_name()
        update_client(client_name)
    elif command == 'D':
        client_index = _get_client_name()
        delete_client(client_index)
    elif command == 'S':
        client_index = _get_client_name()
        search_client(client_index)
    else:
        print('Invalid command')
    list_clients()
    
    
clients = [
    {
        'name': 'Liss',
        'company': 'Google',
        'email': 'Liss@google.com',
        'position': 'Sofware Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
]

if __name__ == "__main__":
    run()
    