<template>
    <div class="car-details">
        <ul class="car-info">

            <SwiperCarsComponent :fetchParams="{ country: 'Китай', type: 'cars', page: 1 }" country="КИТАЯ" :flagPath="require('../assets/flag3.svg')"/>
            <SwiperCarsComponent :fetchParams="{ country: 'Япония', type: 'cars', page: 1 }" country="ЯПОНИИ" :flagPath="require('../assets/flag2.webp')"/>
            <SwiperCarsComponent :fetchParams="{ country: 'Корея', type: 'cars', page: 1 }" country="КОРЕИ" :flagPath="require('../assets/flag.svg')"/>
            <contacts />
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
import SwiperCarsComponent from './SwiperCars/SwiperCarsComponent.vue';
register();
import 'swiper/swiper-bundle.css';
import { reactive } from 'vue';
import ModalForm from '../components/ModalForm.vue';
import ValidationForm from '../components/ValidationForm.vue';
import contacts from '@/components/ContactsPage.vue';
import axios from 'axios';
export default {
    name: 'SwiperCars',
    components: {
        ModalForm,
        ValidationForm,
        contacts,
        SwiperCarsComponent
    },
    data() {
        return {
            itemsChina: [],
            itemsKorea: [],
            itemsJapan: [],
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
        async fetchDataChina(params = {}) {
            return await axios
                .get('/api/filter/', { params })
                .then((response) => {
                    this.itemsChina = response.data;
                    console.log('Fetched data:', this.itemsChina);
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                    throw error;
                });
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
        async fetchDataJapan(params = {}) {
            return await axios
                .get('/api/filter/', { params })
                .then((response) => {
                    this.itemsJapan = response.data;
                    console.log('Fetched data:', this.itemsJapan);
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
            console.log('Progress:', swiper, progress);
        },
        onSlideChange() {
            console.log('Slide changed');
        },
        updateForm(newForm) {
            this.form = newForm;
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

<style scoped>
.control {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.control-row {
    display: flex;
    align-items: center;
    gap: 8px;
}

.flag {
    width: 40px;
    height: auto;
}

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
    margin-left: 200px;
    margin-right: 200px;
}

.left-text {
    margin-left: 200px;
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

.left-column div {
    color: rgba(255, 255, 255, 0.5);
    flex-direction: column;
    width: 45%;
}

.parameter-row div {
    margin-bottom: 8px;
    text-align: left;
}

.swipe-button {
    margin-right: 10px;
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

.control-title1 {
    color: rgba(253, 85, 75, 1);
}

.control-title2 {
    color: rgba(255, 255, 255, 0.3);
}

.control {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    transform: translateX(45%) translateY(120px);
    line-height: 40px;
    font-size: 40px;
    font-weight: 700;
}

.text_flag {
    align-items: flex-start;
    display: inline-flex;
    gap: 12px;
    position: relative;
}

.arrow {
    margin-left: 10px;
}

.swiper-button-next {
    right: unset !important;
    left: 50%;
}

.swiper-button-prev {
    right: unset !important;
    right: 50%;
}


.swiper-slide {

    display: flex;
    justify-content: flex-end;
    padding: 100px 0;
    margin: 0px;
    opacity: 1;
    transition: all 0.3s ease;
}

.swiper-container-wrapper {
    max-width: 1800px;
    margin: 0 auto;
    overflow: hidden;

}

.swiper-item-box {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 338px;
    height: 347px;
    background: #081E36;
    border-radius: 24px;
    opacity: 1;

}

.router-link {

    cursor: pointer;
    text-decoration: none;
}

.swiper-container {

    display: flex;
    justify-content: flex-end;
    width: 100%;
    overflow: visible;

}

.price-button-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 10px;
}

.swiper-additionals {
    color: rgba(255, 255, 255, 0.5);
    font-weight: 700;
    text-align: right;
    z-index: 10;
}

.swiper-title {
    font-size: 24px;
    font-weight: 700;
    text-align: left;
    z-index: 10;
    width: 100%;
    padding-left: 10px;
}

.swiper-title-less {
    opacity: 0.5;
    font-size: 24px;
    font-weight: 700;
    text-align: left;
    z-index: 10;
    width: 100%;
    padding-left: 10px;
}

.swiper-slide-active .swiper-price {
    transition: 0.5s ease;
    font-size: 24px;
    font-weight: 700;
    text-align: left;
    z-index: 10;
    margin-left: 10px;
    transform: translateX(-180px) translateY(50px);
}

.swiper-slide-active .swipe-button {
    transition: 0.5s ease;
    text-align: left;
    z-index: 10;
    width: 100%;
    transform: translateX(180px) translateY(50px);
    font-weight: 500;
    font-size: 14px;
    line-height: 140%;
    border-radius: 30px;
    width: 149px;
    height: 44px;
    z-index: 100;
    color: rgba(255, 255, 255, 1);
    background: rgba(255, 255, 255, 0.34);
    border: none;
    padding: 10px 20px;
    cursor: pointer;
}

.swiper-slide-active .swiper-title {
    transition: 0.5s ease;
    font-size: 24px;
    font-weight: 700;
    text-align: left;
    z-index: 10000;
    width: 100%;
    transform: translateX(-180px) translateY(-30px);
}

.swiper-slide-active .swiper-title-less {
    transition: 0.5s ease;
    font-size: 24px;
    font-weight: 700;
    text-align: left;
    z-index: 10000;
    width: 100%;
    transform: translateX(-180px) translateY(-30px);
}

.swiper-price {
    font-size: 24px;
    font-weight: 700;
    text-align: left;
    z-index: 10;
    margin-left: 10px;
}

.modal-form {
    z-index: 1000;
}

.swiper-slide img {
    border-radius: 16px;
    z-index: 0;
    position: relative;
    width: 322px;
    height: 190px;
    object-fit: cover;
    transition: transform 0.5s ease;
}


.swiper-slide-active {
    margin-right: 200px;
    /* Увеличенное расстояние */
    margin-left: 200px;
    display: flex;
    align-items: right;
    transform: translateY(-50px);

}

.swiper-buttons {
    position: relative;

    z-index: 10000;
    transform: translateX(45%) translateY(80px);
}

.swiper-slide-active img {
    transform: scale(2.27);
    align-items: center;
}
</style>