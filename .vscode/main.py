import random

angka_rahasia = random.randint(1, 25)
kesempatan = 5

print("Tebak angka antara 1 sampai 25!")

while kesempatan > 0:
    tebakan = int(input("masukkan tebakanmu: "))

    if tebakan == angka_rahasia:
        print("Selamat, tebakanmu BENAR!")
        break
    elif tebakan < angka_rahasia:
        print("Kurang besar!")
    else:
        print("Kurang kecil!")

    kesempatan -= 1
    print(f"Sisa kesempatann: {kesempatan}\n")

if kesempatan == 0:
    print(f"Game OVER! Angka yang benar adalah {angka_rahasia}")

