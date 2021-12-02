import random
import rstr
import sqlite3
import datetime

def gen_cpf():
    return rstr.rstr('1234567890', 11)

def gen_phone():
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4))

def gen_citY():
    list_city = [
        [u'São Paulo', 'SP'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return random.choice(list_city)
