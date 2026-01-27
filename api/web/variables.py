import os

def cargarvariables():
    os.environ['DB_USERNAME'] = 'grupo2a'
    os.environ['DB_PASSWORD'] = 'grupo2a'
    os.environ['DB_DATABASE'] = 'ciber'
    os.environ['DB_HOST'] = 'mariadb'
    os.environ['DB_PORT'] = '3306'
    os.environ['PORT'] = '8080'
    os.environ['HOST'] = '0.0.0.0'
