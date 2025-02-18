# from . import ()

modules = []

def register():
    print("Registering JNT ComfyUI extension")

    for mod in modules:
        mod.register()

def unregister():
    print("Unregistering JNT ComfyUI extension")

    for mod in reversed(modules):
        mod.unregister()
