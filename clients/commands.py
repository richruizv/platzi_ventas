import click

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(ctx,name,company,email,position):
    """creates a new client"""
    pass


@clients.command()
@click.pass_context
def list_clients(ctx):
    """List all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx,client_uid):
    """Update my client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx,client_uid):
    """Remove my client"""
    pass


all = clients