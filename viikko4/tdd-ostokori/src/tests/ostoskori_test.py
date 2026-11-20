import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.kanamuna = Tuote("Kanamuna", 5)

    def lisaa_tuotetta(self, tuote, maara=1):
        for _ in range(maara):
            self.kori.lisaa_tuote(tuote)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.lisaa_tuotetta(self.maito)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostokorin_hinta_on_tuotteen_hinta(self):
        self.lisaa_tuotetta(self.maito)
        self.assertEqual(self.kori.hinta(), self.maito.hinta())

    def test_kahden_tuotteen_lisaamisen_jalkeen_ostokorin_hinta_on_tuotteiden_hinta(self):
        self.lisaa_tuotetta(self.maito)
        self.lisaa_tuotetta(self.kanamuna)
        self.assertEqual(self.kori.hinta(), self.maito.hinta() + self.kanamuna.hinta())

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostokorissa_on_kaksi_tavaraa(self):
        self.lisaa_tuotetta(self.maito, 2)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostokorin_hinta_on_2tuotehitna(self):
        self.lisaa_tuotetta(self.maito, 2)
        self.assertEqual(self.kori.hinta(), 2 * self.maito.hinta())

    def test_korissa_2_tuotetta_kun_tuote_poistetaan_yksi_jaa(self):
        self.lisaa_tuotetta(self.maito, 2)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 1)

    def test_tuoteen_lisaamisen_ja_poistamisen_jälkeen_ostokori_on_tyhja(self):
        self.lisaa_tuotetta(self.maito)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(len(self.kori.tavaroita_korissa()), 0)

    def test_tyhejnna_toimii(self):
        self.lisaa_tuotetta(self.maito, 6)
        self.lisaa_tuotetta(self.kanamuna, 11)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.tavaroita_korissa()), 0)
