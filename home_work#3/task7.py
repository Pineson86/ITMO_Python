import pandas as pd
import numpy as np

# Создание DataFrame с примерными данными
data = {
    'Точка маршрута': ["МЕТРО \"СПОРТИВНАЯ\"", "1-Я И КАДЕТСКАЯ ЛИНИЯ", "1-Я И КАДЕТСКАЯ ЛИНИЯ. МЕТРО \"СПОРТИВНАЯ\"", 
                       "МЕТРО \"СПОРТИВНАЯ\"", "КРОНВЕРКСКИЙ ПРОСПЕКТ", "ЗВЕРИНСКАЯ УЛ."],
    'Рейс 2': ["07:24:20", "00:00:00", "07:54:40", "08:07:00", "00:00:00", "00:00:00"]
}

df = pd.DataFrame(data)

# Функция для преобразования времени в секунды
def time_to_seconds(time_str):
    if isinstance(time_str, str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    return np.nan  # Вернуть np.nan, если не строка

# Функция для преобразования секунд обратно в формат ЧЧ:ММ:СС
def seconds_to_time(seconds):
    if pd.isna(seconds):
        return "00:00:00"
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

# Метод скользящего окна для восстановления времени
def moving_average_window(series, window_size=2):
    times_in_seconds = series.apply(lambda x: time_to_seconds(x) if x != "00:00:00" else np.nan)
    
    # Вычисляем среднее значение с учетом только непропущенных значений
    restored_times_in_seconds = times_in_seconds.rolling(window=window_size * 2 + 1, min_periods=1, center=True).mean()
    
    # Преобразуем обратно в формат ЧЧ:ММ:СС
    restored_times = restored_times_in_seconds.apply(lambda x: seconds_to_time(int(x)) if pd.notnull(x) else "00:00:00")
    return restored_times

# Применяем метод к колонке 'Рейс 2' для восстановления значений
df['Рейс 2 (восстановлен)'] = moving_average_window(df['Рейс 2'])

# Выводим строку с метро "Спортивная" и восстановленными значениями
result = df[df['Точка маршрута'] == "МЕТРО \"СПОРТИВНАЯ\""]
print(result[['Точка маршрута', 'Рейс 2', 'Рейс 2 (восстановлен)']])
