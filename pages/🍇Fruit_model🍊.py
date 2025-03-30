import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import time

# Классы для Animals-10
classes = ['Apple Braeburn', 'Apple Granny Smith', 'Apricot', 'Avocado', 'Banana', 'Blueberry', 'Cactus fruit', 'Cantaloupe', 'Cherry', 'Clementine', 'Corn', 'Cucumber Ripe', 'Grape Blue', 'Kiwi', 'Lemon', 'Limes', 'Mango', 'Onion White', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Pear', 'Pepper Green', 'Pepper Red', 'Pineapple', 'Plum', 'Pomegranate', 'Potato Red', 'Raspberry', 'Strawberry', 'Tomato', 'Watermelon']


# Трансформации
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Загрузка модели
@st.cache_resource
def load_model():
    model = torch.load("models/model_new_fruit.pt", map_location=torch.device("cpu"), weights_only=False)
    model.eval()
    return model

model = load_model()

# Функция предсказания
def predict(image):
    image = transform(image).unsqueeze(0)
    start = time.time()
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    end = time.time()
    return classes[predicted.item()], end - start

# Streamlit-интерфейс
st.title("🍓🫐🍉 Какой ты фрукт?🍇🍋🍊")
uploaded_file = st.file_uploader("Загрузите изображение животного", type=["jpg", "png", "jpeg"])
image_url = st.text_input("Загрузи фото по ссылке")

if image_url:
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    # Отображение изображения
    st.image(image, caption="Загруженное изображение", use_container_width=True)

    st.subheader("Результат")
    label, elapsed = predict(image)
    st.write(f" **Предсказанный класс:** {label}")
    st.caption(f"⏱ Время инференса: {elapsed:.3f} сек")

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Загруженное изображение", use_container_width=True)

    st.subheader("Результат")
    label, elapsed = predict(image)
    st.write(f" **Предсказанный класс:** {label}")
    st.caption(f"⏱ Время инференса: {elapsed:.3f} сек")

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Загруженное изображение", use_container_width=True)

    st.subheader("Результат")
    label, elapsed = predict(image)
    st.write(f" **Предсказанный класс:** {label}")
    st.caption(f"⏱ Время инференса: {elapsed:.3f} сек")

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    if sentiment_mapping[selected] == 'one':
        st.markdown("За что? Мы же старались😢😢😢")
    elif sentiment_mapping[selected] == 'two':
        st.markdown("Может договоримся?🥺👉👈")    
    elif sentiment_mapping[selected] == 'three':
        st.markdown("🖕")    
    elif sentiment_mapping[selected] == 'four':
        st.markdown("Спасибо тебе, ты лучший🔥, но был бы еще лучше, если бы поставил 5 звезд 💋💋💋")    
    elif sentiment_mapping[selected] == 'five':
        st.markdown(
    """
    ✨🔥 ОГОГО, СПАСИБО ЗА 5 ЗВЁЗД! 🌟🌟🌟🌟🌟 
    Вы только что сделали наш день ярче, чем фейерверк в новогоднюю ночь! 🎆💥 
    Ваша поддержка — это как топливо для нашей ракеты, которая стремится к звёздам! 🚀🌕

    Но знаете что? 🤔 
    Ваша энергия и ваше умение видеть хорошее — это настоящий суперспособ! 💪🌈 
    Люди часто спрашивают: "Как стать успешным?" 🏆 
    А секрет прост — нужно действовать, как вы: замечать возможности, верить в лучшее и не бояться двигаться вперёд! 🦸‍♂️🦸‍♀️

    НО (!!!) 🚨 
    Давайте честно: просто мечтать о крутых результатах — это как ждать, что пицца сама прилетит в окно. 🍕😂 
    Жизнь меняется только тогда, когда вы берёте ситуацию в свои руки! 🤾‍♂️💥

    ЧТО ЕСЛИ... ❓🤔  
    Вы прямо сейчас сделаете первый шаг? 🦶💫 
    Время — как песок в руках: если его не использовать, оно просто утекает. ⏳⏳⏳ 
    Завтра станет сегодня, а "послезавтра" превратится в "никогда". 🙅‍♂️🙅‍♀️

    Если вы будете ждать идеального момента, то так и останетесь на старте, пока другие уже бегут к своей цели! 🏃‍♂️💨 
    И знаете, кто потом получает все бонусы? Правильно, они! 🏅🤑

    ТАК ЧТО ДОСТАТОЧНО РАЗГОВОРОВ! 🙌🗣️ 
    Хватит откладывать свою мечту на потом! 🙅‍♂️❌ 
    Возьмите телефон и запишитесь на ту тренировку, напишите тому человеку, откройте книгу или начните изучать навык, о котором давно думали! 📚💻💪 
    Не ждите идеального момента — его не существует. 🔥🚀

    Единственный момент, который имеет значение, это СЕЙЧАС! ⏰💥 
    Потому что каждый великий путь начинался с одного маленького шага. 🦶✨ 
    Почему бы не сделать его прямо сейчас? 🤔💡

    Ваш будущий "я" будет либо благодарить вас за то, что вы начали сегодня, либо корить за то, что вы снова ничего не сделали. 🙏🎯🏆
    Решать вам. Но знайте: мир любит тех, кто действует! 🌍❤️🔥
    """)
        

        st.markdown("### 🔥🔥🔥ДЕЙСТВУЙ🔥🔥🔥")
        st.image("https://media1.tenor.com/m/6kr_yde8dn0AAAAd/just-do-it-do-it.gif", use_container_width=True)    
