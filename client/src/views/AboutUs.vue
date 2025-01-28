<template>
    <div class="about-us">
        <div class="about-us-card">
            <div class="about-us-block">
                <div class="about-us-text">
                    <h2>О НАС</h2>
                    <p>
                        Компания «Правый руль» предлагает широкий выбор автомобилей от ведущих мировых производителей. 
                        Мы специализируемся на продаже новых и подержанных авто. 
                        Наша команда профессионалов поможет вам выбрать идеальный автомобиль, учитывая ваши потребности и бюджет.
                    </p>
                    <div class="stages__buttons">
                        <button class="pill-button">Получить консультацию</button>
                        <button class="round-button">
                            <img src="../assets/whatsapp.png" alt="WhatsApp" class="icon-whatsapp" />
                        </button>
                    </div>
                </div>
                <img src="../assets/abot.webp" alt="Команда" class="about-image" />
            </div>
            <div class="list-block">
                <div class="list-item">
                    <span class="list-number">5+</span>
                    <p class="list-text">Лет на рынке</p>
                </div>
                <div class="list-item">
                    <span class="list-number">4 000+</span>
                    <p class="list-text">Довольных клиентов</p>
                </div>
                <div class="list-item-img">
                    <img src="../assets/class.webp" alt="Лайк">
                    <p class="list-text-img">Прозрачное ценообразование с разъяснением затрат</p>
                </div>
                <div class="list-item-img">
                    <img src="../assets/doc.webp" alt="Листок">
                    <p class="list-text-img">Полное сопровождение и отчетность на каждом этапе</p>
                </div>
                <div class="list-item-img">
                    <img src="../assets/dog.webp" alt="Рукопожатие">
                    <p class="list-text-img">Проверенные поставщики</p>
                </div>
            </div>
        </div>
        <div class="stages-of-work-card">
            <div class="stage-title">
              <h2><span>ЭТАПЫ</span> РАБОТЫ</h2>
              <p>Прозрачное ценообразование с подробным <br> разъяснением затрат на каждом этапе</p>
            </div>
            <div class="item-stage">
                <div class="item-images">
                    <img loading="lazy" class="item-icons" src="../assets/work1.webp" alt="work1">
                    <img loading="lazy" class="line_img" src="../assets/line1.svg" alt="line1">
                </div>
                <div class="item-images">
                    <img loading="lazy" class="item-icons"  src="../assets/work2.webp" alt="work2">
                    <img loading="lazy" class="line_img line_img2" src="../assets/line2.svg" alt="line2">
                </div>
                <div class="item">
                    <img loading="lazy" class="item-icons"  src="../assets/work3.webp" alt="work3">
                    <div>
                        <h3><span>Подбор и покупка авто</span></h3>
                        <p><span>Ежедневно менеджер по покупке просматривает доступные лоты и отправляет Вам варианты на
                            согласование до тех пор, пока не будет найден подходящий. Менеджер отправляет точный расчет цены
                            согласованного варианта по курсам на день покупки и мы покупаем автомобиль.</span></p>
                    </div>
                    <img loading="lazy" class="line_img" src="../assets/line2.svg" alt="line2">
                </div>
                <div class="item">
                    <img loading="lazy" class="item-icons"  src="../assets/work4.webp" alt="work4">
                    <div>
                        <h3><span>Доставка и отправка</span></h3>
                        <p><span>Доставляем автомобиль во Владивосток, проходим этапы оформления и отправляем его в Ваш город
                            любым удобным способом.</span></p>
                    </div>
                    <img loading="lazy" class="line_img" src="../assets/line2.svg" alt="line2">
                </div>
                <div class="item-text">
                    <h3><span>Заявка</span></h3>
                    <p><span>Оставьте заявку и получите бесплатную консультацию персонального менеджера. Вам отправят
                        свежие варианты из статистики, рассчитают ориентировочную стоимость автомобиля и ответят на все
                        сопутствующие вопросы о покупке автомобиля.</span></p>
                </div>
                <div class="item-text">
                    <h3><span>Договор</span></h3>
                    <p><span>Если Вас все устроило, заключаем договор. Вы вносите авансовый депозит и менеджер по покупкам
                            начинает активные действия по подбору автомобиля.</span></p>
                </div>
            </div>
            <div class="stages__buttons">
                <button class="pill-button">Получить консультацию</button>
                <button class="round-button">
                    <img src="../assets/whatsapp.png" alt="WhatsApp" class="icon-whatsapp" />
                </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "AboutUs",
};
</script>

<style scoped>
.about-us {
    display: flex;
    flex-direction: column;
    padding: 50px;
    color: white;
    border-radius: 12px;
    gap: 32px;
    text-align: left;
}

.about-us-card {
    display: flex;
    flex-direction: column;
    gap: 24px;
    text-align: left;
}

.about-us-block {
    display: flex;
    justify-content: space-between;
    align-items: center;
    text-align: left;
    gap: 30px;
}

.about-us-text {
    flex: 1;
    max-width: 600px;
    text-align: left;
}

.about-us-text h2 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 70px;
    margin: 0;
    text-align: left;
}

.about-us-text p {
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    line-height: 1.6;
    text-align: left;
}

.stages__buttons {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 24px;
}

.pill-button {
    background: linear-gradient(94.98deg, #0d2f68 0%, #d51117 100%);
    color: white;
    padding: 16px 32px;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
}

.round-button {
    background-color: #FFFFFF1A;
    border: none;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.round-button img {
    width: 24px;
    height: 24px;
}

.about-image {
    width: 603px;
    height: 350px;
}

.list-block {
    display: flex;
    justify-content: space-between;
    margin-top: 32px;
    padding-top: 24px;
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    gap: 24px;
}

.list-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    flex: 1;
}

.list-number {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 48px;
    color: #d51117;
}

.list-text {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    color: #FFFFFF80;
}

.list-item-img{
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    flex: 1;
    gap: 20px;
}

.list-item-img img{
    margin-right: 24px;
    aspect-ratio: 1 / 1;
    width: 41px;
    height: 41px;
    align-items: start;
}

.list-text-img {
    font-family: 'Inter';
    font-size: 16px;
    font-weight: 300;
    line-height: 24px;
    text-align: left;
    color: #fff;
}

.list-item img {
    margin-right: 24px;
    aspect-ratio: 1 / 1;
    width: 41px;
    height: 41px;
}

.stage-of-work-card {
    text-align: center;
    box-sizing: border-box;
    background-image: url(../assets/stage1.webp);
    border-radius: 15px;
    padding-bottom: 80px;
}

.stage-title h2{
    font-family: 'Bebas Neue';
    font-size: 70px;
    margin-bottom: 10px;
}

.stage-title p {
    font-family: 'Inter';
    font-size: 18px;
    color: #FFFFFF80;
}

.stage-title h2 span {
    color: #f8534a;
}

.item-stage {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-top: 20px;
}

.item {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}

.item img {
    width: 38px;
    height: 38px;
}

.line_img {
    width: 203px;
    height: 2px;
}
</style>