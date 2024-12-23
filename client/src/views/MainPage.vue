<template>
  <section class="hero">
      <div class="container">
        <picture>
          <source media="(max-width: 600px)" srcset="../assets/back1.png">
          <source media="(min-width: 601px)" srcset="../assets/back1.png">
          <img fetchpriority="high" decoding="async" class="image" src="../assets/back1.png" alt="Задний фон">
        </picture>
  
        <div class="hero_title">
          <h1>Автомобили под заказ из Южной Кореи, Китая, Японии</h1>
          <p>Подберем. Купим. Доставим. Растаможим. <br>Отправим в любой регион России</p>
          <button class="gradient-button">Расчитать стоимость</button>
        </div>
  
        <div class="bottom_hero">
          <div class="left_info">
            <div class="item"><div>5 +</div><p>Лет на рынке</p></div>
            <div class="item"><div>4 000 +</div><p>довольных клиентов</p></div>
            <div class="item"><div><img src="" alt="Звездочка">4.6</div></div>
          </div>
          <div class="card_discoint">
            <p>Экономия до  <span>30%</span> 
              <br>от рынка авто в наличии</p>
            <button class="gradient-button">Смотреть пример</button>
          </div>
        </div>
      </div>
    </section>
    <section class="cars-section">
    <div class="popular_cars korea">
      <div class="title">
        <h2>Популярные авто <br><span>из Кореи</span> <img src="" alt="Флаг Кореи"></h2>
        <div class="swiper_buttons">
          <div class="swiper_prev" @click="swiper.slidePrev()">
            <img src="" alt="Предыдущая">
          </div>
          <div class="swiper_next" @click="swiper.slideNext()">
            <img src="" alt="Следующая">
          </div>
        </div>
      </div>
      <swiper :slides-per-view="1" :pagination="{ clickable: true }" ref="mySwiper">
        <swiper-slide v-for="car in cars" :key="car.id">
          <a :href="car.link" class="items2 card_{{ car.id }}">
            <div class="top_items">
              <h3>{{ car.name }}</h3>
              <p>{{ car.year }} • {{ car.mileage }} • {{ car.engine }}</p>
            </div>
            <div class="img_items">
              <img class="main_card_img" :src="car.images[0]" :alt="car.name">
            </div>
            <div class="bottoms_als">
              <h4>{{ car.price }} ₽</h4>
              <button class="red_btn" @click="openQuestionnaireForm(car.name)">Оставить заявку</button>
            </div>
            <div class="pagination" @click.prevent>
              <button v-for="(image, index) in car.images" :key="index" @click="changeCardImage(image, car.id)">
                <div :class="['boll', { active: index === 0 }]"></div>
              </button>
            </div>
          </a>
        </swiper-slide>
      </swiper>
    </div>
  </section>
  </template>
  
  <script>
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import 'swiper/swiper-bundle.css';

  export default {
    components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      cars: [
        {
          id: 1,
          name: 'Kia Mohave',
          year: '2020',
          mileage: '53 599 км',
          engine: '3.0 л.',
          price: '4 234 000',
          images: [
            '/path/to/image1.jpg',
            '/path/to/image2.jpg',
            '/path/to/image3.jpg',
          ],
        },
      ],
    };
  },
    name: 'MainPage',
    methods: {
      openQuestionnaireForm() {
        console.log("Я заинтересовался автомобилем ${carName}");
      },
    },
  };
  </script>
  
<style scoped>
.hero {
  position: relative;
  overflow: hidden;
  color: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 20px;
  text-align: center;
}

.image {
  width: 100%;
  height: auto;
  object-fit: cover;
}

.hero_title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
}

.hero_title h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); 
}

.hero_title p {
  font-size: 1.2rem;
  margin-bottom: 30px; 
}

.bottom_hero {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 40px;
}

.left_info {
  display: flex;
  gap: 30px;
}

.item {
  text-align: center;
}

.item div {
  font-size: 1.5rem;
}

.item p {
  margin-top: 5px;
}

.card_discoint {
  background-color: #081E36;
  border-radius: 5px;
  padding: 15px;
}

.card_discoint p {
  font-size: 1.2rem;
}

.card_discoint span {
  font-weight: bold; 
}

.cars-section {
  background-color: #011224;
  padding: 40px 20px;
}

.popular_cars {
  max-width: 1200px;
  margin: 0 auto;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.title {
  text-align: center;
  margin-bottom: 30px;
}

.title h2 {
  font-size: 2rem;
  color: #333;
}

.title span {
  font-weight: bold;
}

.swiper_buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.swiper_prev,
.swiper_next {
  cursor: pointer;
  background-color: #e0e0e0;
  border-radius: 50%;
  padding: 10px;
  transition: background-color 0.3s;
}

.swiper_prev:hover,
.swiper_next:hover {
  background-color: #d0d0d0;
}

.items2 {
  display: flex;
  flex-direction: column;
  border: 1px solid #ddd; /* Рамка карточки */
  border-radius: 8px; /* Скругленные углы карточки */
  overflow: hidden; /* Обрезка содержимого карточки */
  transition: transform 0.3s;
}

.items2:hover {
  transform: scale(1.02); /* Увеличение карточки при наведении */
}

.top_items {
  padding: 15px;
}

.top_items h3 {
  font-size: 1.5rem;
}

.top_items p {
  color: #777;
}

.img_items {
  height: 200px;
  overflow: hidden;
}

.main_card_img {
  width: 100%;
  height: auto;
}

.bottoms_als {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
}

.bottoms_als h4 {
  font-size: 1.2rem;
}

.red_btn {
  background-color: #ff4c4c; 
  color: white;
  border: none; 
  border-radius: 5px;
  padding: 10px 15px;
  cursor: pointer;
}

.red_btn:hover {
  background-color: #ff1a1a;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.boll {
  width: 10px; 
  height: 10px; 
  background-color: #ccc; 
  border-radius: 50%;
  margin-right: 5px; 
}

.boll.active {
  background-color: #ff4c4c; 
}

.gradient-button {
    background: linear-gradient(to right, #0D2F68, #D51117);
    border: none;
    color: white;
    padding: 15px 30px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 50px;
    transition: background 0.3s ease;
  }
  
  .gradient-button:hover {
    background: linear-gradient(to right, #feb47b, #ff7e5f);
  }
</style>