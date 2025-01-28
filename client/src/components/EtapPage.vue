<template> 
    <main class="content">
        <div class="stage_work">
            <div class="container">
            <div class="stage_block">
                <div class="title">
                    <h2><span>Этапы</span> работы</h2>
                    <p>Прозрачное ценообразование с подробным <br> разъяснением затрат на каждом этапе</p>
            </div>
            <div class="itesm_stages">
                    <div class="item">
                        <img loading="lazy" src="../assets/work1.webp" alt="work1">
                        <div>
                            <h3><span>Заявка</span></h3>
                            <p><span>Оставьте заявку и получите бесплатную консультацию персонального менеджера. Вам отправят свежие варианты из статистики, рассчитают ориентировочную стоимость автомобиля и ответят на все сопутствующие вопросы о покупке автомобиля.</span></p>
                        </div>
                        <img loading="lazy" class="line_img" src="../assets/line1.svg" alt="line1">
                    </div>
                    <div class="item">
                        <img loading="lazy" src="../assets/work2.webp" alt="work2">
                        <div>
                            <h3><span>Договор</span></h3>
                            <p><span>Если Вас все устроило, заключаем договор. Вы вносите авансовый депозит и менеджер по покупкам начинает активные действия по подбору автомобиля.</span></p>
                        </div>
                        <img loading="lazy" class="line_img line_img2" src="../assets/line2.svg" alt="line2">
                    </div>
                    <div class="item">
                        <img loading="lazy"  src="../assets/work3.webp" alt="work3">
                        <div>
                            <h3><span>Подбор и покупка авто</span></h3>
                            <p><span>Ежедневно менеджер по покупке просматривает доступные лоты и отправляет Вам варианты на согласование до тех пор, пока не будет найден подходящий. Менеджер отправляет точный расчет цены согласованного варианта по курсам на день покупки и мы покупаем автомобиль.</span></p>
                        </div>
                        <img loading="lazy" class="line_img" src="../assets/line2.svg" alt="line2">
                    </div>
                    <div class="item">
                        <img loading="lazy" src="../assets/work4.webp" alt="work4">
                        <div>
                            <h3><span>Доставка и отправка</span></h3>
                            <p><span>Доставляем автомобиль во Владивосток, проходим этапы оформления и отправляем его в Ваш город любым удобным способом.</span></p>
                        </div>
                        <img loading="lazy" class="line_img" src="../assets/line2.svg" alt="line2">
                    </div>
            </div>
            <div class="btns_stage">
                <button class="gradient-button" @click="openModal">Получить консультацию</button>
                <a href="https://wa.me/79244202432" target="_blank"><img loading="lazy" src="../assets/cta_button1.svg" alt="whatsapp"></a>
            </div>

            </div>
            <div class="save_discount">
                <div>
                    <p>Экономия до <span>30%</span></p>
                    <span>от рынка авто в наличии</span>
                </div>
                <a href="#" aria-label="Открыть карточку">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
                        <path d="M14.0306 8.53074L9.53063 13.0307C9.38973 13.1716 9.19863 13.2508 8.99938 13.2508C8.80012 13.2508 8.60902 13.1716 8.46813 13.0307C8.32723 12.8898 8.24807 12.6987 8.24807 12.4995C8.24807 12.3002 8.32723 12.1091 8.46813 11.9682L11.6875 8.75011H2.5C2.30109 8.75011 2.11032 8.67109 1.96967 8.53044C1.82902 8.38979 1.75 8.19902 1.75 8.00011C1.75 7.8012 1.82902 7.61043 1.96967 7.46978C2.11032 7.32913 2.30109 7.25011 2.5 7.25011H11.6875L8.46937 4.03011C8.32848 3.88921 8.24932 3.69812 8.24932 3.49886C8.24932 3.2996 8.32848 3.10851 8.46937 2.96761C8.61027 2.82671 8.80137 2.74756 9.00062 2.74756C9.19988 2.74756 9.39098 2.82671 9.53187 2.96761L14.0319 7.46761C14.1018 7.53738 14.1573 7.62028 14.1951 7.71155C14.2329 7.80281 14.2523 7.90065 14.2522 7.99943C14.252 8.09822 14.2324 8.19601 14.1944 8.28718C14.1564 8.37836 14.1007 8.46113 14.0306 8.53074Z" fill="white"/>
                    </svg>
                </a>
            </div>
            </div>
        </div>
        <ModalForm :visible="isModalVisible" @close="closeModal" class="modal-form">
            <ValidationForm :form="form" @submit="handleFormSubmit" @update:form="updateForm" />
        </ModalForm>
    </main>
