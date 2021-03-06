from tkinter import Toplevel, ttk, constants, Checkbutton, IntVar
from ops.operations import operations


class EditStorageView:
    """Varaston vaadittavien tavaroiden listauksesta ja varaston poistamisesta
    vastaava näkymä
    """

    def __init__(self, root, handle_select_storage, handle_edit_storage, handle_return):
        """Luokan konstruktori luo varaston muokkausnäkymän

        Attributes:
            root: TkInter-juuri
            handle_select_storage: 
                Välittää kutsun palata varastonäkymään. 
                Saa argumentiksen varaston nimen.
            handle_edit_storage: Välittää kutsun piirtää näkymä uudestaan
            handle_return: Välittää kutsun siirtyä päänäkymään
        """

        self._root = root
        self._frame = None
        self._handle_select_storage = handle_select_storage
        self._handle_edit_storage = handle_edit_storage
        self._handle_return = handle_return

        self._initialize()

    def _initialize(self):
        """Alustaa varaston muokkausnäkymän ja kutsuu tarvittavia metodeja"""

        self._frame = ttk.Frame(master=self._root)

        label_text = f"Add item requirement for {operations.get_active_storage()}"
        storage_label = ttk.Label(master=self._frame, text=label_text)
        name_label = ttk.Label(master=self._frame, text="Item name")
        min_required_label = ttk.Label(
            master=self._frame, text="Minimum required")

        storage_label.grid(row=0, column=1)
        name_label.grid(row=1, column=0)
        min_required_label.grid(row=1, column=1)

        self._entry()

        if len(operations._temp_items) > 0:
            temp_label = ttk.Label(
                master=self._frame, text="Items to be added:")
            temp_label.grid(row=3, column=0)
            for item in operations.get_temp_items():
                self.list_temp_items(item)

        self._footer()

    def _entry(self):
        """Luo syötekentät, valitsimen ja painikkeen"""

        entry_frame = ttk.Frame(master=self._frame)

        essential = IntVar()

        item_name_entry = ttk.Entry(master=entry_frame)
        min_amount_entry = ttk.Entry(master=entry_frame)
        monitored_check = Checkbutton(master=entry_frame, text="Monitored",
                                      variable=essential, onvalue=1, offvalue=0)
        add_item_button = ttk.Button(master=entry_frame,
                                     text="Add required item",
                                     command=lambda: self._add_temp_item(item_name_entry.get(),
                                                                         min_amount_entry.get(), essential.get()))

        item_name_entry.grid(row=0, column=0)
        min_amount_entry.grid(row=0, column=1)
        monitored_check.grid(row=0, column=2)
        add_item_button.grid(row=0, column=3)

        entry_frame.grid(column=0, columnspan=4)

    def _footer(self):
        """Näyttää tallennus-, cancel- ja poista varasto-painikkeet"""

        footer_frame = ttk.Frame(master=self._frame)

        save_button = ttk.Button(
            master=footer_frame, text="Save", command=self.save_changes)
        cancel_button = ttk.Button(master=footer_frame, text="Cancel",
                                   command=lambda: self._handle_select_storage(operations.get_active_storage()))
        delete_button = ttk.Button(
            master=footer_frame, text="Delete storage", command=self._delete_storage)

        save_button.grid(row=0, column=1, sticky=constants.W)
        cancel_button.grid(row=0, column=2, sticky=constants.E)
        delete_button.grid(row=0, column=3)

        footer_frame.grid(column=1, sticky=constants.W)

    def _add_temp_item(self, name, req, mon):
        """Tarkastaa syötteen ja tallentaa oikean syötteen
        väliaikaisesti. Väärä syöte johtaa virheilmoitukseen

        Args:
            name: Tavaran nimi
            req: Minimimäärä
            mon: Arvo joka ilmaisee tavaran tarkestelustatuksen"""

        req = req.strip()
        if len(req) == 0:
            req = 0

        name = name.strip()
        error = operations.check_temp_item_input(name, req)

        if error:
            self._error_popup(error)
        else:
            item = (name, int(req), mon)
            operations.add_temp_item(item)
            self.destroy()
            self._handle_edit_storage()

    def list_temp_items(self, item):
        """Näyttää väliaikaistallennetun tavaran tiedot

        Args:
            item: Tuple jonka alkiot ovat tuotteen nimi, minimimäärä ja tarkastelustatus"""

        temp_frame = ttk.Frame(master=self._frame)
        temp_label = ttk.Label(
            master=temp_frame, text=f"{item[0]} | {item[1]} required | {operations.monitored_message(item[2])}")
        temp_label.grid(column=0, columnspan=2)
        temp_frame.grid(column=0, columnspan=3, sticky=constants.W)

    def save_changes(self):
        """Tallentaa väliaikaistallennetut tavarat tietokantaan"""

        for item in operations.get_temp_items():
            operations.add_new_required_item(item[0], item[1], item[2])
        self._handle_select_storage(operations.get_active_storage())

    def _error_popup(self, message):
        """Luo virheilmoitusponnahdusikkunan jonka viesti riippuu virhesyötteestä

        Args:
            message: Näytettävä virheviesti
        """

        popup = Toplevel(master=self._frame)
        popup.title("Input error")
        msg_label = ttk.Label(master=popup, text=message)
        msg_label.grid(padx=10, pady=10)

    def _delete_storage(self):
        """Poistaa varaston ja välittää kutsun siirtyä päänäkymään"""

        operations.delete_storage()
        self._handle_return()

    def pack(self):
        """Piirtää näytön"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tyhjentää näytön"""

        self._frame.destroy()
