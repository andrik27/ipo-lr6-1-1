str = ('фывафывафыв', 'ывапвправыфпыаП', 'оолдлполд', 'ыафываывоаыв', 'енуоруоршрк', 'фвапаммфукеАплаыпф' ) #Создание строк
x=0 #Значение переменной 
for i in str: #Цикл перебора каждой строки
    for j in i: #Цикл перебора каждого символа строки
        if j == "а" or j == "А": #Проверка символов
            x += 1 #Счетчик 
            break #Прерывание цикла
print ("Количество строк содержащих букву а: ",x) #Вывод на экран