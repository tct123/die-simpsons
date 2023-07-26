import pandas
import csv


def simsonstables():
    article = "https://de.wikipedia.org/wiki/Die_Simpsons%2FEpisodenliste?wprov=sfla1"
    simpsonsdata = pandas.read_html(article)
    for x in range(len(simpsonsdata)):
        simpsonsdata[x].to_csv(path_or_buf=f"simpsons{x}.csv")


simsonstables()
