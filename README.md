# texture_path_generator
This script will make it easy to generate texture file paths for your characters in Genshin Impact.


## How to use it?

1. Download the [textures.py](textures.py) file

2. Place it in any place convenient for you (initially it is provided that it will be in the same folder as your textures, but you can specify the path to the folder manually)

3. Run the "textures.py" file and it will generate a text file "result.txt" for you which will contain all the paths to your texture files.


   - Note: You must have python installed for the script to work.


## Variables
Variables that may be useful to you

- resFile — output file name
- folder — the path to the folder with textures (if the script is in the same folder, you can leave it empty)
- whiteListFormats — list of formats to display (if the file path contains an element of this array, it will be added to the results)
- blackListWords — list of keywords to ignore (if the file path contains an element of this array, it will be skipped)
