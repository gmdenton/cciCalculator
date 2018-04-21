from tkinter import *
from tkinter import ttk
from src.view.view import view
import json
from tkinter import messagebox


class ccCalculator(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Credit card interest calculator")
        self._view = view
        self._initiate_view()

    '''
    
    Initiate the properties within the view object for Tkinter.
    This is done here to abstract Tkinter dependencies from the view object.
    Abstracting this here will allow for reuse of business objects and logic within other gui or web frameworks
    
    '''

    def _initiate_view(self):
        self._view.apr = DoubleVar()
        self._view.openingBalance = DoubleVar()
        self._view.period = IntVar()
        self._view.openingBalance = DoubleVar()
        self._view.newCharges = DoubleVar()
        self._view.payment = DoubleVar()
        self._view.ccType = StringVar()
        self._view.noMonths = IntVar()
        self._view.noMonths.set(3)
        self.ti = DoubleVar()

    def _confirm_clear(self):
        if self.ti.get() > 0:
            messagebox.askquestion("Clear", "Clear previous results?", icon='question')
            if 'yes':
                self._clear_grid()


    def btncalculate_click(self, event):
        self._confirm_clear()
        js = self._view.do_calculate(self._view)
        self.ti.set(self._view.get_total_interest(self._view))
        self._read_json(js)


    def _clear_grid(self):
        x = self.tv.get_children()
        for item in x:
            self.tv.delete(item)

    def _display_about(event):
        messagebox._show("About", "Credit card interest calculator" + '\n\n' + "Created by: Gerard Denton")

    def btnclear_click(self, event):
        self._view.do_clear(self._view)
        self._clear_grid()

    def _read_json(self, data):
        ds = json.loads(data)
        for item in ds:
            self._update_grid(item['_month'], item['_principal'], item['_interest'], item['_balance'])


    def _update_grid(self, month, balance, principal, interest):
        self.tv.insert('', 'end', text=month, values=(balance, principal, interest))

    # Build the main user interface used for data entry
    def _build_user_entry_frame(self):
        first_frame = Frame(self.root)

        Label(first_frame, text="Interest rate").grid(row=0, column=0, sticky="w")
        self.txtApr = Entry(first_frame, width=8, textvariable=self._view.apr).grid(row=0, column=1, sticky="e")
        Label(first_frame, text="%").grid(row=0, column=2, sticky="w")

        Label(first_frame, text="Period").grid(row=1, column=0, sticky="w")
        self.txtPeriod = Entry(first_frame, width=8, textvariable=self._view.period).grid(row=1, column=1, sticky="e")
        Label(first_frame, text="days").grid(row=1, column=2, sticky="e")

        Label(first_frame, text="Opening balance").grid(row=2, column=0, sticky="w")
        Entry(first_frame, width=10, textvariable=self._view.openingBalance).grid(row=2, column=1, sticky="ew")

        Label(first_frame, text="New charges").grid(row=3, column=0, sticky="w")
        Entry(first_frame, width=10, textvariable=self._view.newCharges).grid(row=3, column=1, sticky="ew")

        Label(first_frame, text="Payment amount").grid(row=4, column=0, sticky="w")
        Entry(first_frame, width=10, textvariable=self._view.payment).grid(row=4, column=1, sticky="ew")

        btnCalculate = ttk.Button(first_frame, text="Calculate")
        btnCalculate.bind("<ButtonPress>", self.btncalculate_click)
        btnCalculate.grid(row=1, column=3, sticky='ew', padx=1)
        btnClear = ttk.Button(first_frame, text="Clear")
        btnClear.bind("<ButtonPress>", self.btnclear_click)
        btnClear.grid(row=2, column=3, sticky='ew', padx=1)
        lbabout = Label(first_frame, text="About", foreground='Blue')
        lbabout.bind("<Button-1>", lambda e: self._display_about())
        lbabout.grid(row=3, column=3, sticky="ew")


        Label(first_frame, text="Card type").grid(row=5, column=0, sticky="w")
        ttk.Combobox(first_frame, width=8, state="readonly", values=('AX', 'DN', 'MC', 'VA'), textvariable=self._view.ccType).grid(row=5, column=1, sticky="ew")

        Label(first_frame, text="Total Interest", font=('Arial',12, 'bold')).grid(row=6, column=0, sticky="w")
        Entry(first_frame, width=10, textvariable=self.ti, state=DISABLED).grid(row=6, column=1, sticky="ew")

        first_frame.pack()

    # display radio buttons for number of months to be displayed after calculation
    def _build_selector(self):
        second_frame = Frame(self.root)
        Label(second_frame, text="Calculate for: ").grid(row=0, column=1, sticky="w")

        rb1 = Radiobutton(second_frame, text="3 Months", padx=8, variable=self._view.noMonths, value=3)
        rb1.grid(row=0, column=2, sticky="w")

        rb2 = Radiobutton(second_frame, text="6 Months", padx=8, variable=self._view.noMonths, value=6)
        rb2.grid(row=0, column=3, sticky="w")

        rb3 = Radiobutton(second_frame, text="1 Year", padx=8, variable=self._view.noMonths, value=12)
        rb3.grid(row=0, column=4, sticky="w")

        second_frame.pack()

    # Build the results grid to display calculations of interest for each month requested range (3, 6 or 12 months)
    def _build_grid(self):
        self.third_frame = Frame(self.root)
        self.tv = ttk.Treeview(self.third_frame)
        self.tv['columns'] = ('principal', 'interest', 'balance')
        self.tv.column('#0', width=100, anchor='w')
        self.tv.column('principal', width=100, anchor='center')
        self.tv.column('interest', width=100, anchor='center')
        self.tv.column('balance', width=100, anchor='center')
        self.tv.heading('#0', text='Month', anchor='w')
        self.tv.heading('principal', text='Principal')
        self.tv.heading('interest', text='Interest')
        self.tv.heading('balance', text='Balance')
        self.tv.grid(sticky=(N, S, W, E))
        self.third_frame.grid_rowconfigure(0, weight=1)
        self.third_frame.grid_columnconfigure(0, weight=1)
        self.third_frame.pack()

    # Execute gui build functions to create user interface frames and components
    def build_gui(self):
        self._build_user_entry_frame()
        self._build_selector()
        self._build_grid()
        self.root.mainloop()

if __name__ == '__main__':
    cc = ccCalculator()
    cc.build_gui()