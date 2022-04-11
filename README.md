# Varasto-sovellus

Varasto-sovelluksella voidaan luoda varastokirjanpito. Varastolle määritellään minimivarustelu ja tuotteita lisättäessä niille voidaan määritellä parasta ennen-päiväys. Sovelluksen graafisen käyttöliittymän avulla käyttäjä voi muokata ja seurata varaston tilaa.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

- Asenna riippuvuudet komennolla poetry install
- Alusta tietokannat komennolla poetry run invoke initiate
- Käynnistä graafinen käyttöliittymä komennolla poetry run invoke start
  - Tässä vaiheessa toiminnoiltaan monipuolisempi tekstikäyttöliittymä käynnistetään kommennolla poetry run invoke cli

## Komentorivitoiminnot

### Ohjelman käynnistys
Ohjelman graafinen käyttöliittymä suoritetaan kommennolla poetry run invoke start
Ohjelman komentorivikäyttöliittymä suoritetaan komennolla poetry run invoke cli

### Testaus
Testit voidaan suorittaa komennolla poetry run invoke test

### Testauskattavuus
Testikattavuusraportti luodaan komennolla poetry run invoke coverage-report

### Pylint
Pylint tarkastukset suoritetaan komennolla poetry run invoke pylint
