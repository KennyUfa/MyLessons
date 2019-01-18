import os  # программа которая позволяет перемещаться по папкам в компьютере
text = []

def start():
    user_input = input('введи путь: ')             #ввод от пользователя
    if user_input == ('.'):                        #если ввести ' . ' вернет на одну дирректорию назад
        text.pop(-1)
    else:
        text.extend(user_input.split('\\'))
    return text


def folders_print(text):                                    #отображает где мы находимя сейчас
    text2 = '\\'.join(text)
    try:
        print(os.listdir(text2))
    except FileNotFoundError:
        print('такой папки не существует')
        print(text)
        text.pop(-1) and print(os.listdir(text))
    finally:

        folders_print(start())


while True:
    folders_print(start())

# def start():
#     print("Hello my frend")
#     f = input("введи диррвекторию(типа d:/): ")
#     direktory = str(f)
#     return direktory
#
#
# def folders_print(direktory):
#     all_folders = os.listdir(direktory)
#     list_folser = []
#     for fold in all_folders:
#         list_folser.append(fold)
#     print(direktory)
#
#     return list_folser
#
# # def brouse(direktory):
# #     print(direktory)
#
#
# print(folders_print(start()))
