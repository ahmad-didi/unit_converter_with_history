import tkinter as tk
from tkinter import ttk, messagebox
from converters.length_converter import LengthConverter
from converters.mass_converter import MassConverter
from converters.temperature_converter import TemperatureConverter
from history.history_manager import HistoryManager

class App:
    def __init__(self, root):
        self.root = root
        root.title('Group 7 - Unit Converter with History')
        root.geometry('700x460')

        self.history_mgr = HistoryManager()
        self.categories = {
            'Length': LengthConverter(),
            'Mass': MassConverter(),
            'Temperature': TemperatureConverter(),
        }
        self._build_ui()
        self._load_history()

    def _build_ui(self):
        frm = ttk.Frame(self.root, padding=12)
        frm.pack(fill=tk.BOTH, expand=True)

        ctrl = ttk.Frame(frm)
        ctrl.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(ctrl, text='Category:').grid(row=0, column=0, sticky=tk.W, pady=4)
        self.cat_var = tk.StringVar(value='Length')
        self.cat_cb = ttk.Combobox(ctrl, textvariable=self.cat_var, values=list(self.categories.keys()), state='readonly')
        self.cat_cb.grid(row=0, column=1, padx=6)
        self.cat_cb.bind('<<ComboboxSelected>>', lambda e: self._refresh_units())

        ttk.Label(ctrl, text='From:').grid(row=0, column=2, sticky=tk.W, padx=(12,0))
        self.from_var = tk.StringVar()
        self.from_cb = ttk.Combobox(ctrl, textvariable=self.from_var, state='readonly')
        self.from_cb.grid(row=0, column=3, padx=6)

        ttk.Label(ctrl, text='To:').grid(row=0, column=4, sticky=tk.W, padx=(12,0))
        self.to_var = tk.StringVar()
        self.to_cb = ttk.Combobox(ctrl, textvariable=self.to_var, state='readonly')
        self.to_cb.grid(row=0, column=5, padx=6)

        ttk.Label(ctrl, text='Value:').grid(row=1, column=0, sticky=tk.W, pady=8)
        self.value_var = tk.StringVar()
        self.value_entry = ttk.Entry(ctrl, textvariable=self.value_var)
        self.value_entry.grid(row=1, column=1, padx=6)

        self.convert_btn = ttk.Button(ctrl, text='Convert', command=self._on_convert)
        self.convert_btn.grid(row=1, column=3, padx=6)

        self.clear_btn = ttk.Button(ctrl, text='Clear History', command=self._on_clear_history)
        self.clear_btn.grid(row=1, column=5, padx=6)

        res_frame = ttk.Frame(frm, padding=(0,10))
        res_frame.pack(fill=tk.X)
        self.result_var = tk.StringVar(value='Result will appear here')
        ttk.Label(res_frame, textvariable=self.result_var, font=('Segoe UI', 12)).pack(anchor=tk.W)

        hist_frame = ttk.LabelFrame(frm, text='History (most recent last)')
        hist_frame.pack(fill=tk.BOTH, expand=True)

        self.hist_list = tk.Listbox(hist_frame)
        self.hist_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll = ttk.Scrollbar(hist_frame, orient=tk.VERTICAL, command=self.hist_list.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.hist_list.config(yscrollcommand=scroll.set)

        self._refresh_units()

    def _refresh_units(self):
        cat = self.cat_var.get()
        conv = self.categories[cat]
        try:
            units = conv.units()
        except Exception:
            units = []
        self.from_cb['values'] = units
        self.to_cb['values'] = units
        if units:
            self.from_var.set(units[0])
            self.to_var.set(units[1] if len(units) > 1 else units[0])

    def _on_convert(self):
        cat = self.cat_var.get()
        conv = self.categories[cat]
        from_u = self.from_var.get()
        to_u = self.to_var.get()
        try:
            val = float(self.value_var.get())
        except ValueError:
            messagebox.showerror('Input error', 'Please enter a numeric value')
            return
        try:
            out = conv.convert(val, from_u, to_u)
        except Exception as e:
            messagebox.showerror('Conversion error', str(e))
            return
        result_text = f"{val} {from_u} = {round(out, 6)} {to_u}"
        self.result_var.set(result_text)

        entry = {
            'category': cat,
            'from': from_u,
            'to': to_u,
            'input': val,
            'output': round(out, 6)
        }
        self.history_mgr.add(entry)
        self.hist_list.insert(tk.END, result_text)

    def _load_history(self):
        h = self.history_mgr.load()
        for rec in h:
            s = f"{rec.get('input')} {rec.get('from')} = {rec.get('output')} {rec.get('to')}"
            self.hist_list.insert(tk.END, s)

    def _on_clear_history(self):
        if messagebox.askyesno('Confirm', 'Clear history?'):
            self.history_mgr.clear()
            self.hist_list.delete(0, tk.END)
