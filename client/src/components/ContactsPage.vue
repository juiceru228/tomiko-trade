<template>
    <section class="contacts">
        <div class="container">
            <div class="contact_row">
                <div class="contact_left">
                    <div class="title">
                        <h2>Контактная информация
                            <img src="../assets/contact_title_image.webp" alt="Контактная информация">
                        </h2>
                    </div>
                    <p class="section_description">Оставьте свою заявку и наш менеджер свяжется с Вами для уточнения
                        деталей.</p>
                    <div class="contact_item">
                        <p>Звонок по России бесплатный</p>
                        <a href="tel:+8 (800) 775-67-29">8 (800) 775-67-29</a>
                    </div>
                    <div class="contact_item">
                        <p>WhatsApp</p>
                        <a href="https://wa.me/79244202432" target="_blank">+7 924 420-24-32</a>
                    </div>
                    <div class="contact_item">
                        <p>Офис</p>
                        <div>г. Владивосток, ул. Жигура 9в, 1 этаж, офис 1</div>
                    </div>
                </div>
                <form @submit.prevent="submitForm" class="custom-form"  @click="handleFormClick">
                    <div class="desc1">Оставить заявку</div>
                    <div class="description">Оставьте заявку и менеджер отправит Вам актуальные варианты автомобилей под
                        Ваши
                        требования 👨‍💻</div>
                    <div class="form-row">
                        <div class="left-column">
                            <div class="input-wrapper">
                                <label class="input-describe" for="name">Имя</label>
                                <input class="first-field" type="text" placeholder="Введите имя"
                                    v-model="localForm.name" @input="$emit('update:form', localForm)" />
                                <div class="error-tooltip" v-if="errors.name">{{ errors.name }}</div>
                            </div>
                        </div>
                        <div class="right-column">
                            <div class="input-wrapper">
                                <label class="input-describe" for="phone_number">Телефон</label>
                                <input class="second-field" v-mask="'+7 (###) ###-##-##'" placeholder="+7" type="text"
                                    v-model="localForm.phone_number" @input="$emit('update:form', localForm)" />
                                <div class="error-tooltip" v-if="errors.phone_number">{{ errors.phone_number }}</div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <label class="input-describe" for="description">Уточните свой вопрос</label>
                        <textarea rows=3 class="third-field"
                            placeholder="Введите текст сообщения, укажите страну, марку и год машины."
                            v-model="localForm.description" @input="$emit('update:form', localForm)"></textarea>
                        <div class="error-tooltip-description" v-if="errors.description">{{ errors.description }}</div>


                    </div>
                    <div class="input-wrapper">
                        <div class="checkbox-container">
                            <input class="agreed-box" type="checkbox" v-model="localForm.isAgreed" id="checkbox" />
                            <label class="agreed-label">С <span class="link">правилами политики
                                    конфиденциальности</span>
                                ознакомлен</label>
                            <div class="error-tooltip" v-if="errors.isAgreed">{{ errors.isAgreed }}</div>
                        </div>
                    </div>
                    <button class="commit-button" type="submit" @submit="submitForm" >Отправить</button>
                </form>
            </div>
        </div>

        <div class="position-fixed top-0 end-0 p-3" style="z-index: 11">
            <div id="liveToast" class="toast hide" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header">
                    <img src="/static/img/modal_logo.webp" alt="logo">
                </div>
                <div class="toast-body">
                    Вы оставили свой запрос, скоро мы свяжемся с Вами!
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';
import { mask } from 'vue-the-mask';

export default {
    directives: {
        mask,
    },
    name: 'FormModal',
    methods: {
        handleFormSubmit(formData) {
            console.log('Форма успешно отправлена!', formData);
            alert('Форма успешно отправлена!');

            this.localForm.name = '';
            this.localForm.phone_number = '';
            this.localForm.description = '';
            this.localForm.isAgreed = false;

            this.isConsultationModalVisible = false;
        },
    },
    setup(props, { emit }) {
        const localForm = reactive({
            name: '',
            phone_number: '',
            description: '',
            isAgreed: false
        });
        const errors = reactive({
            name: '',
            phone_number: '',
            description: '',
            isAgreed: ''
        });

        const validateForm = () => {
            const phoneRegex = /^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$/;
            errors.name = localForm.name ? '' : 'Имя обязательно';
            errors.phone_number = phoneRegex.test(localForm.phone_number) ? '' : 'Номер телефона должен быть в формате +71231231231';
            errors.description = localForm.description ? '' : 'Описание обязательно';
            errors.isAgreed = localForm.isAgreed ? '' : 'Вы должны согласиться с правилами';

            return !errors.name && !errors.phone_number && !errors.description && !errors.isAgreed;
        };

        const fetchData = (params = {}) => {
            return axios
                .post('/api/bid/', params)
                .then((response) => {
                    console.log('Ответ от сервера:', response.data);
                })
                .catch((error) => {
                    console.error('Ошибка при отправке данных:', error);
                    throw error;
                });
        };

        const submitForm = () => {
            if (validateForm()) {
                const formData = { ...localForm };

                fetchData(formData)
                    .then(() => {
                        // После успешной отправки можно показать уведомление
                        console.log('Данные отправлены:', formData);
                        this.handleFormSubmit(this.localForm);
                        emit('submit', formData);
                    })
                    .catch((error) => {
                        console.error('Ошибка при отправке данных:', error);
                    });
            }
        };

        const handleFormClick = () => {
            Object.keys(errors).forEach((key) => {
                errors[key] = '';  // Очистить ошибки при клике
            });
        };

        return {
            localForm,
            errors,
            validateForm,
            submitForm,
            handleFormClick,
        };
    },
};
</script>

