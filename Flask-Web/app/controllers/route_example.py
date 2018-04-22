from app import app, Session
from app.models.contacts import Contacts
from flask import render_template, url_for

def insert(conn):
    conn.add( Contacts('aaaaaaaaaaaa','10') )
    conn.add( Contacts('bbbbbbbb','11') )
    conn.add( Contacts('cccc','12') )

    conn.commit()

def readall(conn):
    query = conn.query(Contacts).order_by(Contacts.name).all()
    #[print(f'Name: {row.name[:10]:10} - Fone: {row.fone}') for row in query]
    return [(row.name,row.fone) for row in query]


def crud(function):
    conn = Session()
    result = function(conn)
    conn.close()
    return result


@app.route('/')
def hello_world():
    crud(insert)
    return render_template('index.html', contacts=crud(readall))

    