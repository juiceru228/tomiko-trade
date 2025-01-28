<template>
    <section class="subscribe">
    <div class="container">
        <div class="subscribe_row">
            <img loading="lazy" src="../assets/subscribe_image.webp" alt="Подпишись" class="subscribe_image">
            <div class="subscribe_right">
                <div class="title">
                    <h2><span>Подпишись</span>, чтобы не пропустить выгодные предложения от нашей компании!</h2>
                </div>
                <a href="https://vk.com/tomiko_trade" class="subscribe_item" target="_blank">
                    <div class="subscribe_item_img">
                        <img loading="lazy" src="../assets/ico-wk.svg" alt="ВК">
                    </div>
                    <div>
                        VK
                        <img loading="lazy" src="../assets/arr_link.svg" alt="Стрелка2">
                    </div>
                </a>
                <a href="https://www.instagram.com/praviyrul.jp?igsh=N3VucnNibWsyZzVk" class="subscribe_item" target="_blank">
                    <div class="subscribe_item_img">
                        <img loading="lazy" src="../assets/ico-insta.svg" alt="Inst">
                    </div>
                    <div>
                        Instagram
                        <img loading="lazy" src="../assets/arr_link.svg" alt="Стрелка3">
                    </div>
                </a>
            </div>
        </div>
    </div>
</section>
</template>

<script>
export default {
    name: 'SubscrivePage',
};
</script>

<style scoped>
.subscribe {
    margin: 0 0 174px 0;
    padding: 80px 0 0 0;
}
@media only screen and (max-width: 1200px) {
    .subscribe .subscribe_image {
        max-width: 450px;
        margin: -50px 0 0 0;
    }
}
.subscribe .subscribe_image {
    margin: -100px 0 -80px 0;
    width: 505px;
    aspect-ratio: 505 / 693;
}
.subscribe .subscribe_row::before {
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    background: #081e36;
    border-radius: 28px;
    z-index: -1;
}
.subscribe .subscribe_row .subscribe_right {
    padding-block: 40px;
}
.subscribe .title h2 span {
    color: #fd554b;
}

@media only screen and (max-width: 1200px) {
    .subscribe .title h2 {
        font-size: 60px;
    }
}
.subscribe .title h2 {
    font-size: 70px;
    font-weight: 700;
    line-height: normal;
    color: #FFF;
}
.subscribe .subscribe_row::after {
    position: absolute;
    content: "";
    width: 90%;
    height: 87px;
    left: 50%;
    bottom: -12px;
    -webkit-transform: translate(-50%, 0) rotate(-1deg);
    transform: translate(-50%, 0) rotate(-1deg);
    background-color: #d51117;
    border-radius: 28px;
    z-index: -2;
}

@media only screen and (max-width: 1200px) {
    .subscribe .subscribe_row {
        gap: 40px;
    }
}
.subscribe .subscribe_row {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    gap: 144px;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    border-radius: 28px;
    background: #081e36;
    padding: 0 140px 0 0;
    position: relative;
    z-index: 1;
}
.subscribe .subscribe_item {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    gap: 24px;
    font-size: 24px;
    font-weight: 300;
    color: #FFF;
    margin: 0 0 12px 0;
}
</style>