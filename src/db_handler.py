import sqlite3
from os import path
from env import DATABASE_ROOT_PATH

VIDEOS_DATABASE_PATH = path.join(DATABASE_ROOT_PATH, 'videos.sqlite3')
TABLE_NAME = 'videos_list'

class SqliteHandler(object):
    def __init__(self):
        self.conn = sqlite3.connect(VIDEOS_DATABASE_PATH)
        self.conn.set_trace_callback(print)
        self.cur = self.conn.cursor()
        self.createTableIfNotExist(self.cur, TABLE_NAME)
        self.conn.commit()

    def close(self):
        self.conn.commit()
        self.conn.close()

    def createTableIfNotExist(self, cur, table_name):
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id integer PRIMARY KEY,
                url varchar NOT NULL,
                filename varchar NOT NULL
            );
        """)

    def isAlreadyRegistered(self, url):
        ret = self.getCountOfData(self.cur, TABLE_NAME, url)[0]
        return ret is not None and 0 < ret

    def selectAll(self):
        self.cur.execute(f"""
            SELECT * FROM {TABLE_NAME} 
        """)
        return self.cur.fetchone()

    def getCountOfData(self, cur, table_name, url):
        cur.execute(f"""
            SELECT count(*) FROM {table_name}
            WHERE url = '{url}';
        """)
        return cur.fetchone()

    def registerVideo(self, url, filename):
        self.insertRecordIfNotExists(self.cur, TABLE_NAME, url, filename)

    def insertRecordIfNotExists(self, cur, table_name, url, filename):
        cur.execute(f"""
            INSERT OR IGNORE INTO {table_name} (url, filename) VALUES ('{url}', '{filename}');
        """)

if __name__ == '__main__':
    print('started')
    sh = SqliteHandler()
    tmp = sh.selectAll()
    print('finished')
