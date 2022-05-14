# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne on kolmitasoinen: 

- *ui* (käyttöliittymä)
- *ops* (sovelluslogiikka)
- *repositories* (tietokantojen käsittely)

Luokka/pakkauskaavio alempana.

## Käyttöliittymä

Ohjelmalla on graafinen käyttöliittymä, joka koostuu viidestä eri näkymästä:

- Päänäkymä
- Varaston luontinäkymä
- Varastonäkymä
- Varaston muokkausnäkymä
- Tavaran muokkausnäkymä

Kukin näkymä on omassa luokassaan *ui*-pakkauksessa. GUI-luokka vastaa näkymien hallinnasta.

## Sovelluslogiikka

Ohjelma käsittelee SQLite tietokantaa, johon tallennetaan tietoa varastoista ja niiden täyttötilanteista. Sovelluslogiikan ydin on Operations-luokka, joka yhdistää käyttöliittymän ja tietokantaoperaatiot toisiinsa. Käyttöliittymä kutsuu Operations-luokan metodeja joka puolestaan välittää tarvittavat kutsut edelleen StorageManager-luokalle. StorageManagerin tehtävä on suorittaa tietokantaoperaatiot. Varastonhallinnan helpottamiseksi Operations-luokka käyttää ItemStatus-luokkaa tarkastellakseen varaston tietyn tavaran täyttöasteen ja ajantasaisuuden ja StorageStatus-luokkaa koko varaston tilanteen tarkasteluun. Käyttöliittymään tieto välitetään värikoodein.

Sovelluksen luokka/pakkauskaavio:

![pakkauskaavio](./kuvat/pakkauskaavio.png)
  
## Tietojen pysyväistallennus

*repositories*-pakkauksessa sijaitseva StorageManager-luokka käsittelee SQLite-tietokantaa. Tietokannassa on kaksi taulua: Storages ja Items. Storages-tauluun tallennetaan olemassa olevien varastojen nimi. Items-taulu referoi Storages-tauluun ja siihen tallennetaan varastoitavat tavarat ja niiden täyttöaste, vanhenemispäivä, tarkastelustatus ja vapaa lisätietomerkkijono.

![dbdiagram](./kuvat/dbdiagram.png)

Tietokanta tallennetaan juuressa sijaitsevaan data-hakemistoon. Tietokanta-tiedoston oletusnimi on "data.db", mutta käyttäjä voi halutessaan muokata tiedoston nimeä juuressa sijaitsevan .env-tiedoston avulla.

Taulut alustetaan init_db.py-tiedostossa. 

## Päätoiminnallisuudet

### Uuden varaston luominen ja päänäkymän logiikka

Käyttäjä syöttää Create new storage-näkymän syötekenttään uuden varaston nimen ja valitsee "Create"-painikkeen.

```mermaid
sequenceDiagram
    actor User
    User->>GUI: click "Create" button
    GUI->>Operations: create_new_storage("Kuivakaappi")
    Operations->>StorageManager: create_new_storage("Kuivakaappi")
    StorageManager ->> StorageManager: INSERT INTO Storages (name) VALUES ("Kuivakaappi)
    GUI->>Operations: get_all_storages()
    Operations->>StorageManager: view_storages()
    StorageManager->>StorageManager: SELECT name FROM Storages
    StorageManager -->> Operations: all_storages
    Operations-->>GUI: all_storages
    GUI->>GUI: list_storages()
```

Tapahtumankäsittelijä kutsuu Operations-luokkaa, joka puolestaan välittää kutsun StorageManager-luokalle. StorageManager tallentaa Storages-tauluun uuden varaston nimen. Tämän jälkeen tapahtumankäsittelijä palauttaa päänäkymän joka kutsuu Operations-luokan kautta StorageManageria. StorageManager palauttaa listan kaikkien varastojen nimistä. Seuraavaksi päänäkymän list_storages-metodi käy läpi listan varastot ja kutsuu kunkin varaston kohdalla Operations-luokan check_storage_status-metodia, joka puolestaan kutsuu StorageStatus-luokkaa joka palauttaa varaston täyttötilanteen.

```mermaid
sequenceDiagram
    GUI->>Operations:check_storage_status("Kuivakaappi")
    Operations->>StorageManager:find_all_items_in_storage("Kuivakaappi")
    StorageManager-->>Operations:all_items()
    Operations->>stor_stat:StorageStatus(all_items)
    stor_stat->>stor_stat: total_amount(), days_until_expire(), determine_colors()
    stor_stat-->>Operations:totals, days_to_exp, colors
    Operations-->>GUI:totals, days_to_exp, colors
```

list_storages-metodi luo päänäkymään listan josta selviää kunkin varaston nimi, täyttöaste muodossa xx/xx, päivien lukumäärä ennen ensimmäiseksi vastaan tulevaa vanhenemispäivää ja painikkeen jonka kautta käyttäjä voi avata varaston tarkempaa tarkastelua ja muokkausta varten. Varaston tiedot on värikoodattu StorageStatus-luokan avulla.

### Varasto-näkymän logiikka

Kun käyttäjä valitsee päänäkymästä varaston riviltä "Open storage" painikkeen, aukeaa varastonäkymä. Varastonäkymä hakee listan kaikista varaston tavaroista ja käsittelee listan tavarat list_items-metodissa.

```mermaid
sequenceDiagram
    actor User
    User->>GUI: click "Open storage" button
    GUI->>Operations:get_all_items("Kuivakaappi")
    Operations-->>GUI:items
    GUI->>GUI:list_items(item)
    GUI->>Operations:check_item_status(item)
    Operations->>status: ItemStatus(item)
    status->>status:check_amount(), check_expdate(), determine_total_status()
    status-->>Operations:amount_status, exp_status, total_status
    Operations-->>GUI:colors
```

list_items-metodi generoi listan varaston tavaroista värikoodattuna. Listan rivi koostuu varaston nimestä, täyttöasteesta, vanhenemispäivämäärästä, tiedosta onko tavara tarkastelun alainen, lisätietokentästä sekä painikkeesta, jonka avulla käyttäjä pääsee muokkaamaan tuotteen parametrejä.