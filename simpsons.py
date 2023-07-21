import pandas


def simsonstables():
    article = "https://de.wikipedia.org/wiki/Die_Simpsons%2FEpisodenliste?wprov=sfla1"
    simpsonsdata = pandas.read_html(article)
    for x in range(len(simpsonsdata)):
        with open(f"simpsons{x}.csv","w") as file:
            file.write(str(simpsonsdata[x]))


simsonstables()
