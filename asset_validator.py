# import unreal
# from typing import Dict, List

# class AssetValidator:
#     def __init__(self, naming_conventions: Dict[str, str]):
#         self.naming_conventions = naming_conventions
#         self.asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

#     def validate_asset(self, asset: unreal.AssetData) -> bool:
#         asset_name = str(asset.asset_name)  # Conversion en chaîne de caractères

#         # Tentative d'obtenir la classe de l'asset via get_class() si asset_class est None
#         try:
#             asset_class = asset.get_class().get_name()
#         except AttributeError:
#             asset_class = None

#         # Recherche du préfixe de nommage correspondant
#         prefix = self.naming_conventions.get(asset_class)

#         # Validation du nom de l'asset
#         if prefix is not None:
#             return asset_name.startswith(prefix)
#         return True

#     def get_invalid_assets(self) -> List[unreal.AssetData]:
#         invalid_assets = []
#         for asset_class in self.naming_conventions.keys():
#             filter = unreal.ARFilter(class_names=[asset_class], recursive_paths=True)
#             assets = self.asset_registry.get_assets(filter)
#             for asset in assets:
#                 if not self.validate_asset(asset):
#                     invalid_assets.append(asset)
#         return invalid_assets

#     def get_asset_class(self, asset: unreal.AssetData) -> str:
#         try:
#             return asset.get_class().get_name()
#         except AttributeError:
#             return "None"

import unreal
from typing import Dict, List

class AssetValidator:
    def __init__(self, naming_conventions: Dict[str, str]):
        self.naming_conventions = naming_conventions
        self.asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

    def validate_asset(self, asset: unreal.AssetData) -> bool:
        asset_name = str(asset.asset_name)  # Conversion en chaîne de caractères

        # Tentative d'obtenir la classe de l'asset via get_class() si asset_class est None
        try:
            asset_class = asset.get_class().get_name()
        except AttributeError:
            asset_class = None

        # Recherche du préfixe de nommage correspondant
        prefix = self.naming_conventions.get(asset_class)

        # Validation du nom de l'asset
        if prefix is not None:
            is_valid = asset_name.startswith(prefix)
            return is_valid
        return True

    def get_invalid_assets(self) -> List[unreal.AssetData]:
        invalid_assets = []
        project_content_dir = unreal.Paths.project_content_dir()  # Obtient le répertoire de contenu du projet

        # Convertir en chemin complet
        project_content_dir = unreal.Paths.convert_relative_path_to_full(project_content_dir).replace("\\", "/")

        all_assets = self.asset_registry.get_all_assets()

        for asset in all_assets:
            asset_path = str(asset.package_path)
            if asset_path.startswith("/Game"):
                asset_class = asset.get_class().get_name()
                if asset_class in self.naming_conventions.keys():
                    if not self.validate_asset(asset):
                        invalid_assets.append(asset)

        unreal.log(f"Assets invalides trouvés: {len(invalid_assets)}")
        return invalid_assets

    def get_asset_class(self, asset: unreal.AssetData) -> str:
        try:
            return asset.get_class().get_name()
        except AttributeError:
            return "None"

