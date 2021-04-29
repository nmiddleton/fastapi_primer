import json
from pathlib import Path
def get():
    file = Path('config/settings.json').absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
        raise Exception("settings.json file not found, you cannot continue, please see settings_template.json")

    with open('config/settings.json') as fin:
        settings = json.load(fin)
        return settings.get('api_key')
