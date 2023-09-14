import json

def read_json_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Ошибка чтения JSON из файла: {e}")
        return None
    
def conc(*args):
    result = "".join(map(str, args))
    return result