from repositories.storage_manager import StorageManager
from ops.status_app import ItemStatus, StorageStatus


class Operations:
    """Sovelluslogiikasta vastaava luokka. Luokka ottaa vastaan kutsuja käyttöliittymästä,
    kutsuu StoragManager-luokkaa tietokantojen käsittelyä varten ja kutsuu ItemStatus- ja StorageStatus-luokkia
    tavaran ja varaston täyttötilanteen tarkastelua varten"""

    def __init__(self):
        """Luokan konstruktori luo yhteyden StorageManager-luokkaan ja alustaa tarvittavat luokkamuuttujat"""

        self._manager = StorageManager()
        self._active_storage = None
        self._active_item = None
        self._temp_items = []

    def get_all_storages(self):
        """Palauttaa listan olemassa olevien varastojen nimistä
        
        Returns:
            Lista varastojen nimistä
        """

        raw = self._manager.view_storages()
        all_storages = [storage[0] for storage in raw]
        return all_storages

    def create_intro_text(self):
        """Luo päänäkymän tekstin riippuen siitä yhtään varastoa luotu
        
        Returns:
            Merkkijono, josta muodostetaan päänäkymän teksti
        """

        if len(self.get_all_storages()) == 0:
            return "No storages created yet. Start by creating one."
        return "Available storages:"

    def check_if_storage_already_exists(self, storage_name):
        """Välittää kyselyn, jolla tarkastetaan, onko saman niminen varasto jo olemassa
        
        Args:
            Varaston nimi

        Return:
            Kyselyn mukainen totuusarvo
        """

        if self._manager.if_storage_exists(storage_name):
            return True
        return False

    def check_if_item_already_in_storage(self, item_name):
        """Välittää kyselyn, jolla tarkastetaan, onko saman niminen tavara jo kyseisessä varastossa
        
        Args:
            Tavaran nimi

        Return:
            Kyselyn mukainen totuusarvo
        """

        if self._manager.if_item_in_storage_exists(self._active_storage, item_name):
            return True
        return False

    def create_new_storage(self, storage_name: str):
        """Välittää uuden varaston luomisen tietokantaan
        Args:
            Varaston nimi
        """

        self._manager.create_new_storage(storage_name)

    def delete_storage(self):
        """Välittää varaston poiston tietokannasta
        Args:
            Varaston nimi
        """
        self._manager.delete_storage(self._active_storage)

    def set_active_storage(self, storage):
        """Asettaa parametrinä olevan varaston nimen luokkamuuttujan _active_storage arvoksi luokan operaatioita varten

        Args:
            Varaston nimi
        """

        self._active_storage = storage

    def get_active_storage(self):
        """Palauttaa _active_storage-luokkamuuttujan arvon
        
        Returns:
            Käsiteltävän varaston nimi
        """

        return self._active_storage

    def set_active_item(self, item_name):
        """Asettaa parametrinä olevan tavaran nimen luokkamuuttujan _active_item arvoksi luokan operaatioita varten

        Args:
            Tavaran nimi
        """

        self._active_item = item_name

    def get_active_item(self):
        """Palauttaa _active_item- ja _active_storage luokkamuuttujien mukaisen tuotteen.
        
        Returns:
            Käsiteltävän tavaran nimi, määrä, minimimäärä, vanhenemispäivä, tarkasteltava-valinta, lisätieto
        """

        return self._manager.pick_item(self._active_item, self._active_storage)[0]

    def get_all_items(self):
        """Välittää kyselyn joka palauttaa kaikki tavarat varastossa

        Returns:
            Lista _active_storage-varaston kaikista tuotteista 
        """

        return self._manager.find_all_items_in_storage(self._active_storage)

    def add_temp_item(self, item: tuple):
        """Lisää tuotteen _temp_items-luokkamuuttujaan. Muuttujaa käytetään väliaikaisena tallennuspaikkana varastoon lisättäville tuotteille.
        Args:
            Tuple joka sisältää tuotteen nimen, minimimäärän ja tarkasteltava-valinnan
        """

        self._temp_items.append(item)

    def clear_temp_items(self):
        """Tyhjentää _temp_items-luokkamuuttujassa olevan listan"""

        self._temp_items.clear()

    def get_temp_items(self):
        """Palauttaa _temp_items-luokkamuuttujan tiedot
        Returns:
            Lista väliaikaisesti tallennetuista tavaroista"""

        return self._temp_items

    def add_new_required_item(self, item_name, min_amount, monitored):
        """Välittää tietokantaoperaation, jolla lisätään valittu tuote tietokantaan
        Args:
            Tuotteen nimi, minimimäärä ja tarkasteltava-valinta. Käyttöliittymä käsittelee luokan _temp_items-listaa,
            jonka arvot välitetään metodin parametreinä.
        """

        self._manager.insert_required_item_to_storage(
            self._active_storage, item_name, min_amount, monitored)

    def update_amount(self, new_amount):
        """Välittää tietokantaoperaation jolla muutetaan tieto tavaran määrästä
        
        Args:
            Uusi määrä
        """

        self._manager.update_amount(
            self._active_storage, self._active_item, new_amount)

    def update_minimum_amount(self, new_minimum_amount):
        """Välittää tietokantaoperaation jolla muutetaan tieto tavaran mimimimäärästä
        
        Args:
            Uusi minimimäärä
        """

        self._manager.update_minimum_amount(
            self._active_storage, self._active_item, new_minimum_amount)

    def update_expiry_date(self, expiry_date):
        """Välittää tietokantaoperaation jolla muutetaan tieto tavaran vanhenemispäivästä
        
        Args:
            Uusi vanhenemispäivämäärä
        """

        self._manager.set_expiry_date(
            self._active_storage, self._active_item, expiry_date)

    def update_monitored_status(self, status):
        """Välittää tietokantaoperaation jolla muutetaan tarkasteltava-valinta
        
        Args:
            Tarkestaltava-valinta (1 tai 0)
        """

        self._manager.set_monitored_status(
            self._active_storage, self._active_item, status)

    def update_misc(self, misc):
        """Välittää tietokantaoperaation jolla muutetaan tavaran lisätietokentän arvo
        
        Args:
            Uusi lisätieto
        """

        self._manager.set_misc(self._active_storage, self._active_item, misc)

    def monitored_message(self, value):
        """Palauttaa merkkijonon joka näytetään käyttöliittymässä
        
        Args:
            1 tai 0 riippuen riippuen tavaran tarkasteltava-valinnasta
        
        Returns:
            Merkkijono joka ilmaisee onko tuote tarkatelun alainen.
        """

        if value == 1:
            return "Monitored"
        return "Not monitored"

    def check_item_status(self, item):
        """Kutsuu ItemStatus-luokkaa jonka tehtävänä on määrittää tuotteen täyttöaste ja ilmaista tieto värikoodein
        
        Args:
            Tuotteen nimi
        Returns:
            Tuple joka sisältää värikoodin jota käyttöliittymä käyttää tiedon ilmaisemiseen
        """

        self.set_active_item(item)
        data = self.get_active_item()
        amount_color = None
        exp_color = None
        name_color = None
        if data[4] == 1:
            status = ItemStatus(data[1], data[2], data[3])
            amount_color = status.amount_status
            exp_color = status.exp_status
            name_color = status.total_status
        self.set_active_item(None)
        return amount_color, exp_color, name_color

    def check_storage_status(self, storage_name):
        """Kutsuu StorageStatus-luokkaa jonka tehtävä on määrittää varaston täyttöaste. StorageStatus-luokka palauttaa
        tiedon varaston täyttöasteesta, jäljellä olevista päivistä ennen vanhemista ja värikoodin jolla tieto ilmaistaan käyttöliittymässä.
        
        Args:
            Varaston nimi
            
        Returns:
            Lista joka sisältää tiedot joita käyttöliittymän päänäkymä käyttää varaston tietojen ilmaisemiseen
        """

        self.set_active_storage(storage_name)
        all_items = self._manager.find_all_items_in_storage(self._active_storage)
        stor_stat = StorageStatus(all_items)
        totals = [stor_stat.totals, stor_stat.days_to_exp, stor_stat.colors]
        self.set_active_storage(None)
        return totals


    def delete_item(self):
        """Välittää tietokanta-operaation jolla poistetaan tuote minimivarustelusta"""

        self._manager.delete_required_item_from_storage(
            self._active_storage, self._active_item)

    def delete_all(self):
        """Välittää tietokanta-operaation jolla poistetaan kaikki tiedot tietokannan tauluista"""

        self._manager.delete_all()


operations = Operations()
