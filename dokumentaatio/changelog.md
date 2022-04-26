# Changelog

## Viikko 3

- Konfiguraatio-tiedosto ja ohjelman alustava rakenne luotu
- SQLite tietokantojen yhteys ja taulut alustettu
- StorageManager-luokka luotu, joka vastaa tietokannan käsittelystä
- Ensimmäiset testit aloitettu
- Tekstikäyttöliittymällä voi lisätä ja poistaa varastoja, lisätä ja poistaa vaadittavia tuotteita.

## Viikko 4

- Komentorivikäyttöliittymän toiminnallisuutta lisätty mm. varaston tuotteiden määrien käsittelyn osalta.
- Tekstikäyttöliittymän sovelluslogiikka poikkeaa suunnitellusta, mutta tullaan liittämään GUI:n logiikkaan myöhemmin.
- Graafisen käyttöliittymän toteutus aloitettu. Käyttöliittymän eriytystä sovelluslogiikasta selkeytetty.
- GUI:n käynnistäminen näyttää olemassa olevat varastot. 
- Päänäkymästä voi siirtyä luomaan uuden varaston. Luonnin jälkeen varasto lisätään päänäkymään.
- Päänäkymästä voi siirtyä varastonäkymään, joissa ei kuitenkaan vielä varaston nimen lisäksi muuta sisältöä.
- Testejä lisätty
- Pylint ja automaattinen formatointi alustettu
- Arkkitehtuuri-dokumentti lisätty dokumentaatioon

## Viikko 5

- Graafista käyttöliittymää kehitetty. 
- Päänäkymästä voi siirtyä varastonäkymään. Varastonäkymä näyttää varaston tilan. Käyttäjä voi siirtyä muokkaamaan varaston sisältöä.
- Käyttäjä voi poistaa olemassa olevan varaston.
- Käyttäjä voi lisätä vaadittavia tavaroita varastoon.
- Käyttäjä voi muokata vaadittavia tavaroita "Edit item" alasivulla.
- Lisätty tkcalendar, jonka avulla voi valita vanhenemispäivän.
- Testeihin lisätty Operations-luokka