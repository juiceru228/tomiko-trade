<template>
    <div class="not-found">
        <div class="pic-not-found">
            <img alt="NotFoundPic" src="../assets/NotFoundPic.png">
        </div>
        <div class="text-not-found">
            <span class="title">Ничего нет, возможно страница была удалена</span>
            <span class="subtitle">Оставьте совю заявку и наш менеджер свяжется с Вами для уточнения деталей</span>
        </div>
        <div class="buttons-container">
            <button class="pill-button" id="consultation">Получить консультацию</button>
            <button class="round-button"><img alt="whatsapp" src="../assets/whatsapp.png"></button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'NotFound',
};
</script>

<style scoped>
.not-found {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0px;
    gap: 46px;

    position: absolute;
    width: 663px;
    height: 394px;
    left: calc(50% - 663px/2);
    top: calc(50% - 394px/2 - 65.01px);
}

.text-not-found {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0px;
    gap: 8px;
}

.title {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 600;
    font-size: 18px;
    line-height: 22px;
    text-align: center;

    color: #FFFFFF;
}

.subtitle {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 150%;
    display: flex;
    align-items: center;
    text-align: center;

    color: rgba(255, 255, 255, 0.5);
}

.buttons-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
    padding: 0px;
    gap: 12px;

    width: 382px;
    height: 70px;


    flex: none;
    order: 1;
    flex-grow: 0;
}

.pill-button {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 24px 40px;
    gap: 12px;
    background: linear-gradient(94.98deg, #0D2F68 0%, #D51117 100%);
    border-radius: 60px;
    border: none;
    outline: none;
    box-shadow: none;
    cursor: pointer;
}

#consultation {
    font-family: 'Inter';
    font-style: normal;
    font-weight: 600;
    font-size: 18px;
    line-height: 22px;

    color: #FFFFFF;
}

.round-button {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 21px;
    gap: 10px;
    width: 70px;
    height: 70px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 122px;
    flex: none;
    order: 1;
    border: none;
    flex-grow: 0;
    outline: none;
    box-shadow: none;
    cursor: pointer;
}

.round-button img {
    width: 28px;
    height: 28px;
    flex: none;
    order: 1;
    flex-grow: 0;
}

button:focus,
button:active {
    outline: none;
    box-shadow: none;
}

.pic-not-found {
    width: 200px;
    height: 200px;

    flex: none;
    order: 0;
    flex-grow: 0;
}

.pic-not-found img {
    bottom: 0;
    width: 116.63px;
    height: 116px;
}
</style>