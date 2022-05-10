from tkinter import ttk, constants
from ops.operations import operations


class MainView:
    """Päänäkymästä vastaava luokka"""

    def __init__(self, root, handle_select_storage, handle_create_storage):
        """Luokan konstruktori luo päänäkymän joka koostuu luotujen varastojen listasta.
        Jos varastoja ei ole luotu, näytetään ohjeteksti joka ohjaa varaston luontiin.

        Attributes:
            root: TkInter-juuri
            handle_select_storage: 
                Välittää kutsun käyttöliittymälle, jolla siirrytään
                tietyn varaston näkymään. Saa argumentikseen varaston nimen
            handle_create_storage:
                Välittää kutsun, jolla siirrytään uuden varaston luomisnäkymään
        """

        self._root = root
        self._frame = None
        self._handle_select_storage = handle_select_storage
        self._handle_create_storage = handle_create_storage

        self._initialize()

    def pack(self):
        """Piirtää näkymän"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tyhjentää näkymän"""

        self._frame.destroy()

    def _initialize(self):
        """Alustaa näkymän ja kutsuu tarvittavia metodeja"""

        self._frame = ttk.Frame(master=self._root)
        intro_label = ttk.Label(
            master=self._frame, text="Welcome to the Storage manager!")
        intro_label_2 = ttk.Label(
            master=self._frame, text=operations.create_intro_text())
        intro_label.grid(padx=5, pady=5)
        intro_label_2.grid(padx=5, pady=5)
        storages = operations.get_all_storages()
        for storage in storages:
            self._list_storages(storage)
        self._footer()

    def _list_storages(self, storage):
        """Listaa argumenttina olevan varaston. Varasto alustetaan omaan frameensa.

        Args:
            storage: listattavan varaston nimi
        """

        storage_frame = ttk.Frame(master=self._frame)

        status = operations.check_storage_status(storage)

        label = ttk.Label(master=storage_frame, text=storage,
                          foreground=status[2][0])
        status_label = ttk.Label(
            master=storage_frame, text=f"{status[0][0]} / {status[0][1]}", foreground=status[2][1])
        days_to_exp_label = ttk.Label(
            master=storage_frame, text=status[1], foreground=status[2][2])
        button = ttk.Button(master=storage_frame, text="Open storage",
                            command=lambda: self._handle_select_storage(storage))
        label.grid(row=0, column=0, padx=3, sticky=constants.W)
        status_label.grid(row=0, column=1, padx=3)
        days_to_exp_label.grid(row=0, column=2, padx=3)
        button.grid(row=0, column=3)

        storage_frame.grid_columnconfigure(0, minsize=200)
        storage_frame.grid_columnconfigure(1, minsize=50)
        storage_frame.grid_columnconfigure(2, minsize=200)
        storage_frame.grid_columnconfigure(3, minsize=100)

        storage_frame.grid()

    def _footer(self):
        """Luo näkymän loppuun valintapainikkeen"""

        button = ttk.Button(
            master=self._frame, text="Create new storage", command=self._handle_create_storage)
        button.grid()
