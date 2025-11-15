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


### Выводы
Система контроля версий Git является незаменимым инструментом в современной разработке программного обеспечения. Она обеспечивает надежное хранение истории изменений, позволяет эффективно организовать командную работу