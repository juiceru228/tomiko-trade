<template>
    <div class="car-details">
        <ul class="car-info">

            <SwiperCarsComponent :fetchParams="{ country: 'Китай', type: 'cars', page: 1 }" country="КИТАЯ" :flagPath="require('../assets/flag3.svg')"/>
            <SwiperCarsComponent :fetchParams="{ country: 'Япония', type: 'cars', page: 1 }" country="ЯПОНИИ" :flagPath="require('../assets/flag2.webp')"/>
            <SwiperCarsComponent :fetchParams="{ country: 'Корея', type: 'cars', page: 1 }" country="КОРЕИ" :flagPath="require('../assets/flag.svg')"/>
            
        </ul>




    </div>
</template>
<script>
import { register } from 'swiper/element/bundle';
import { ref } from 'vue';
import SwiperCarsComponent from './SwiperCars/SwiperCarsComponent.vue';
register();
import 'swiper/swiper-bundle.css';

import axios from 'axios';
export default {
    name: 'SwiperCars',
    components: {
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
.car-details {
    color: white;
    margin-bottom: 20px;
}

.car-info {
    list-style: none;
    padding: 0;
}

.modal-form {
    z-index: 1000;
}
</style>