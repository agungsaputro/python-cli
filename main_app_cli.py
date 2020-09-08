import click
from functools import reduce
import statistics
import socket
from urllib import request


@click.group()
def cli():
    pass

# @click.command()
# def hello():
#     click.echo('Hello World!')

#1
@cli.command(name="Lowercase")
# @click.option('--string', prompt='input text',  help='The person to greet.')
@click.argument('sentence')
def lower(sentence):
    print(sentence.lower())

@cli.command(name="Uppercase")
# @click.option('--text', prompt='input text',  help='The person to greet.')
@click.argument('sentence')
def upper(sentence):
    print(sentence.upper())

@cli.command(name="Capitalize")
# @click.option('--string', prompt='input text',  help='The person to greet.')
@click.argument('sentence')
def capitalize(sentence):
    lst = [word[0].upper() + word[1:] for word in sentence.split()]
    word = " ".join(lst)
    print(word)

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

#3
@cli.command(name="Mean")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    print(statistics.mean(l))

@cli.command(name="Median")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    print(statistics.median(l))

@cli.command(name="Mode")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    print(statistics.mode(l))

@cli.command(name="Fmean")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    l = list(number)
    print(statistics.fmean(l))

#4
@cli.command(name="Palindrome")
@click.argument('sentence')
def palindrome(sentence):
    l, h = 0, len(sentence) - 1
    s = sentence.lower() 

    while (l <= h): 
    
        if (not(s[l] >= 'a' and s[l] <= 'z')): 
            l += 1
        elif (not(s[h] >= 'a' and s[h] <= 'z')): 
            h -= 1

        elif (s[l] == s[h]): 
            l += 1
            h -= 1
        else: 
            return print("NO")
    return print("YES")

#5
@cli.command(name="Obfuscate")
@click.argument('sentence')
def lower(sentence):
    sentence = list(sentence)
    text = ''.join(list(map(lambda char: f"&#{ord(char)};", sentence)))
    print(text)

#6

#7
@cli.command(name="IP")
@click.argument("ip")
def get_ip(ip):
    ip = socket.gethostbyname(socket.gethostname())

    print(ip)

#8
@cli.command(name="IP External")
def get_public_ip(ip):
    ip = request.urlopen('https://api.ipify.org').read().decode('utf8')
    print(ip)

#9
@cli.command(name="Sum")
@click.option('--num', prompt='enter number ke 1 :', help='oke')
def sum(num):
    numbers = num
    total = int(num)
    i = 1
    while num != '' and numbers != '':
        i+=1
        numbers = input(f"enter number ke {i}: ")
        if numbers !='':
            total += int(numbers)
    print("hasil",total)
#10


if __name__ == "__main__":
    cli()