</template>

<script>
import { reactive } from 'vue';
import ModalForm from '../components/ModalForm.vue';
import ValidationForm from '../components/ValidationForm.vue';
export default {
    name: 'EtapPage',
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

.stage_work .save_discount {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    gap: 11px;
    margin: 14px 0 0 80px;
    position: relative;
    z-index: 1;
}

.stage_work .save_discount::after {
    position: absolute;
    content: "";
    width: 96%;
    height: 130px;
    border-radius: 24px;
    left: -25px;
    bottom: 24px;
    background-color: #d51117;
    z-index: -1;
    -webkit-transform: rotate(-2deg);
    transform: rotate(-4deg);
}
@media only screen and (max-width: 1200px) {
    .stage_work .save_discount::after {
        bottom: 10px;
    }
}

.stage_work { 
  padding: 40px 20px;
  margin-bottom: 80px;
}

@media only screen and (max-width: 992px) {
    .stage_work .itesm_stages .item {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: start;
        -ms-flex-align: start;
        align-items: flex-start;
    }
}

.stage_work .itesm_stages .item {
    max-width: 259px;
    position: relative;
}

.stage_work .stage_block .itesm_stages img {
    aspect-ratio: 1 / 1;
    width: 52px;
    height: 52px;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
}

.stage_work .save_discount p {
    font-size: 24px;
    font-weight: 300;
    line-height: normal;
    color: #FFF;
}
.stage_work .save_discount p span {
    font-weight: 900;
    font-size: 32px;
}
.stage_work .save_discount span {
    font-size: 14px;
    font-weight: 300;
    line-height: 150%;
    color: #FFF;
}
.stage_work .save_discount p+span {
    display: block;
    margin: -8px 0 0 0;
}
.stage_work .save_discount a {
    padding: 8px 16px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.3);
    margin: -22px 0 0 0;
}

a {
    text-decoration: none !important;
}
.stage_block {
  text-align: center;
  box-sizing: border-box;
  background-image: url(../assets/stage1.webp);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  border-radius: 15px;
  z-index: 2;
}

.stage_work .title h2 span {
    color: #f8534a;
}

.stage_work .title h2 {
    font-size: 70px;
    font-weight: 700;
    line-height: 70px;
    text-align: center;
    color: #fff;
    margin-bottom: 16px;
}

.stage_work .itesm_stages .item h3 span {
    color: #fff;
}

.stage_work .itesm_stages .item p {
    font-size: 14px;
    font-weight: 300;
    line-height: 24px;
    text-align: left;
    color: rgba(255, 255, 255, 0.7);
}

.stage_work .stage_block .itesm_stages img {
    aspect-ratio: 1 / 1;
    width: 52px;
    height: 52px;
}

@media only screen and (max-width: 1200px) {
    .stage_work .itesm_stages .item .line_img {
        left: 80px;
        max-width: 139px;
    }
}
.stage_work .itesm_stages .item .line_img {
    position: absolute;
    top: 27px;
    left: 77px;
}
.stage_work .stage_block .itesm_stages .line_img {
    aspect-ratio: 203 / 2;
    width: 203px;
    height: 2px;
}
.stage_work .stage_block .itesm_stages img {
    aspect-ratio: 1 / 1;
    width: 52px;
    height: 52px;
}

.stage_work .btns_stage img {
    aspect-ratio: 1 / 1;
    width: 70px;
    height: 70px;
}

.btns_stage {
  margin-top: 30px;
}

.content {
  background-color: var(--background-color);
  min-height: 400px;
}

.title h2 {
  font-size: 2rem;
  margin-bottom: 10px;
}

.title p {
  font-size: 1rem;
}

.itesm_stages {
  display: flex; 
  flex-wrap: wrap; 
  justify-content: space-between;
  margin-top: 20px;
}

.item {
  flex: 1 1 calc(25% - 20px);
  margin: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.title h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
}

.title p {
  font-size: 1.2rem;
  margin-bottom: 30px;
}

.stage_work .stage_block {
    padding: 80px;
    border-radius: 28px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    position: relative;
    z-index: 2;
}

.stage_work .itesm_stages .item p {
    font-size: 14px;
    font-weight: 300;
    line-height: 24px;
    text-align: left;
    color: rgba(255, 255, 255, 0.7);
}
</style>