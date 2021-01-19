# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class MeliscrapySqlitePipeline:

    def __init__(self):
        self.ids_seen = set()
        self.create_connection()
        #self.create_table()
        #quitamos create para que los datos se signa acumulando en cada llamada
    def create_connection(self):
        self.conn = sqlite3.connect('mymeli2.db')
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute('''drop table if exists meli_tb''')

        self.curr.execute('''create table meli_tb(
                         título text,
                         rooms  text,
                         baths  text,
                         precio text,
                         surface text
                         )''')

    def process_item(self, item, spider):
        #adapter = ItemAdapter(item)
        #if adapter['id']  in self.ids_seen:
        #    raise DropItem(f"Duplicate item found: {item!r}")
        #else:
        #    self.ids_seen.add(adapter['id'])
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute('''insert into meli_tb values ( ?,?,?,?,?) ''',(
            item['titulo'][0],
            item['rooms'][0],
            item['baths'][0],
            item['precio'][0],
            item['surface'][0]

        ))
        self.conn.commit()
