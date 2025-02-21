from . import (
    ui
)

modules = [
    ui
]

def register():
    print("Registering JNT Sandbox extension")

    for mod in modules:
        mod.register()

def unregister():
    print("Unregistering JNT Sandbox extension")

    for mod in reversed(modules):
        mod.unregister()
