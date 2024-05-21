import psycopg2


connection = psycopg2.connect(database="db_vehicles", 
                              host="localhost", 
                              user="postgres", 
                              password="admin",
                              port="5432",
                              options='-c client_encoding=UTF8')
print(connection.info)
print(connection.status)

#Abrir cursos para operações do banco de dados
cur = connection.cursor()

cur.execute("""CREATE TABLE vehicles(
            vehicles_id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            vehicle_class VARCHAR(30),
            features VARCHAR (50),
            acquisition VARCHAR (50),
            price INT,
            storage_location VARCHAR (50),
            delivery_metho VARCHAR (50),
            modifications VARCHAR (50),
            resale_flag VARCHAR (50),
            resale_price INT,
            race_availability VARCHAR(50),
            top_speed_in_game INT,
            based_on VARCHAR(50),
            seats INT,
            weight_in_kg INT,
            drive_train VARCHAR(20),
            release_date DATE,
            release_dlc VARCHAR (20),
            top_speed_real VARCHAR(10),
            lap_time TIME,
            bulletproof VARCHAR(50),
            waepon1_resistence INT,
            waepon2_resistence INT,
            waepon3_resistence INT,
            waepon4_resistence INT,
            waepon5_resistence INT,
            speed FLOAT,
            acceleration FLOAT,
            braking FLOAT,
            handling FLOAT,
            overall FLOAT, 
            vehicle_url VARCHAR(100));
            """)
#Fazer alterações no banco de dados persistente
connection.commit()

#Fecha o cursor com a comunicação com banco de dados
cur.close()
connection.close()