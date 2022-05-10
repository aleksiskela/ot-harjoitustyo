from db_connection import get_db_connection


class StorageManager:
    """Tietokannan käsittelystä vastaava luokka"""

    def __init__(self):
        """Luokan konstruktori luo yhteyden tietokantaan"""

        self._db = get_db_connection()

    def _find_storage_id(self, storage_name: str):
        """Palauttaa käsiteltävän varaston id:n.

        Args:
            storage_name: Käsiteltävän varaston nimi

        Returns:
            Käsiteltävän varaston id Storages-taulusta
        """

        return self._db.execute(
            "SELECT id FROM Storages WHERE name=?",
            [storage_name]).fetchone()[0]

    def if_storage_exists(self, storage_name: str):
        """Tarkastaa onko varasto nimi käytössä

        Args:
            storage_name: Tarkasteltavan varaston nimi

        Returns:
            True, jos varaston nimi jo käytössä
            False, jos varaston nimi ei käytössä
        """

        if self._db.execute(
            "SELECT name FROM Storages WHERE name=?",
                [storage_name]).fetchone() is None:
            return False
        return True

    def if_item_in_storage_exists(self, storage_name: str, item_name: str):
        """Tarkastaa onko tavara jo listattu varaston minimivarustukseen

        Args:
            storage_name: Varaston nimi
            item_name: Tavaran nimi

        Returns:
            True jos tavara jo varaston minimivarustelistassa
            False jos tavaran nimi ei vielä varaston listauksessa
        """
        if self._db.execute(
            "SELECT item_name FROM Items WHERE storage_id=? AND item_name=?",
                [self._find_storage_id(storage_name), item_name]).fetchone() is None:
            return False
        return True

    def create_new_storage(self, storage_name: str):
        """Lisää uuden varaston nimen tietokannan Storages-tauluun

        Args:
            storage_name: Varaston nimi
        """

        self._db.execute(
            "INSERT INTO Storages (name) VALUES (?)", [storage_name])

    def view_storages(self):
        """Kysely palauttaa kaikkien varastojen nimen

        Returns:
            Lista olemassa olevien varastojen nimistä
        """

        return self._db.execute("SELECT name FROM Storages").fetchall()

    def delete_storage(self, storage_name: str):
        """Poistaa kaikki varaston tavarat Items-taulusta ja itse varaston Storages-taulusta

        Args:
            storage_name: Varaston nimi
        """

        storage_id = self._find_storage_id(storage_name)
        self._db.execute("DELETE FROM Items WHERE storage_id=?", [storage_id])
        self._db.execute("DELETE FROM Storages WHERE name=?", [storage_name])

    def find_all_items_in_storage(self, storage_name: str):
        """Kysely palauttaa listan varaston tavaroista

        Args:
            storage_name: Varaston nimi

        Returns:
            Lista varaston tavaroista. Kysely palauttaa kunkin tavaran nimen, määrän, minimimäärän,
            vanhenemispäivän, tarkastelu-valinnan ja vapaan lisätietomerkkijonon.
        """

        storage_id = self._find_storage_id(storage_name)
        return self._db.execute(
            """SELECT item_name, amount, minimum_amount,
            expiry_date, monitored, misc FROM Items WHERE storage_id=?""",
            [storage_id]).fetchall()

    def insert_required_item_to_storage(self, storage_name: str, item_name: str,
                                        minimum_amount: int, required: int):
        """Lisää uuden tavaran varaston minimivarusteluun

        Args:
            storage_name: Varaston nimi
            item_name: Tavaran nimi
            minimum_amount: Minimimäärä
            required: Tarkasteltava-valinta (1 tai 0)
        """

        storage_id = self._find_storage_id(storage_name)
        self._db.execute(
            "INSERT INTO Items (storage_id, item_name, minimum_amount, monitored) VALUES (?,?,?,?)",
            [storage_id, item_name, minimum_amount, required])

    def pick_item(self, item_name, storage_name):
        """Kysely palauttaa tietyn tavaran tiedot varastosta
        Args:
            item_name: Tavaran nimi
            storage_name: Varaston nimi

        Returns:
            Varastossa olevan tavaran nimi, määrä, minimimäärä,
            vanhenemispäivä, tarkasteltava-valinta ja lisätieto
        """

        storage_id = self._find_storage_id(storage_name)
        return self._db.execute(
            """SELECT item_name, amount, minimum_amount, expiry_date,
            monitored, misc FROM Items WHERE storage_id=? AND item_name=?""",
            [storage_id, item_name]).fetchall()

    def delete_required_item_from_storage(self, storage_name: str, item_name: str):
        """Poistaa vaadittavan tavaran Items-taulusta

        Args:
            storage_name: Varaston nimi
            item_name: Tavaran nimi
        """

        storage_id = self._find_storage_id(storage_name)
        self._db.execute("DELETE FROM Items WHERE storage_id=? AND item_name=?",
                         [storage_id, item_name])

    def update_amount(self, storage_name, item_name, amount):
        """Päivittää Items-tauluun tavaran lukumäärän

        Args:
            storage_name: Varaston nimi
            item_name: Tavaran nimi
            amount: Uusi määrä
        """

        storage_id = self._find_storage_id(storage_name)
        self._db.execute(
            "UPDATE Items SET amount=? WHERE storage_id=? AND item_name=?",
            [amount, storage_id, item_name])

    def update_minimum_amount(self, storage_name, item_name, min_amount):
        """Päivittää Items-tauluun tavaran minimimäärän

        Args:
            storage_name: Varaston nimi
            item_name: Tavaran nimi
            min_amount: Uusi minimimäärä
        """

        storage_id = self._find_storage_id(storage_name)
        self._db.execute(
            "UPDATE Items SET minimum_amount=? WHERE storage_id=? AND item_name=?",
            [min_amount, storage_id, item_name])

    def set_expiry_date(self, storage_name, item_name, exp_date):
        """Päivittää Items-tauluun tavaran vanhenemispäivämäärän

        Args:
            storage_name: Varaston nimi
            item_name: Tavaran nimi
            exp_date: Uusi vanhenemispäivä
        """

        storage_id = self._find_storage_id(storage_name)
        self._db.execute("UPDATE Items SET expiry_date=? WHERE storage_id=? AND item_name=?", [
                         exp_date, storage_id, item_name])

    def set_monitored_status(self, storage_name, item_name, monitored_status):
        """Päivittää Items-tauluun tavaran tarkasteltava-valinnan

        Args:
            storage_name: Varaston nimi
            item_name: Tavaran nimi
            monitored_status: Uusi tarkasteltava-valinta
        """

        storage_id = self._find_storage_id(storage_name)
        self._db.execute("UPDATE Items SET monitored=? WHERE storage_id=? AND item_name=?", [
                         monitored_status, storage_id, item_name])

    def set_misc(self, storage_name, item_name, misc):
        """Päivittää Items-tauluun tavaran lisätietokentän

        Args:
            storage_name: Varaston nimi
            item_name: Tavaran nimi
            misc: Uusi lisätieto-merkkijono
        """

        storage_id = self._find_storage_id(storage_name)
        self._db.execute("UPDATE Items SET misc=? WHERE storage_id=? AND item_name=?", [
                         misc, storage_id, item_name])

    def delete_all(self):
        """Poistaa kaikki rivit Items- ja Storages tauluista"""

        self._db.execute("DELETE FROM Items")
        self._db.execute("DELETE FROM Storages")
