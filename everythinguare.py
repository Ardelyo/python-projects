import time
import sys

# --- Data Lirik (Urutan Kata dan Penanda) ---
# None = Ganti baris dan tunggu Enter
# __END__ = Akhir simulasi
lyrics_sequence = [
    "Cerita", "kita", "tak", "jauh", "berbeda", None,
    "Got", "beat", "down", "by", "the", "world", None,
    "Sometimes", "I", "wanna", "fold", None,
    "__END__" # Penanda akhir
]

# --- Fungsi Bantu ---
def type_word(word, delay=0.05):
    """Menampilkan satu kata dengan efek ketik + spasi."""
    # Jangan ketik penanda None atau __END__
    if word is None or word == "__END__":
        return

    for char in word:
        sys.stdout.write(char)  # Tulis karakter ke layar
        sys.stdout.flush()      # Pastikan langsung tampil
        time.sleep(delay)       # Jeda antar huruf
    sys.stdout.write(' ')       # Tambah spasi setelah kata selesai
    sys.stdout.flush()

# --- Logika Utama Simulasi ---
def run_simulation():
    """Menjalankan loop untuk menampilkan lirik, berhenti per baris."""
    print("Memulai simulasi lirik (Tekan Enter untuk lanjut per baris)...")
    time.sleep(1) # Jeda awal sedikit

    # Loop melalui setiap item dalam sequence
    for item in lyrics_sequence:
        if item is None:
            # Jika item adalah None, ganti baris dan tunggu input Enter
            print() # Pindah ke baris baru di terminal
            try:
                # Berhenti dan tunggu user menekan Enter
                input("Tekan Enter untuk baris berikutnya...")
            except EOFError: # Menangani jika input stream ditutup (jarang terjadi di run normal)
                 print("\nInput dihentikan, keluar.")
                 break
        elif item == "__END__":
            # Jika item adalah penanda akhir, tampilkan pesan dan keluar loop
            print("\n\n--- Simulasi Selesai ---")
            break
        else:
            # Jika item adalah kata biasa, tampilkan dengan efek ketik
            type_word(item)

# --- Menjalankan Program ---
if __name__ == "__main__":
    try:
        # Langsung jalankan simulasi utama
        run_simulation()
    except KeyboardInterrupt:
        # Menangani jika user menekan Ctrl+C untuk keluar paksa
        print("\nSimulasi dihentikan paksa oleh pengguna.")