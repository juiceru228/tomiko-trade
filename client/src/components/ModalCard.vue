<template>
    <div>
        <form @skidka.prevent="skidka" class="custom-form" @click="handleFormClick">
            <div class="modal_ show">
                <div class="modal_content">
                    <span class="close_modal">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                            <path d="M19.5469 17.954C19.7582 18.1653 19.8769 18.452 19.8769 18.7509C19.8769 19.0497 19.7582 19.3364 19.5469 19.5477C19.3355 19.7591 19.0489 19.8778 18.75 19.8778C18.4511 19.8778 18.1645 19.7591 17.9531 19.5477L12.0009 13.5937L6.04687 19.5459C5.83553 19.7572 5.54888 19.8759 5.25 19.8759C4.95111 19.8759 4.66447 19.7572 4.45312 19.5459C4.24178 19.3345 4.12305 19.0479 4.12305 18.749C4.12305 18.4501 4.24178 18.1635 4.45312 17.9521L10.4072 11.9999L4.455 6.04586C4.24365 5.83451 4.12492 5.54787 4.12492 5.24898C4.12492 4.9501 4.24365 4.66345 4.455 4.45211C4.66634 4.24076 4.95299 4.12203 5.25187 4.12203C5.55076 4.12203 5.8374 4.24076 6.04875 4.45211L12.0009 10.4062L17.955 4.45117C18.1663 4.23983 18.453 4.12109 18.7519 4.12109C19.0508 4.12109 19.3374 4.23983 19.5487 4.45117C19.7601 4.66251 19.8788 4.94916 19.8788 5.24804C19.8788 5.54693 19.7601 5.83358 19.5487 6.04492L13.5947 11.9999L19.5469 17.954Z" fill="white" fill-opacity="0.6"></path>
                        </svg>
                    </span>
                    <div class="modal_title">Экономия до <span>30%</span> от рынка авто в наличии</div>
                    <div class="modal_row">
                        <div class="modal_left">
                            <img loading="lazy" src="/static/img/modal1.webp" alt="screen1">
                            <p>Привезли мы</p>
                            <div class="price">2 585 000 руб.</div>
                        </div>
                        <div class="modal_right">
                            <img loading="lazy" src="/static/img/modal2.webp" alt="screen2">
                            <p>В наличии на Дром Авто</p>
                            <img loading="lazy" src="/static/img/modal_red_arrow.svg" alt="Стрелка" class="modal_red_arrow">
                            <div class="price d-block d-sm-none">3 550 000 руб.</div>
                        </div>
                    </div>
                    <div class="modal_actions">
                        <button class="gradient-button" @click="openModal">
                            Получить консультацию
                        </button>
                        <a href="https://wa.me/79244202432" target="_blank" class="social">
                            <img loading="lazy" src="/static/img/ico-whatsapp.svg" alt="whatsapp">
                        </a>
                        <a href="https://t.me/+RkSgbPfr1BJhODE6" target="_blank" class="social">
                            <img loading="lazy" src="/static/img/ico-tg2.svg" alt="tg">
                        </a>
                    </div>
                </div>
            </div>
        </form>
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
    name: 'ModalCard',
    components: {
        ModalForm,
        ValidationForm,
    },
    data() {
    return {
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
.modal_.show {
    opacity: 1;
    visibility: visible;
}
.modal_ {
    visibility: hidden;
}
@media only screen and (max-width: 1800px) {
    .modal_ {
        max-width: 700px;
    }
}
.modal_ {
    position: fixed;
    left: 50%;
    top: 50%;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    max-width: 900px;
    width: 100%;
    max-height: calc(100svh - 10%);
    padding: 24px 40px 40px 40px;
    border-radius: 24px;
    background: #081e36;
    opacity: 0;
    visibility: hidden;
    -webkit-transition: .3s all ease;
    transition: .3s all ease;
    z-index: 4;
}

.modal_ .close_modal {
    position: absolute;
    top: 24px;
    right: 24px;
    cursor: pointer;
    width: 34px;
    height: 34px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    padding: 5px;
}

img, svg {
    vertical-align: middle;
}

.modal_ .modal_title {
    font-family: Inter;
    font-size: 24px;
    font-weight: 400;
    color: #FFF;
    margin: 0 0 24px 0;
}

.modal_ .modal_title span {
    font-size: 48px;
    font-weight: 900;
    color: #fd554b;
}

.modal_ .modal_row {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    gap: 20px;
    margin: 0 0 48px 0;
}

.modal_ .modal_left, .modal_ .modal_right {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    gap: 8px;
    position: relative;
}

.modal_ .modal_left img {
    aspect-ratio: 401 / 356;
}
.modal_ .modal_row img {
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    width: 100%;
}

.modal_ .modal_left p, .modal_ .modal_right p {
    font-family: Inter;
    font-size: 16px;
    font-weight: 400;
    text-align: center;
    color: rgba(255, 255, 255, 0.5);
}

.modal_ .modal_left .price {
    font-family: Inter;
    font-size: 18px;
    font-weight: 700;
    line-height: 150%;
    color: #FFF;
    border-radius: 45px;
    background: #d51117;
    padding: 8px 16px;
    position: absolute;
    bottom: 25%;
    right: -7%;
    z-index: 1;
}

.modal_ .modal_left, .modal_ .modal_right {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    gap: 8px;
    position: relative;
}

.modal_ .modal_row img {
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    width: 100%;
}
.modal_ .modal_right .modal_red_arrow {
    position: absolute;
    border: 0;
    border-radius: 0;
    width: auto;
    height: auto;
    bottom: 35%;
    left: -26%;
    z-index: 1;
}
.modal_ .modal_right img {
    aspect-ratio: 49 / 89;
}
.modal_ .modal_row img {
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    width: 100%;
}
.modal_ .modal_actions {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    gap: 12px;
}

.gradient-button {
  background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
  border: none;
  color: white;
  padding: 15px 30px;
  font-size: 18px;
  cursor: pointer;
  border-radius: 50px;
  transition: background 0.3s ease;
}

.gradient-button:hover {
  background: linear-gradient(to right, var(--hover-color), var(--hover-bg-color));
}

.modal_ .modal_actions .social {
    width: 70px;
    height: 70px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
    border-radius: 122px;
    background: rgba(255, 255, 255, 0.1);
    -webkit-backdrop-filter: blur(7px);
    backdrop-filter: blur(7px);
}

.modal_ .modal_actions img {
    width: 24px;
    height: 24px;
    aspect-ratio: 1 / 1;
}
</style>