<style scoped>
.contacts {
    margin: 0 0 116px 0;
}

.contacts .title h2 {
    font-size: 70px;
    font-weight: 700;
    line-height: 100%;
    color: #FFF;
}

.contacts .title img {
    width: 63px;
    height: 60px;
    -o-object-fit: cover;
    object-fit: cover;
    -o-object-position: center;
    object-position: center;
}

.contacts .section_description {
    font-size: 18px;
    font-weight: 300;
    color: rgba(255, 255, 255, 0.5);
    margin: 0 0 60px 0;
}

.contacts .contact_row {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    gap: 30px;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
}

.contacts .contact_item p {
    font-size: 16px;
    font-weight: 300;
    line-height: normal;
    letter-spacing: -0.64px;
    color: rgba(255, 255, 255, 0.5);
}


.contacts .contact_item a,
.contacts .contact_item div {
    font-size: 18px;
    font-weight: 500;
    line-height: normal;
    letter-spacing: -0.72px;
    color: #FFF;
}

.contacts .contact_left {
    max-width: 405px;
}

.checkbox-container {
    display: flex;
    align-items: center;
}

.form-row {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}

.left-column,
.right-column {
    color: white;
    flex: 1;

}

.agreed-label {
    margin-left: 8px;
    cursor: pointer;
}

.agreed-box {
    background-color: #FFFFFF;
    border-radius: 8px;
    width: 28px;
    height: 28px;
    border: none;
    outline: none;
}

.input-wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.error-tooltip {
    position: absolute;
    top: 100%;
    left: 0;
    background-color: white;
    color: black;
    padding: 5px;
    font-size: 12px;
    border-radius: 4px;
    width: 100%;
    margin-top: 5px;
    text-align: left;
    z-index: 10;
}

.error-tooltip-description {
    top: 100%;
    left: 0;
    background-color: white;
    color: black;
    font-size: 12px;
    border-radius: 4px;
    width: 100%;
    margin-top: 5px;
    text-align: left;
    z-index: 10;
}

.input {
    flex-direction: column;
}

.input-describe {
    display: block;
    text-align: left;

}

.desc1 {
    display: block;
    text-align: left;
    line-height: 40px;
    font-size: 40px;
    font-weight: 700;
    font-family: 'Bebas Neue', sans-serif;
}

.description {
    display: block;
    text-align: left;
    line-height: 19.36px;
    font-size: 16px;
    font-weight: 400;
    font-family: 'Bebas Neue', sans-serif;
}

.custom-form {
    width: 640px;
    height: 598px;
    gap: 24px;
    padding: 40px;
    background-color: #081E36;
    border-radius: 28px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.first-field,
.second-field {
    padding: 16px;
    text-align: left;
    color: #FFFFFF80;
    width: 100%;
    background-color: #20344A;
    border-radius: 32px;
    border: none;
    outline: none;
    font-size: 16px;
    line-height: 19.36px;
    height: 51px;
}

.third-field {

    text-align: left;
    color: #FFFFFF80;
    padding-top: 10px;
    padding-left: 10px;
    width: 100%;
    background-color: #20344A;
    border-radius: 16px;
    border: none;
    outline: none;
    font-size: 16px;
    line-height: 19.36px;
    resize: none;
    height: 101px;
}

span {
    color: red;
}

.commit-button {
    border-radius: 60px;
    padding-top: 24px;
    padding-left: 40px;
    padding-right: 40px;
    padding-bottom: 24px;
    border: none;
    outline: none;
    background-color: #20344A;
    color: #FFFFFF80;
}
</style>