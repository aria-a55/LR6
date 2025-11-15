# LR6
Лабораторная работа №6
## Система контроля версий Git

### Цель работы:
изучение базовых возможностей системы
управления версиями, опыт работы с Git Api, опыт работы с локальным и
удаленным репозиторием.

### Ход работы:

1. Клонирование репозитория на компьютер(рисю image.png)
![alt text](image.png)

2. Получения истории операций
![alt text](image-1.png)

3. Слияние двух веток(рис. image-2.png)
![alt text](image-2.png)

4. Удаление побочной ветки командой 
git branch -d conclusion

5. Измненение файлов и фиксирование изменений(рис. image-3.png)
![alt text](image-3.png)

6. Откат коммита (рис. image-4.png)
![alt text](image-4.png)

7. Создание ветки для отчета
![alt text](image-6.png)

## Лог команд
   git config --global user.name "4414_Паксялина Дарья Сергеевна"
   git config --global user.email "paksyalinnd@mail.ru"
   git clone https://github.com/aria-a55/LR6
   git pull origin master
   git log --oneline --all
   git show
   git pull origin master
   git merge conclusion
   git pull origin conclusion
   git branch -a
   git checkout master
   git add .
   git commit -m "локальные изменения"
   git pull origin master
   git add file.txt
   git commit -m "Изменение файла file.txt"
   git commit -m "Изменение файла file_for_changing.txt"
   git reset --soft HEAD~1
   git status
   git checkout -b report
   git push -u origin report
   git commit -m "Создание отчета"

Историю операций
68940bd 2025-11-16 4414_Паксялина Дарья Сергеевна: Добавление лога команд
5151928 2025-11-15 4414_Паксялина Дарья Сергеевна: Создание отчета
4bf4e0e 2025-11-15 4414_Паксялина Дарья Сергеевна: Изменение файла file.txt
4d3c1dc 2025-11-15 4414_Паксялина Дарья Сергеевна: Merge branch 'master' of https://github.com/aria-a55/LR6
b9dbd95 2025-11-15 4414_Паксялина Дарья Сергеевна: локальные изменения
f49f1b9 2025-11-15 Daria: Create file_for_changing.txt
7f8be69 2025-11-15 Daria: Create file.txt
96cbb93 2025-11-15 Daria: Create file.py
921f53b 2020-11-21 Kurtyanik: Обновление информации
c08a654 2020-11-21 Kurtyanik: Файл создан пустым
3c6e913 2020-11-21 Kurtyanik: Initial commit

### Выводы
Система контроля версий Git является незаменимым инструментом в современной разработке программного обеспечения. Она обеспечивает надежное хранение истории изменений, позволяет эффективно организовать командную работу