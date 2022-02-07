import click
from clients.services import ClientService
from clients.models import Client
@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
                type=str,
                prompt=True,
                help='Client')
@click.option('-c', '--company',
                type=str,
                prompt=True,
                help='Client company')
@click.option('-p', '--position',
                type=str,
                prompt=True,
                help='Client position')
@click.pass_context
def create(ctx, name, company, position):
    """Creates new client"""
    client = Client(name,company, position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def read(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.read_clients()
    click.echo(' ID | Name | Company | Position')
    click.echo ('-'*50)
    for client in clients_list:
        click.echo('{uid} | {name} | {company} | {position}'.format(
            uid=client['id'],
            name=client['name'],
            company=client['company'],
            position=client['position']
        ))

def _update_client_flow(client):
    click.echo('Leave Empty when value remains the same')

    client.name = click.prompt('New name',type=str, default=client.name)
    client.company = click.prompt('New company',type=str, default=client.company)
    client.position = click.prompt('New position',type=str, default=client.position)

    return client

@clients.command()
@click.argument('client_id',
                type=str)
@click.pass_context
def update(ctx, client_id):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.read_clients()

    client = [client for client in client_list if client['id'] == client_id]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client Updated')
    else:
        click.echo('Client updated')


@clients.command()
@click.argument('client_uid',
                type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    if click.confirm('Are you sure you want to delete the client with uid: {}'.format(client_uid)):
        client_service.delete_client(client_uid)

all_c = clients
