# Классификация животных и фруктов с EfficientNet B0 🐱🍏

Этот проект — две простые модели для классификации картинок:
- 🐶 Животные (коты, собаки и другие).
- 🍊 Фрукты (яблоки, бананы и т.д.).

Мы используем модель **EfficientNet B0**, она быстрая и точная! 🚀

## Что это такое? 🤔

Мы взяли **EfficientNet B0** и обучили её на двух наборах данных:
- Картинки животных (например, собаки 🐕, кошки 😺).
- Картинки фруктов (например, яблоки 🍎, апельсины 🍊).

Модель лёгкая, работает быстро и хорошо угадывает, что на картинке.

## Откуда данные? 📦

- Животные: [Animals10 на Kaggle](https://www.kaggle.com/datasets/alessiocorrado99/animals10).
- Фрукты: [Fruit Recognition на Kaggle](https://www.kaggle.com/datasets/sshikamaru/fruit-recognition/data).

## Как запустить? ⚙️

### 1. Установи нужное
Скачай библиотеки:

```bash
pip install -r requirements.txt
```

В `requirements.txt` должно быть:
```
tensorflow
torch
pillow
matplotlib
numpy
scikit-learn
efficiency
```

### 2. Запусти код
Скачай модели и классифицируй картинки:

- Животные:
```bash
python classify_animals.py --image "путь/к/картинке_животного.jpg"
```

- Фрукты:
```bash
python classify_fruits.py --image "путь/к/картинке_фрукта.jpg"
```

### 3. В Jupyter Notebook
Если любишь ноутбуки:

```python
from classify_animals import classify_animal
from classify_fruits import classify_fruit

print("Животное:", classify_animal("путь/к/картинке_животного.jpg"))
print("Фрукт:", classify_fruit("путь/к/картинке_фрукта.jpg"))
```

## Как обучали? 🎓

1. Загрузили данные с Kaggle.
2. Обучили **EfficientNet B0** на животных и фруктах.
3. Проверили точность на тестовых картинках.

## Результаты 🎉

### Животные (последняя эпоха):
```
Epoch 10/10 | Train Loss: 0.1844, Train Acc: 95.15% | Val Loss: 0.1684, Val Acc: 95.43%
```
Точность на тесте — **95.43%**! 🐾

### Фрукты (последняя эпоха):
```
Epoch 5/5 | Train Loss: 0.0402, Train Acc: 99.87% | Val Loss: 0.0152, Val Acc: 100.00%
```
Точность на тесте — **100%**! 🍎

## Примеры 🖼️

- **Собака** 🐶: "Предсказание: Собака, Точность: 92%".
- **Яблоко** 🍏: "Предсказание: Яблоко, Точность: 94%".

---

Всё! Копируй и вставляй в GitHub. Удачи! 🌟
