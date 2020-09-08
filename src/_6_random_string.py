import click
from functools import reduce
import statistics
import socket
from urllib import request
import random

@click.group()
def cli():
    pass

@cli.command(name="random_string")
@click.option('--length', default=5, help='lengt of random')
@click.option('--letters',default=False,is_flag=True,type=click.BOOL, help='only alphabet')
@click.option('--uppercase',default=False,is_flag=True,type=click.BOOL, help='uppercase random string')
@click.option('--lowercase',default=False,is_flag=True,type=click.BOOL, help='lowercase random string')
@click.option('--numbers',default=False,is_flag=True,type=click.BOOL, help='only number')

def random_string(length,letters,numbers,uppercase,lowercase):
    char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = list("1234567890")
    print(type(letters))
    output = ''
    for i, rand in enumerate(char):
        charnum = list([char,num])
        select = random.randrange(0,2)
        if numbers == True:
            select = 1
        if letters == True:
            select = 0
        # print(charnum)
        output+=charnum[select][random.randrange(0, len(charnum[select]), 3)]
        
        if i == length:
            break

    
    if uppercase == True:
        output = output.upper()
    if lowercase == True:
        output = output.lower()
    # if number == False
    print(output)
    print(length)

if __name__ == "__main__":
    cli()