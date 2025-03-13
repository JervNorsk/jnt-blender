import bpy

# -----------------------------------------------------------------------------

def get_repository():
    module_name = __name__.split('.')[1]
    for (name, repository) in bpy.context.preferences.extensions.repos.items():
        if repository.module == module_name:
            return repository
    return None

def reload_repository():
    repository = get_repository()
    repository.enabled = False
    repository.enabled = True
