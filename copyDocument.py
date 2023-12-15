import shutil

path = "E:\\Коды\\сайты\\Part_2\\task"
formatHTML = ".html"
formatCSS = ".css"

for i in range(2,31):
    #print(path+str(i)+formatCSS)
    shutil.copy(path+"1"+formatCSS, path+str(i)+formatCSS)