import bpy

# -----------------------------------------------------------------------------

from bl_ui import (
    node_add_menu
)
from bl_ui.node_add_menu_geometry import (
    NODE_MT_geometry_node_GEO_ATTRIBUTE
)

class NODE_MT_geometry_node_GEO_ATTRIBUTE(NODE_MT_geometry_node_GEO_ATTRIBUTE):

    def draw(self, context):
        super().draw(context)

        layout = self.layout
        layout.separator()
        node_add_menu.add_node_type(layout, "GeometryNodeSetTags")

# -----------------------------------------------------------------------------

from bpy.types import (
    GeometryNode
)
from mathutils import (
    Color
)

class GeometryNodeSetTags(GeometryNode):
    bl_idname = "GeometryNodeSetTags"
    bl_label = "Set Tags"

    color = Color((0.0, 0.0, 1.0))



# -----------------------------------------------------------------------------

classes = (
    NODE_MT_geometry_node_GEO_ATTRIBUTE,
    GeometryNodeSetTags,
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

