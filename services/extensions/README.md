## Build

1. Move on the root of the project
2. Ensure that all work is committed
3. Digit these commands:

   ```shell
   mise r blender:extensions version <extension> v<version>

   mise r blender:extensions publish
   ```

## Installation

1. Open Blender and go to Edit > Preferences > Extensions:
2. Open the right top corner icon to expand available repositories:
3. Add a new element and fill fields with these elements:
   - URL: https://raw.githubusercontent.com/JervNorsk/jnt-blender/refs/heads/release/extensions/index.json
   - Name: JNT
   - Module: jnt
4. Enable repository
5. Search available extensions prefixed with JNT
6. Enable the extension desired:
   - JNT Sandbox
