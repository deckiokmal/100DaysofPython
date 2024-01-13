from random import randint
from replit import clear


def guesing_game():
    game_end = False
    random_number = randint(1, 100)

    print("wellcome to the number guesing game.")
    print("tebak angka antara 1 sampai 100.")

    game_level = input('Pilih game level. "easy" or "hard" \n').lower()

    if game_level == "easy":
        life = 10
        print("Anda memiliki kesempatan 10 kali.")
    elif game_level == "hard":
        life = 5
        print("Anda memiliki kesempatan 5 kali.")

    while not game_end:
        tebak = int(input("tebak angka: "))

        if life == 1:
            print("Kesempatan anda habis.")
            print("You lose.")
            play_again = input('ingin bermain lagi? type "y" or "n" \n').lower()
            if play_again == "y":
                clear()
                guesing_game()
            else:
                print("\nterimakasih sudah bermain bersama kami.")
                game_end = True
        elif tebak == 0:
            print("invalid input")
            print("tebak lagi.")
            life -= 1
            print(f"sisa kesempatan {life}.")
        elif tebak == random_number:
            print("Tebakan anda benar")
            play_again = input('ingin bermain lagi? type "y" or "n" \n').lower()
            if play_again == "y":
                clear()
                guesing_game()
            else:
                print("\nterimakasih sudah bermain bersama kami.")
                game_end = True
        elif tebak > random_number:
            print("to high.")
            print("tebak lagi.")
            life -= 1
            print(f"sisa kesempatan {life}.")
        elif tebak < random_number:
            print("to low.")
            print("tebak lagi.")
            life -= 1
            print(f"sisa kesempatan {life}.")
        else:
            print("out of range.")
            print("tebak lagi.")
            life -= 1
            print(f"sisa kesempatan {life}.")


guesing_game()
