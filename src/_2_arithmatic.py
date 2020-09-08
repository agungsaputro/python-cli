import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

#2
@cli.command(name="Add")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    res = reduce(lambda x,y: x+y,l)
    print(res)

@cli.command(name="Substract")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    res = reduce(lambda x,y:x-y, l)
    print(res)

@cli.command(name="Multiply")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    res = reduce(lambda x,y:x*y, l)
    print(res)

@cli.command(name="Devide")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    res = reduce(lambda x,y:x/y,l)
    print(res)

if __name__ == "__main__":
    cli()
