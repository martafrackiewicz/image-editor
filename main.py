import os
from PIL import Image

OPTION_DECREASE = "-"
OPTION_INCREASE = "+"


class EmptyPath(OSError):
    def __init__(self, *args, **kwargs):
        OSError.__init__(self, *args, **kwargs)


def get_dir_path():
    message_dir_path = "Podaj ścieżkę dostępu do folderu: "
    dir_path = input(message_dir_path)
    if dir_path == "":
        raise EmptyPath("Ścieżka nie może być pusta.")
    return dir_path + "\\"


def get_files_names(dir_path):
    files_names_list = os.listdir(dir_path)
    return files_names_list


def get_choice():
    message_get_choice = "Wpisz {}, jeśli chcesz zmniejszyć obrazki lub {}, jeśli chcesz je zwiększyć: ".format(
        OPTION_INCREASE, OPTION_DECREASE)
    choice = input(message_get_choice)
    while choice != OPTION_INCREASE and choice != OPTION_DECREASE:
        print("Wpisz poprawny kod wyboru.")
        choice = input(message_get_choice)
    return choice


def get_percent():
    message_get_choice = "Wpisz liczbę procentów, o jakie ma się zmniejszyć lub zwiększyć obrazek: "
    percent = int(input(message_get_choice))
    while percent < 0:
        print("Procent nie może być mniejszy od 0.")
        percent = int(input(message_get_choice))
    return percent


def calculate_size(image, choice, percent):
    new_width = None
    new_height = None

    if choice == OPTION_INCREASE:
        new_width = int(image.width - (image.width * (int(percent) / 100)))
        new_height = int(image.height - (image.height * (int(percent) / 100)))

    if choice == OPTION_DECREASE:
        new_width = int(image.width + (image.width * (int(percent) / 100)))
        new_height = int(image.height + (image.height * (int(percent) / 100)))

    new_size = (new_width, new_height)
    return new_size


def resize_image(image, new_size):
    print("Original width: {}; Original height: {}".format(str(image.width), str(image.height)))
    print("New width: " + str(new_size[0]) + "; New height: " + str(new_size[1]))
    new_image = image.resize(new_size)
    return new_image


def save_image(file_name, dir_path, new_image):
    try:
        new_file_path = "{}new_{}".format(dir_path, file_name)
        new_image.save(new_file_path)
        print("Zapisano {}".format(file_name))
    except OSError as err:
        print("Nie udało się zapisać z powodu {}".format(err))


def main():

    files_names_list = []
    ask_for_path = True
    while ask_for_path:
        try:
            dir_path = get_dir_path()
            files_names_list = get_files_names(dir_path)
        except OSError as err:
            print("Niepoprawna ścieżka. Błąd: {}".format(err))
        else:
            ask_for_path = False

    print("Wczytane pliki: " + str(files_names_list))

    choice = get_choice()
    percent = get_percent()

    for file_name in files_names_list:
        file_path = dir_path + file_name
        opened_image = Image.open(file_path)
        new_size = calculate_size(opened_image, choice, percent)
        new_image = resize_image(opened_image, new_size)
        save_image(file_name, dir_path, new_image)

    print("Zakończono. Zmieniono rozmiar " + str(len(files_names_list)) + " obrazków.")


main()
