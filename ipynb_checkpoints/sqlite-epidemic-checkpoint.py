import sqlite3
!rm epidemic.db
DB_PATH = 'epidemic.db'
db = sqlite3.connect(DB_PATH)
cursor = db.cursor() #This cursor helps making queries by interacting with the DB loaded from the disk above
query = """
                        CREATE TABLE Hospital
                         (
                             id INT PRIMARY KEY,
                             name TEXT NOT NULL,
                             location TEXT NOT NULL,
                             userid INT NOT NULL
                         );
        """
cursor.execute(query)
db.commit()
query = """
                    CREATE TABLE Diseases
                         (
                             id INT PRIMARY KEY,
                             name TEXT NOT NULL,
                             meansofspread TEXT NOT NULL,
                             symptoms TEXT
                         );

"""                        
cursor.execute(query)
db.commit()
query = """
                
                         CREATE TABLE Drugs
                         (
                             drugid INT PRIMARY KEY,
                             drugname TEXT NOT NULL,
                             drugreq INT NOT NULL,
                             available INT NOT NULL, 
                             diseaseid INT NOT NULL,
                             FOREIGN KEY (diseaseid)
                             REFERENCES Diseases(id)
                         );
"""
cursor.execute(query)
db.commit()

query = """
                        CREATE TABLE Stats
                         (
                             diseaseid INT PRIMARY KEY,
                             ncases INT NOT NULL,
                             ndeaths INT NOT NULL,
                             spreadprob INT,
                             FOREIGN KEY (diseaseid)
                             REFERENCES Diseases(id)
                         );
"""
cursor.execute(query)
db.commit()

query = """
                    CREATE TABLE Cases
                    (
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         date TEXT NOT NULL,
                         diseaseid INT NOT NULL,
                         death INT,
                         location TEXT NOT NULL,
                         FOREIGN KEY (diseaseid) REFERENCES Diseases(id)
                         FOREIGN KEY (location) REFERENCES Hospital(location)
                     );
"""
cursor.execute(query)
db.commit()

query = """
                CREATE TABLE Login
                (
                        id INTEGER PRIMARY KEY,
                        password varchar(20) NOT NULL
                
                );
"""
cursor.execute(query)
db.commit()
db.close()
