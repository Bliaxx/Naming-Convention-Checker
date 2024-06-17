import unreal
import sys
import os

# Ajouter le répertoire des scripts au chemin de recherche des modules Python
script_dir = os.path.dirname(__file__)
sys.path.append(script_dir)

from configuration_loader import ConfigurationLoader
from asset_validator import AssetValidator
from asset_reporter import AssetReporter

class NamingConventionChecker:
    def __init__(self, config_path: str):
        self.config_loader = ConfigurationLoader(config_path)
        self.naming_conventions = self.config_loader.load_naming_conventions()
        unreal.log(f"Naming conventions loaded: {self.naming_conventions}")
        self.asset_validator = AssetValidator(self.naming_conventions)
        self.asset_reporter = AssetReporter()

    def run(self) -> None:
        invalid_assets = self.asset_validator.get_invalid_assets()
        self.asset_reporter.report(invalid_assets, self.asset_validator)

# Construire le chemin vers le fichier de configuration
config_path = os.path.join(unreal.Paths.project_dir(), "Config/naming_conventions.json")

# Exécuter la vérification
checker = NamingConventionChecker(config_path)
checker.run()
