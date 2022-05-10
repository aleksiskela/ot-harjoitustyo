from tkinter import Toplevel, ttk, constants
from ops.operations import operations


class CreateStorageView:
    """Uuden varaston luomisesta vastaava näkymä"""

    def __init__(self, root, handle_return):
        """Konstuktori luo luontinäkymän

        Attributes:
            root: TkInter-juuri
            handle_return: Välittää kutsun jolla siirrytään päänäkymään
        """

        self._root = root
        self._frame = None
        self._handle_return = handle_return

        self._initialize()

    def _initialize(self):
        """Alustaa näkymän"""

        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Create new storage")
        name_label = ttk.Label(master=self._frame, text="Storage name")
        name_entry = ttk.Entry(master=self._frame)
        create_button = ttk.Button(master=self._frame, text="Create",
                                   command=lambda: self._create_storage(name_entry.get()))
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._handle_return)

        label.grid(row=0, columnspan=3)
        name_label.grid(row=1, column=0)
        name_entry.grid(row=1, column=1)
        create_button.grid(row=2, column=1, sticky=constants.W)
        cancel_button.grid(row=2, column=1, sticky=constants.E)

    def _error_popup(self, error_msg):
        """Metodi luo ponnahdusikkunan, joka ilmoittaa virhesyötteen

        Args:
            error_msg: Näytettävä virheviesti
        """

        popup = Toplevel(master=self._frame)
        popup.title("Input error")
        popup_label = ttk.Label(
            master=popup, text=error_msg)
        popup_label.grid(padx=10, pady=10)

    def pack(self):
        """Piirtää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tyhjentää näkymän"""

        self._frame.destroy()

    def _create_storage(self, name):
        """Luo uuden varaston. Jos syötteessä on virhe, kutsuu metodia, joka
        ilmoittaa virhesyötteestä

        Args:
            name: Luotavan varaston nimi
        """

        error = None
        name = name.strip()

        if operations.check_storage_name(name):
            error = "The name must have at least one character"
        elif operations.check_if_storage_already_exists(name):
            error = "A storage by the same name already exists"

        if error:
            self._error_popup(error)
        else:
            operations.create_new_storage(name)
            self._handle_return()
