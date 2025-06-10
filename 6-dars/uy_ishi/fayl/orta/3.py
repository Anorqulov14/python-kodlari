
with open("countries.txt", "r") as f1, open("capitals.txt", "r") as f2:
    countries = f1.read().split()
    capitals = f2.read().split()

combined = zip(countries, capitals)

with open("file.txt", "w") as f:
    for country, capital in combined:
        f.write(f"{country} - {capital}\n")
