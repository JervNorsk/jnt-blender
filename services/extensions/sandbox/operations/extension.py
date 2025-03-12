import bpy
from bpy.types import (
    Operator
)

from ..utils import extension

# -----------------------------------------------------------------------------
class EXTENSIONS_OT_repo_reload(Operator):
    # """Scan extension & legacy add-ons for changes to modules & meta-data (similar to restarting). """ \
    # """Any issues are reported as warnings"""
    bl_idname = "extensions.repo_reload"
    bl_label = "Reload Extension Repository"

    name = None

    def _exceptions_as_report(self, repo_name, ex):
        self.report({'WARNING'}, "{:s}: {:s}".format(repo_name, str(ex)))

    def execute(self, _context):
        extension.reload_repository()
        return {'FINISHED'}

# -----------------------------------------------------------------------------

classes = (
    EXTENSIONS_OT_repo_reload,
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
        if it.__name__ in bpy.types:
            try:
                print(f"# Unregistering {__name__}.{it.__name__}")
                bpy.utils.unregister_class(it)
            except Exception as e:
                print(f"# Unregistering {__name__}.{it.__name__} [FAILED]")
                print(e)
