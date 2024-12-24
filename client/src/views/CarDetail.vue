<template>
    <div class="car-details">
        <ul class="car-info">
            <li v-for="item in mainCar" :key="item.id" class="item">
                <div class="item-content">
                    <div class="left-text">
                        <div class="title">{{ mainCar[0].brand_country.brand }} {{ mainCar[0].model }}, {{
                            mainCar[0].year }}</div>
                        <div class="price">{{ mainCar[0].price }} ₽</div>

                        <div>
                            <button @click="openModal" class="gradient-button">Оставить заявку</button>
                            <img class="whatsup" src="../assets/cta_button1.svg" />
                        </div>
                        <div>Экономия до 30% от рынка авто в наличии</div>
                        <div class="parameter-row">
                            <div class="left-column">
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
                            <div class="right-column">
                                <div>{{ mainCar[0].year }} г.</div>
                                <div>Машина</div>
                                <div>{{ mainCar[0].brand_country.country }}</div>
                                <div>{{ mainCar[0].transmission }}</div>
                                <div>Бензиновый</div>
                                <div>{{ mainCar[0].engine_volume }} лс</div>
                                <div>{{ mainCar[0].drive }}</div>
                                <div>{{ mainCar[0].color }}</div>
                                <div>{{ mainCar[0].mileage }}</div>
                            </div>
                        </div>
                        <button @click="openModal" class="info-button-red">Подробный расчет</button>
                    </div>

                    <!-- Правая часть с изображением -->
                    <div class="right-text">
                        <img class="image_frame" :src="`${mediaUrl}${selectedImage}`" alt="Car image" />
                        <div class="image-thumbnails">
                            <img v-for="(image, index) in item.image.split('%2C')" :key="index"
                                :src="`${mediaUrl}${image}`" class="thumbnail" @click="selectImage(image)"
                                :class="{ selected: selectedImage === image }" alt="Car thumbnail" />
                        </div>
                    </div>

                </div>
            </li>
            <div class="swiper-container-wrapper">

                <swiper-container :slides-per-view="3" navigation="true" @swiperprogress="onProgress"
                    @swiperslidechange="onSlideChange">
                    <swiper-slide class="swiper-slide" v-for="(item, index) in items" :key="index">
                        <div class="swiper-item-box">
                            <div class="swiper-title">{{ item.brand_country.brand }} {{ item.model }}</div>
                            <div class="swiper-title">{{ item.year }} Бензиновый, {{ item.mileage }}</div>


                            <img :src="`${mediaUrl}${item.image.split('%2C')[0]}`" class="swipe-img-thumbnail" />
                            <div class="price-button-wrapper">
                                <div class="swiper-price">{{ item.price }} ₽</div>
                                <button class="swipe-button">Оставить заявку</button>
                            </div>
                        </div>
                    </swiper-slide>
                </swiper-container>

            </div>
        </ul>

        <!-- Модальное окно -->
        <ModalForm :visible="isModalVisible" @close="closeModal">
            <ValidationForm :form="form" @submit="handleFormSubmit" />
        </ModalForm>


    </div>
</template>

<script>
import { register } from 'swiper/element/bundle';
import { ref } from 'vue';

register();

import { reactive } from 'vue';
import ModalForm from '../components/ModalForm.vue';
import ValidationForm from '../components/ValidationForm.vue';
import axios from 'axios';
export default {
    components: {
        ModalForm,
        ValidationForm,
    },
    data() {
        return {
            selectedImage: '',
            mainCar: [],
            items: [],
            isModalVisible: false,
            car: null,
            mediaUrl: 'http://localhost:8080/media/',
            form: reactive({
                name: '',
                phone_number: '',
                description: '',
                isAgreed: false
            }),
        };
    },
    watch: {
        'mainCar': function () {
            if (this.mainCar.length > 0 && this.mainCar[0].image) {
                this.selectedImage = this.mainCar[0].image.split('%2C')[0];
            }
        }
    },
    mounted() {
        const carId = this.$route.params.id;
        this.fetchDataMain({ id: carId, type: "cars" });
    },
    methods: {
        getAllImages() {
            return this.items.flatMap(item => item.image.split('%2C'));
        },
        selectImage(image) {
            this.selectedImage = image;
        },
        openModal() {
            this.isModalVisible = true;
        },
        closeModal() {
            this.isModalVisible = false;
        },
        async fetchDataMain(params = {}) {
            return await axios
                .get('http://localhost:8080/api/filter/', { params })
                .then((response) => {
                    this.mainCar = response.data;
                    this.fetchDataRelevant({ country: this.mainCar[0].brand_country.country, type: "cars", page: 1 });
                    console.log('Fetched data:', this.mainCar[0].brand_country.country);
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                    throw error;
                });
        },
        async fetchDataRelevant(params = {}) {
            return await axios
                .get('http://localhost:8080/api/filter/', { params })
                .then((response) => {
                    this.items = response.data;
                    console.log('Fetched data:', this.items);
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                    throw error;
                });
        },
        handleFormSubmit(formData) {
            console.log('Форма успешно отправлена!', formData);
            alert('Форма успешно отправлена!');
            this.isModalVisible = false;
        },
        onProgress(e) {
            const [swiper, progress] = e.detail;
            console.log('Progress:', progress);
        },
        onSlideChange() {
            console.log('Slide changed');
        },
    },
};
</script>

