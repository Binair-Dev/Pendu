from utils.dbutils import *
from models.Utilisateur import Utilisateur

db_name = "demodb"
db_user = "postgres"
db_password = "Test1234@"
db_host = "localhost"
db_port = "5432"

connexion = create_connection(db_name, db_user, db_password, db_host, db_port)

if connexion is not None:
    #region insert
    # query = "INSERT INTO utilisateurs (nom, email) VALUES (%s, %s);"
    # parameters = ["Robert", "rob.stark@gmail.com"]
    # resultat = execute_query(connexion, fetchall=False, query=query, parameters=parameters)
    # print("Utilisateur inséré avec succès.")
    #endregion
    
    #region select
    # query = "SELECT * FROM utilisateurs"
    # resultat = execute_query(connexion, True, query)
    # print(f"Utilisateur trouvé: {resultat}")
    #endregion
    
    # region select one
    # query = "SELECT * FROM utilisateurs WHERE nom LIKE %s"
    # parameter = ["M%"]
    # resultat = execute_query(connexion, False, query, parameters=parameter)
    # print(f"Utilisateur trouvé: {resultat}")
    # #endregion
    
    # #region select mapped
    # query = "SELECT * FROM utilisateurs"
    # resultat = execute_query(connexion, True, query)
    # print("Utilisateurs: ")
    # print("==================")
    # for row in resultat:
    #     print(f"ID: {row[0]}")
    #     print(f"Nom: {row[1]}")
    #     print(f"Email: {row[2]}")
    #     print("==================")
    # #endregion
    
    # #region select mapped objet
    # query = "SELECT id, nom, email FROM utilisateurs;"
    # resultat = execute_query(connexion, True, query)
    
    # utilisateurs = [Utilisateur(*row) for row in resultat]
    # print("Utilisateurs: ")
    # print("==================")
    # for utilisateur in utilisateurs:
    #     print(utilisateur)
    #     print("==================")
    # #endregion
    
    #Fermer la connexion une fois les requetes éxécutées.
    close_connection(connexion)