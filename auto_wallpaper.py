import subprocess
import requests
import os
import random



WWO_CODE = {
    "Clear" : "Sunny",
    "Sunny" : "Sunny",
    "PartlyCloudy": "PartlyCloudy",
    "Cloudy" : "Cloudy",
    "VeryCloudy": "Cloudy",
    "Fog": "Fog",
    "LightShowers": "Rain",
    "LightSleetShowers": "Rain",
    "LightSleet": "Rain",
    "ThunderyShowers": "Thunder",
    "LightSnow": "Snow",
    "HeavySnow": "Snow",
    "Fog": "Fog",
    "LightRain": "Rain",
    "HeavyShowers": "Rain",
    "LightSnowShowers": "Snow",
    "HeavySnowShowers": "Snow",
    "HeavyRain": "Rain",
    "ThunderyHeavyRain": "Thunder",
    "ThunderySnowShowers": "Thunder",
}

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""


def createImagesFolders(list_folders_name):
    username = os.getlogin()
    folder_path = "/Users/"+username+"/wallpaper/"
    for name in list_folders_name:
        os.mkdir(folder_path+name)
    return 0



def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)
    return 0


def checkIfFoldersAreAlreadyHere(list_folders_name):
    username = os.getlogin()
    folder_path = "/Users/"+username+"/wallpaper/"
    for name in list_folders_name:
        if os.path.isdir(folder_path+name) == False:
            return False
    return True

def main():
    list_folders_name = ["Sunny", "PartlyCloudy", "Cloudy", "Rain", "Fog", "Snow", "Thunder"]
    if checkIfFoldersAreAlreadyHere(list_folders_name) == False:
        createImagesFolders(list_folders_name)

    location = "Evry"
    r = requests.get("https://wttr.in/"+location+"?format=%C")
    text_response = r.text.replace(" ","")
    weather = WWO_CODE[text_response]
    username = os.getlogin()
    folder_path = "/Users/"+username+"/wallpaper/"
    folder_images = folder_path+weather+"/"
    list_images = os.listdir(folder_images)
    if list_images:
        selected_image = list_images[random.randint(0,len(list_images)-1)]
        set_desktop_background(folder_images + selected_image)
    else:
        print("Add images to the folder")
    return 0

if __name__=="__main__":
    main()
