# InfoCity
Um módulo Python com funções que retornam informações de uma cidade, como temperatura, noticias e outros.

## Necessario

* Selenium. (`pip install selenium`)
* Google Chrome
* Chrome Driver

### Como usar?

* Baixe o repositorio e extraia dentro da pasta do seu projeto.
* Importe o módulo usando: `import infocity`.
* Veja o exemplo para ver a utilização na prática. (`example.py`)

#### Funções

* `infocity.getClimate(city)´

Função recebe como parametro o nome de uma cidade e retorna uma descrição do clima.
Exemplo `print(infocity.getClimate('São Paulo')`
