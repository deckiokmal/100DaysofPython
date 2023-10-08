from art import logo, vs
from game_data import data
from random import choice
from replit import clear


def generate_akun():
    """Generate random akun dari game data"""
    return choice(data)


def format_data(akun):
    """Memformat data akun dalam bentuk printable format"""
    name = akun["name"]
    desc = akun["description"]
    coun = akun["country"]

    return f"{name}, a {desc}, from {coun}"


def cek_jawaban(tebakan, follower_a, follower_b):
    """Cek jumlah Follower dan return Boolean"""
    if follower_a > follower_b:
        return tebakan == "a"
    else:
        return tebakan == "b"


def game():
    print(logo)

    akun_a = generate_akun()
    akun_b = generate_akun()

    score = 0

    lanjutkan = True

    while lanjutkan:
        # Jawaban benar, generate new akun_b dan pindahkan pilihan benar ke akun_a
        akun_a = akun_b
        akun_b = generate_akun()

        # Generate ulang jika akun_a sebanding dengan akun_b
        while akun_a == akun_b:
            akun_b = generate_akun()

        print(f"Compare A : {format_data(akun_a)}")
        print(vs)
        print(f"Against B : {format_data(akun_b)}")

        tebakan = input('Follower siapa yang lebih besar? type "A" or "B": ').lower()
        follower_count_a = akun_a["follower_count"]
        follower_count_b = akun_b["follower_count"]

        jawaban_benar = cek_jawaban(tebakan, follower_count_a, follower_count_b)

        clear()
        print(logo)
        if jawaban_benar:
            score += 1
            print(f"Jawaban anda benar, score {score}")
        else:
            lanjutkan = False
            print(f"Jawaban anda salah. Final score {score}")


game()
