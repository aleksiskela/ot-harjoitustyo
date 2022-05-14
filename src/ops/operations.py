from repositories.storage_manager import StorageManager
from ops.status_app import ItemStatus, StorageStatus


class Operations:
    """Sovelluslogiikasta vastaava luokka. Luokka ottaa vastaan kutsuja käyttöliittymästä,
    kutsuu StoragManager-luokkaa tietokantojen käsittelyä varten ja kutsuu ItemStatus-
    ja StorageStatus-luokkia tavaran ja varaston täyttötilanteen tarkastelua varten
    """

    def __init__(self):
        """Luokan konstruktori luo yhteyden StorageManager-
        luokkaan ja alustaa tarvittavat luokkamuuttujat
        """

        self._manager = StorageManager()
        self._active_storage = None
        self._active_item = None
        self._temp_items = []

    def get_all_storages(self):
        """Palauttaa listan olemassa olevien varastojen nimistä

        Returns:
            all_storages: Lista varastojen nimistä
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

    def check_if_storage_already_exists(self, storage_name: str):
        """Välittää kyselyn, jolla tarkastetaan, onko saman niminen varasto jo olemassa

        Args:
            storage_name: Varaston nimi

        Return:
            Kyselyn mukainen totuusarvo
        """

        if self._manager.if_storage_exists(storage_name):
            return True
        return False

    def check_storage_name(self, storage_name: str):
        """Tarkastaa että varaston nimi ei ole tyhjä merkkijono

        Args:
            storage_name: Varaston nimi

        Returns:
            True jos syöte on tyhjä rivi, muuten False
        """

        if len(storage_name) == 0:
            return True

        return False

    def check_if_item_already_in_storage(self, item_name):
        """Välittää kyselyn, jolla tarkastetaan, onko saman niminen tavara jo kyseisessä varastossa

        Args:
            item_name: Tavaran nimi

        Return:
            Kyselyn mukainen totuusarvo
        """

        if self._manager.if_item_in_storage_exists(self._active_storage, item_name):
            return True
        return False

    def create_new_storage(self, storage_name: str):
        """Välittää uuden varaston luomisen tietokantaan

        Args:
            storage_name: Varaston nimi
        """

        self._manager.create_new_storage(storage_name)

    def delete_storage(self):
        """Välittää varaston poiston tietokannasta"""

        self._manager.delete_storage(self._active_storage)

    def set_active_storage(self, storage):
        """Asettaa parametrinä olevan varaston nimen
        luokkamuuttujan _active_storage arvoksi luokan operaatioita varten

        Args:
            storage: Varaston nimi
        """

        self._active_storage = storage

    def get_active_storage(self):
        """Palauttaa _active_storage-luokkamuuttujan arvon

        Returns:
            Käsiteltävän varaston nimi
        """

        return self._active_storage

    def set_active_item(self, item_name):
        """Asettaa parametrinä olevan tavaran nimen
        luokkamuuttujan _active_item arvoksi luokan operaatioita varten

        Args:
            item_name: Tavaran nimi
        """

        self._active_item = item_name

    def get_active_item(self):
        """Palauttaa _active_item- ja _active_storage luokkamuuttujien mukaisen tuotteen.

        Returns:
            Tuple jonka alkiot ovat: käsiteltävän tavaran nimi, määrä, minimimäärä,
            vanhenemispäivä, tarkasteltava-valinta, lisätieto
        """
        return self._manager.pick_item(self._active_item, self._active_storage)[0]

    def get_all_items(self):
        """Välittää kyselyn joka palauttaa kaikki tavarat varastossa

        Returns:
            Lista _active_storage-varaston kaikista tuotteista
        """

        return self._manager.find_all_items_in_storage(self._active_storage)

    def check_temp_item_input(self, item_name, min_req):
        """Tarkastaa lisättävän tavaran syötteen oikeellisuuden
        ja virhesyötteen tapauksessa palauttaa virheviestin.

        Args:
            item_name: Lisättävän tavaran nimi
            min_req: vaadittava minimimäärä

        Return:
            Merkkijono joka ilmaisee virhellisen syötteen, muuten None
        """

        try:
            min_req = int(min_req)
        except ValueError:
            return "Required amount must be an integer"

        if min_req < 0:
            return "Required amount cannot be negative"

        if len(item_name) == 0:
            return "Item name must contain at least one character"

        if self.check_if_item_already_in_storage(item_name):
            return f"{item_name} already listed for {self.get_active_storage()}"

        if item_name in [
                temp_item[0] for temp_item in self._temp_items if temp_item[0] == item_name]:
            return f"{item_name} already to be added"

        return None

    def add_temp_item(self, item: tuple):
        """Lisää tavaran _temp_items-luokkamuuttujaan.
        Muuttujaa käytetään väliaikaisena tallennuspaikkana varastoon lisättäville tavaroille.

        Args:
            item: Tuple jonka alkioina tuotteen nimi, minimimäärä ja tarkasteltava-valinta
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
        """Välittää tietokantaoperaation, jolla lisätään valittu tuote tietokantaan.
        Käyttöliittymä käsittelee luokan _temp_items-listaa,
        jonka arvoja käytetään metodin parametreinä

        Args:
            item_name: Tuotteen nimi
            min_amount: Minimimäärä
            monitored: Tarkasteltava-valinta
        """

        self._manager.insert_required_item_to_storage(
            self._active_storage, item_name, min_amount, monitored)

    def update_amount(self, new_amount):
        """Välittää tietokantaoperaation jolla muutetaan tieto tavaran määrästä

        Args:
            new_amount: Uusi määrä
        """

        self._manager.update_amount(
            self._active_storage, self._active_item, new_amount)

    def update_minimum_amount(self, new_minimum_amount):
        """Välittää tietokantaoperaation jolla muutetaan tieto tavaran mimimimäärästä

        Args:
            new_minimum_amount: Uusi minimimäärä
        """

        self._manager.update_minimum_amount(
            self._active_storage, self._active_item, new_minimum_amount)

    def update_expiry_date(self, expiry_date):
        """Välittää tietokantaoperaation jolla muutetaan tieto tavaran vanhenemispäivästä

        Args:
            expiry_date: Uusi vanhenemispäivämäärä
        """

        self._manager.set_expiry_date(
            self._active_storage, self._active_item, expiry_date)

    def update_monitored_status(self, status):
        """Välittää tietokantaoperaation jolla muutetaan tarkasteltava-valinta

        Args:
            status: Tarkastaltava-valinta (1 tai 0)
        """

        self._manager.set_monitored_status(
            self._active_storage, self._active_item, status)

    def update_misc(self, misc):
        """Välittää tietokantaoperaation jolla muutetaan tavaran lisätietokentän arvo

        Args:
            misc: Uusi lisätieto
        """

        self._manager.set_misc(self._active_storage, self._active_item, misc)

    def monitored_message(self, value):
        """Palauttaa merkkijonon joka näytetään käyttöliittymässä

        Args:
            value: 1 tai 0 riippuen riippuen tavaran tarkasteltava-valinnasta

        Returns:
            Merkkijono joka ilmaisee onko tuote tarkatelun alainen.
        """

        if value == 1:
            return "Monitored"
        return "Not monitored"

    def check_item_status(self, item):
        """Kutsuu ItemStatus-luokkaa jonka tehtävänä on määrittää
        tuotteen täyttöaste ja ilmaista tieto värikoodein

        Args:
            item: Tuotteen nimi
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
        """Kutsuu StorageStatus-luokkaa jonka tehtävä on määrittää varaston täyttöaste.
        StorageStatus-luokka palauttaa tiedon varaston täyttöasteesta,
        jäljellä olevista päivistä ennen vanhemista ja
        värikoodin jolla tieto ilmaistaan käyttöliittymässä.

        Args:
            storage_name: Varaston nimi

        Returns:
            Lista joka sisältää tiedot joita käyttöliittymän
            päänäkymä käyttää varaston tietojen ilmaisemiseen
        """

        self.set_active_storage(storage_name)
        all_items = self._manager.find_all_items_in_storage(
            self._active_storage)
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
