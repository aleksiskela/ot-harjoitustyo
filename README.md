# Varasto-sovellus

Varasto-sovelluksella voidaan luoda varastokirjanpito. Varastolle määritellään minimivarustelu ja tuotteita lisättäessä niille voidaan määritellä parasta ennen-päiväys. Sovelluksen graafisen käyttöliittymän avulla käyttäjä voi muokata ja seurata varaston tilaa.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

- Asenna riippuvuudet komennolla poetry install
- Alusta tietokannat komennolla poetry run invoke initiate
- Käynnistä komentorivikäyttöliittymä komennolla poetry run invoke start
  - Graafinen käyttöliittymä tulee myöhemmin

## Komentorivitoiminnot

### Ohjelman käynnistys
Ohjelman komentorivikäyttöliittymä suoritetaan komennolla poetry run invoke start

### Testaus
Testit voidaan suorittaa komennolla poetry run invoke test

### Testauskattavuus
Testikattavuusraportti luodaan komennolla poetry run invoke coverage-report
