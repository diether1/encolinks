# encoding: utf-8

from encolinks import db
import string
import random


class Link(db.Model):
    __tablename__ = 'links'
    cod = db.Column(db.String(6), primary_key=True)
    url = db.Column(db.String)
    qtd = db.Column(db.BigInteger)
    last_access = db.Column(db.DateTime)

    def __generate_cod(self):
        chars = string.ascii_letters + string.digits
        return ''.join([
            random.choice(chars) for _ in range(6)
        ])

    def __init__(self, url):
        self.url = url
        self.cod = self.__generate_cod()
        self.qtd = 0

