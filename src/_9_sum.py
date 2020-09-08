import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass


@cli.command(name="sum_number")
@click.option('--num', prompt='enter number ke 1 :', help='oke')
def sum_number(num):
    numbers = num
    total = int(num)
    i = 1
    while num != '' and numbers != '':
        i+=1
        numbers = input(f"enter number ke {i}: ")
        if numbers !='':
            total += int(numbers)
    print("hasil",total)

if __name__ == "__main__":
    cli()
