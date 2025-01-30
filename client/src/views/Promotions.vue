<template>
  <div class="promotions">
    <h1 class="title">АКЦИИ</h1>
    <div class="promo-container">
      <div class="promo-card promo-friend">
        <div class="promo-content">
          <div class="promo-text">
            <h2>Приведи друга 👍</h2>
            <p>
              Каждый третий клиент обращается к нам по рекомендации знакомых, друзей, родственников. Этот факт нас
              безумно радует, и в знак благодарности мы запустили акцию “Приведи друга”.
            </p>
            <ul>
              <li>
                <span>1</span> Вы рекомендуете нашу компанию;
              </li>
              <li>
                <span>2</span> По вашей рекомендации человек заключает с нами договор на приобретение автомобиля;
              </li>
              <li>
                <span>3</span> Вы получаете денежное вознаграждение или скидку на следующий заказ.
              </li>
            </ul>
            <p>Более подробную информацию можно узнать у наших менеджеров.</p>
            <div class="stages__buttons">
              <button @click="openModal" class="pill-button">
                Получить консультацию
                <img src="../assets/whatsapp.png" alt="WhatsApp" class="icon-whatsapp" />
              </button>
            </div>
          </div>
          <img src="../assets/prom1.png" alt="Приведи друга" class="promo-image" />
        </div>
      </div>

      <div class="promo-card">
        <div class="promo-content">
          <div class="promo-text">
            <h2>Оптовые заказы 🚗 🚙</h2>
            <p>
              Если вы планируете заказать сразу более 1 автомобиля, то для вас действует система лояльности – 10% скидка
              на комиссию компании на каждый последующий автомобиль в заказе.
            </p>
            <button @click="openModal" class="pill-button">Оставить заявку</button>
          </div>
          <img src="../assets/prom2.png" alt="Оптовые заказы" class="promo-image" />
        </div>
      </div>

      <div class="promo-card">
        <div class="promo-content">
          <div class="promo-text">
            <h2>Оплата депозита двумя частями 🤝</h2>
            <p>
              За долгие годы работы мы выработали для вас идеальную схему работы. Представьте, что мы нашли для вас
              идеальный вариант автомобиля, но у вас нет полной суммы для оплаты депозита на руках.
            </p>
            <p>
              Не проблема! В нашей компании вы можете оплатить депозит частями. Первую часть депозита оплачиваете в
              момент заключения договора, вторую – после покупки автомобиля.
            </p>
            <p>Важно уточнить, что конечная цена от этого не изменится. Делаем всё для вашего удобства и доверия.</p>
            <button @click="openModal" class="pill-button">Оставить заявку</button>
          </div>
          <img src="../assets/prom3.png" alt="Оплата" class="promo-image" />
        </div>
      </div>
    </div>
  </div>
  <ModalForm :visible="isModalVisible" @close="closeModal" class="modal-form">
    <ValidationForm :form="form" @submit="handleFormSubmit" @update:form="updateForm" />
  </ModalForm>
</template>

<script>
import { reactive } from 'vue';
import ModalForm from '../components/ModalForm.vue';
import ValidationForm from '../components/ValidationForm.vue';
export default {
  data() {
    return {
      isModalVisible: false,
      form: reactive({
        name: '',
        phone_number: '',
        description: '',
        isAgreed: false
      }),
    }
  },
  name: "PromotionsComponent",
  components: {
    ModalForm,
    ValidationForm,
  },
  methods: {
    openModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
		handleFormSubmit(formData) {
			console.log('Форма успешно отправлена!', formData);
			alert('Форма успешно отправлена!');
			this.isModalVisible = false;
			this.form.name = '';
			this.form.phone_number = '';
			this.form.description = '';
			this.form.isAgreed = false;
		},
    updateForm(newForm) {
      this.form = newForm;
    },
  },
};
</script>

<style scoped>
.modal-form {
    z-index: 1000;
}
.promotions {
  font-family: Arial, sans-serif;
  color: white;
  text-align: left;
  padding: 20px;
}

.title {
  font-family: 'Bebas Neue';
  font-size: 70px;
  margin-bottom: 30px;
  text-align: left;
}

.promo-container {
  display: flex;
  flex-direction: column;
  text-align: left;
  gap: 30px;
}

.promo-card {
  background: #081e36;
  border: 1px solid #ffffff1f;
  border-radius: 28px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  text-align: left;
  gap: 20px;
}

.promo-content {
  display: flex;
  justify-content: space-between;
  gap: 30px;
  align-items: left;
  text-align: left;
}

.promo-text {
  font-family: 'Inter';
  flex: 1;
  text-align: left;
  align-items: left;
}

.promo-text h2 {
  font-family: 'Bebas Neue';
  font-size: 40px;
  margin-bottom: 10px;
}

.promo-text ul {
  list-style: none;
  text-align: left;
  padding: 0;
  margin: 20px 0;
}

.promo-text ul li {
  display: flex;
  text-align: left;
  align-items: left;
  font-size: 16px;
}

.promo-text ul li span {
  background-color: #20344a;
  color: white;
  font-weight: bold;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 10px;
}

.stages__buttons {
  display: flex;
  justify-content: left;
  align-items: left;
  gap: 12px;
}

.pill-button {
  background: linear-gradient(94.98deg, #0d2f68 0%, #d51117 100%);
  color: white;
  padding: 24px 40px 24px 40px;
  border-radius: 50px;
  border: none;
  cursor: pointer;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.icon-whatsapp {
  width: 20px;
  height: 20px;
}

.promo-image {
  max-width: 540px;
  height: auto;
}
</style>