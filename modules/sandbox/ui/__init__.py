from . import (
    topbar
)

modules = [
    topbar
]

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in reversed(modules):
        mod.unregister()
