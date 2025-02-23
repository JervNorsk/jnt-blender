import sys
import os
import importlib
import toml

import bpy

def get_extension_id():
    current_module = __name__
    return current_module.rsplit('.', 1)[0] if '.' in current_module else None

def get_extension_path():
    extension_module = get_extension_id()

    if extension_module and extension_module in sys.modules:
        path = getattr(sys.modules[extension_module], "__file__", None)
        # print(f"Extension path at {path}")
        return path
    else:
        return None

def validate_extension_asset_library_is_present():
    asset_library = find_extension_asset_library();
    if asset_library is None:
        print("# Extension AssetLibrary not present!")
    else:
        print("# Extension AssetLibrary present!")

def find_extension_asset_library():
    for it in bpy_asset_libraries:
        if it.path in jnt_extension_path:
            return it
    return None

# -----------------------------------------------------------------------------

bpy_asset_libraries = bpy.context.preferences.filepaths.asset_libraries
jnt_extension_id = get_extension_id()
jnt_extension_path = get_extension_path()

def register():
    validate_extension_asset_library_is_present()

    jnt_extension_asset_library = find_extension_asset_library()
    if jnt_extension_asset_library is None:
        jnt_extension_asset_library = bpy_asset_libraries.new(name="JNT Sandbox")
        jnt_extension_asset_library.path = jnt_extension_path
        jnt_extension_asset_library.import_method = 'LINK'
        # bpy_asset_libraries.add(jnt_asset_library)

    validate_extension_asset_library_is_present()
    # checkout()

def unregister():
    validate_extension_asset_library_is_present()

    jnt_asset_library = find_extension_asset_library()
    if jnt_asset_library is not None:
        bpy_asset_libraries.remove(jnt_asset_library)
        bpy.ops.wm.save_userpref()

    validate_extension_asset_library_is_present()

# def checkout():
#     name = jnt_extension_id.rsplit('.', 1)[-1]
#     for addon in bpy.context.preferences.addons:
#         if f'.{name}' in addon.module:
#             addon_module = importlib.import_module('bl_ext.jnt_develop.sandbox')
#             print(addon)
#             print(addon_module)
#             print()
#
#             addon_path = addon_module.__path__[0]
#             manifest_path = os.path.join(addon_path, "blender_manifest.toml")
#
#             # Verifica se il file esiste
#             if os.path.exists(manifest_path):
#                 # Carica il file TOML
#                 with open(manifest_path, 'r') as file:
#                     manifest_data = toml.load(file)
#
#                 # Estrai il nome dell'addon
#                 addon_name = manifest_data.get("blender", {}).get("name", "Nome non trovato")
#                 print(f"Nome dell'addon estratto dal manifest: {addon_name}")
#             else:
#                 print(f"Il file '{manifest_path}' non esiste.")
