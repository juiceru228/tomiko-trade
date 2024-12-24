<template>
    <div>

        <form @submit.prevent="submitForm" class="custom-form" @click="handleFormClick">
            <div class="desc1">Оставить заявку</div>
            <div class="description">Оставьте заявку и менеджер отправит Вам актуальные варианты автомобилей под Ваши
                требования 👨‍💻</div>
            <div class="form-row">
                <div class="left-column">
                    <div class="input-wrapper">
                        <label class="input-describe" for="name">Имя</label>
                        <input class="first-field" type="text" placeholder="Введите имя" v-model="localForm.name"
                            @input="$emit('update:form', localForm)" />
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
                    <label class="agreed-label">С <span class="link">правилами политики конфиденциальности</span>
                        ознакомлен</label>
                    <div class="error-tooltip" v-if="errors.isAgreed">{{ errors.isAgreed }}</div>
                </div>
            </div>
            <button class="commit-button" type="submit">Отправить</button>
        </form>
    </div>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';
import { mask } from 'vue-the-mask';
export default {
    directives: {
        mask,
    },
    props: {
        form: {
            type: Object,
            required: true,

        },
    },
    emits: ['submit'],
    setup(props, { emit }) {
        const localForm = reactive({ ...props.form });
        const errors = reactive({});

        const validateForm = () => {
            const phoneRegex = /^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$/;
            errors.name = props.form.name ? '' : 'Имя обязательно';
            errors.phone_number = phoneRegex.test(props.form.phone_number) ? '' : 'Номер телефона должен быть в формате +71231231231';
            errors.description = props.form.description ? '' : 'Описание обязательно';
            errors.isAgreed = props.form.isAgreed ? '' : 'Вы должны согласиться с правилами';

            return !errors.name && !errors.phone_number && !errors.description && !errors.isAgreed;
        };
        const fetchData = (params = {}) => {
            return axios
                .post('http://localhost:8080/api/bid/', params)
                .then((response) => {
                    console.log('Ответ от сервера:', response.data);
                })
                .catch((error) => {
                    console.error('Ошибка при отправке данных:', error);
                    throw error;
                });
        };

        const handleFormClick = () => {
            Object.keys(errors).forEach((key) => {
                errors[key] = '';
            });
        };

        const submitForm = () => {
            if (validateForm()) {
                emit('submit', { ...localForm });
                fetchData(props.form).then(() => {
                    emit('submit', { ...localForm });
                    console.log('Данные отправлены:', localForm.form);
                })
                    .catch((error) => {
                        console.error('Ошибка при отправке данных:', error);
                    });
            }
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