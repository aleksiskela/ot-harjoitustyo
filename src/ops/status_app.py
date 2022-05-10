from datetime import date, timedelta


class ItemStatus:
    """Tavaran täyttöasteen tarkastelusta vastaava luokka.
    Luokan metodit määrittelevät luokan muuttujien arvot,
    jotka Operations-luokka välittää käyttöliittymälle

    Attributes:
        amount: Määrä
        min_amount: Minimimäärä
        expdate: Vanhenemispäivämäärä.
    """

    def __init__(self, amount, min_amount, expdate):
        """Luokan konstruktorissa tarkasteltavat muuttujat
        saavat arvonsa parametreista ja palautettavat muuttujat alustetaan.
        Konstruktori myös käynnistää tarkastelumetodit.

        Args:
            amount: Määrä
            min_amount: Minimimäärä
            expdate: Vanhenemispäivämäärä.
        """

        self._amount = amount
        self._min_amount = min_amount
        self._expdate = expdate
        self.amount_status = None
        self.exp_status = None
        self.total_status = None

        self._check_amount()
        self._check_expdate()
        self._determine_total_status()

    def _check_amount(self):
        """Tarkastelee tavaran määrää suhteessa minimimäärään ja
        määrittelee sen perusteella määrälle värikoodin
        """

        if self._amount < 3/4*self._min_amount:
            self.amount_status = "red"
        elif self._amount >= self._min_amount:
            self.amount_status = "green"
        else:
            self.amount_status = "orange"

    def _check_expdate(self):
        """Tarkastelee tavaran vanhenemispäivää suhteessa nykyhetkeen
        ja määrittelee sen perusteella värikoodin.
        Jos tavaralle ei ole määritelty vanhenemispäivää,
        jää tavara tarkastelun ulkopuolelle ja saa värikoodikseen arvon None
        """

        if self._expdate != "-":
            temp = self._expdate.split("-")
            expdate = date(int(temp[0]), int(temp[1]), int(temp[2]))
            delta = expdate - date.today()

            if delta > timedelta(2):
                self.exp_status = "green"
            elif delta < timedelta(0):
                self.exp_status = "red"
            else:
                self.exp_status = "orange"

    def _determine_total_status(self):
        """Metodi tarkastelee aikaisemmin määriteltyjä muuttujien arvoja
        ja määrittelee niiden perusteella tavaralle lopullisen värikoodin
        """

        self.total_status = "green"
        if self.amount_status == "orange" or self.exp_status == "orange":
            self.total_status = "orange"
        if self.amount_status == "red" or self.exp_status == "red":
            self.total_status = "red"


class StorageStatus:
    """Varaston täyttöasteen tarkastelusta vastaava luokka.
    Operations-luokka välittää tiedot käyttöliittymälle

    Attributes:
        all_items: Lista varaston tavaroista
    """

    def __init__(self, all_items):
        """Luokan konstruktori saa parametrikseen varaston kaikki
        tuotteet määrittelee tarkasteltavat muuttujat ja alustaa palautusmuutujat.
        Konstuktori myös käynnistää tarkastelumoetodit

        Args:
            all_items: Lista kaikista varaston tuotteista
        """

        self._all_items = all_items
        self.totals = ()
        self.days_to_exp = None

        self.storage_color = None
        self.totals_color = None
        self.exp_color = None

        self._total_amount()
        self._days_until_expiry()
        self._determine_colors()

        self.colors = [self.storage_color, self.totals_color, self.exp_color]

    def _total_amount(self):
        """Metodi laskee varaston tavaroiden täyttömäärää.
        Jos tuote on tarkastelun alainen (listan alkion indeksi 4 perusteella),
        tarkastetaan täyttyykö tuotteen minimimäärä.
        Jos kyllä tai jos tavara ei ole tarkasteltava,
        kasvatetaan saturated_amount-apumuuttujan arvoa.
        Lopuksi apumuuttujan arvo ja varaston tavaroiden
        lukumäärä tallennetaan tuplena totals-muuttujaan.
        """

        saturated_amount = 0
        total_items = len(self._all_items)
        for item in self._all_items:
            if item[4] == 0:
                saturated_amount += 1
            else:
                if item[1] >= item[2]:
                    saturated_amount += 1
        self.totals = saturated_amount, total_items

    def _days_until_expiry(self):
        """Metodi tarkastelee varaston tavaroiden vanhemispäivämääriä.
        Jos tavaralle ei ole määritelty vanhenemispäivää,
        niin se jätetään tarkastelun ulkopuolelle.
        Metodi määrittelee lyhyimmän vanhenemisajan nykyhetkeen nähden ja määrittelee
        ajan perusteella vanhenemisajalle värikoodin.
        Lyhyin vanhenemisaika tallennetaan merkkijonona days_to_exp-muuttujaan.
        Värikoodi tallennetaan exp_color-muuttujaan.
        """

        deltae = []
        for item in self._all_items:
            if item[3] != "-":
                temp = item[3].split("-")
                expdate = date(int(temp[0]), int(temp[1]), int(temp[2]))
                delta = expdate - date.today()
                deltae.append(delta.days)
        if len(deltae) == 0:
            self.days_to_exp = "Expiry date not defined"
            self.exp_color = None
        else:
            lowest_delta = min(deltae)
            if lowest_delta >= 0:
                self.days_to_exp = f"Expires in {lowest_delta} days"
                self.exp_color = "green"
                if lowest_delta < 3:
                    self.exp_color = "orange"
            else:
                self.days_to_exp = f"Expired {abs(lowest_delta)} days ago"
                self.exp_color = "red"

    def _determine_colors(self):
        """Metodi määrittelee värikoodit varaston täyttöasteelle
        ja vertailee määriteltyjä värikoodeja määrittääkseen
        yhteisvärikoodin varastolle
        """

        if self.totals[1] == 0:
            self.totals_color = None
        else:
            if self.totals[0]/self.totals[1] < 0.75:
                self.totals_color = "red"
            elif self.totals[0]/self.totals[1] >= 1:
                self.totals_color = "green"
            else:
                self.totals_color = "orange"

        self.storage_color = "green"
        if self.totals_color == "orange" or self.exp_color == "orange":
            self.storage_color = "orange"
        if self.totals_color == "red" or self.exp_color == "red":
            self.storage_color = "red"
