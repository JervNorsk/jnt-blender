from . import (
    ui,
    asset
)

modules = [
    ui,
    asset
]

def register():
    print("--------------------------------------------------------------------------------")
    print("Registering JNT Sandbox extension")
    print("--------------------------------------------------------------------------------")

    for mod in modules:
        if hasattr(mod, 'register'):
            mod.register()

    print()

def unregister():
    print("--------------------------------------------------------------------------------")
    print("Unregistering JNT Sandbox extension")
    print("--------------------------------------------------------------------------------")

    for mod in reversed(modules):
        if hasattr(mod, 'unregister'):
            mod.unregister()

    print()
