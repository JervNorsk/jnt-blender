import bpy

modules = []

def register():
    for module in modules:
        module.register()
    pass

def unregister():
    for module in reversed(modules):
        module.unregister()
    pass
