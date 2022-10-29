import sqlite3
import string
import random

con = sqlite3.connect('URL_shortener.db')
cur = con.cursor()
creator_query = '''CREATE TABLE IF NOT EXISTS urls(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Original VARCHAR, 
                    Shortened VARCHAR
                    );'''
cur.execute(creator_query)

long_url = input('Paste full URL: ')

checker_query = f'''SELECT Shortened 
                    FROM urls 
                    WHERE Original='{long_url}'
                    ;'''

def check_repeat_link():
    result = cur.execute(checker_query)
    data = result.fetchone() 
    if data:
        return data[0]
    else:
        pass

def link_generator():
    symbols = [symbol for symbol in string.ascii_letters + string.digits if symbol]
    random_symbols = random.choices(symbols,  k=6)
    short_url = 'dbshort.me/' + ''.join(random_symbols)
    return short_url



def url_shortener():
    link = check_repeat_link()
    if link:
        return link
    else:
        short_url = link_generator()
        cursor_instructions = f''' 
        INSERT INTO urls(Original, Shortened) VALUES
            ("{long_url}", "{short_url}")'''
        cur.execute(cursor_instructions)
        con.commit()
        con.close()
        return short_url

if __name__ == '__main__':
    link = url_shortener()
    print(link)
