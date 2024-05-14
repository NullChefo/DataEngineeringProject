# DataEngineeringProject
Data Engineering Project


# EN

*** Task Description: *** Creating a simple data processing architecture.

*** Objective: *** The goal of this task is to start your journey in data engineering. The idea is for each of you individually to transfer data from a source to a target database.

Conditions:
- The mandatory toolkit to use includes Apache Airflow (or a similar tool), Python, and databases.
- Using Python, each student must extract data from the respective datasets provided in the document below. The databases you can use are at your discretion.
- Using Apache Airflow, you need to set the Python code to run regularly (on a specific schedule).
Since your data sources come in different formats, you will need to perform the necessary processing to make them suitable for your target database.
- The data should initially be loaded from Kaggle into the first database using Python code and subsequently transferred to another database.
- Example implementation: (Kaggle -> MSSQL -> Oracle).

*** Datasets:  ***

### IMDB

https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset/data
https://www.kaggle.com/datasets/thedevastator/netflix-imdb-scores

---

# BG


*** Описание на задачата: *** Създаване на проста архитектура на обработка на данни.

*** Цел: ***  Целта на тази задача е да поставите начало на вашия път в инженерството на данни (Data engineering). Идеята е всеки от вас индивидуално да трансферира данни от източник към целева база от данни.

Условия: 
- Инструментариумът, който е задължителен за използване е Apache Airflow (или подобен tool), Python и бази от данни.
- Използвайки Python всеки студент трябва да извлече данните от съответните набори от данни, предоставени в документът по-долу. Базите, които можете да използвате са по ваше желание.
- Чрез Apache Airflow трябва да зададете Python кодът да се изпълнява регулярно (по определен график).
Тъй като източниците ви на данни са в различни формати, ще трябва да направите съответната преработка, за да можете да ги предоставите в удобен за вашата целева база от данни вид.
- Данните трябва да бъдат заредени първоначално от Kaggle в първата база от данни чрез Python код и в последствие прехвърлена в друга база от данни. 
- Примерно изпълнение: (Kaggle -> MSSQL -> Oracle).


*** Набори от данни:  ***

### IMDB

https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset/data
https://www.kaggle.com/datasets/thedevastator/netflix-imdb-scores




# Set up the project

### 1. execute the build.sh

### 2. docker compose up


More info at:
https://www.youtube.com/watch?v=N3Tdmt1SRTM




# Python (Winodws)

1. Creating venv:
```bash
python -m venv ./venv 
```

2. Activating venv
```bash
venv/scripts/activate
```
