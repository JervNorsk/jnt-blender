def git_version():
    import subprocess

    # result = subprocess.run(['git', 'tag', '--sort=-v:refname'], capture_output=True, text=True)
    # result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True)
    result = subprocess.run('git describe --tags --abbrev=0'.split(" "), capture_output=True, text=True)

    version = result.stdout.strip().split('\n')[0].lstrip('v')

    return version
