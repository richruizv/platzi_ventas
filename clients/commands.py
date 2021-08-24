import click
from clients.services import ClientService
from clients.models import Client
from tabulate import tabulate

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
@click.option('-n','--name', type=str,prompt=True,help="The client name")
@click.option('-c','--company', type=str,prompt=True,help="The company which the client works")
@click.option('-e','--email', type=str,prompt=True,help="The client's work email")
@click.option('-p','--position', type=str,prompt=True,help="The client's position in the company")
def create(ctx,name,company,email,position):
    client = Client(name,company,email,position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list_clients(ctx):
    client_service = ClientService(ctx.obj['clients_table'])

    clients = client_service.list_clients()
    headers = [field.capitalize() for field in Client.schema()]
    table = []

    for client in clients:
        table.append(
            [client['name'],
             client['company'],
             client['email'],
             client['position'],
             client['uid']])

    print(tabulate(table, headers))


@clients.command()
@click.pass_context
@click.argument('client_uid')
def update(ctx,client_uid):
    client_service = ClientService(ctx.obj['clients_table'])

    clients = client_service.list_clients()

    client = [ client for client in clients if client['uid'] == client_uid]
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found,perhaps do you have spaces in your Uid?')

def _update_client_flow(client):
    click.echo("Leave empty if you don't want to modify the value")
    client.name = click.prompt("New name",type=str,default=client.name)
    client.company = click.prompt("New company",type=str,default=client.company)
    client.email = click.prompt("New email",type=str,default=client.email)
    client.position = click.prompt("New position",type=str,default=client.position)
    
    return client


@clients.command()
@click.pass_context
def delete(ctx,client_uid):
    """Remove my client"""
    pass


all = clients
