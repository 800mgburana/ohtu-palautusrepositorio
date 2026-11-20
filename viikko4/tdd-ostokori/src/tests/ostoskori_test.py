import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostokorin_hinta_on_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), maito.hinta())

    def test_kahden_tuotteen_lisaamisen_jalkeen_ostokorin_hinta_on_tuotteiden_hinta(self):
        maito = Tuote("Maito", 3)
        kanamuna = Tuote("Kanamuna", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kanamuna)
        self.assertEqual(self.kori.hinta(), maito.hinta()+kanamuna.hinta())

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostokorissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostokorin_hinta_on_2tuotehitna(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 2*maito.hinta())

    def test_korissa_2_tuotetta_kun_tuote_poistetaan_yksi_jaa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 1)

    def test_tuoteen_lisaamisen_ja_poistamisen_jälkeen_ostokori_on_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 0)

    def test_tyhejnna_toimii(self):
        maito = Tuote("Maito", 3)
        kanamuna = Tuote("Kanamuna", 5)
        for i in range(6): self.kori.lisaa_tuote(maito)
        for i in range(11): self.kori.lisaa_tuote(kanamuna)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.tavaroita_korissa()), 0)

