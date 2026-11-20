import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()

        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "kanamuna", 3)
            if tuote_id == 3:
                return Tuote(3, "suklaa", 7)
            
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        self.nimi = "pekka"
        self.tili_numero = "12345"

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostos_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili_numero)

        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili_numero, self.kauppa._kaupan_tili, 5)

    def test_kaksi_eri_tavara_ostos_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.nimi, self.tili_numero)

        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili_numero, self.kauppa._kaupan_tili, 8)

    def test_kaksi_sama_tavara_ostos_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili_numero)

        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili_numero, self.kauppa._kaupan_tili, 10)

    def test_loppunut_tuote(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.nimi, self.tili_numero)

        self.varasto_mock.hae_tuote.assert_called_once_with(1)
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, ANY, self.tili_numero, self.kauppa._kaupan_tili, 5)

    def test_aloita_asionti_nollaa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili_numero)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili_numero)

        maksetut_summat = [call.args[-1] for call in self.pankki_mock.tilisiirto.call_args_list]
        self.assertEqual(maksetut_summat, [10,5])

    # kauppa pyytää uuden viitenumeron jokaiselle maksutapahtumalle
    def test_uusi_viitenumero(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tili_numero)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(self.nimi, self.tili_numero)

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_poista_tuote(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        
        self.kauppa.poista_korista(1)
        self.kauppa.poista_korista(1)

        self.kauppa.tilimaksu(self.nimi, self.tili_numero)
        self.pankki_mock.tilisiirto.assert_called_once_with(ANY, ANY, ANY, ANY, 5)

