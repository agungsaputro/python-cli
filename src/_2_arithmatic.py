import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

#2
@cli.command(name="add")
@click.argument("number", type=click.INT, nargs=-1)
def add(number):
    l = list(number)
    res = reduce(lambda x,y: x+y,l)
    print(res)

@cli.command(name="substract")
@click.argument("number", type=click.INT, nargs=-1)
def subtract(number):
    l = list(number)
    res = reduce(lambda x,y:x-y, l)
    print(res)

@cli.command(name="multiply")
@click.argument("number", type=click.INT, nargs=-1)
def multiply(number):
    l = list(number)
    res = reduce(lambda x,y:x*y, l)
    print(res)

@cli.command(name="divide")
@click.argument("number", type=click.INT, nargs=-1)
def divide(number):
    l = list(number)
    res = reduce(lambda x,y:x/y,l)
    print(res)

if __name__ == "__main__":
    cli()
