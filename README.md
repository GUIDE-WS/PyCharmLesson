# PyCharmLesson

## Время выполнения файлов

*Время выполнения ```filter.py```:*
![](ResultsScren/Screenshot_1.png)
*Время выполнения ```old_filter.py```:*
![](ResultsScren/Screenshot_2.png)

Разница во времени вызвана тем, что в новом варианте фильтра большая часть времени выполнения затрачивается на ввод
данных пользователем.

*Время выполнения ```filter_with_filename.py```:*
![](ResultsScren/Screenshot_3.png)

Сильное уменьшение времени работы файла вызвано тем, что данные не вводятся пользователем. Так же быстродействию
способствует использование библиотеки numpy, вместо ручных циклов, при работе с матрицами.

## Исходное изображение и результаты

*Исходное изображение:*
![](img1.jpg)
*Результат работы ```filter_with_filename.py```:*
![](res_new.jpg)
*Результат работы ```old_filter.py```:*
![](res_old.jpg)

## Doc-тесты

*doc-тест для ```img_to_nparr()```:*

![](ResultsScren/Screenshot_4.png)

*часть doc-теста для ```create_pixel_art()```:*

![](ResultsScren/Screenshot_5.png)

## Отладчик

*Ширина и высота изображения:*
- ![](ResultsScren/Screenshot_7.png)
- ![](ResultsScren/Screenshot_8.png)

*Тип изображения:*
- ![](ResultsScren/Screenshot_6.png)

*Значение ширины блока и количество градаций серого:*
- ![](ResultsScren/Screenshot_9.png)
- ![](ResultsScren/Screenshot_10.png)