<template>
    <div class="car-details">
        <ul class="car-info">
            <li v-for="item in items" :key="item.id" class="item">
                <div class="item-content">

                    <div class="left-text">
                        <div class="title">{{ item.brand_country.brand }} {{ item.model }}, {{ item.year }}</div>
                        <div class="price">{{ item.price }} ₽</div>

                        <div>
                            <button class="gradient-button">Оставить заявку</button> <img class="whatsup"
                                src="../assets/cta_button1.svg">
                        </div>
                        <div>Экономия до 30% от рынка авто в наличии</div>
                        <div class="parameter-row">
                            <div class="right-column">
                                <div>Год выпуска:</div>
                                <div>Кузов:</div>
                                <div>Страна:</div>
                                <div>КПП:</div>
                                <div>Двигатель:</div>
                                <div>Объём двигателя:</div>
                                <div>Привод:</div>
                                <div>Цвет:</div>
                                <div>Пробег:</div>
                            </div>
                            <div class="left-column">
                                <div>{{ item.year }}</div>
                                <div>Машина</div>
                                <div>{{ item.brand_country.country }}</div>
                                <div>{{ item.transmission }}</div>
                                <div>Бензиновый</div>
                                <div>{{ item.engine_volume }}</div>
                                <div>{{ item.drive }}</div>
                                <div>{{ item.color }}</div>
                                <div>{{ item.mileage }}</div>
                            </div>

                        </div>
                        <button class="info-button-red">Подробный расчет</button>
                    </div>

                    <!-- Правая часть с изображением -->
                    <div class="right-text">
                        <img class="image_frame" :src="`${mediaUrl}${item.image}`" alt="Car image">
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            items: [],

            car: null,
            mediaUrl: 'http://localhost:8080/media/'
        };
    },
    mounted() {
        const carId = this.$route.params.id;
        this.fetchData({ id: carId, type: "cars" });
    },
    methods: {
        fetchData(params = {}) {

            return axios.get('http://localhost:8080/api/filter/', { params })
                .then(response => {
                    this.items = response.data;
                    console.log('Fetched data:', this.items);

                }).catch(error => {
                    console.error('Error fetchiong data:', error)
                    throw error;
                });
        },
    }
};
</script>

<style>
.car-details {
    color: white;
}

.car-info {
    list-style: none;
    padding: 0;
}

.item-content {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 20px;

    padding-bottom: 20px;
}

.left-text {
    flex: 2;
    margin-right: 20px;
}

.right-text {
    flex: 1;
    display: flex;
    justify-content: flex-end;
}

.image_frame {
    width: 856px;
    height: 510px;
    border-radius: 8px;
}

.whatsup{
    width: 70px;
    height: 70px;
}

/* Action Button Text */
.title {
    font-size: 40px;
    line-height: 40px;
    color: #FFFFFF;
    font-weight: 700;
    font-family: 'Bebas Neue', sans-serif;
}

.price {
    margin-top: 30px;
    text-align: left;
    font-size: 36px;
    line-height: 36px;
    color: #FFFFFF;
    font-weight: 700;
    font-family: 'Bebas Neue', sans-serif;
}


.info-button-red {
    /* Auto layout */
    line-height: 19.6px;
    font-weight: 600;
    font-size: 14px;
    text-align: center;
    width: 190px;
    height: 44px;
    background: #D51117;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 0px;
    gap: 24px;
    /* Inside auto layout */
    flex: none;
    order: 0;
    flex-grow: 1;
    border: none;
    color: white;
    padding: 15px 30px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 50px;
    transition: background 0.3s ease;
}

.gradient-button {
    line-height: 21.78px;
    margin-top: 30px;
    font-weight: 600;
    font-size: 18px;
    width: 308px;
    height: 70px;
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

.parameter-row {
    display: flex;
    margin-top: 20px;
}

.left-column {
    flex: 1;
}

.right-column {
    all: unset;
    display: block;
    text-align: left;
    flex: 1;
    padding-left: 20px;
    color: #999;
}

.parameter-row div {
    margin-bottom: 8px;
    text-align: left;
}
</style>