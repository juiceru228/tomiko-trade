<template>
  <div class="contact-section">
    <div class="contact-wrapper">
      <div class="contact-details">
        <h1>КОНТАКТНАЯ<br>ИНФОРМАЦИЯ<span style="white-space: nowrap;"> 👋</span></h1>
        <p class="subtitle">Оставьте свою заявку и наш менеджер свяжется с Вами для уточнения деталей.</p>
        <div class="contact-info">
          <div class="column-left">
            <p class="title"><strong>Адрес</strong></p>
            <p class="s-title">690088, г. Владивосток, ул. Жигура 9в</p>
            <p class="title"><strong>Звонок по России бесплатный</strong></p>
            <p class="s-title">8 (800) 775-67-29</p>
            <p class="s-title">8 (924) 123-45-67</p>
            <div class="row-of-images">
              <img src="../assets/telegram.png" alt="Telegram png" />
              <img src="../assets/whatsapp.png" alt="Whatsapp png" />
              <img src="../assets/vk.png" alt="VK png" />
              <img src="../assets/Insta.png" alt="Insta png" />
            </div>
          </div>
          
          <div class="column-right">
            <p class="title"><strong>Компания</strong></p>
            <p class="s-title">ООО "АВТОЦЕНТР-ВЛ"</p>
            <p class="title"><strong>ИНН/КПП</strong></p>
            <p class="s-title">2536263238 / 253601001</p>
            <p class="title"><strong>ОГРН</strong></p>
            <p class="s-title">1132536004622</p>
          </div>
        </div>
      </div>

      <div class="contact-container">
        <form @submit.prevent="submitForm"> 
          <div class="form-row">
            <div class="form-group">
              <label for="name">Имя</label>
              <input
                id="name"
                type="text"
                v-model="form.name"
                placeholder="Введите имя"
                required
              />
            </div>

            <div class="form-group">
              <label for="phone">Телефон</label>
              <input
                id="phone"
                type="text"
                v-model="form.phone"
                placeholder="+7"
                @input="formatPhone"
                required
              />
            </div>
          </div>

          <div class="form-group">
            <label for="message">Уточните свой вопрос</label>
            <textarea
              id="message"
              v-model="form.message"
              placeholder="Введите текст сообщения, укажите страну, марку и год машины"
              maxlength="200"
              required
            ></textarea>
          </div>

          <div class="form-group privacy">
            <input
              type="checkbox"
              v-model="form.privacy"
              id="privacy"
              required
            />
            <label for="privacy">
              С <a href="/privacy-policy.pdf" target="_blank">правилами политики конфиденциальности</a> ознакомлен
            </label>
          </div>

          <button type="submit" class="submit-btn">Отправить</button>
        </form>
      </div>
    </div>
    <div class="map-comp">
      <MapComponent />
    </div>
  </div>
</template>

<script>
import MapComponent from '../components/MapComponent.vue';
export default {
  name: 'ContactPage',
  components: {
    MapComponent
  },
  data() {
    return {
      form: {
        name: "",
        phone: "",
        message: "",
        privacy: false,
      },
    };
  },
  methods: {
    formatPhone() {
      let digits = this.form.phone.replace(/\D/g, "");
      if (digits.length > 1) {
        digits =
          "+7 " +
          digits.substring(1, 4) +
          " " +
          digits.substring(4, 7) +
          " " +
          digits.substring(7, 9) +
          " " +
          digits.substring(9, 11);
      }
      this.form.phone = digits.trim();
    },
    submitForm() {
      if (!this.form.privacy) {
        alert("Пожалуйста, ознакомьтесь с политикой конфиденциальности.");
        return;
      }
      alert("Форма отправлена!");
      this.form = { name: "", phone: "", message: "", privacy: false };
    },
  },
};
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  background-color: #011224;
  color: #fff;
  display: flex;
  height: 100vh;
  flex-direction: column;
}

.contact-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3% 10% 0px;
}

.contact-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 60px;
  width: 100%;
  margin-bottom: 15px;
}

.contact-details {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  width: 30%;
  padding: 0;
}

.contact-details h1 {
  font-family: 'Bebas Neue';
  font-weight: 700;
  font-size: 50px;
  align-items: flex-start;
  text-align: left;
  line-height: 60px;
  color: #FFFFFF;
  margin-bottom: 10px;
}

.contact-details .subtitle {
  font-family: 'Inter';
  font-weight: 400;
  font-size: 18px;
  align-items: flex-start;
  text-align: left;
  line-height: 150%;
  color: rgba(255, 255, 255, 0.5);
  margin-bottom: 30px;
}

.title {
  font-family: 'Inter';
  font-weight: 400;
  align-items: flex-start;
  text-align: left;
  font-size: 16px;
  color: rgba(255, 255, 255, 0.5);
}

.s-title {
  font-family: 'Inter';
  font-weight: 500;
  align-items: flex-start;
  text-align: left;
  font-size: 18px;
  color: #FFFFFF;
}

.contact-info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
}

.column-left,
.column-right {
  width: 45%;
  align-items: flex-start;
}

.column-left {
  text-align: left;
}

.column-right {
  text-align: left;
}

.column-left p {
  left: 0;
}

.column-left img {
  width: 100%;
}

form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  padding: 40px;

  margin: 0 auto;
  width: 640px;
  height: 448px;

  background: #081E36;
  border-radius: 28px;

  flex: none;
  order: 1;
  flex-grow: 0;

}

label {
  font-size: 14px;
  margin-bottom: 5px;
  color: #fff;
}

input,
textarea {
  width: 100%;
  margin-bottom: 20px;
  padding: 15px;
  border: none;
  border-radius: 25px;
  font-size: 14px;
  background-color: #20344A;
  color: #fff;
}

textarea {
  resize: none;
  height: 80px;
}

input[type="checkbox"] {
  width: 24px;
  height: 24px;
  align-self: flex-start;
  background: #FFFFFF;
  border-radius: 8px;

  flex: none;
  order: 0;
  flex-grow: 0;

}

.submit-btn {
  background-color: #20344A;
  color: #FFFFFF;
  padding: 15px 20px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  font-size: 16px;
  width: 100%;
}

.submit-btn:hover {
  background-color: #20344A;
}

.privacy {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  text-align: left;
  justify-content: flex-start;
  gap: 12px;
  width: 100%;

}

.form-group privacy {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  text-align: left;
  justify-content: flex-start;
  padding: 0px;
  gap: 12px;
  text-align: left;

  width: 560px;
  height: 24px;

  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

.privacy label {
  font-family: 'Inter';
  font-weight: 400;
  font-size: 14px;
  color: #fff;
}

.privacy a {
  color: #c22e2e;
  text-decoration: none;
}

.privacy a:hover {
  text-decoration: underline;
}

.form-row {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.form-group {
  text-align: left;
  align-items: start;
  width: 100%;
}

.input-field {
  text-align: left;
}

#name, #phone, #message {
  text-align: left;
}

.map-comp {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.row-of-images {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  gap: 12px;
}

.row-of-images img {
  width: 24px;
  height: 24px;
}

@media (max-width: 768px) {
  .contact-wrapper {
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }

  .contact-details h1 {
    font-size: 40px;
  }

  .contact-details .subtitle {
    font-size: 16px;
  }

  .contact-container {
    width: 100%;
    max-width: 480px;
  }
  
  .map-comp {
    height: 300px;
  }
}
</style>