from tkinter import ttk, constants, StringVar, IntVar, Checkbutton
from tkcalendar import Calendar
from datetime import date
from ops.operations import operations


class EditItemView:
    """Tavaran muokkauksesta- ja poistosta vastaava näkymä

    Attributes:
        root: TkInter-juuri
        handle_select_storage: Välittää kutsun siirtyä takaisin varastonäkymään
    """

    def __init__(self, root, handle_select_storage):
        """Konstruktori luo tavaran muokkausnäkymän

        Args:
            root: TkInter-juuri
            handle_select_storage: Välittää kutsun siirtyä takaisin varastonäkymään
        """

        self._root = root
        self._frame = None
        self._handle_select_storage = handle_select_storage
        self._active_item = operations.get_active_item()

        self._initialize()

    def _initialize(self):
        """Alustaa tavaran muokkausnäkymän"""

        self._frame = ttk.Frame(master=self._root)

        self._init_temp_data()
        self._display_temp_data()
        self._display_calendar()
        self._display_edit_data()
        self._footer()

    def _display_temp_data(self):
        """Näyttää muokattavan tavaran tiedot ennen muokkausta ja
        väliaikaistallennettuna muokkauksen aikana
        """

        title_n = ttk.Label(master=self._frame, text="Item name")
        title_a = ttk.Label(master=self._frame, text="Amount")
        title_m = ttk.Label(master=self._frame, text="Required amount")
        title_e = ttk.Label(master=self._frame, text="Expiry date")
        title_misc = ttk.Label(master=self._frame, text="Additional info")

        name_label = ttk.Label(master=self._frame, text=self._active_item[0])
        var_label = ttk.Label(master=self._frame,
                              textvariable=self._temp_amount)
        cap_label = ttk.Label(master=self._frame,
                              textvariable=self._temp_required)
        exp_label = ttk.Label(master=self._frame, textvariable=self._temp_exp)
        misc_label = ttk.Label(
            master=self._frame, textvariable=self._temp_misc)

        title_n.grid(row=0, column=0)
        title_a.grid(row=0, column=1)
        title_m.grid(row=0, column=2)
        title_e.grid(row=0, column=3)
        title_misc.grid(row=0, column=4)

        name_label.grid(row=1, column=0)
        var_label.grid(row=1, column=1)
        cap_label.grid(row=1, column=2)
        exp_label.grid(row=1, column=3)
        misc_label.grid(row=1, column=4)

    def _display_edit_data(self):
        """Näyttää muokkausalueen painikkeet, syötekentän ja valintaruudun"""

        mon_check = Checkbutton(master=self._frame, text="Monitored",
                                variable=self._temp_monitored, onvalue=1, offvalue=0)

        mod_label = ttk.Label(master=self._frame, text="Modify amount")
        inc_button = ttk.Button(
            master=self._frame, text="+", command=self._increase_amount, width=7)
        dec_button = ttk.Button(
            master=self._frame, text="-", command=self._decrease_amount, width=7)

        inc_req_button = ttk.Button(
            master=self._frame, text="+", command=self._increase_required_amount, width=5)
        dec_req_button = ttk.Button(
            master=self._frame, text="-", command=self._decrease_required_amount, width=5)

        mod_misc_label = ttk.Label(
            master=self._frame, text="Additional information")
        misc_entry = ttk.Entry(master=self._frame)
        misc_button = ttk.Button(master=self._frame, text="Update additional info",
                                 command=lambda: self._temp_misc.set(misc_entry.get()))

        mod_label.grid(row=2, column=0)
        inc_button.grid(row=2, column=1, sticky=constants.W)
        dec_button.grid(row=2, column=1, sticky=constants.E)
        inc_req_button.grid(row=2, column=2, sticky=constants.W)
        dec_req_button.grid(row=2, column=2, sticky=constants.E)

        mon_check.grid(row=3, column=4)

        mod_misc_label.grid(row=4, column=0)
        misc_entry.grid(row=4, column=1)
        misc_button.grid(row=4, column=2)

    def _display_calendar(self):
        """Luo Calendar-olion tkcalender-moduulin avulla 
        ja näyttää siihen liittyvät elementit"""

        today = date.today()

        calendar = Calendar(
            self._frame, selectmode="day", year=today.year, month=today.month, day=today.day)

        date_label = ttk.Label(master=self._frame, text="Set expiry date")
        date_button = ttk.Button(master=self._frame, text="Confirm date",
                                 command=lambda: self.change_date(calendar.get_date()))
        clear_date_button = ttk.Button(
            master=self._frame, text="Clear date", command=lambda: self._temp_exp.set("-"))

        date_label.grid(row=3, column=0)
        calendar.grid(row=3, column=1)
        date_button.grid(row=3, column=2)
        clear_date_button.grid(row=3, column=3)

    def _footer(self):
        """Näyttää tallennus-, perumis- ja poistopainikkeen"""

        save_button = ttk.Button(
            master=self._frame, text="Save changes", command=self.save_changes)
        cancel_button = ttk.Button(master=self._frame, text="Cancel",
                                   command=lambda: self._handle_select_storage(operations.get_active_storage()))
        delete_button = ttk.Button(
            master=self._frame, text="Delete item from storage", command=self.delete_item)

        save_button.grid(row=5, column=1)
        cancel_button.grid(row=5, column=2)
        delete_button.grid(row=5, column=3)

    def _init_temp_data(self):
        """Alustaa väliaikaismuuttujat"""

        self._temp_amount = StringVar()
        self._temp_amount.set(self._active_item[1])

        self._temp_required = StringVar()
        self._temp_required.set(self._active_item[2])

        self._temp_exp = StringVar()
        self._temp_exp.set(self._active_item[3])

        self._temp_monitored = IntVar()
        self._temp_monitored.set(self._active_item[4])

        self._temp_misc = StringVar()
        self._temp_misc.set(self._active_item[5])

    def _increase_amount(self):
        """Kasvattaa temp-määrän arvoa"""

        old_amount = int(self._temp_amount.get())
        new_amount = old_amount + 1
        self._temp_amount.set(str(new_amount))

    def _decrease_amount(self):
        """Pienentää temp-määrän arvoa"""

        old_amount = int(self._temp_amount.get())
        new_amount = old_amount - 1
        if new_amount < 0:
            new_amount = 0
        self._temp_amount.set(str(new_amount))

    def _increase_required_amount(self):
        """Kasvattaa temp-minimimäärän arvoa"""

        old_req = int(self._temp_required.get())
        new_req = old_req + 1
        self._temp_required.set(str(new_req))

    def _decrease_required_amount(self):
        """Pienentää temp-minimimäärän arvoa"""

        old_req = int(self._temp_required.get())
        new_req = old_req - 1
        if new_req < 0:
            new_req = 0
        self._temp_required.set(str(new_req))

    def save_changes(self):
        """Kutsuu Operations-luokan metodeja, joilla muuttujakentän arvot
        päivitetään tietokantaan"""

        operations.update_amount(self._temp_amount.get())
        operations.update_minimum_amount(self._temp_required.get())
        operations.update_expiry_date(self._temp_exp.get())
        operations.update_monitored_status(self._temp_monitored.get())
        operations.update_misc(self._temp_misc.get())
        self._handle_select_storage(operations.get_active_storage())

    def change_date(self, datestr):
        """Muuttaa temp-vanhenemispäivämäärän. Metodi tarkastaa ensin 
        argumenttina saamansa merkkijonon ja muokkaa siitä temp-tallennettavan
        date-arvon. Try/except tarkastus varmistaa oikean formaatin, joka
        vaikuttaa olevan käyttöjärjestelmäriippuvainen.

        Args:
            datestr: päivämäärä tkcalendar-moduulin tuottamana merkkijonona
        """

        try:
            datelist = datestr.split(".")
            std = date(int(datelist[2]), int(
                datelist[1]), int(datelist[0])).isoformat()
        except IndexError:
            datelist = datestr.split("/")
            std = date(int(datelist[2]), int(
                datelist[1]), int(datelist[0])).isoformat()
        self._temp_exp.set(std)

    def delete_item(self):
        """Poistaa tavaran varaston listauksesta"""

        operations.delete_item()
        self._handle_select_storage(operations.get_active_storage())

    def pack(self):
        """Piirtää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tyhjentää näkymän"""

        self._frame.destroy()
