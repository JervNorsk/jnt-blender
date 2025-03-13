import toml
import sys

from get_version import (
    git_version
)

def update_version(manifest_file, new_version):
    # Load file content as TOML
    with open(manifest_file, 'r') as file:
        manifest_data = toml.load(file)

    # Update the version
    manifest_data['version'] = new_version

    # Write the updated data back to the TOML file
    with open(manifest_file, 'w') as file:
        toml.dump(manifest_data, file)
    print(f"[{manifest_data['id']}] Version updated to {new_version}")

# update_version(f'{sys.argv[1]}', sys.argv[2])
update_version(f'{sys.argv[1]}', git_version())