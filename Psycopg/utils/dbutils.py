import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connexion = None
    try:
        connexion = psycopg2.connect(
            dbname= db_name,
            user= db_user,
            password= db_password,
            host= db_host,
            port= db_port,
        )
        print(f"Connexion a la base de donnée {db_name} réussie")
    except OperationalError as e:
        print(f"L'erreur {e} est survenie")
    return connexion


def execute_query(connexion, fetchall, query, parameters=[]):
    connexion.autocommit = True
    cursor = connexion.cursor()
    resultat = ()
    try:
        cursor.execute(query, parameters)
        if fetchall:
            resultat = cursor.fetchall()
        else:
            resultat = cursor.fetchone()
        print("Requête éxécutée avec succès")
    except OperationalError as e:
        print(f"L'erreur {e} est survenie")
    finally:
        cursor.close()
        return resultat
        
def close_connection(connexion):
    connexion.close()
    print("Connexion à la base de donnée fermée")