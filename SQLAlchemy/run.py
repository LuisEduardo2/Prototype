from app import Session

from app.model.contacts import Contacts


def insert(conn):
    conn.add( Contacts('aaaaaaaaaaaa','10') )
    conn.add( Contacts('bbbbbbbb','11') )
    conn.add( Contacts('cccc','12') )

    conn.commit()

def readall(conn):
    query = conn.query(Contacts).order_by(Contacts.name).all()
    [print(f'Name: {row.name[:10]:10} - Fone: {row.fone}') for row in query]


def crud(function):
    conn = Session()
    function(conn)
    conn.close()

if __name__ == '__main__':
    crud(insert)
    crud(readall)
