# InfoCity
Um módulo Python com funções que retornam informações de uma cidade, como temperatura, noticias e outros.

## Necessario

* Selenium. (`pip install selenium`)
* Google Chrome
* Chrome Driver

## Como usar?

* Baixe o repositorio e extraia dentro da pasta do seu projeto.
* Importe o módulo usando: `import infocity`.
* Veja o exemplo para ver a utilização na prática. (`example.py`)

## Funções

* `infocity.getClimate(city)`

Função recebe como parametro o nome de uma cidade e retorna uma descrição de texto do clima atual. 
<br/>Exemplo:  ```print(infocity.getClimate('São Paulo')``` <- Retornará uma descrição do clima de São Paulo

* `infocity.getRain(city)`

Função recebe como parametro o nome de uma cidade e retorna, em porcentagem, a probabilidade de chover desta cidade.
<br/>Exemplo: `print(infocity.getRain('Belo Horizonte'))` <- Retornará a probabilidade de chover, em porcentagem, em Belzonte

* `infocity.getHumidity(city)`

Função recebe como parametro o nome de uma cidade e retorna, em porcentagem, a umidade do ar desta cidade.
<br/>Exemplo: `print(infocity.getHumidty('Campinas'))` <- Retornará a umidade de campinas

* `infocity.getWind(city)`

Função recebe como parametro o nome de uma cidade e retorna, em kilometros por hora, a velocidade do vento desta cidade.
<br/>Exemplo: `print(infocity.getWind('New York'))` <- Retornará a velocidade do vento de Nova Iorque

* `infocity.getTemp(city)`

Função recebe como parametro o nome de uma cidade e retorna a temperatura desta cidade (dependendo do seu IP, ele poderá vir em `Fahrenheit` ou `Celsius`).
<br/>Exemplo: `print(infocity.getTemp('Brasília'))` <- Retornará a temperatura de Brasília

* `infocity.getfirstnews(city)`

Função recebe como parametro o nome de uma cidade e retorna a primeira notícia localizada desta cidade.
<br/>Exemplo: `print(infocity.getfirstnews('Chicago'))` <- Retornará a primeira notícia encontrada de Chicago

* `infocity.getNews(city, num)` 

Função recebe como parametro o nome de uma cidade e um numero inteiro representanto a quantidade de noticias que se deve retornar. Retorna a quantidade de notícias solicitadas desta cidade.
<br/>Exemplo: `print(infocity.getNews('Salvador, 5'))` <- Retornará 5 notícias de Salvador

### Avisos

* Os dados são todos adquiridos pelo `Google` e `Google News` via `WebScrap`.
* Mantenha seu Google Chrome atualizado, caso não utilize, pode-se alterar o `webdriver` no código fonte.
* Mantenha o `Selenium` atualizado.
* Matenha o seu WebDriver atualizado.
* O exemplo não precisa ser importado para pasta do seu projeto.
* Obrigado por usar

:D


