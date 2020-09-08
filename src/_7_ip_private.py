import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

@cli.command(name="get_ip")
@click.argument("ip")
def get_ip(ip):
    ip = socket.gethostbyname(socket.gethostname())

    print(ip)

if __name__ == "__main__":
    cli()