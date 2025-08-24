from ..libs.jnt import (
    JntBlenderClass
)
import bpy
import bl_ui

# -----------------------------------------------------------------------------
class TOPBAR_CL_extension_JNT(JntBlenderClass):

    def get_classes(self) -> list[type[object]]:
        return [
            TOPBAR_MT_extension_JNT
        ]

    def get_menus(self) -> list[tuple[type[object], str, object]]:
        return [
            (TOPBAR_MT_extension_JNT, "TOPBAR_MT_editor_menus", TOPBAR_MT_extension_JNT.draw_parent)
        ]

# -----------------------------------------------------------------------------
class TOPBAR_MT_extension_JNT(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_extension_JNT"
    bl_label = "JNT"

    @staticmethod
    def draw_parent(self, context):
        self.layout.menu(TOPBAR_MT_extension_JNT.bl_idname)

    def draw(self, context):
        pass
