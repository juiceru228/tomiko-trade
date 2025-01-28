<template>
   <footer>
            <div class="footer_top">
                <div class="container">
                    <div class="footer_row">
                        <div class="footer_left">
                            <a href="/" class="brand_logo">
                                <img loading="lazy" src="../assets/logo.webp" alt="logo">
                            </a>
                            <div class="footer_links">
                                <ul>
                                  <li>Каталог</li>
                                  <li><router-link to="/korea">Авто из Кореи</router-link></li>
                                  <li><router-link to="/china">Авто из Китая</router-link></li>
                                  <li><router-link to="/japan">Авто из Японии</router-link></li>
                                </ul>
                                <ul>
                                    <li>Компания</li>
                                        <li><router-link to="">О компании</router-link></li>
                                        <li><router-link to="">Доставка</router-link></li>
                                        <li><router-link to="">Отзывы</router-link></li>
                                </ul>
                            </div>
                        </div>
                        <div class="footer_contact">
                            <p>Звонок по России бесплатный</p>
                            <a href="tel:+8 (800) 775-67-29">8 (800) 775-67-29</a>
                            <div class="social">
                                <a href="https://wa.me/79244202432" target="_blank"><img loading="lazy" src="../assets/ico-whatsapp.svg" alt="whatsapp"></a>
                                <a href="https://vk.com/tomiko_trade" target="_blank"><img loading="lazy" src="../assets/ico-wk2.svg" alt="ВК"></a>
                                <a href="https://www.instagram.com/praviyrul.jp?igsh=N3VucnNibWsyZzVk" target="_blank"><img loading="lazy" src="../assets/ico-insta2.svg" alt="Instagram"></a>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <div class="footer_bottom">
                <div class="container">
                    <p>© 2024 ООО «Правый руль» Автомобили под заказ из Кореи, Китая и Японии</p>
                    <p><a target="_blank" href="">Политика конфиденциальности</a></p>
                </div>
            </div>

    </footer>
</template>

<script>
export default {
    name: 'AppFooter'
}
</script>

<style scoped>
footer {
    border-top: 4px solid #d51117;
    background: #081e36;
    box-sizing: border-box;
    display: block;
    unicode-bidi: isolate;
}

footer .footer_left {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    gap: 60px;
}

footer .footer_top {
    padding: 40px 0 24px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

footer .footer_links {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    gap: 80px;
}

footer .footer_row {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    gap: 24px;
}

ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

dl,
ol,
ul {
    margin-top: 0;
    margin-bottom: 1rem;
}

ol,
ul {
    padding-left: 2rem;
}

ul {
    display: block;
    list-style-type: disc;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 40px;
    unicode-bidi: isolate;
}

footer .brand_logo img {
    width: 80px;
    height: 80px;
}

img,
svg {
    vertical-align: middle;
}

img {
    overflow-clip-margin: content-box;
    overflow: clip;
}

footer .footer_bottom {
    padding: 24px 0;
}

footer .social img {
    width: 24px;
    height: 24px;
    aspect-ratio: 1 / 1;
}

footer .social {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    gap: 12px;
}


footer .footer_contact p {
    font-size: 20px;
    font-style: normal;
    font-weight: 300;
    margin: 0 0 12px 0;
    color: rgba(255, 255, 255, 0.5);
}

footer .footer_contact a:not(.social a) {
    font-size: 48px;
    font-weight: 700;
    color: #FFF;
    margin: 0 0 16px 0;
}

footer .footer_links a {
    font-size: 16px;
    font-weight: 300;
    color: rgba(255, 255, 255, 0.5);
}

a {
    text-decoration: none !important;
}

a {
    color: white;
    text-decoration: underline;
}

li {
    display: list-item;
    text-align: -webkit-match-parent;
    unicode-bidi: isolate;
}

li {
    list-style: none;
}

footer .footer_links li {
    font-size: 24px;
    font-weight: 600;
    line-height: normal;
    color: #FFF;
    margin: 0 0 12px 0;
}
</style>