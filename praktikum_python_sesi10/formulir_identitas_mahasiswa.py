"""
Praktikum Sesi 1 - Formulir Identitas Mahasiswa (Tkinter)

Fitur:
- Jendela berjudul "Formulir Identitas Mahasiswa"
- Label + Entry untuk Nama dan NIM
- Combobox Program Studi
- Text widget untuk Alamat (tugas pengembangan 1)
- Skema warna konsisten (tugas pengembangan 2)
- Validasi Nama dan NIM tidak boleh kosong (tugas pengembangan 3)
- Seluruh layout memakai grid() (tugas pengembangan 4)
- Tombol Simpan, Reset, dan Keluar (tugas pengembangan 5)
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------------
# Konfigurasi warna & font (satu tempat agar tampilan konsisten)
# ---------------------------------------------------------------
WARNA_BG = "#EAF2FB"        # latar jendela
WARNA_PANEL = "#FFFFFF"     # latar kotak hasil
WARNA_UTAMA = "#1F4E79"     # judul & teks penting
WARNA_TEKS = "#222222"      # teks biasa
WARNA_SIMPAN = "#2E8B57"    # tombol Simpan (hijau)
WARNA_RESET = "#E0A800"     # tombol Reset (kuning)
WARNA_KELUAR = "#C0392B"    # tombol Keluar (merah)

FONT_JUDUL = ("Arial", 15, "bold")
FONT_LABEL = ("Arial", 10, "bold")
FONT_INPUT = ("Arial", 10)
FONT_TOMBOL = ("Arial", 10, "bold")

# ---------------------------------------------------------------
# Jendela utama
# ---------------------------------------------------------------
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("460x560")
root.configure(bg=WARNA_BG)
root.resizable(False, False)

# Agar kolom di root bisa rata tengah
root.columnconfigure(0, weight=1)

# ---------------------------------------------------------------
# Judul
# ---------------------------------------------------------------
tk.Label(
    root,
    text="FORM IDENTITAS MAHASISWA",
    font=FONT_JUDUL,
    bg=WARNA_BG,
    fg=WARNA_UTAMA,
).grid(row=0, column=0, pady=(15, 10))

# ---------------------------------------------------------------
# Frame formulir (layout grid)
# ---------------------------------------------------------------
form = tk.Frame(root, bg=WARNA_BG)
form.grid(row=1, column=0, padx=20, pady=5)


def buat_label(teks, baris):
    """Membuat label di kolom 0 pada baris tertentu."""
    tk.Label(
        form, text=teks, font=FONT_LABEL, bg=WARNA_BG, fg=WARNA_TEKS
    ).grid(row=baris, column=0, sticky="nw", padx=(0, 10), pady=6)


# Nama
buat_label("Nama", 0)
nama = tk.Entry(form, width=32, font=FONT_INPUT)
nama.grid(row=0, column=1, pady=6, sticky="w")

# NIM
buat_label("NIM", 1)
nim = tk.Entry(form, width=32, font=FONT_INPUT)
nim.grid(row=1, column=1, pady=6, sticky="w")

# Program Studi
buat_label("Program Studi", 2)
prodi = ttk.Combobox(
    form,
    values=["Informatika", "Manajemen", "Akuntansi"],
    state="readonly",
    width=29,
    font=FONT_INPUT,
)
prodi.grid(row=2, column=1, pady=6, sticky="w")

# Alamat (widget Text)
buat_label("Alamat", 3)
alamat = tk.Text(form, width=32, height=4, font=FONT_INPUT, wrap="word")
alamat.grid(row=3, column=1, pady=6, sticky="w")

# ---------------------------------------------------------------
# Label hasil input
# ---------------------------------------------------------------
hasil = tk.Label(
    root,
    text="",
    font=FONT_INPUT,
    bg=WARNA_PANEL,
    fg=WARNA_TEKS,
    justify="left",
    anchor="nw",
    width=48,
    height=7,
    relief="groove",
    bd=2,
    padx=8,
    pady=6,
    wraplength=380,
)
hasil.grid(row=2, column=0, padx=20, pady=12)


# ---------------------------------------------------------------
# Fungsi tombol
# ---------------------------------------------------------------
def simpan():
    """Validasi input lalu tampilkan hasil pada Label."""
    isi_nama = nama.get().strip()
    isi_nim = nim.get().strip()
    isi_prodi = prodi.get()
    isi_alamat = alamat.get("1.0", tk.END).strip()

    # Validasi: nama dan NIM tidak boleh kosong
    if not isi_nama:
        messagebox.showwarning("Validasi", "Nama tidak boleh kosong!")
        nama.focus_set()
        return
    if not isi_nim:
        messagebox.showwarning("Validasi", "NIM tidak boleh kosong!")
        nim.focus_set()
        return

    hasil.config(
        text=(
            f"Nama: {isi_nama}\n"
            f"NIM: {isi_nim}\n"
            f"Program Studi: {isi_prodi if isi_prodi else '-'}\n"
            f"Alamat: {isi_alamat if isi_alamat else '-'}"
        )
    )


def reset():
    """Mengosongkan seluruh isian formulir dan label hasil."""
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END)
    hasil.config(text="")
    nama.focus_set()


def keluar():
    """Menutup aplikasi setelah konfirmasi."""
    if messagebox.askyesno("Keluar", "Apakah Anda yakin ingin keluar?"):
        root.destroy()


# ---------------------------------------------------------------
# Tombol (layout grid)
# ---------------------------------------------------------------
tombol = tk.Frame(root, bg=WARNA_BG)
tombol.grid(row=3, column=0, pady=5)

tk.Button(
    tombol, text="Simpan", command=simpan, width=10,
    font=FONT_TOMBOL, bg=WARNA_SIMPAN, fg="white",
    activebackground="#256F46", activeforeground="white",
).grid(row=0, column=0, padx=6)

tk.Button(
    tombol, text="Reset", command=reset, width=10,
    font=FONT_TOMBOL, bg=WARNA_RESET, fg="black",
    activebackground="#B88A00", activeforeground="black",
).grid(row=0, column=1, padx=6)

tk.Button(
    tombol, text="Keluar", command=keluar, width=10,
    font=FONT_TOMBOL, bg=WARNA_KELUAR, fg="white",
    activebackground="#992D22", activeforeground="white",
).grid(row=0, column=2, padx=6)

# Fokus awal pada kolom Nama
nama.focus_set()

root.mainloop()