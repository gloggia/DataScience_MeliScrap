import scrapy
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
#from meliscrapy_Sqlite.items import MeliscrapySqliteItem
#Se quita la referencia al directorio items ya que se si lllama desde otro programa no la resuleve
#por lo que se crea la clase local Meliscra1

class Meliscra1(Item):
    descripcion = Field()
    titulo = Field()
    precio = Field()
    rooms =  Field()
    baths = Field()
    surface = Field()

class melispiders(CrawlSpider):
    name = 'mercadoLibre'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        #Se quita dado que Meli no permite descargar mas de 7 deptos por ejecuciòn.
        #Las reglas estan escritas en robot.exe el cual se lee y antes de ejecutar los comandos respetando sus reglas
        #'CLOSESPIDER_PAGECOUNT': 27
        #'CLOSESPIDER_ITEMCOUNT': 270

    }
    download_delay = 1
    #=70620*1.645*1.645*0.5*0.5/(0.05*0.05*(70620-1)+ 1.645*1.645*0.5*0.5) = 270 casos
    allowed_domains = ['departamento.mercadolibre.com.ar', 'inmuebles.mercadolibre.com.ar/departamentos']   #puedo poner más dominios solo poniendo comas


    start_urls = [
     'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Agronomía/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Almagro/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Balvanera/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Barracas/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Barrio-Norte/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Belgrano/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Belgrano-Barrancas/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Belgrano-C/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Belgrano-Chico/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Belgrano-R/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Boedo/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Botánico/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Caballito/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Chacarita/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Coghlan/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Colegiales/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Congreso/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Constitución/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Flores/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Floresta/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/La-Boca/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Las-Cañitas/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Liniers/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Mataderos/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Monserrat/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Monte-Castro/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Nueva-Pompeya/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Núñez/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Once/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Palermo/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Palermo-Chico/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Palermo-Hollywood/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Palermo-Nuevo/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Palermo-Soho/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Palermo-Viejo/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Parque-Avellaneda/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Parque-Chacabuco/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Parque-Chas/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Parque-Patricios/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Paternal/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Puerto-Madero/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Recoleta/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Retiro/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Saavedra/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/San-Cristóbal/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/San-Nicolás/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/San-Telmo/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Santa-Rita/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Velez-Sarsfield/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Versalles/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Crespo/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-del-Parque/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Devoto/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Gral.-Mitre/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Lugano/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Luro/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Ortúzar/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Pueyrredón/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Real/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Soldati/',
    'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/Villa-Urquiza/']




#    ,'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/belgrano/'
#    ,'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/palermo/'
#    ,'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/caballito/'
#    ,'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/palermo-hollywood/'
#    ,'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/almagro/'
#    ,'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/coghlan/'
#    ,'https://inmuebles.mercadolibre.com.ar/departamentos/venta/propiedades-individuales/capital-federal/nunez/']

    #start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/propiedades-individuales//capital-federal/']
    #start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/propiedades-individuales/capital-federal/barrio-norte/']
    #start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/propiedades-individuales/capital-federal/belgrano/']
    #start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/propiedades-individuales/capital-federal/palermo/']
    #start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/propiedades-individuales/capital-federal/caballito/']
    #start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/propiedades-individuales/capital-federal/palermo-hollywood/']
    #start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/propiedades-individuales/capital-federal/almagro/']
    #start_urls = ['https://inmuebles.mercadolibre.com.ar/departamentos/propiedades-individuales/capital-federal/nunez/']



    rules = (
        Rule(  # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(
                allow=r'/_Desde_\d+'
            ), follow=True),

        Rule(   # REGLA #2 => VERTICALIDAD AL DETALLE PRODUCTOS
            LinkExtractor(
                allow=r'/MLA-'
            ), follow=True, callback='parse_items'),
    )



    def limpiarTexto(self,texto):
        nuevoTexto= texto.replace('\n',' ').replace('\r',' ').replace('\t',' ').strip()
        return nuevoTexto

#item = ItemLoader(MeliscrapySqliteItem1(), response)
#Se quita la llamada a la clase del directorio items porque si se llama de afuera no lo resuelve
#item.add_xpath('descripcion', '//div[@class="item-description__text"]/p/text()', MapCompose(self.limpiarTexto))

    def parse_items(self, response):

        item = ItemLoader(Meliscra1(), response)

        item.add_xpath('titulo','//h1/text()',MapCompose(self.limpiarTexto))
        item.add_xpath('baths', '//dd[@class="align-bathroom"]/text()',MapCompose(self.limpiarTexto))
        item.add_xpath('rooms', '//dd[@class="align-room"]/text()',MapCompose(self.limpiarTexto))
        item.add_xpath('precio', '//span[@class="price-tag-fraction"]/text()')
        item.add_xpath('surface', '//dd[@class="align-surface"]/text()',MapCompose(self.limpiarTexto))
        yield item.load_item()
#scrapy runspider melisql.py
