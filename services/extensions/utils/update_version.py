import os
import sys
import toml

def get_toml_file_data(module_path, file_name):
    # Check if file to update exists
    file_path = os.path.join(module_path, file_name)
    if not os.path.exists(file_path):
        # print(f"File {file_name} not exists!")
        return None

    # Load file content as TOML
    with open(file_path, 'r') as file:
        file_data = toml.load(file)

    return file_data

def set_toml_file_data(module_path, file_name, file_data):

    # Check if file to update exists
    file_path = os.path.join(module_path, file_name)
    if not os.path.exists(file_path):
        # print(f"File {file_name} not exists!")
        return

    # Write the updated data back to the TOML file
    with open(file_path, 'w') as file:
        toml.dump(file_data, file)


def update_version_in_toml_file(module_path, module_name, file_name, field_path=":version"):

    # Get file data from module
    file_data = get_toml_file_data(module_path, file_name)

    if file_data is None:
        return

    # Get the version from git tags
    from get_version import get_git_tag_version
    module_version = get_git_tag_version(module_name)

    # Update the version in TOML data
    file_data_keys = field_path.split(':')
    file_data_target = file_data
    for file_data_key in file_data_keys[1:-1]:
        if file_data_key not in file_data_target:
            print(f"Table '{file_data_key}' not found in {file_name}")
            return
        file_data_target = file_data_target[file_data_key]
    file_data_target[file_data_keys[-1]] = module_version

    # Set the TOML data updated
    set_toml_file_data(module_path, file_name, file_data)

    print(f"[{module_name}] Version updated to {module_version} at {file_name}")

if __name__ == "__main__":
    update_version_in_toml_file(sys.argv[1], sys.argv[2], 'pyproject.toml', ':project:version')
    update_version_in_toml_file(sys.argv[1], sys.argv[2], 'blender_manifest.toml', ":version")