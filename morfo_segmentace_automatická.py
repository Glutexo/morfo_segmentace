import csv

cisla = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "slouč"] #"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "slouč"

for cislo in cisla:

    # načtení morfologického slovníku jako slovníku (haha)
    with open("můj_slovník.csv", encoding="UTF-8") as soubor:
        obsah_slovniku = csv.reader(soubor, delimiter=";")

        polozky_ze_slovniku = []
        for polozka in obsah_slovniku:
            dvojice = (polozka[0], polozka[1])
            polozky_ze_slovniku.append(dvojice)

    slovnik = dict(polozky_ze_slovniku)

    # načtení textu/slov k segmentaci (a odstranění případné mezery na konci)
    with open(f"foneticky_přepsaný_stud_{cislo}.txt", encoding="UTF-8") as soubor:
        slova_k_segmentaci = soubor.read().strip().split(sep=" ")

    # autosegmentace
    for i in range(len(slova_k_segmentaci)):
        try:
            slova_k_segmentaci[i] = slovnik[slova_k_segmentaci[i]]
        except KeyError:
            print(f"POZOR! SLOVO {slova_k_segmentaci[i]} CHYBÍ VE SLOVNÍKU A TUDÍŽ NEBUDE SEGMENTOVÁNO!")
            pass   #

    text_segmentovany_slouceny = " ".join(slova_k_segmentaci)

    # uložení výsledku segmentace do souboru
    with open(f"vysledek_segmentace_stud_{cislo}.txt", mode="x" ,encoding="UTF-8") as soubor:
        print(text_segmentovany_slouceny, file=soubor)