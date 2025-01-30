<template>
    <div class="logos_brand">
      <div class="logo-carousel">
        <div class="marquee">
            <button v-for="(logo, index) in logos" :key="index" @click="openModal">
              <img loading="lazy" :src="logo.src" :alt="logo.alt">
            </button> 
        </div>
      </div>
      <ModalForm :visible="isModalVisible" @close="closeModal" class="modal-form">
            <ValidationForm :form="form" @submit="handleFormSubmit" @update:form="updateForm" />
        </ModalForm>
    </div>
  </template>
  
<script>
import { reactive } from 'vue';
import ModalForm from '../components/ModalForm.vue';
import ValidationForm from '../components/ValidationForm.vue';
export default {
    name: "LentaFunc",
    components: {
        ModalForm,
        ValidationForm,
    },
    data() {
      return {
        logos: [
          { src: require('../assets/brand1.webp'), alt: 'Logo 1' },
          { src: require('../assets/brand2.webp'), alt: 'Logo 2' },
          { src: require('../assets/brand3.webp'), alt: 'Logo 3' },
          { src: require('../assets/brand4.webp'), alt: 'Logo 4' },
          { src: require('../assets/brand5.webp'), alt: 'Logo 5' },
          { src: require('../assets/brand6.webp'), alt: 'Logo 6' },
          { src: require('../assets/brand7.webp'), alt: 'Logo 7' },
          { src: require('../assets/brand8.webp'), alt: 'Logo 8' },
          { src: require('../assets/brand9.webp'), alt: 'Logo 9' },
          { src: require('../assets/brand10.webp'), alt: 'Logo 10' },
          { src: require('../assets/brand11.webp'), alt: 'Logo 11' },
          { src: require('../assets/brand12.webp'), alt: 'Logo 12' },
          { src: require('../assets/brand13.webp'), alt: 'Logo 13' },
          { src: require('../assets/brand1.webp'), alt: 'Logo 1' },
          { src: require('../assets/brand2.webp'), alt: 'Logo 2' },
          { src: require('../assets/brand3.webp'), alt: 'Logo 3' },
          { src: require('../assets/brand4.webp'), alt: 'Logo 4' },
          { src: require('../assets/brand5.webp'), alt: 'Logo 5' },
          { src: require('../assets/brand6.webp'), alt: 'Logo 6' },
          { src: require('../assets/brand7.webp'), alt: 'Logo 7' },
          { src: require('../assets/brand8.webp'), alt: 'Logo 8' },
          { src: require('../assets/brand9.webp'), alt: 'Logo 9' },
          { src: require('../assets/brand10.webp'), alt: 'Logo 10' },
          { src: require('../assets/brand11.webp'), alt: 'Logo 11' },
          { src: require('../assets/brand12.webp'), alt: 'Logo 12' },
          { src: require('../assets/brand13.webp'), alt: 'Logo 13' },
          { src: require('../assets/brand1.webp'), alt: 'Logo 1' },
          { src: require('../assets/brand2.webp'), alt: 'Logo 2' },
          { src: require('../assets/brand3.webp'), alt: 'Logo 3' },
          { src: require('../assets/brand4.webp'), alt: 'Logo 4' },
          { src: require('../assets/brand5.webp'), alt: 'Logo 5' },
          { src: require('../assets/brand6.webp'), alt: 'Logo 6' },
          { src: require('../assets/brand7.webp'), alt: 'Logo 7' },
          { src: require('../assets/brand8.webp'), alt: 'Logo 8' },
          { src: require('../assets/brand9.webp'), alt: 'Logo 9' },
          { src: require('../assets/brand10.webp'), alt: 'Logo 10' },
          { src: require('../assets/brand11.webp'), alt: 'Logo 11' },
          { src: require('../assets/brand12.webp'), alt: 'Logo 12' },
          { src: require('../assets/brand13.webp'), alt: 'Logo 13' },
        ],
        isModalVisible: false,
    form: reactive({
      name: '',
      phone_number: '',
      description: '',
      isAgreed: false
      }),
      };
    },
    methods: {
    openModal() {
            this.isModalVisible = true;
        },
        closeModal() {
            this.isModalVisible = false;
        },
  },

  handleFormSubmit(formData) {
            console.log('Форма успешно отправлена!', formData);
            alert('Форма успешно отправлена!');
            this.isModalVisible = false;
  },
  updateForm(newForm) {
            this.form = newForm;
  },
  };
</script>

<style scoped>  
.modal-form {
    z-index: 1000;
}
button { 
  background-color: transparent;
  border: none;
}   
.logos_brand {
  max-width: 2000px;
  margin-bottom: -10px;
  overflow: hidden;
}

.logos_brand .logo-carousel {
  max-width: 2000px;
  width: 100%;
  overflow: hidden;
  padding: 10px 0;
}

element.style {
    max-width: 2000px;
    margin-right: 0px;
    float: left;
    display: inline-flex;
    margin-left: 0px;
}

.marquee img {
    -webkit-transition: -webkit-transform .3s ease;
    transition: -webkit-transform .3s ease;
    transition: transform .3s ease;
    transition: transform .3s ease, -webkit-transform .3s ease;
    width: 100px;
    height: 100px;
}

img, svg {
    vertical-align: middle;
}

button, select {
    text-transform: none;
}


button {
    border-radius: 0;
}

.logo-carousel {
    position: relative;
    white-space: nowrap;
}
      
.marquee {
        max-width: 1800px;
        animation: scrolling 30s linear infinite;
        white-space: nowrap;
        display: inline-block;
        will-change: transform;
}

@keyframes scrolling {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(-100%);
    }
  }
</style>