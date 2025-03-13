# from . import ()

modules = []

def register():
    # print("--------------------------------------------------------------------------------")
    # print("Registering JNT ComfyUI extension")
    # print("--------------------------------------------------------------------------------")

    for mod in modules:
        mod.register()

def unregister():
    # print("--------------------------------------------------------------------------------")
    # print("Unregistering JNT ComfyUI extension")
    # print("--------------------------------------------------------------------------------")

    for mod in reversed(modules):
        mod.unregister()
