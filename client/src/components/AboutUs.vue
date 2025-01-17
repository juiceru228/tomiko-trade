<template>
    <div class="about_us">
          <p>
              <a name="about_us" style="scroll-margin-top: 150px;"></a>
              <a name="about_us2" style="scroll-margin-top: 350px;"></a>
          </p>
          <div class="container">
              <div class="about_block">
                  <h2 class="d-flex d-lg-none">О нас</h2>
                  <div class="titles">
                      <h2 class="d-none d-lg-block">О нас</h2>
                      <div class="img_abouts">
                        <img src="../assets/abot.webp" alt="О компании">
                      </div>
                      <p>Компания “Tomiko Trade” - ваш надежный поставщик по доставке новых 
                        <br>и подержанных автомобилей из Южной Кореи, Японии и Китая.
                        <br>
                        <br>Вам не нужно разбираться в тонкостях процесса приобретения автомобиля. Мы 
                        <br>делаем это за Вас. Наша цель - помочь Вам приобрести юридически чистый 
                        <br>автомобиль без пробега по РФ с экономией от 300 000₽.</p>
                      <div class="btns_stage">
                        <button class="gradient-button">Подобрать авто</button>
                      <a href="https://wa.me/79244202432" target="_blank"><img src="../assets/cta_button1.svg" alt="whatsapp"></a>
                    </div>
                  </div>
              </div>
              <div class="bottom_abouts">
                  <div class="item">
                      <h3>5 +</h3>
                      <p>Лет на рынке</p>
                  </div>
                  <div class="item">
                      <h3>4 000 +</h3>
                      <p>довольных клиентов</p>
                  </div>
                  <div class="items">
                      <img src="../assets/class.webp" alt="Лайк">
                      <p>Прозрачное ценообразование с <br> подробным разъяснением затрат на <br> каждом этапе</p>
                  </div>
                  <div class="items">
                      <img src="../assets/doc.webp" alt="Листок">
                      <p>Полное сопровождение и <br> предоставление фото/видео <br> отчета на протяжение всей сделки</p>
                  </div>
                  <div class="items">
                      <img src="../assets/dog.webp" alt="Рукопожатие">
                      <p>Проверенные <br> поставщики</p>
                  </div>
              </div>
          </div>
    </div>      
</template>

<script>
export default {
  name: 'AboutUs'
}
</script>

<style scoped>
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

.about_us .about_block h2 {
    font-family: Bebas-Neue, Arial, sans-serif;
    font-size: 70px;
    font-weight: 700;
    line-height: 70px;
    text-align: left;
    color: #fff;
    margin-bottom: 16px;
}
@media (min-width: 992px) {
    .d-lg-block {
        display: block !important;
    }
}

.about_us .about_block .titles p {
    font-family: Inter;
    font-size: 18px;
    font-weight: 400;
    line-height: 28px;
    text-align: left;
    color: #fff;
    white-space: pre-wrap;
}

.about_us .about_block {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    border-bottom: 1px solid #2a3847;
    padding: 0 0 40px 0;
}

@media only screen and (max-width: 1200px) {
    .about_us .about_block .img_abouts img {
        -webkit-transform: none;
        transform: none;
        max-width: 500px;
        height: auto;
    }
}

.about_us .about_block .img_abouts img {
    -webkit-box-shadow: 0 24px 100px 0 rgba(213, 17, 23, 0.4);
    box-shadow: 0 24px 100px 0 rgba(213, 17, 23, 0.4);
    border-radius: 16px;
    aspect-ratio: 500 / 301;
    width: 603px;
    height: 363px;
}

.about_us .about_block .titles .btns_stage {
    margin-top: 40px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
}

.about_us .btns_stage img {
    aspect-ratio: 1 / 1;
    width: 70px;
    height: 70px;
}

.about_us .about_block .titles {
    max-width: 748px; 
}

.about_us .bottom_abouts .item h3 {
    font-family: Bebas-Neue, Arial, sans-serif;
    font-size: 48px;
    font-weight: 700;
    line-height: 48px;
    text-align: center;
    color: #fd554b;
    margin-bottom: 4px;
}

.about_us .bottom_abouts .item p {
    font-family: Inter;
    font-size: 14px;
    font-weight: 300;
    line-height: 16.94px;
    text-align: center;
    color: rgba(255, 255, 255, 0.5019607843);
}

.about_us .bottom_abouts .items img {
    margin-right: 24px;
    aspect-ratio: 1 / 1;
    width: 41px;
    height: 41px;
}

.about_us .bottom_abouts .items p {
    font-family: Inter;
    font-size: 16px;
    font-weight: 300;
    line-height: 24px;
    text-align: left;
    color: #fff;
}

.about_us .bottom_abouts .items {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
}

.about_us .bottom_abouts {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    margin-top: 33px;
}

div {
    display: block;
    unicode-bidi: isolate;
}

.about_us .btns_stage img {
    aspect-ratio: 1 / 1;
    width: 70px;
    height: 70px;
}
img, svg {
    vertical-align: middle;
}

.about_us .about_block .titles p {
    font-family: Inter;
    font-size: 18px;
    font-weight: 400;
    line-height: 28px;
    text-align: left;
    white-space: pre-wrap;
}
</style>