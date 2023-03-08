from unittest import TestCase
from guru import Guru

class TestGuru(TestCase):

    def test_ask(self):
        guru: Guru = Guru()
        # note these values may change a little as time moves on
        self.assertEqual('69', guru.ask('how old is Tony Blair'))
        self.assertEqual('76', guru.ask('how old is trump'))
        self.assertEqual('8908081', guru.ask('what is the population of London'))
        self.assertEqual('2165423', guru.ask('what is the population of Paris'))