# Прогнозування Відтоку Клієнтів для Телекомунікаційної компанії

Метою даного проекту є розробка прогностичної моделі для ідентифікації ймовірності припинення клієнтами користування телекомунікаційними послугами на основі історичних даних про клієнтів.

## Опис Даних
Надається набір даних, який включає інформацію про клієнтів телекомунікаційної компанії: демографічні характеристики, історію використання послуг, тарифні плани, дані про відток(Churn).

# Обробка вхідних даних

Включає наступні етвпи:
* Завантаження вхадних даних
* Перевірка записів на дублікати 
* Перевірка на пусті значення і їх обробка: або заміна на нульові значення, або видалення відповідних даних
* Аналіз кореляції між вхідними параметрами і цільовим значенням
* Аналіз кореляції між деякими вхідними параметрами між собою
* Пошук і обробка викидів (outlayers)
* Зберігання обробленого датасета для подальшого тренування моделей

# Моделювання проводилося за допомогою кількох різних методів

* Logistic Regression
* RandomForest
* Neural Network
* XGBoost
* Support Vector Machine

# Веб інтерфейс

Дозволяє ввести параметри тестового клієнта і отримати результат передбачення, залишиться клієнт чи піде.
Можна порівняти результати передбачень різних моделей, а також перевірити передбачення якоїсь конкретної моделі окремо.


# Інсталяція

## Вручну

### Створення віртуального середовища

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Unix/Linux/Mac)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
```

### Встановлення Залежностей

```bash
# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
streamlit run app/main.py
```

## Запуск в докер контейнері

### Створення образу

```bash
docker build -t prognosis-app  .
```

### Запуск контейнера

```bash
docker run -d -p 8089:8089 --name prognosis-app-container prognosis-app 
```

The application will be available at http://127.0.0.1:8089

# Development team
1. Team Lead [Олексій П'явка](https://github.com/piavik) 
2. Scrum Master [Назар Сало](https://github.com/peakodev) 
3. Developer [Олександр Полшведкін](https://github.com/Polshvedkin-Aleksandr) 
4. Developer [Шгор Гієвський](https://github.com/GievskiyIgor) 

# Онлайн версія 

https://prognosis.streamlit.app/

