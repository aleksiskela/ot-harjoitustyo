import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.ladattu_kortti = Maksukortti(500)
        self.tyhja_kortti = Maksukortti(100)

    def test_kassan_alustus_toimii(self):
        self.assertEqual(str(self.kassa), "kassassa 1000.0 euroa, ostotapahtumia 0")

    def test_kassan_saldo_kasvaa_kun_syo_edullisesti_ja_maksu_riittava(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(str(self.kassa), "kassassa 1002.4 euroa, ostotapahtumia 1")

    def test_kassan_saldo_kasvaa_kun_syo_maukkasti_ja_maksu_riittava(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(str(self.kassa), "kassassa 1004.0 euroa, ostotapahtumia 1")

    def test_syo_edullisesti_kateisella_palauttaa_oikean_erotuksen_kun_maksu_riittava(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)

    def test_syo_maukkaasti_kateisella_palauttaa_oikean_erotuksen_kun_maksu_riittava(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_kassan_saldo_ei_muutu_kun_syo_edullisesti_ja_maksu_ei_riittava(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassa), "kassassa 1000.0 euroa, ostotapahtumia 0")

    def test_kassan_saldo_ei_muutu_kun_syo_maukkaasti_ja_maksu_ei_riittava(self):
        self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(str(self.kassa), "kassassa 1000.0 euroa, ostotapahtumia 0")

    def test_vaihtoraha_koko_maksu_kun_syo_edullisesti_mutta_maksu_ei_riittava(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)

    def test_vaihtoraha_koko_maksu_kun_syo_maukkaasti_mutta_maksu_ei_riittava(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300), 300)

    def test_syo_edullisesti_kortilla_toimii_kun_kortilla_saldoa(self):
        self.kassa.syo_edullisesti_kortilla(self.ladattu_kortti)
        self.assertEqual(str(self.kassa), "kassassa 1000.0 euroa, ostotapahtumia 1")

    def test_syo_edullisesti_kortilla_palauttaa_true_kun_saldoa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.ladattu_kortti), True)

    def test_kortin_saldo_vahenee_oikein_kun_syo_edullisesti(self):
        self.kassa.syo_edullisesti_kortilla(self.ladattu_kortti)
        self.assertEqual(str(self.ladattu_kortti), "saldo: 2.6")

    def test_syo_maukkaasti_kortilla_toimii_kun_kortilla_saldoa(self):
        self.kassa.syo_maukkaasti_kortilla(self.ladattu_kortti)
        self.assertEqual(str(self.kassa), "kassassa 1000.0 euroa, ostotapahtumia 1")

    def test_syo_maukkaasti_kortilla_palauttaa_true_kun_saldoa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.ladattu_kortti), True)

    def test_kortin_saldo_vahenee_oikein_kun_syo_maukkaasti(self):
        self.kassa.syo_maukkaasti_kortilla(self.ladattu_kortti)
        self.assertEqual(str(self.ladattu_kortti), "saldo: 1.0")

    def test_syo_edullisesti_kortilla_ei_muuta_kassaa_kun_saldo_ei_riita(self):
        self.kassa.syo_edullisesti_kortilla(self.tyhja_kortti)
        self.assertEqual(str(self.kassa), "kassassa 1000.0 euroa, ostotapahtumia 0")

    def test_syo_edullisesti_kortilla_palauttaa_false_kun_saldo_ei_riita(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.tyhja_kortti), False)

    def test_kortin_saldo_ei_muutu_kun_syo_edullisesti_kortilla_ja_saldo_ei_riita(self):
        self.kassa.syo_edullisesti_kortilla(self.tyhja_kortti)
        self.assertEqual(str(self.tyhja_kortti), "saldo: 1.0")

    def test_syo_maukkaasti_kortilla_ei_muuta_kassaa_kun_saldo_ei_riita(self):
        self.kassa.syo_maukkaasti_kortilla(self.tyhja_kortti)
        self.assertEqual(str(self.kassa), "kassassa 1000.0 euroa, ostotapahtumia 0")

    def test_syo_maukkaasti_kortilla_palauttaa_false_kun_saldo_ei_riita(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.tyhja_kortti), False)

    def test_kortin_saldo_ei_muutu_kun_syo_maukkaasti_kortilla_ja_saldo_ei_riita(self):
        self.kassa.syo_maukkaasti_kortilla(self.tyhja_kortti)
        self.assertEqual(str(self.tyhja_kortti), "saldo: 1.0")

    def test_kortin_saldo_kasvaa_oikein_kun_lataa_rahaa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.tyhja_kortti, 100)
        self.assertEqual(str(self.tyhja_kortti), "saldo: 2.0")

    def test_kassan_raha_kasvaa_kun_lataa_rahaa_kortille(self):
        self.kassa.lataa_rahaa_kortille(self.tyhja_kortti, 100)
        self.assertEqual(str(self.kassa), "kassassa 1001.0 euroa, ostotapahtumia 0")

    def test_lataa_rahaa_kortille_ei_hyvaksy_negatiivista_summaa(self):
        self.kassa.lataa_rahaa_kortille(self.tyhja_kortti, -100)
        self.assertEqual(str(self.kassa), "kassassa 1000.0 euroa, ostotapahtumia 0")
