def git_version():
    import subprocess

    result = subprocess.run(['git', 'tag', '--sort=-v:refname'], capture_output=True, text=True)

    version = result.stdout.strip().split('\n')[0].lstrip('v')

    return version
