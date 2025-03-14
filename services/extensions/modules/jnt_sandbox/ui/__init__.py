import bpy
from . import (
    topbar
)

# -----------------------------------------------------------------------------

modules = (
    topbar,
)

def register():
    for it in modules:
        if hasattr(it, 'register'):
            try:
                print(f"# Registering {it.__name__}")
                it.register()
            except Exception as e:
                print(f"# Registering {it.__name__} [FAILED]")
                print(e)

def unregister():
    for it in modules:
        if hasattr(it, 'unregister'):
            try:
                print(f"# Unregistering {it.__name__}")
                it.unregister()
            except Exception as e:
                print(f"# Unregistering {it.__name__} [FAILED]")
                print(e)
