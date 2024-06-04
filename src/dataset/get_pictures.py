import os
import shutil
from platform import platform as pf
is_win = pf().startswith('Win')

PATH = "C:\\home_screen\\programming\\algoritm and data structure\\Dataset" if is_win else "/Users/maus/Downloads/images"
cwd = os.getcwd()

class Dataset_operations:
    @staticmethod
    def get_images(PATH: str=PATH,
                   start: int=0,
                   end: int=0,
                   for_using: str="train",
                   all: bool=False,
                   similar: bool=False) -> None:
        
        DESTINATION_PATH = f"{cwd}\\dataset\\{for_using}\\other_artist" if is_win else f"{cwd}/dataset/{for_using}/other_artist"
        for path in [PATH, DESTINATION_PATH]:
            if not os.path.isdir(path):
                    raise NameError("No such directory " + path)

        if similar:
            names_folder = [
                "Raphael",
                "Michelangelo",
                "Titian",
                "Sandro_Botticelli",
                "Jan_van_Eyck"
            ]
        else:
            names_folder = os.listdir(PATH)
        k = 0
        for folder in names_folder:
            if all:
                k += Dataset_operations.get_pictures_folder(PATH, all=True, folder=folder, for_using=for_using)
            else:
                k += Dataset_operations.get_pictures_folder(PATH, start=start, end=end, folder=folder, for_using=for_using)

        print(f"скопировано {k} картинок в {for_using}")
        
    @staticmethod
    def get_mona_original(PATH: str=PATH,
                          resolution: str = "low") -> None:
        shutil.copy(f"{PATH}\\Mona\\{resolution}_resolution\\mona_original.png" if is_win else f"{PATH}/Mona/{resolution}_resolution/mona_original.png",
                    f"{cwd}\\dataset\\train\\artist" if is_win else f"{cwd}/dataset/train/artist"
                    )
        
    @staticmethod
    def get_mona_younger(PATH: str=PATH,
                          resolution: str = "low") -> None:
        
        for mona_name in os.listdir(f"{PATH}\\Mona\\{resolution}_resolution" if is_win else f"{PATH}/Mona/{resolution}_resolution"):
            if "younger" in mona_name:
                shutil.copy(f"{PATH}\\Mona\\{resolution}_resolution\\{mona_name}" if is_win else f"{PATH}/Mona/{resolution}_resolution/{mona_name}",
                            f"{cwd}\\dataset\\test\\artist" if is_win else f"{cwd}/dataset/test/artist"
                            )
                
    @staticmethod
    def get_mona_replica(PATH: str=PATH,
                          resolution: str = "low") -> None:
        
        for mona_name in os.listdir(f"{PATH}\\Mona\\{resolution}_resolution" if is_win else f"{PATH}/Mona/{resolution}_resolution"):
            if "replica" in mona_name:
                shutil.copy(f"{PATH}\\Mona\\{resolution}_resolution\\{mona_name}" if is_win else f"{PATH}/Mona/{resolution}_resolution/{mona_name}",
                            f"{cwd}\\dataset\\test\\artist" if is_win else f"{cwd}/dataset/test/artist"
                            )
        
        
    @staticmethod
    def get_work_dataset(PATH: str=PATH,
                         percentage_train: int=80) -> None:
        if not os.path.isdir(PATH):
            raise NameError("No such directory " + PATH)
        
        names_folder = [
            "Raphael",
            "Michelangelo",
            "Titian",
            "Sandro_Botticelli",
            "Jan_van_Eyck"
        ]
        k_train = 0
        k_test =0
        for folder in names_folder:
            files = [file for root, dirs, files in os.walk(os.path.join(PATH, folder)) for file in files]
            for_using = "train"
            end_for_train = round(len(files) * percentage_train / 100)
            k_train += Dataset_operations.get_pictures_folder(PATH, start=0, end=end_for_train, folder=folder, for_using=for_using)
            for_using = "test"
            k_test += Dataset_operations.get_pictures_folder(PATH, start=end_for_train, end=len(files), 
                                                        folder=folder, for_using=for_using)

        print(f"скопировано {k_train} картинок в train\nскопировано {k_test} картинок в test")  
        
    @staticmethod
    def get_work_train_dataset(PATH: str=PATH,
                               percentage_train: int=50) -> None:
        if not os.path.isdir(PATH):
            raise NameError("No such directory " + PATH)
        
        
        names_folder = [
            "Raphael",
            "Michelangelo",
            "Titian",
            "Sandro_Botticelli",
            "Jan_van_Eyck"
        ]
        k_train = 0
        for folder in names_folder:
            files = [file for root, dirs, files in os.walk(os.path.join(f"{PATH}\\Images" if is_win else f"{PATH}/Images", folder)) for file in files]
            end_for_train = round(len(files) * percentage_train / 100)
            k_train += Dataset_operations.get_pictures_folder(PATH, start=0, end=end_for_train, folder=folder, for_using="train")
            
        print(f"скопировано {k_train} картинок в train")
            
    
    @staticmethod
    def get_pictures_folder(PATH: str=PATH,
                            start: int=0,
                            end: int=0,
                            all: bool=False,
                            folder: str = "",
                            for_using: str="") -> int:
        
        
        DESTINATION_PATH = f"{cwd}\\dataset\\{for_using}\\other_artist" if is_win else f"{cwd}/dataset/{for_using}/other_artist"
        k=0
        for subdir, dirs, files in os.walk(os.path.join(f"{PATH}\\Images" if is_win else f"{PATH}/Images", folder)):
                if all:
                    for file in files:
                        file_path = os.path.join(subdir, file)

                        shutil.copy(file_path, DESTINATION_PATH)
                        k += 1
                else:
                    for file in files[start:end]:
                        file_path = os.path.join(subdir, file)

                        shutil.copy(file_path, DESTINATION_PATH)
                        k += 1
        return k
    
    @staticmethod
    def clear() -> None:   
        for role in ["train", "test"]:
            for artist in ["artist", "other_artist"]:
                path = f"{cwd}\\dataset\\{role}\\{artist}" if is_win else f"{cwd}/dataset/{role}/{artist}" 
                shutil.rmtree(path)
                os.mkdir(path)
                
    
    
                                