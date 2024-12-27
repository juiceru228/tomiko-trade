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
                                      <li><router-link to="">Клипы</router-link></li>
                                      <li><router-link to="">Отзывы</router-link></li>
                                </ul>
                                <ul>
                                  <li></li>
                                  <li><router-link to="">Условия работы</router-link></li>
                                  <li><router-link to="">Акции</router-link></li>
                                  <li><router-link to="">Контакты</router-link></li>
                              </ul>
                          </div>
                      </div>
                      <div class="footer_contact">
                          <p>Звонок по России бесплатный</p>
                          <a href="tel:+8 (800) 775-67-29">8 (800) 775-67-29</a>
                          <div class="social">
                              <a href="https://wa.me/79244202432" target="_blank"><img loading="lazy" src="/static/img/ico-whatsapp.svg" alt="whatsapp"></a>
                              <a href="https://vk.com/tomiko_trade" target="_blank"><img loading="lazy" src="/static/img/ico-wk2.svg" alt="ВК"></a>
                              <a href="https://www.instagram.com/praviyrul.jp?igsh=N3VucnNibWsyZzVk" target="_blank"><img loading="lazy" src="/static/img/ico-insta2.svg" alt="Instagram"></a>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
          <div class="footer_bottom">
              <div class="container">
                  <p>© 2024 ООО «Автоцентр-ВЛ» Автомобили под заказ из Кореи, Китая и Японии</p>
                  <p><a target="_blank" href="/static/files/%D0%9F%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0%20%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20tomiko-trade.pdf">Политика конфиденциальности</a></p>
              </div>
          </div>
    </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style>
footer {
    border-top: 4px solid #d51117;
    background: #081e36;
    box-sizing: border-box;
}

footer {
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
</style>