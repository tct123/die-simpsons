import pandas

article = "https://de.wikipedia.org/wiki/Die_Simpsons%2FEpisodenliste?wprov=sfla1"
simpsonsdata = pandas.read_html(article)
print(simpsonsdata[0])
