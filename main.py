import os
from PIL import Image


def get_files_names(dir_path):

    files_names_list = os.listdir(dir_path)
    return files_names_list


def calculate_size(image, choice, percent):
    if choice == str(1):
        new_width = int(image.width - (image.width * (int(percent) / 100)))
        new_height = int(image.height - (image.height * (int(percent) / 100)))

    if choice == str(2):
        new_width = int(image.width + (image.width * (int(percent) / 100)))
        new_height = int(image.height + (image.height * (int(percent) / 100)))

    new_size = (new_width, new_height)
    return new_size


def resize_image(image, new_size):

        print("Original width: {}; Original height: {}".format(str(image.width), str(image.height)))
        print("New width: {}; New height: {}".format(str(new_size[0]), str(new_size[1])))
        new_image = image.resize(new_size)
        return new_image


def save_image(file_name, dir_path, new_image):

        new_file_path = "{}new_{}".format(dir_path, file_name)
        new_image.save(new_file_path)
        print("Zapisano {}".format(file_name))


def main():

    dir_path = input("Podaj ścieżkę dostępu do folderu: ") + "\\"
    
    files_names_list = get_files_names(dir_path)
    print("Wczytane pliki: " + str(files_names_list))

    choice = input("Wpisz 1, jeśli chcesz zmniejszyć obrazki lub 2, jeśli chcesz je zwiększyć: ")
    percent = input("Wpisz liczbę procentów, o jakie ma się zmniejszyć lub zwiększyć obrazek: ")

    for file_name in files_names_list:
        file_path = dir_path + file_name
        opened_image = Image.open(file_path)
        new_size = calculate_size(opened_image, choice, percent)
        new_image = resize_image(opened_image, new_size)
        save_image(file_name, dir_path, new_image)

    print("Zakończono. Zmieniono rozmiar " + str(len(files_names_list)) + " obrazków.")


main()

