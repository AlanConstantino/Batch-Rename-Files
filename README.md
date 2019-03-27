##### Note: This was written using Python 3.6.7

---

### What does this script do?
This script renames all of the files within a directory to a single name with an appended number at the end of the name which increases (i.e. file0.txt, file1.txt, file2.txt, etc).

### How to use?
```python BatchRenameFiles.py path filename extension```
- ```path``` [mandatory] -- specify a path to a directory

- ```filename``` [mandatory] -- specify a new filename or number '0' to indicate that you don't want to change the filename

- ```extension``` [optional] -- specify file extension type

### Examples
#### Changing both the filename and the file extension

```python BatchRenameFiles.py C:/Users/MyPC/Desktop/Folder IMG_A_ jpg```

-  The line above will rename files from the path ```C:/Users/MyPC/Desktop/Folder``` to ```IMG_A_X``` where X is a number that increases so as to not have two files with the same name. The line above will also change the extension of each file to ```jpg```
  
#### Changing only the filename
```python BatchRenameFiles.py C:/Users/MyPC/Desktop/Folder MyDocument```
  
-  The line above will change all of the files from the path ```C:/Users/MyPC/Desktop/Folder``` to ```MyDocumentX``` where X is a number that increases so as to not have two files with the same name.

#### Changing only the file extension

```python BatchRenameFiles.py C:/Users/MyPC/Desktop/Folder 0 txt```

-  By specifying the ```0``` as the ```filename``` and ```txt``` as the ```extension```, the line above will keep the current filename and only change the extension to ```txt```

### Running on MacOS/Linux
- To run on macOS or Linux you'll have the change 6 lines of code (lines 9, 10, 17, 18, 25, and 26).

#### Change the lines to the following

- Line 9 to ```src = path + "/" + filename```

- Line 10 to ```dest = path + "/" + newName + str(count) + oldExtension[1]```

- Line 17 to ```src = path + "/" + filename```

- Line 18 to ```dest = path + "/" + newName + str(count) + "." + newExtension```

- Line 25 to ```src = path + "/" + filename```

- Line 26 to ```dest = path + "/" + oldName[0] + "." + newExtension```
  
---
