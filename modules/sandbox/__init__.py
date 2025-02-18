from . import (
    ui
)

modules = [
    ui
]

def register():
    print("Registering JNT extension")

    for mod in modules:
        mod.register()

def unregister():
    print("Unregistering JNT extension")

    for mod in reversed(modules):
        mod.unregister()
