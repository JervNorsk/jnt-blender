import toml
import sys

def update_version_in_manifest(manifest_file, new_version):
    # Load file content as TOML
    with open(manifest_file, 'r') as file:
        manifest_data = toml.load(file)

    # Update the version
    if 'version' in manifest_data:
        manifest_data['version'] = new_version
    else:
        print("Version key not found in the manifest file.")
        return

    # Write the updated data back to the TOML file
    with open(manifest_file, 'w') as file:
        toml.dump(manifest_data, file)
    print(f"[{manifest_data['id']}] Version updated to {new_version}")

update_version_in_manifest(f'./modules/extensions/{sys.argv[1]}/blender_manifest.toml', sys.argv[2])