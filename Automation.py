import os
import shutil


# Dateiendungen und Zielordner
DATEI_TYPEN = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Musik": [".mp3", ".wav", ".flac", ".m4a"],
    "PDFs": [".pdf"],
    "Dokumente": [".doc", ".docx", ".txt", ".odt"],
    "Excel": [".xls", ".xlsx", ".csv"],
    "Archive": [".zip", ".rar", ".7z"],
}

def finde_ordner(endung):

    for ordner, endungen in DATEI_TYPEN.items():

        if endung.lower() in endungen:
            return ordner

    return "Sonstiges"


def dateien_sortieren(pfad):

    if not os.path.exists(pfad):
        print("❌ Dieser Ordner existiert nicht.")
        return

    dateien = os.listdir(pfad)

    verschoben = 0

    for datei in dateien:

        voller_pfad = os.path.join(pfad, datei)

        # Ordner überspringen
        if os.path.isdir(voller_pfad):
            continue

        # Dateiendung bestimmen
        endung = os.path.splitext(datei)[1]

        ordner = finde_ordner(endung)

        zielordner = os.path.join(
            pfad,
            ordner
        )

        # Ordner erstellen
        os.makedirs(
            zielordner,
            exist_ok=True
        )

        ziel = os.path.join(
            zielordner,
            datei
        )

        # Falls Datei bereits existiert
        if os.path.exists(ziel):

            name, extension = os.path.splitext(datei)

            zaehler = 1

            while os.path.exists(ziel):

                neuer_name = (
                    f"{name}_{zaehler}{extension}"
                )

                ziel = os.path.join(
                    zielordner,
                    neuer_name
                )

                zaehler += 1

        # Datei verschieben
        shutil.move(
            voller_pfad,
            ziel
        )

        print(f"✓ {datei} → {ordner}")

        verschoben += 1

    print()
    print("==============================")
    print("FERTIG!")
    print(f"{verschoben} Dateien sortiert.")
    print("==============================")


def main():

    print("==============================")
    print("     DATEI-SORTIERER")
    print("==============================")

    pfad = input(
        "\nWelchen Ordner möchtest du sortieren?\n"
    )

    pfad = pfad.strip().strip('"')

    dateien_sortieren(pfad)


if __name__ == "__main__":
    main()