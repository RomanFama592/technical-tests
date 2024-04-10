import json

def json_to_dict(file) -> dict | None:
    try:
        jsonfile = open(file)
        dict_json = json.load(jsonfile)
        jsonfile.close()
        return dict_json
    except:
        return None
