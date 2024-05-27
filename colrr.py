import random
import time
import os
from colorama import init, Fore

# colorama başlatma
init()

# Terminal boyutlarını al
columns = os.get_terminal_size().columns if os.name == 'posix' else os.get_terminal_size()[0]
rows = os.get_terminal_size().lines if os.name == 'posix' else os.get_terminal_size()[1]

# Matriks karakterleri
matrix_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

# Matriks efekt fonksiyonu
def matrix_effect():
    # Sonsuz döngü
    while True:
        # Yeni satır
        line = ''
        for _ in range(columns):
            # %50 ihtimalle karakter veya boşluk ekle
            if random.random() > 0.5:
                line += random.choice(matrix_chars)
            else:
                line += ' '

        # Yeşil renkte yazdır
        print(Fore.GREEN + line)

        # Ekranı kaydırmak için kısa bir süre bekle
        time.sleep(0.05)

        # Çok fazla satır olmaması için en üst satırı sil
        print("\033[1A", end='', flush=True)

try:
    matrix_effect()
except KeyboardInterrupt:
    # Kullanıcı Ctrl+C ile durdurursa çık
    print("\033[0m")
    print("Matrix efekti durduruldu.")
