# Varasto-sovellus

Varasto-sovelluksella voidaan luoda varastokirjanpito. Varastolle määritellään minimivarustelu ja tavaroita lisättäessä niille voidaan määritellä vanhenemispäivämäärä. Sovelluksen graafisen käyttöliittymän avulla käyttäjä voi muokata ja seurata varaston tilaa.

## Release

[Uusin release](https://github.com/aleksiskela/ot-harjoitustyo/releases/tag/viikko6) 

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/aleksiskela/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

## Asennus

- Asenna riippuvuudet komennolla poetry install
- Alusta tietokannat komennolla poetry run invoke initiate
- Käynnistä graafinen käyttöliittymä komennolla poetry run invoke start

## Komentorivitoiminnot

### Ohjelman käynnistys
Ohjelman graafinen käyttöliittymä suoritetaan kommennolla poetry run invoke start

### Testaus
Testit voidaan suorittaa komennolla poetry run invoke test

### Testauskattavuus
Testikattavuusraportti luodaan komennolla poetry run invoke coverage-report

### Pylint
Pylint tarkastukset suoritetaan komennolla poetry run invoke lint
