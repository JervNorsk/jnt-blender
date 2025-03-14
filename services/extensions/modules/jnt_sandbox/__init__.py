import importlib

# -----------------------------------------------------------------------------
from . import (
    operations,
    nodes,
    ui,
    assets,
)
from .utils import extension

modules = (
    operations,
    nodes,
    ui,
    assets,
)

def register():
    print("--------------------------------------------------------------------------------")
    print("Registering JNT Sandbox extension")
    print("--------------------------------------------------------------------------------")

    for it in modules:
        if hasattr(it, 'register'):
            try:
                print(f"# Registering {it.__name__}")
                it.register()
            except Exception as e:
                print(f"# Registering {it.__name__} [FAILED]")
                print(e)

    print()

def unregister():
    print("--------------------------------------------------------------------------------")
    print("Unregistering JNT Sandbox extension")
    print("--------------------------------------------------------------------------------")

    for it in modules:
        if hasattr(it, 'unregister'):
            try:
                print(f"# Unregistering {it.__name__}")
                it.unregister()
            except Exception as e:
                print(f"# Unregistering {it.__name__} [FAILED]")
                print(e)

    print()

def reload():
    extension.reload_repository()