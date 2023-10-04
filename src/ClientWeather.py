import DB
import utils
import openpyxl

if __name__ == "__main__":
    data = utils.read_json_from_file("/home/server/priority2030_servers/Weather/conf/config.json")
    db_host = data["db"]["dbaddr"]
    db_name = data["db"]["dbname"]
    db_user = data["db"]["user"]
    db_password = data["db"]["password"]
    
    db = DB.PostgreSQLDatabase(db_host, db_name, db_user, db_password)
        
    db.connect()
    
    wb = openpyxl.load_workbook(data["predict"]["file"], data_only=True)
                
    sheet = wb.active
    
    start_row = 8

    step = 8
    power_pre
    for row_number, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if row_number >= start_row and (row_number - start_row) % step == 0:
            
            data = row[16]
            if (data != None):
                data = data.split(' ')[0]

                weather_power = row[28]

                if (weather_power):                    
                    query = utils.conc("SELECT update_or_insert_data('",
                    data,
                    "'::date, ",
                    weather_power,
                    "::double precision",
                    ");")
                    
                    db.execute_query(query)
            
            else:
                a = 1
                        
    wb.close()
        
    