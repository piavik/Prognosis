import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 1. Подготовка данных
current_directory = os.getcwd()
print(f"Current_directory:{current_directory}")
file_path = os.path.join(current_directory, 'datasets/internet_service_churn.csv')
df = pd.read_csv(file_path)
numeric_columns = ['subscription_age', 'bill_avg', 'reamining_contract', 'service_failure_count', 'download_avg', 'upload_avg', 'download_over_limit']
# Заполнение пропущенных значений нулями
df.fillna(0, inplace=True)
# Разделяем на признаки и целевую переменную
X = df.drop(['id', 'churn'], axis=1)
y = df['churn']

# Разделение на тренировочные и тестовые выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Масштабирование данных
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. Создание модели нейронной сети

model = Sequential()

# Добавляем входной слой и скрытые слои
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))  
model.add(Dense(64, activation='relu'))  
model.add(Dense(32, activation='relu'))  
model.add(Dense(16, activation='relu'))  
model.add(Dense(1, activation='sigmoid'))  # Выходной слой для бинарной классификации

# Компиляция модели
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# 3. Обучение модели
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# 4. Оценка модели

# Предсказания на тестовой выборке
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)  # Преобразуем вероятности в классы 0 или 1

# Оценка метрик
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 score: {f1:.4f}")
