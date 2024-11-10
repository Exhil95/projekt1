import tkinter as tk
from tkinter import messagebox

def wylicz_bmi():
    try:
        waga = float(waga_dane.get())
        wzrost = float(wzrost_dane.get())
        
        if wzrost <= 0 or waga <= 0:
            messagebox.showerror("Błąd", "Waga i wzrost muszą być większe od zera.")
            return

        bmi = waga / (wzrost ** 2)
        wynik_label.config(text=f"Twoje BMI: {bmi:.2f}")

        if bmi < 18.5:
            kategoria = "Niedowaga"
        elif 18.5 <= bmi < 24.9:
            kategoria = "Waga prawidłowa"
        elif 25 <= bmi < 29.9:
            kategoria = "Nadwaga"
        else:
            kategoria = "Otyłość"
        
        kategoria_label.config(text=f"Kategoria: {kategoria}")
    except ValueError:
        messagebox.showerror("Błąd", "Proszę podać prawidłowe wartości dla wagi i wzrostu.")


window = tk.Tk()
window.title("Kalkulator BMI")


tk.Label(window, text="Waga (kg):").grid(row=0, column=0, padx=10, pady=10)
waga_dane = tk.Entry(window)
waga_dane.grid(row=0, column=1, padx=10, pady=10)


tk.Label(window, text="Wzrost (m):").grid(row=1, column=0, padx=10, pady=10)
wzrost_dane = tk.Entry(window)
wzrost_dane.grid(row=1, column=1, padx=10, pady=10)


wylicz_button = tk.Button(window, text="Oblicz BMI", command=wylicz_bmi)
wylicz_button.grid(row=2, column=0, columnspan=2, pady=10)


wynik_label = tk.Label(window, text="Twoje BMI:")
wynik_label.grid(row=3, column=0, columnspan=2, pady=10)


kategoria_label = tk.Label(window, text="Kategoria:")
kategoria_label.grid(row=4, column=0, columnspan=2, pady=10)


window.mainloop()
