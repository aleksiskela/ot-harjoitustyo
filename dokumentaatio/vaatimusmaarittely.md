# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella voidaan luoda varastokirjanpito varaston minimivarustelu ja vanhenemispäiväys huomioiden. Varastolle määritellään minimivarustelu, jonka ajantasaisuutta on helppo valvoa graafisen käyttöliittymän avulla. Sovellusta voidaan käyttää esimerkiksi 72 tunnin hätävaran ylläpitoon.

## Käyttäjät

Sovelluksella on lähtökohtaisesti vain yksi käyttäjäprofiili

## Perusversion tarjoama toiminnallisuus

### Statustila
- [x] Käyttäjä näkee luodut varastot
- [] Käyttäjä näkee varastojen statuksen
  - [] Varaston nimen vieressä varaston täyttöaste formaatissa ##/##
  - [] Rivi korostettuna vihreällä, jos kaikki kunnossa
  - [] Rivi korostettuna keltaisella, jos jokin tuote vanhenemassa pian tai kun täyttöaste alle täyden
  - [] Rivi korostettuna punaisella, jos jokin tuote vanhentunut tai kun täyttöaste yli 10% alle täyden
- [x] Käyttäjä voi luoda uuden varaston
- [x] Käyttäjä voi avata varaston tarkastelua tai muokkausta varten

### Uuden varaston luominen
- [] Käyttäjä voi antaa varastolle seuraavia tietoja:
  - [x] Varaston nimi
  - [] Tuotteet:
    - [] Nimi
    - [] Minimilukumäärä
- [] Tuotteen parametrit: nimi, lukumäärä, minimilukumäärä, vanhenemispäivä ja lisätietokenttä.

### Varaston tarkastelu ja muokkaus
- [] Käyttäjä voi lisätä ja vähentää tuotteen lukumäärää
- [] Käyttäjä voi lisätä tai muokata tuotteen vanhenemispäivää
- [] Käyttäjä voi muokata lisätietokentän tekstiä

## Jatkokehitysideoita

- Tuotteen vanhenemispäivän sijaan voidaan antaa päivien lukumäärä, jonka jälkeen tuote vanhenee
- Lisättäessä tuotetta tallennetaan lisäysaika, jolloin keltainen korostus voidaan suhteuttaa tuotteen säilyvyysaikaan
- Tuote voidaan merkitä kuuluvaksi minimivarusteluun tai olemaan sen ulkopuolella
  - Minimivarustelun ulkopuolella olevaa tuotetta ei huomioida statuksessa esim. värikoodeissa
  - Tuotteen kuuluvuus minimivarusteluun voidaan valita varaston luonnin tai muokkauksen yhteydessä
- Tuotteen jokaisen kappaleen vanhenemispäivä voidaan määritellä erikseen. Yleisnäkymässä voi näkyä esimerkiksi ensimmäinen vanhenemispäivä, ja tuote valittuna näyttää kaikki vanhenemispäivät
