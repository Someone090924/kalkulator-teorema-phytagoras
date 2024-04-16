import math
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ab():
    clear_terminal()
    print("Teorema Pythagoras")
    print("     a    ")
    print("    /|   ")
    print("   / |   untuk perhitungan AB ")
    print("  /__]   Rumus: √(BC² + CA²)")
    print(" b    c  ")
    print()
    bc = float(input("Masukkan panjang sisi BC: "))
    ca = float(input("Masukkan panjang sisi CA: "))
    result = math.sqrt(bc**2 + ca**2)
    print("Panjang sisi AB adalah:", result)
    repeat()

def ac():
    clear_terminal()
    print("Teorema Pythagoras")
    print("     a    ")
    print("    /|   ")
    print("   / |   untuk perhitungan AC")
    print("  /__]   Rumus: √(BC² - BA²)")
    print(" b    c  ")
    print()
    ba = float(input("Masukkan panjang sisi BA: "))
    bc = float(input("Masukkan panjang sisi BC: "))
    result = math.sqrt(bc**2 - ba**2)
    print("Panjang sisi AC adalah:", result)
    repeat()

def ba():
    clear_terminal()
    print("Teorema Pythagoras")
    print("     a    ")
    print("    /|   ")
    print("   / |   untuk perhitungan BA")
    print("  /__]   Rumus: √(BC² - AC²)")
    print(" b    c  ")
    print()
    ac = float(input("Masukkan panjang sisi AC: "))
    bc = float(input("Masukkan panjang sisi BC: "))
    result = math.sqrt(bc**2 - ac**2)
    print("Panjang sisi BA adalah:", result)
    repeat()

def bc():
    clear_terminal()
    print("Teorema Pythagoras")
    print("     a    ")
    print("    /|   ")
    print("   / |   untuk perhitungan BC")
    print("  /__]   Rumus: √(AB² + AC²)")
    print(" b    c  ")
    print()
    ab = float(input("Masukkan panjang sisi AB: "))
    ac = float(input("Masukkan panjang sisi AC: "))
    result = math.sqrt(ab**2 + ac**2)
    print("Panjang sisi BC adalah:", result)
    repeat()

def ca():
    clear_terminal()
    print("Teorema Pythagoras")
    print("     a    ")
    print("    /|   ")
    print("   / |    untuk perhitungan CA")
    print("  /__]   Rumus: √(BA² - AB²)")
    print(" b    c  ")
    print()
    ab = float(input("Masukkan panjang sisi AB: "))
    ba = float(input("Masukkan panjang sisi BA: "))
    result = math.sqrt(ba**2 - ab**2)
    print("Panjang sisi CA adalah:", result)
    repeat()

def cb():
    clear_terminal()
    print("Teorema Pythagoras")
    print("     a    ")
    print("    /|   ")
    print("   / |   untuk perhitungan CB ")
    print("  /__]   Rumus: √(AB² + CA²)")
    print(" b    c  ")
    print()
    ab = float(input("Masukkan panjang sisi AB: "))
    ca = float(input("Masukkan panjang sisi CA: "))
    result = math.sqrt(ab**2 + ca**2)
    print("Panjang sisi CB adalah:", result)
    repeat()

def teorema_pythagoras():
    clear_terminal()
    print("Teorema Pythagoras")
    print("     a    ")
    print("    /|   ")
    print("   / |   github: Someone090924")
    print("  /__]   instagram:Someone.py")
    print(" b    c  ")
    print()
    print("Pilihan:")
    print("1. AB - √(BC² + CA²)")
    print("2. AC - √(BC² - BA²)")
    print("3. BA - √(BC² - AC²)")
    print("4. BC - √(AB² + AC²)")
    print("5. CA - √(BA² - AB²)")
    print("6. CB - √(AB² + CA²)")
    pil = input("Masukkan pilihan: ")
    if pil == '1':
        ab()
    elif pil == '2':
        ac()
    elif pil == '3':
        ba()
    elif pil == '4':
        bc()
    elif pil == '5':
        ca()
    elif pil == '6':
        cb()
    else:
        print("Pilihan tidak valid.")

def repeat():
    repeat_option = input("Apakah Anda ingin melakukan perhitungan lagi? (y/n): ")
    if repeat_option.lower() == 'y':
        teorema_pythagoras()
    elif repeat_option.lower() == 'n':
        print("Terima kasih telah menggunakan kalkulator Pythagoras.")
    else:
        print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
        repeat()

teorema_pythagoras()
