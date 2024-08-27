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
    
def get_roblox_directory(path):
    for v in os.listdir(path):
        if os.path.exists(path+"\\"+v+"\\content\\fonts\\"):
            if os.path.exists(path+"\\"+v+"\\RobloxPlayer.exe") or os.path.exists(path+"\\"+v+"\\RobloxPlayerBeta.exe"):
                return path+"\\"+v

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
        
        print("changing cursor...")
        time.sleep(1)
        
        try:
            if os.path.exists("./cursor/cursor.png"):
                print("USING CURSOR: ./cursor/cursor.png")
                
                print("ArrowCursor.png")
                delete_file(self.robloxVersionPath+"/content/textures/Cursors/KeyboardMouse/ArrowCursor.png")
                print("ArrowFarCursor.png")
                delete_file(self.robloxVersionPath+"/content/textures/Cursors/KeyboardMouse/ArrowFarCursor.png")
                time.sleep(1)
                copy_file("./cursor/cursor.png", self.robloxVersionPath+"/content/textures/Cursors/KeyboardMouse/ArrowCursor.png")
                copy_file("./cursor/cursor.png", self.robloxVersionPath+"/content/textures/Cursors/KeyboardMouse/ArrowFarCursor.png")
                print("REPLACED CURSORS WITH cursor.png")
                
                print("changes complete!")
                time.sleep(2)
            
        except Exception as e:
            print(f"An Error Occured when changing cursor: {e}")
           
app = main()