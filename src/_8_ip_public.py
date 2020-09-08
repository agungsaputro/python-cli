import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

#8
@cli.command(name="IP External")
def get_public_ip(ip):
    ip = request.urlopen('https://api.ipify.org').read().decode('utf8')
    print(ip)



if __name__ == "__main__":
    cli()