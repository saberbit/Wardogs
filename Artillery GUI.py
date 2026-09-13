
import tkinter as tk
from tkinter import messagebox
import math


def calculate():
    try:
        # Get gun coordinates
        gun_x, gun_y = map(
            float,
            gun_entry.get().replace(" ", "").split(",")
        )

        # Get target coordinates
        target_x, target_y = map(
            float,
            target_entry.get().replace(" ", "").split(",")
        )

        # Calculate coordinate differences
        dx = gun_x - target_x
        dy = gun_y - target_y

        # Pythagorean distance
        coordinate_distance = math.sqrt(dx**2 + dy**2)

        # Convert to metres
        range_metres = coordinate_distance * 100

        # RNG value
        rng = round(range_metres)

        # Show results
        range_label.config(text=f"{range_metres:.1f} m")
        rng_label.config(text=str(rng))

        # Ask what to do next
        answer = messagebox.askyesno(
            "Calculation Complete",
            f"Range: {range_metres:.1f} m\n"
            f"RNG Setting: {rng}\n\n"
            "Calculate another shot?"
        )

        if answer:
            reset()
        else:
            root.destroy()

    except ValueError:
        messagebox.showerror(
            "Invalid Coordinates",
            "Please enter coordinates like:\n\n"
            "98.43, 110.38"
        )


def reset():
    gun_entry.delete(0, tk.END)
    target_entry.delete(0, tk.END)

    range_label.config(text="---")
    rng_label.config(text="---")

    gun_entry.focus()


def close_program():
    root.destroy()


# -----------------------------
# WINDOW
# -----------------------------

root = tk.Tk()
root.title("Artillery RNG Calculator")
root.geometry("460x520")
root.resizable(False, False)
root.configure(padx=20, pady=20)


# -----------------------------
# TITLE
# -----------------------------

title = tk.Label(
    root,
    text="ARTILLERY RNG CALCULATOR",
    font=("Segoe UI", 18, "bold")
)
title.pack(pady=(0, 20))


# -----------------------------
# GUN COORDINATES
# -----------------------------

gun_label = tk.Label(
    root,
    text="Gun Coordinates (X, Y)",
    font=("Segoe UI", 11, "bold")
)
gun_label.pack(anchor="w")

gun_entry = tk.Entry(
    root,
    font=("Consolas", 16),
    justify="center"
)
gun_entry.pack(fill="x", pady=(5, 15))


# -----------------------------
# TARGET COORDINATES
# -----------------------------

target_label = tk.Label(
    root,
    text="Target Coordinates (X, Y)",
    font=("Segoe UI", 11, "bold")
)
target_label.pack(anchor="w")

target_entry = tk.Entry(
    root,
    font=("Consolas", 16),
    justify="center"
)
target_entry.pack(fill="x", pady=(5, 20))


# -----------------------------
# CALCULATE BUTTON
# -----------------------------

calculate_button = tk.Button(
    root,
    text="CALCULATE",
    font=("Segoe UI", 13, "bold"),
    command=calculate,
    height=2
)
calculate_button.pack(fill="x", pady=(0, 20))


# -----------------------------
# RANGE RESULT
# -----------------------------

range_title = tk.Label(
    root,
    text="CALCULATED RANGE",
    font=("Segoe UI", 10, "bold")
)
range_title.pack()

range_label = tk.Label(
    root,
    text="---",
    font=("Segoe UI", 20, "bold")
)
range_label.pack(pady=(0, 15))


# -----------------------------
# RNG RESULT
# -----------------------------

rng_title = tk.Label(
    root,
    text="RNG SETTING",
    font=("Segoe UI", 11, "bold")
)
rng_title.pack()

rng_label = tk.Label(
    root,
    text="---",
    font=("Segoe UI", 52, "bold")
)
rng_label.pack(pady=(0, 10))


# -----------------------------
# CLOSE BUTTON
# -----------------------------

close_button = tk.Button(
    root,
    text="CLOSE",
    font=("Segoe UI", 10),
    command=close_program
)
close_button.pack(pady=(10, 0))


# Press Enter to calculate
root.bind("<Return>", lambda event: calculate())

# Start with gun field selected
gun_entry.focus()

# Start application
root.mainloop()
