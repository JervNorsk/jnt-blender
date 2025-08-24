from .libs.jnt import (
    JntBlenderAddon
)
from . import (
    app,
    assets,
    ops
)

# -----------------------------------------------------------------------------
bpy_addon = JntBlenderAddon(
    [
        app,
        assets,
        ops
    ]
)

# -----------------------------------------------------------------------------
def register():
    """This method is called by Blender on Addon registration"""
    bpy_addon.register()

def unregister():
    """This method is called by Blender on Addon un-registration"""
    bpy_addon.unregister()

def reload():
    """This method is called by Blender on Addon reloading"""
    bpy_addon.reload()