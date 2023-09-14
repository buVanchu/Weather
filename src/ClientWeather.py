import DB
import utils
import openpyxl



if __name__ == "__main__":
    
    
    data = utils.read_json_from_file("/home/vanchu/Weather/conf/DBconfig.json")
    db_host = data["dbaddr"]
    db_name = data["dbname"]
    db_user = data["user"]
    db_password = data["password"]
    
    
    db = DB.PostgreSQLDatabase(db_host, db_name, db_user, db_password)
        
    db.connect()
    
    wb = openpyxl.load_workbook("/home/vanchu/Weather/tables/op.xlsx", data_only=True)
                
    sheet = wb.active
    
    
    
    start_row = 8

    step = 8

    for row_number, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if row_number >= start_row and (row_number - start_row) % step == 0:
            
            data = row[16]
            if (data != None):
                data = data.split(' ')[0]

                weather_power = row[28]

                if (weather_power):                    
                    query = utils.conc("insert into weather.power_prediction(power, data) values(",
                    weather_power,
                    ", '",
                    data,
                    "'",
                    ");")
                    
                    db.execute_query(query)
            
            else:
                a = 1
                        
    wb.close()
        
    