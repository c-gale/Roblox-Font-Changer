import lib.jsonReader as jR
import os, time, shutil

os.chdir(str(__file__).rstrip(str(__file__)[-(len(str(__name__))-1):]))

def get_file_extensions(directory):
    extensions = set()
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            _, extension = os.path.splitext(filename)
            extensions.add(extension)
    return extensions

def has_font_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower() in ['.ttf', '.otf']

def is_file_blacklisted(file_path, blacklist):
    return os.path.basename(file_path) in blacklist
    
def get_roblox_directory(path):
    for v in os.listdir(path):
        if os.path.exists(path+"\\"+v+"\\content\\fonts\\"):
            if os.path.exists(path+"\\"+v+"\\RobloxPlayer.exe") or os.path.exists(path+"\\"+v+"\\RobloxPlayerBeta.exe"):
                return path+"\\"+v
            

def hasFileInDirectory(directory):
    for t in os.listdir(directory):
        if has_font_extension(t):
            return True
    return False

def copy_file(source_file, destination_directory):
    shutil.copy(source_file, destination_directory)

def rename_file(old_file_path, new_file_name):
    directory = os.path.dirname(old_file_path)
    new_file_path = os.path.join(directory, new_file_name)
    os.rename(old_file_path, new_file_path)

def delete_file(file_path):
    try:
        os.remove(file_path)
        print("|-> File deleted successfully")
    except OSError as e:
        print(f"Error: {file_path} : {e.strerror}")

class main():
    def __init__(self) -> None:
        self.config = jR.readJsonFile("./config.json")
        self.robloxVersionPath = get_roblox_directory(self.config["robloxVersionsPath"])
        print(f"GOT VERSION: ({os.path.basename(self.robloxVersionPath)})")
        
        print("INITIALIZING FONTS...")
        time.sleep(1)
        
        self.fonts = {}
        
        self.getAllFontsInRBLX(self.robloxVersionPath + r"\content\fonts")

        if hasFileInDirectory("./font/"):
            print("USING FONT PATH "+str(__file__).rstrip(str(__file__)[-(len(str(__name__))-1):])+r"font\font.ttf")
            self.replacementFont = str(__file__).rstrip(str(__file__)[-(len(str(__name__))-1):])+r"font\font.ttf"
            
        print("REMOVING ALL OLD FONTS")
        for t in self.fonts:
            print("|-REMOVING" + self.fonts[t] + "FROM DIRECTORY" + self.robloxVersionPath+ r"\content\fonts")
            if os.path.exists(self.robloxVersionPath + "\\content\\fonts\\" + self.fonts[t]):
                delete_file(self.robloxVersionPath+ '\\content\\fonts\\' + self.fonts[t])

        for t in self.fonts:
            copy_file(self.replacementFont, self.robloxVersionPath+"/content/fonts/")
            if os.path.exists(self.robloxVersionPath+"/content/fonts/font.ttf"):
                newPath = self.robloxVersionPath+"/content/fonts/font.ttf"
                rename_file(newPath, self.fonts[t])
            else:
                print("WAHT DA HELL WEN WRONG?")
                return
            
        print("everything should be that font now!")

    def getAllFontsInRBLX(self, path):
        if os.path.exists(path):
            for index, t in enumerate(os.listdir(path)):
                print(t)
                if has_font_extension(t):
                    if not is_file_blacklisted(t, self.config["fontBlacklist"]):
                        self.fonts[index] = t
                        print(path+t)
           
app = main()