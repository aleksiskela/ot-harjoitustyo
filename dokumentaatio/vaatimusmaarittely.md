# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella voidaan luoda varastokirjanpito varaston minimivarustelu ja vanhenemispäiväys huomioiden. Varastolle määritellään minimivarustelu, jonka ajantasaisuutta on helppo valvoa graafisen käyttöliittymän avulla. Sovellusta voidaan käyttää esimerkiksi 72 tunnin hätävaran ylläpitoon.

## Käyttäjä ja varastot

Sovelluksella on yksi käyttäjäprofiili joka voi luoda useita varastoja.

## Käyttöliittymä

Sovelluksen käyttöliittymä koostuu viidestä eri näkymästä. Sovellus käynnistyy päänäkymään, joka koostuu luotujen varastojen yleiskatsauksesta. Päänäkymästä käyttäjä voi siirtyä luomaan uusia varastoja tai muokkaamaan valittua varastoa. 

Varaston avattuaan käyttäjä näkee listan varaston tavaroista. Varastonäkymästä voidaan siirtyä varaston muokkausnäkymään tai tavaran muokkausnäkymään. Alasivut tarjoavat toiminnot varaston minimivarustelun määrittelyyn tai varaston poistamiseen, sekä tietyn tavaran tietojen, kuten määrän ja vanhenemispäivän, muokkaamiseen tai tavaran poistamiseen.

## Perusversion tarjoama toiminnallisuus

### Päänäkymä
- Käyttäjä näkee luodut varastot
- Käyttäjä näkee varastojen statuksen
  - Varaston täyttöaste formaatissa ##/##
  - Jäljellä olevat päivät varaston ensimmäiseksi vanhenevan tuotteen vanhenemispäivään
  - Rivin merkinnät korostettuna vihreällä, jos kaikki kunnossa
  - Rivin merkinnät korostettuna keltaisella, jos jokin tavara vanhenemassa pian tai kun varaston täyttöaste 75-99 % 
  - Rivin merkinnät korostettuna punaisella, jos jokin tavara vanhentunut tai kun varaston täyttöaste alle 75 %
- Käyttäjä voi luoda uuden varaston
- Käyttäjä voi avata varaston tarkastelua tai muokkausta varten

### Uuden varaston luominen
- Käyttäjä voi syöttää uuden varaston nimen
- Käyttäjä voi poistua luontinäkymästä tallentamalla uuden varaston tai perumalla luonnin

### Varastonäkymä
- Käyttäjä näkee varaston tavarat värikoodattuna listana josta ilmenee:
  - Tavaran nimi, täyttöaste formaatissa ##/##, vanhenemispäivämäärä, monitorointi-status ja vapaa lisätietokenttä
  - Rivin merkinnät korostettuna samalla periaatteella kuin päänäkymässä
- Käyttäjä voi siirtyä muokkaamaan tavaraa, muokkaamaan varaston minimivarustelua tai palata päänäkymään

### Varaston minimivarustelun määrittely
- Käyttäjä voi määritellä varaston vaadittavat tavarat
- Tavaralle annettavat tiedot:
  - Nimi
  - Minimilukumäärä
  - Valintaruutu, jolla käyttäjä määrittelee kuuluuko tavara minimivarusteluun. Valinta vaikuttaa tavaran värikoodaukseen
- Käyttäjä näkee lisättäväksi määrittelemänsä tavarat listana
- Käyttäjä voi siirtyä varastonäkymään tallentamalla lisättävien listan tai perumalla lisäyksen

### Minimivarusteluun kuuluvan tavaran muokkaaminen
- Käyttäjä näkee tavaran tiedot
- Käyttäjä voi lisätä tai vähentää määrää tai minimimäärää
- Käyttäjä voi valita kalenterista tavaralle vanhenemispäivän
- Käyttäjä voi määritellä tavaran kuulumisen minimivarusteluun ("Monitored")
- Käyttäjä voi lisätä tavaralle vapaamuotoisen lisätiedon
- Käyttäjä voi siirtyä takaisin varastonäkymään tallentamalla tai perumalla muutokset

### Varaston tai tavaran poistaminen
- Varasto poistetaan varaston muokkausnäkymästä
- Tavara poistetaan tavaran muokkausnäkymästä

## Jatkokehitysideoita

- Vanhenemispäivän sijaan voidaan antaa päivien lukumäärä, jonka jälkeen tavara vanhenee
- Lisättäessä tavaraa tallennetaan lisäysaika, jolloin keltainen korostus voidaan suhteuttaa säilyvyysaikaan
- Yksittäisen tavaran jokaisen kappaleen vanhenemispäivä voidaan määritellä erikseen. Yleisnäkymässä voi näkyä esimerkiksi ensimmäinen vanhenemispäivä, ja tuote valittuna näyttää kaikki vanhenemispäivät
