# Roblox-Font-Changer
I made this quickly so it's not the most refined but yeah it works so who cares!

# Installation
### Use Python 3.10 or higher (that's what I used)

To start, install the repository through .zip or clone it and then change your ```config.json``` to have the ```"robloxVersionsPath"``` field be your Roblox versions directory, also feel free to add to the blacklist in the JSON file if you want some fonts not to be changed!
Save that and then drop the font you would like to use in the ```font``` directory and rename it to ```font.ttf``` (make sure you have the file extension as .ttf)

Now go ahead and run the Python script (IMPORTANT: make sure you have Roblox closed otherwise it'll break it and you'll have to reinstall, trust me I accidentally did it to myself.)

## Running The Script & What to look out for
Your script should end with 
```
everything should be that font now!
```

however, make sure that before it says that you see something along the lines of this:
```
|-REMOVING zekton_rg.ttf FROM DIRECTORY C:\Users\le gale boiz\AppData\Local\Roblox\Versions\version-24872f7beace4d0a\content\fonts
|-> File deleted successfully
```

If all of that is working then go ahead and start up Roblox, now everything should be that font now!

If you run into any errors or bugs then it's probably something wrong with your JSON format so make sure to double-check that!