<style scoped>
.car-details {
    color: white;
}

.car-info {
    list-style: none;
    padding: 0;
}

.image-thumbnails {
    justify-content: flex-start;
    display: flex;
    margin-top: 10px;
}

.thumbnail {
    width: 100px;
    height: 80px;

    box-sizing: border-box;
    object-fit: cover;
    cursor: pointer;
    padding: 2px;
    border-radius: 16px;
    margin: 0 5px;
    transition: transform 0.2s ease;
}

.thumbnail:hover {
    transform: scale(1.1);
}

.thumbnail.selected {
    background: linear-gradient(#0D2F68, #D51117);
    position: relative;
    border-radius: 16px;
}


.item-content {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.right-text {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
    width: 55%;
    margin-left: 20px;
}

.left-text {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 60%;
}

.image_frame {
    max-width: 856px;
    height: 510px;
    object-fit: cover;
    border-radius: 8px;
}

.image_frame {
    width: 856px;
    height: 510px;
    border-radius: 8px;
}

.whatsup {
    width: 70px;
    height: 70px;
    margin-left: 10px;
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
    padding-top: 24px;
    padding-left: 40px;
    padding-right: 40px;
    padding-bottom: 24px;
}

.gradient-button:hover {
    background: linear-gradient(to right, #feb47b, #ff7e5f);
}

.parameter-row {
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
    width: 100%;
}

.right-column {
    display: flex;
    flex-direction: column;
    width: 45%;
}

.left-column {
    color: #FFFFFF80;
    display: flex;
    flex-direction: column;
    width: 45%;
}

.parameter-row div {
    margin-bottom: 8px;
    text-align: left;
}

.swipe-button {
font-weight: 500;
font-size: 14px;
line-height: 140%;
/* identical to box height, or 20px */
text-align: center;
    border-radius: 30px;
    width: 149px;
    height: 44px;
    z-index: 100;
    color: #FFFFFF;
    background: #20344A;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}



.swiper-slide {
    display: flex;
    justify-content: flex-end;
    padding: 200px 0;
    margin: 0px;
    background: #011224;
    transition: all 0.3s ease;
}

.swiper-container-wrapper {
    max-width: 1800px;

}

.swiper-item-box {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 338px;
    height: 347px;
    transition: all 0.3s ease;
    background: #081E36;
    border-radius: 24px;

}

.swiper-container {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    width: 100%;
    overflow: hidden;

}

.price-button-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.swiper-additionals{
    color: rgba(255, 255, 255, 0.5);
    font-weight: 700;
    text-align: right;
    z-index: 10;  
}
.swiper-title{
    font-size: 24px;
    font-weight: 700;
    text-align: right;
    z-index: 10;  
}
.swiper-price {
    font-size: 24px;
    font-weight: 700;
    text-align: right;
    z-index: 10;
}
.swiper-slide img {
    border-radius: 16px;
    z-index: 0;
    position: relative;
    width: 322px;
    height: 190px;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.swipe-img-thumbnail {}

.swiper-slide-active {

    z-index: 2;
    align-items: center;
}

.swiper-slide-active img {
    transform: scale(2.27);
    z-index: 2;
    align-items: center;
}
</style>