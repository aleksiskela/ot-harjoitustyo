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
- Luotu ItemStatus-luokka, jonka tehtävä on tarkastaa tuotteen riittävyys ja ajantasaisuus. Tässä vaiheessa luokan avulla voidaan korostaa tuote punaisella, jos vaadittava määrä ei täyty, ja vihreällä jos määrä on riittävä. Jos tuote on merkitty "Not Monitored", tekstin väri on musta.
- Arkkitehtuuri-dokumenttiin lisätty varaston luonti sekvenssikaaviona.

## Viikko 6

- ItemStatus-luokkaa kehitetty. Luokka korostaa oleellisen osan tuotteesta määritellyllä värillä riippuen tuotteen statuksesta.
- StorageStatus-luokka luotu. Luokan tehtävä on samankaltainen kuin ItemStatus, mutta koko varaston osalta. Käyttäjä näkee etusivulta kaikkien varastojen yleistilanteen ja jäljellä olevat päivät ennen ensimmäisenä vanhenevan tuotteen vanhenemista. 
- Virhesyötteiden käsittelyä parannettu.
- Docstring-dokumentaatio aloitettu.
- Operations-luokan testejä lisätty.
- Arkkitehtuuri-dokumenttiin lisätty sekvenssikaavioita.
- Käyttöohjeen ensimmäinen versio luotu

## Viikko 7

- status_app_test.py-tiedosto lisätty. Testikattavuus nostettu yli 90 prosentin.
- EditItemView jaettu erillisiin metodeihin
- Docstring-dokumentaatiota lisätty
- Dokumentaatiota päivitetty
- Komentorivikäyttöliittymään liittyvä koodi poistettu