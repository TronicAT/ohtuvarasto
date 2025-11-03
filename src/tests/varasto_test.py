import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_lisays_yli_tilavuuden_rajoittaa_saldoa(self):
        self.varasto.lisaa_varastoon(15)  # enemmän kuin tilavuus
        self.assertAlmostEqual(self.varasto.saldo, 10)  # saldo ei ylitä tilavuutta

    def test_lisays_negatiivinen_maara_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_liikaa_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)  # enemmän kuin saldo
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_negatiivinen_maara_palauttaa_nolla(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_varasto_nolla_tilavuus(self):
        v = Varasto(0)
        self.assertAlmostEqual(v.tilavuus, 0)
        self.assertAlmostEqual(v.saldo, 0)

    def test_varasto_negatiivinen_saldo(self):
        v = Varasto(10, -5)
        self.assertAlmostEqual(v.saldo, 0)

    def test_varasto_alku_saldo_suurempi_kuin_tilavuus(self):
        v = Varasto(10, 15)
        self.assertAlmostEqual(v.saldo, 10)

    def test_str_metodi(self):
        self.varasto.lisaa_varastoon(5)
        s = str(self.varasto)
        self.assertIn("saldo = 5", s)
        self.assertIn("vielä tilaa 5", s)