import infocity

cidade = input('Insira o nome da cidade: ')

temperatura = int(infocity.getTemp(cidade))
vento = infocity.getWind(cidade)
noticia = infocity.getfirstnews(cidade)
noticias = infocity.getNews(cidade, 5)

print(temperatura)
print(vento)
print(noticia)
print(noticias)