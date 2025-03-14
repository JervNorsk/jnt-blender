def get_git_tag_version(module_name):
    import subprocess

    result = subprocess.run(["git", "tag", "--sort=-v:refname"], capture_output=True, text=True)
    # result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True)
    # result = subprocess.run("git describe --tags --abbrev=0".split(" "), capture_output=True, text=True)

    versions = result.stdout.strip().split("\n")

    version = next((v for v in versions if f"extensions/{module_name}/" in v), None)

    if version:
        version = version.replace(f"extensions/{module_name}/", "")
        if version.startswith("v"):
            version = version.replace(f"v", "")

    return version
