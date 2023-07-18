from rich import print
from rich.progress import track
import requests
import csv
import os

# === Main Function ===
def main():
    # Constants
    FILENAME = "data/pokemon_species_names.csv"
    URL = "https://raw.githubusercontent.com/PokeAPI/pokeapi/master/data/v2/csv/pokemon_species_names.csv"

    # Create the data directory if it doesn't exist

    if not os.path.exists("data"):
        os.makedirs("data")

    # Download the data

    print("[bold dark_green]Downloading Pokemon...[/bold dark_green]")

    f = requests.get(URL, stream=True)

    # Write the data to a file

    with open(FILENAME, "wb") as file:
        for chunk in track(f.iter_content(chunk_size=128)):
            if chunk:
                file.write(chunk)

    print("[bold green]Download Complete![/bold green]")

    print("[bold dark_green]Reading Data...[/bold dark_green]")

    # Read the data from the file

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")

        print("[bold dark_green]Filtering Data (German Names)...[/bold dark_green]")

        # Filter: only German names

        german_names = []

        for row in reader:
            if row[1] == "6":
                german_names.append(row[2])

        print("[bold green]Filtering Complete![/bold green]")
        

        # Filter: only names that end with a vowel

        print("[bold dark_green]Filtering Data (Name must end with a vowel)...[/bold dark_green])")

        filtered_german_names = []

        for name in german_names:
            if name[-1] in ["a", "e", "i", "o", "u"]:
                filtered_german_names.append(name)

        print("[bold green]Filtering Complete![/bold green]")

        # Write the data to a file

        print("[bold dark_green]Writing Data to file...[/bold dark_green]")

        with open("data/filtered_german_names.txt", "w") as f:
            for name in filtered_german_names:
                f.write(name + "\n\n")

        print("[bold green]Writing Complete![/bold green]")

        print("[bold green]Done![/bold green]")
    


if __name__ == "__main__":
    main()
