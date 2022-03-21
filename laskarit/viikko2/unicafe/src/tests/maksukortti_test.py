import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldo_oikein_lataamisen_jalkeen(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")

    def test_otto_toimii_saldo_vahenee_oikein_kun_saldoa_riittaa(self):
        self.maksukortti.lataa_rahaa(100)
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_otto_ei_muuta_saldoa_jos_saldoa_liian_vahan(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_otto_boolean_toimii_kun_ota_rahaa_saldo_ei_riita(self):
        arvo = self.maksukortti.ota_rahaa(20)
        self.assertEqual(arvo, False)

    def test_otto_boolean_toimii_kun_ota_rahaa_saldo_riittaa(self):
        self.maksukortti.lataa_rahaa(100)
        arvo = self.maksukortti.ota_rahaa(20)
        self.assertEqual(arvo, True)