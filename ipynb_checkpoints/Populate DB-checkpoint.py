import sqlite3
import numpy as np
import string
import random
import os
import datetime
def make_connection():
    db_name = "epidemic.db"
    try:
        con = sqlite3.connect(db_name)
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
    except Exception as e:
        print(e)
        print(f"Error connecting to the database")
        return False, False
    return con, cursor
  def randomNumber(be, en):
    return np.random.randint(be, en)
    def randomString(size, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))
    def updateStats(values, con, cursor, stats):
    """
    diseaseid, ncases, ndeaths, spreadprob 
    """
#     print('heyyy')
    diseaseid = values[1]
    spreadprob = random.random()
    new_values = [diseaseid, 1, values[2], spreadprob]
    
    query = f"""
        SELECT * from Stats
        WHERE diseaseid = {diseaseid};
            """
    try:
        cursor.execute(query)
#         print('first query')
    except Exception as e:
        return_val = str(e) + "Error in executing query for updating stats"
    data = cursor.fetchone()
#     print('frist query done')
    print(data)
    if not data:
        query = """
                INSERT INTO Stats
                VALUES (?, ?, ?, ?);
                """
        stats[diseaseid] = new_values[1:]
#         print('new query\n\n')
    else:
        query = f"""
                UPDATE Stats
                SET ncases = ncases + 1, ndeaths = ndeaths + {values[2]}
                WHERE diseaseid = {diseaseid};
                """
#         print('Old update\n')
        new_values = False
        stats.update({diseaseid: [stats[diseaseid][0]+1, stats[diseaseid][1] + values[2], spreadprob]})
#     print(f"Doing query {query} and values {new_values}")
    try:
        if new_values:
            cursor.execute(query, new_values)
        else:
            cursor.execute(query)
        con.commit()
    except Exception as e:
        return_val = str(e) + "Can't execute the query."
    return return_val

    def populateDB(values, type = None, stats = None):
    con, cursor = make_connection()
    return_val = "Done"
    
    if type == 'Hospital':
        query = f"""
                    INSERT INTO Hospital(id, name, location, userid)
                    VALUES(?, ?, ?, ?);
        """
    elif type == 'Diseases':
        query = f"""
                    INSERT INTO Diseases
                    VALUES(?, ?, ?, ?);
        """
    elif type == 'Drugs':
        query = f"""
                    INSERT INTO Drugs
                    VALUES(?, ?, ?, ?, ?);
        """
    elif type == 'Cases':
        query = f"""
                    INSERT INTO Cases(date, diseaseid, death, location)
                    VALUES(?, ?, ?, ?);
        """
        try:
            cursor.execute(query, values)
            con.commit()
            updateStats(values, con, cursor, stats)
        except:
            print("comeon")
            con.close()
    try:
        cursor.execute(query, values)
        con.commit()
    except Exception as e:
        return_val = str(e)
    finally:
        con.close()
    return return_val

    def generateLocation(lat, lon, be, en):
    hosp_loc = []
    for i in range(len(lat)):
        ranNum = randomNumber(be, en)
        for j in range(10):
            longi = lon + ranNum
            lat = lat + ranNum
            loc = str(lat) + ' ' + str(longi)
            hosp_loc.append(loc)


be = 10000
en = 99999

hosp_id = []
hosp_userid = []
hosp_name = []
hosp_loc = []

dummyLat = [30.553983, 26.619224, 22.463071, 25.712074, 23.957391, 21.116530, 17.927783, 13.145015, 26.146809]
dummyLong = [77.080078, 75.761719, 76.333008, 79.672852, 83.759766, 79.848633, 77.124023, 77.387695, 92.988281]

be = 0.0001, en = 1.6
# longbe = 0.0001, longen = 1.6

hosp_loc = generateLocations(dummyLat, dummyLong, be, en)

for i in range(500):
    ID = randomNumber(be, en)
    Userid = randomNumber(be, en)
    Name = randomString(randomNumber(6, 12))
    Location = random.uniform(0.01, 1.2)
    
    hosp_id.append(ID)
    hosp_loc.append(Location)
    
    a = populateDB(tuple([ID, Name, Location, Userid]), 'Hospital')

disease_id = []
disease_name = []
disease_mos = []
disease_sym = []

for i in range(50):
    id = randomNumber(be, en)
    name = randomString(randomNumber(6, 10))
    mos = random.choice(['air', 'water', 'food', 'animal'])
    sym = randomString(100)
    
    disease_id.append(id)
    disease_name.append(name)
    disease_mos.append(mos)
    disease_sym.append(sym)
    
    a = (populateDB(tuple([id, name, mos, sym]), 'Diseases'))

drug_id = []
drug_name = []
drug_req = []
drug_avail =[]
disease_drug = {}

for i in range(len(disease_id)):
    curDisease = disease_id[i]
    for j in range(randomNumber(1,4)):
        id = randomNumber(be, en)
        name = randomString(randomNumber(6, 12))
        req = randomNumber(6, 15)
        avail = randomNumber(1500, 3000)
        
        drug_id.append(id)
        drug_name.append(name)
        drug_req.append(req)
        drug_avail.append(avail)
        
        #storing drug ids corresponding to each disease
        if(curDisease in disease_drug):
            disease_drug[curDisease].append(id)
        else:
            disease_drug[curDisease] = [id]
            
        a = populateDB(tuple([id, name, req, avail, disease_id[i]]), 'Drugs')

!cp backup.db epidemic.db
!ls

# id- auto-incremental
case_date = []
case_diseaseid = []
case_death = []
case_location = []

#stats
stats = {}
#for each disease id in stats, we will store ncases, ndeaths and spreadprob

curDate = str(datetime.datetime.now().date())
for i in range(len(disease_id)):
    curDisease = disease_id[i]
    for j in range(randomNumber(20, 40)):
        date = str(randomNumber(2018, 2020)) + '-' + str(randomNumber(1, 12)) + '-' + str(randomNumber(1, 30))
        if(date < curDate):
            death = randomNumber(0, 2)
            location = random.choice(hosp_loc)

            case_date.append(date)
            case_diseaseid.append(curDisease)
            case_death.append(death)
            case_location.append(location)
            a = populateDB(tuple([date, curDisease, death, location]), 'Cases', stats)
