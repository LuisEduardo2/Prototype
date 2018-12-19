from app import Session

from app.model.contacts import Contacts


def insert(data):
    conn = Session()
    conn.add(data)
    conn.commit()
    conn.close()

def readall():
    conn = Session()
    query = conn.query(Contacts).order_by(Contacts.name).all()
    result = [(row.name,row.fone) for row in query]
    conn.close()
    return result

if __name__ == '__main__':
    insert(Contacts('data1','1111'))
    insert(Contacts('data2','2222'))
    insert(Contacts('data3','3333'))
    [print(f'Name: {row[0][:10]:10} - Fone: {row[1]}') for row in readall()]
