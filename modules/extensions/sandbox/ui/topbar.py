import bpy

class TOPBAR_MT_extension(bpy.types.Menu):
    bl_label = "Extension"

    def draw(self, context):
        layout = self.layout

        show_developer = context.preferences.view.show_developer_ui

        layout.operator("wm.url_open_preset", text="Manual", icon='URL').type = 'MANUAL'

classes = [
   TOPBAR_MT_extension
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()