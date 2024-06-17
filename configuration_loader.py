import json
import unreal
from typing import Dict

class ConfigurationLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def load_naming_conventions(self) -> Dict[str, str]:
        try:
            with open(self.config_path, 'r') as file:
                naming_conventions = json.load(file)
            return naming_conventions
        except (IOError, json.JSONDecodeError) as e:
            unreal.log_error(f"Erreur lors du chargement des conventions de nommage: {e}")
            return {}
