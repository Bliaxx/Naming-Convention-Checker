import unreal
from typing import List

class AssetReporter:
    def report(self, invalid_assets: List[unreal.AssetData], validator) -> None:
        if invalid_assets:
            unreal.log_warning("Assets non conformes trouvés:")
            for asset in invalid_assets:
                asset_class = validator.get_asset_class(asset)
                unreal.log_warning(f"{asset.asset_name} ({asset_class})")
        else:
            unreal.log("Tous les assets sont conformes aux conventions de nommage.")
