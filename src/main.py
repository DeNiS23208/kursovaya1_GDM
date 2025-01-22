import pandas as pd


def load_and_process_data(file_path):
    """
    Загружает и обрабатывает данные из файла CSV.

    :param file_path: Путь к файлу CSV.
    :return: DataFrame с отфильтрованными полями.
    """
    # Определяем необходимые столбцы
    required_columns = [
        'Дата платежа', 'Сумма операции', 'Валюта операции',
        'Категория', 'Описание', 'Тип'
    ]

    try:
        # Загружаем данные
        data = pd.read_csv(file_path, delimiter=',', encoding='utf-8')

        # Проверяем, содержатся ли нужные столбцы в файле
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"В файле отсутствуют необходимые столбцы: {missing_columns}")

        # Фильтруем только нужные столбцы
        filtered_data = data[required_columns]

        print("Данные успешно загружены и обработаны!")
        return filtered_data

    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return None
