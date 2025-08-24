from ..libs.jnt import (
    JntBlenderClass
)

import bpy

# -----------------------------------------------------------------------------
class JNT_CL_repo_reload(JntBlenderClass):
    """
        JNT class that manage a set of Blender class
    """
    def get_classes(self):
        return [
            JNT_OP_repo_reload
        ]

    def get_menus(self) -> list[tuple[type[object], str, object]]:
        return [
            (JNT_OP_repo_reload, "TOPBAR_MT_extension_JNT", JNT_OP_repo_reload.draw_menu)
        ]

class JNT_OP_repo_reload(bpy.types.Operator):
    """
        Scan extension & legacy add-ons for changes to modules & meta-data (similar to restarting).

        Any issues are reported as warnings
    """
    bl_idname = "jnt.repo_reload"
    bl_label = "Reload JNT Repository"

    name = None

    def _exceptions_as_report(self, repo_name, ex):
        self.report({'WARNING'}, "{:s}: {:s}".format(repo_name, str(ex)))

    def execute(self, _context):
        reload_repository()
        return {'FINISHED'}

    @staticmethod
    def draw_menu(self, context):
        layout = self.layout

        op = layout.operator("jnt.repo_reload", text="Reload", icon='FILE_REFRESH')
        # print(op)
        # print(self.__module__)
        # print(hasattr(op, "name"))
        # op.name = __name__.split('.')[1]

# -----------------------------------------------------------------------------
def get_repository():
    module_name = __name__.split('.')[1]
    for (name, repository) in bpy.context.preferences.extensions.repos.items():
        if repository.module == module_name:
            return repository
    return None

def reload_repository():
    repository = get_repository()
    repository.enabled = False
    repository.enabled = True