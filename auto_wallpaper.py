import subprocess
import requests
import os
import random


# use the list of weather type define by wttr.in
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


#Script using Apple service
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""



def createImagesFolders(list_folders_name):
    """
    create the different folders for each weather, i.e. Sunny, Snow, etc.
    """
    username = os.getlogin()
    folder_path = "/Users/"+username+"/wallpaper/"
    for name in list_folders_name:
        os.mkdir(folder_path+name)
    return 0



def set_desktop_background(filename):
    """
    Run the Apple Service
    """
    subprocess.Popen(SCRIPT%filename, shell=True)
    return 0


def checkIfFoldersAreAlreadyHere(list_folders_name):
    """
    Check if the different weather folders are already created
    """
    username = os.getlogin()
    folder_path = "/Users/"+username+"/wallpaper/"
    for name in list_folders_name:
        if os.path.isdir(folder_path+name) == False:
            return False
    return True

def main():
    """
    main routine, check if weather folders exist, if no create them.
    Then, parse wttr.in/Location to obtain the weather.
    Select randomly an image in the weather folder associated to today weather
    """
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
