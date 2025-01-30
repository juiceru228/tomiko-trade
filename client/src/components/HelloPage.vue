<template>
  <div class="hello">
    <div class="titles">
      <h1>Автомобиль вашей мечты здесь</h1>
      <p>Прозрачное ценообразование с подробным
        <br>разъяснением затрат на каждом этапе
      </p>
      <button class="gradient-button" @click="openConsultationModal">Рассчитать стоимость</button>
    </div>
    <section class="ZAP">
      <div class="left_info">
        <div class="item">
          <div>5 +</div>
          <p>Лет на рынке</p>
        </div>
        <div class="item">
          <div>4 000 +</div>
          <p>Довольных клиентов</p>
        </div>
        <div class="item">
          <div><img src="../assets/star.webp" alt="Звездочка">4.6</div>
        </div>
      </div>
      <div class="card_discount">
        <p>Экономия до <span>30%</span><br>от рынка авто в наличии</p>
        <button class="gradient-button" @click="isEconomyModalVisible = true">Смотреть пример</button>

      </div>
    </section>
    <modal-show v-if="showModalEx" @close="closeModalExample" class="modal-form" />
    <div class="overlay" v-if="showModalEx"></div>


  </div>

  <EconomyModal :visible="isEconomyModalVisible" @close="isEconomyModalVisible = false"
    @open-consultation="openConsultationModal" class="modal-form"/>

  <ModalForm :visible="isConsultationModalVisible" @close="isConsultationModalVisible = false" class="modal-form">
    <ValidationForm :form="form" @submit="handleFormSubmit" @update:form="updateForm" />
  </ModalForm>

</template>

<script>
import { reactive } from 'vue';

import EconomyModal from '@/components/EconomyModal.vue';
import ModalForm from '@/components/ModalForm.vue';
import ValidationForm from '@/components/ValidationForm.vue';
export default {
  name: 'HelloPage',
  components: {
    EconomyModal,
    ModalForm,
    ValidationForm
  },
  data() {
    return {
      isEconomyModalVisible: false,
      isConsultationModalVisible: false,
      isModalCalculatorVisible: false,
      showModalExample: false,
      form: reactive({
        name: '',
        phone_number: '',
        description: '',
        isAgreed: false
      }),
    };
  },
  methods: {
    openConsultationModal() {
      this.isEconomyModalVisible = false;
      this.isConsultationModalVisible = true;
    },

    openModalCalculator() {
      this.isModalCalculatorVisible = true;
    },
    closeModalCalculator() {
      this.isModalCalculatorVisible = false;
    },
    showModalEx() {
      this.showModalExample = true;
      console.log("Нажал на кнопку");
    },
    closeModalExample() {
      this.showModalExample = false;
      console.log("Нажал на кнопку");
    },
    handleFormSubmit(formData) {
      console.log('Форма успешно отправлена!', formData);
      alert('Форма успешно отправлена!');
      this.isConsultationModalVisible = false;
      this.form.name = '';
      this.form.phone_number = '';
      this.form.description = '';
      this.form.isAgreed = false;

    },
    updateForm(newForm) {
      Object.assign(this.form, newForm);
    }
  },

};
</script>

<style scoped>
.modal-form {
  z-index: 1000;
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

.hello {
  position: relative;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/back1.png);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  background-color: var(--background-color);
  min-height: 800px;
  width: 100%;
  margin: 0 auto;
  padding: 60px 20px;
}

.hello .titles h1 {
  font-size: 64px;
  font-weight: 700;
  line-height: 76.8px;
  color: #fff;
  text-align: center;
  margin-bottom: 8px;
  text-transform: uppercase;
}

.hello .titles p {
  font-size: 24px;
  font-weight: 400;
  line-height: 36px;
  text-align: center;
  color: #fff;
  margin-bottom: 48px;
  padding: 0 25%;
}

.save_discount {
  margin-top: 40px;
  text-align: right;
}

.save_discount p {
  font-size: 1.5rem;
}

.save_discount span {
  font-weight: bold;
}

.save_discount a img {
  width: 40px;
}

.tittle img {
  height: 50px;
}

.ZAP {
  width: 100%;
  position: relative;
  z-index: 1;
  border-bottom: 1px solid #344150;
  padding-bottom: 40px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  -webkit-box-align: end;
  -ms-flex-align: end;
  align-items: end;
}

.ZAP .card_discoint {
  background: #081e36;
  padding: 16px;
  border-radius: 18px;
  max-width: 325px;
}

.ZAP .left_info .item {
  margin-right: 80px;
  position: relative;
}

.ZAP .left_info .item:last-child {
  margin-right: 0;
}

.ZAP .left_info .item div {
  font-size: 48px;
  font-weight: 700;
  line-height: 48px;
  text-align: center;
  color: #fff;
  margin-bottom: 4px;
}

.ZAP .left_info .item p {
  font-size: 14px;
  font-weight: 400;
  line-height: 16.94px;
  text-align: center;
  color: rgba(255, 255, 255, 0.5019607843);
}

.ZAP .left_info .item div img {
  margin-right: 12px;
  aspect-ratio: 1 / 1;
  height: 25px;
  width: 25px;
}

.ZAP .left_info .item div {
  font-size: 48px;
  font-weight: 700;
  line-height: 48px;
  text-align: center;
  color: #fff;
  margin-bottom: 4px;
}

.ZAP .left_info {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.ZAP .card_discoint p {
  font-size: 24px;
  font-weight: 400;
  line-height: 36px;
  color: #fff;
  text-align: left;
  margin-bottom: 24px;
}

.ZAP .card_discoint span {
  font-size: 48px;
  font-weight: 900;
  line-height: 72px;
  text-align: left;
  color: #fd554b;
}

.card_discount {
  flex: 0 0 300px;
  background-color: var(--card-bg-color);
  border-radius: 5px;
  padding: 15px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.card_discount p {
  font-size: 1.2rem;
}

.card_discount span {
  font-weight: bold;
}

.left_info {
  display: flex;
  justify-content: space-around;
  gap: 30px;
  align-items: left;
}

.titles {
  margin-top: 5%;
  text-align: center;
  margin-bottom: 20%;
}

.titles p {
  font-size: 24px;
  font-weight: 400;
  line-height: 36px;
  text-align: center;
  color: #fff;
  margin-bottom: 48px;
  padding: 0 25%;
}

.titles h1 {
  font-size: 64px;
  font-weight: 700;
  line-height: 76.8px;
  color: #fff;
  text-align: center;
  margin-bottom: 8px;
  text-transform: uppercase;
}
</style>