import pandas


def simsonstables():
    article = "https://de.wikipedia.org/wiki/Die_Simpsons%2FEpisodenliste?wprov=sfla1"
    simpsonsdata = pandas.read_html(article)
    with open("simpsons.csv","w") as file:
        file.write(str(simpsonsdata[0]))


simsonstables()
