def main():
    words = get_words()
    check_words(user=words)




def get_words():
    words = input("Введите предложение: ")

    return words

def check_words(user):
    glas = "ауоыиэяюёеАУОЫИЭЯЮЁЕ"
    soglas = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

    track_glas = 0
    track_soglas = 0

    for line in user:
        for glas_t in glas:
            if glas_t == line:
                track_glas += 1
        for soglas_t in soglas:
            if soglas_t == line:
                track_soglas += 1
    print(f"Soglas: {track_soglas}")
    print(f"Glas: {track_glas}")

main()

