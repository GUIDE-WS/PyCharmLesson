# PyCharmLesson

*Время выполнения filter.py:*
![](ResultsScren/Screenshot_1.png)
*Время выполнения old_filter.py:*
![](ResultsScren/Screenshot_2.png)

Разница во времмени вызвана тем, что в новом варианте фильтра большая часть времени выполнения затрачивается на ввод
данных пользователем.

*Время выполнения filter_with_filename.py:*
![](ResultsScren/Screenshot_3.png)

Сильное уменьшение времени работы файла вызвано тем, что данные не вводятся пользователем. Так же быстродействию
способствует использование библиотеки numpy, вместо ручных циклов, при работе с матрицами.

*Исходное изображение:*
![](img1.jpg)
*Результат работы filter_with_filename.py:*
![](res_new.jpg)
*Результат работы old_filter.py:*
![](res_old.jpg)


*doc-тест для img_to_nparr():*
![](ResultsScren/Screenshot_4.png)

*часть doc-теста для create_pixel_art():*
![](ResultsScren/Screenshot_5.png)

