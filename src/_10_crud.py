import click,json

@click.group()
def cli():
    pass

@cli.command(name="read")
def read():
    read = open("./users.json", "r").read()
    print(read)