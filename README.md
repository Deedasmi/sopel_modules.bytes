# sopel_modules.bytes
Byte conversion module for Sopel

# Installation
1. ```git clone https://github.com/Deedasmi/sopel_modules.bytes.git```
 OR
 download from PyPi/pip

2. Place this folder in .sopel/modules/ (or wherever you store modules)

3. Modify ~/.sopel/default.cfg (or your sopel config file) and add the line:
```extra = ``` followed by the absolute path where you saved the module folder in step 2, including '/sopel_modules.bytes'

# Usage

```.bytes *num_bytes [Units]*```

Valid units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'], or use lower case b for bits instead of bytes.

See @examples in bytes.py

