import os
from PIL import Image


def open_images(dir_path):
    # wczytywanie obrazków
    print("")

    try:
        file_names_list = os.listdir(dir_path)
    except FileNotFoundError:
        print("Podana ścieżka jest nieprawidłowa.")
    else:
        opened_images_list = []

        for file_name in file_names_list:
            file_path = dir_path + file_name
            opened_image = Image.open(file_path)
            opened_images_list.append(opened_image)

        return opened_images_list


def get_files_names(dir_path):

    try:
        files_names_list = os.listdir(dir_path)
    except FileNotFoundError:
        print("Podaj poprawną ścieżkę.")
    else:
        return files_names_list


def decrease_images(images_list, files_names, dir_path):
    # zmniejszanie obrazków

    percent = input("Wpisz liczbę procentów, o jakie ma się zmniejszyć lub zwiększyć obrazek: ")
    for i in range(0, len(images_list)):
        # image.show() # otwieranie obrazków w przeglądarce zdjęć
        image = images_list[i]
        file_name = files_names[i]
        print(image) # wypisanie danych obrazka
        print("Original width: " + str(image.width))
        print("Original height: " + str(image.height))
        new_width = int(image.width - (image.width * (int(percent)/100)))
        new_height = int(image.height - (image.height * (int(percent) / 100)))
        small_image = image.resize((new_width, new_height))
        print("New width: " + str(new_width))
        print("New height: " + str(new_height))
        new_file_path = dir_path + 'new_' + file_name
        small_image.save(new_file_path)
        print("Zapisano " + file_name)


def increase_images(images_list, files_names, dir_path):
    # zwiększanie obrazków

    percent = input("Wpisz liczbę procentów, o jakie ma się zmniejszyć lub zwiększyć obrazek: ")
    for i in range (0, len(images_list)):
        # image.show() # otwieranie obrazków w przeglądarce zdjęć
        image = images_list[i]
        file_name = files_names[i]
        print(image)  # wypisanie danych obrazka
        print("Original width: " + str(image.width))
        print("Original height: " + str(image.height))
        new_width = int(image.width + (image.width * (int(percent) / 100)))
        new_height = int(image.height + (image.height * (int(percent) / 100)))
        big_image = image.resize((new_width, new_height))
        print("New width: " + str(new_width))
        print("New height: " + str(new_height))
        new_file_path = dir_path + 'new_' + file_name
        big_image.save(new_file_path)
        print("Zapisano " + file_name)


def main():                      # definicja funkcji main
    # wywołanie moich funkcji

    dir_path = input("Podaj ścieżkę dostępu do folderu: ") + "\\"
    # dir_path = 'C:\\Users\\Marta\\Desktop\\python_projekty\\obrazki\\'

    loaded_images_list = open_images(dir_path)  # open_images() zwraca opened_images_list[]
    while loaded_images_list is None:
        dir_path = input("Podaj ścieżkę dostępu do folderu: ") + "\\"
        loaded_images_list = open_images(dir_path)
    else:
        loaded_images_list = open_images(dir_path)

    files_names_list = get_files_names(dir_path)
    if files_names_list is None:
        dir_path = input("Podaj ścieżkę dostępu do folderu: ") + "\\"
    else:
        print("Wczytane pliki: " + str(files_names_list))

    choice = input("Wpisz 1, jeśli chcesz zmniejszyć obrazki lub 2, jeśli chcesz je zwiększyć: ")

    if choice == "1":
        decrease_images(loaded_images_list, files_names_list, dir_path)

    if choice == "2":
        increase_images(loaded_images_list, files_names_list, dir_path)


main()

