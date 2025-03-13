import bpy
from bpy.types import (
    Operator
)
from bl_ui.space_topbar import (
    TOPBAR_MT_editor_menus
)

from ..utils import extension

# -----------------------------------------------------------------------------

class TOPBAR_MT_editor_menus(TOPBAR_MT_editor_menus):

    def draw(self, context):
        layout = self.layout
        super().draw(context)
        layout.menu("TOPBAR_MT_extension_JNT")


class TOPBAR_MT_extension_JNT(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_extension_JNT"
    bl_label = "JNT"

    def draw(self, context):
        layout = self.layout

        op = layout.operator("extensions.repo_reload", text="Reload", icon='FILE_REFRESH')
        print(op)
        print(hasattr(op, "name"))
        # op.name = __name__.split('.')[1]

# -----------------------------------------------------------------------------

classes = (
    TOPBAR_MT_editor_menus,
    TOPBAR_MT_extension_JNT,
)

def register():
    for it in classes:
        try:
            print(f"# Registering {__name__}.{it.__name__}")
            bpy.utils.register_class(it)
        except Exception as e:
            print(f"# Registering {__name__}.{it.__name__} [FAILED]")
            print(e)

def unregister():
    for it in classes:
        try:
            print(f"# Unregistering {__name__}.{it.__name__}")
            bpy.utils.unregister_class(it)
        except Exception as e:
            print(f"# Unregistering {__name__}.{it.__name__} [FAILED]")
            print(e)
