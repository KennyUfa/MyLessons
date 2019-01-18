import os
# черновик поиска фаилов по форматам
text = (
    'D:\\tor\\Microsoft Office 2013 Professional Plus 15.0.4569.1506 SP1 RePack by D!akov\\[CourseDevil.com] The-modern-python3-bootcamp')
text2 = os.listdir(text)
print(text2)
for i in range(len(text2)):
    text3 = os.listdir(text + '\\' + text2[i])
    format = ('.srt')
    for a in text3:
        if a[-(len(format)):] == str(format):
            # print(i)
            # save = (text+'\\')
            print(text + '\\' + text2[i] + '\\' + a)


# format = ('.srt')
# for i in text2:
#     if i[-(len(format)):] == str(format):
#         print(i)
