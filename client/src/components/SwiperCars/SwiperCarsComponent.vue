<template>
    <div class="car-details">
        <ul class="car-info">
            <div class="swiper-container-wrapper">
                <div class="control">
                    <div class="control-title1">ПОПУЛЯРНЫЕ АВТО</div>
                    <div class="control-row">
                        <div class="control-title2">ИЗ {{ country }}</div>
                        <img :src="flagPath" alt="ФЛАГ" class="flag" />
                        <div class="swiper-buttons">
                            <img src="../../assets/rigthArrow.svg" @click="prevHandler('korea')" />
                            <img class="arrow" src="../../assets/leftArrow.svg" @click="nextHandler('korea')" />


                        </div>
                    </div>
                </div>

                <swiper-container :slides-per-view="5" ref="koreaRef" @swiperprogress="onProgress"
                    @swiperslidechange="onSlideChange">

                    <swiper-slide class="swiper-slide" v-for="(item, index) in itemsKorea" :key="index">
                        <router-link :to="{ name: 'CarDetail', params: { id: item.id } }" class="router-link">
                            <div class="swiper-item-box">

                                <div class="swiper-title">{{ item.brand_country.brand }} {{ item.model }}</div>
                                <div class="swiper-title-less">{{ item.year }} Бензиновый, {{ item.mileage }}</div>


                                <img :src="`${mediaUrl}${item.image.split('%2C')[0]}`" class="swipe-img-thumbnail" />

                                <div class="price-button-wrapper">
                                    <div class="swiper-price">{{ item.price }} ₽</div>
                                    <button class="swipe-button" @click.prevent="openModal">Оставить заявку</button>

                                </div>

                            </div>

                        </router-link>
                    </swiper-slide>

                    <swiper-slide class="swiper-slide"></swiper-slide>
                    <swiper-slide class="swiper-slide"></swiper-slide>

                </swiper-container>
                <router-view :key="$route.fullPath"></router-view>
            </div>
        </ul>
        <!-- Модальное окно -->
        <ModalForm :visible="isModalVisible" @close="closeModal" class="modal-form">
            <ValidationForm :form="form" @submit="handleFormSubmit" @update:form="updateForm" />
        </ModalForm>
    </div>
</template>
<script>
import { register } from 'swiper/element/bundle';
import { ref } from 'vue';
register();
import { reactive } from 'vue';
import ModalForm from '../../components/ModalForm.vue';
import ValidationForm from '../../components/ValidationForm.vue';
import 'swiper/swiper-bundle.css';
import axios from 'axios';
export default {
    name: 'SwiperCarsComponent',
    components: {
        ModalForm,
        ValidationForm,
    },
    props: {
        fetchParams: {
            type: Object,
            default: () => ({ country: "китай", type: "cars", page: 1 })
        },
        country: {
            type: String,
            default: "Корея",
        },
        flagPath: {
            type: String,
            default: require('@/assets/flag.svg'),
        },
    },
    data() {
        return {
            itemsKorea: [],
            selectedImage: '',
            mainCar: [],
            items: [],
            isModalVisible: false,
            car: null,
            mediaUrl: '/media/',
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
        },
    },
    mounted() {
        this.fetchDataKorea(this.fetchParams);
    },
    methods: {
        getAllImages() {
            return this.items.flatMap(item => item.image.split('%2C'));
        },
        selectImage(image) {
            this.selectedImage = image;
        },
        async fetchDataKorea(params = {}) {
            return await axios
                .get('/api/filter/', { params })
                .then((response) => {
                    this.itemsKorea = response.data;
                    console.log('Fetched data:', this.itemsKorea);
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                    throw error;
                });
        },
        onProgress(e) {
            const [swiper, progress] = e.detail;
            console.log('Progress:', swiper, progress);
        },
        onSlideChange() {
            console.log('Slide changed');
        },
        openModal() {
            this.isModalVisible = true;
        },
        closeModal() {
            this.isModalVisible = false;
        },
        updateForm(newForm) {
            this.form = newForm;
        },
        handleFormSubmit(formData) {
            console.log('Форма успешно отправлена!', formData);
            alert('Форма успешно отправлена!');
            this.form.name = '';
            this.form.phone_number = '';
            this.form.description = '';
            this.form.isAgreed = false;
            this.isModalVisible = false;
        },
    },
    setup() {
        const chinaRef = ref(null);
        const koreaRef = ref(null);
        const japanRef = ref(null);

        const getSwiperInstance = (swiperName) => {
            if (swiperName === "china") return chinaRef.value.swiper;
            if (swiperName === "korea") return koreaRef.value.swiper;
            if (swiperName === "japan") return japanRef.value.swiper;
            return null;
        };

        const prevHandler = (swiperName) => {
            const swiper = getSwiperInstance(swiperName);
            if (swiper) swiper.slidePrev();
        };

        const nextHandler = (swiperName) => {
            const swiper = getSwiperInstance(swiperName);
            if (swiper) swiper.slideNext();
        };

        return {
            chinaRef,
            koreaRef,
            japanRef,
            prevHandler,
            nextHandler,
        };
    },
};
</script>
<style src="./SwiperCars.css" lang="css" scoped></style>