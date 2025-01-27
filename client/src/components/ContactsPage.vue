<template>
    <section class="contacts">
        <div class="container">
            <div class="contact_row">
                <div class="contact_left">
                    <div class="title">
                        <h2>Контактная информация
                            <img src="../assets/contact_title_image.webp" alt="Контактная информация">
                        </h2>
                    </div>
                    <p class="section_description">Оставьте свою заявку и наш менеджер свяжется с Вами для уточнения
                        деталей.</p>
                    <div class="contact_item">
                        <p>Звонок по России бесплатный</p>
                        <a href="tel:+8 (800) 775-67-29">8 (800) 775-67-29</a>
                    </div>
                    <div class="contact_item">
                        <p>WhatsApp</p>
                        <a href="https://wa.me/79244202432" target="_blank">+7 924 420-24-32</a>
                    </div>
                    <div class="contact_item">
                        <p>Офис</p>
                        <div>г. Владивосток, ул. Жигура 9в, 1 этаж, офис 1</div>
                    </div>
                </div>
                <form class="contact_form" id="contactForm" method="post" action="">
                    <input type="hidden" name="csrfmiddlewaretoken"
                        value="WnXA2zTNsNQ0cY8mt4Z7OJIyOy161QIbX70MVcyuYtZooRtgNQTkbTu9UEmsUh5E">
                    <div class="form_group">
                        <label>
                            <p>Имя</p>
                            <input type="text" name="name" placeholder="Введите имя" pattern="^[A-Za-zА-Яа-яЁё\s]+$"
                                title="Имя должно содержать только буквы и пробелы." maxlength="20" required
                                aria-describedby="id_name_helptext" id="id_name">
                        </label>
                        <label>
                            <p>Телефон</p>
                            <input type="tel" name="phone_number" placeholder="+7"
                                pattern="^\+7 [0-6,9]\d{2} \d{3} \d{2} \d{2}$"
                                title="Формат: &#x27;+7 999 999 99 99&#x27; и номер не должен начинаться с 8 или 7 после кода +7"
                                maxlength="16" required aria-describedby="id_phone_number_helptext"
                                id="id_phone_number">
                        </label>
                    </div>
                    <div class="form_group">
                        <label>
                            <p>Уточните свой вопрос</p>
                            <textarea name="content" cols="40" rows="10"
                                placeholder="Введите текст сообщения, укажите страну, марку и год машины."
                                maxlength="200" id="id_content"></textarea>
                        </label>
                    </div>
                    <div class="form_group">
                        <label>
                            <span class="checkmark"></span>
                            <input type="checkbox" name="privacy_policy_agreed" required id="id_privacy_policy_agreed"
                                checked>
                            <p>С <a target="_blank" href="/static/files/tomiko-trade.pdf">правилами политики
                                    конфиденциальности</a> ознакомлен</p>
                        </label>
                    </div>
                    <div class="form_group">
                        <button type="submit" name="submit">Отправить</button>
                    </div>
                </form>
            </div>
        </div>

        <div class="position-fixed top-0 end-0 p-3" style="z-index: 11">
            <div id="liveToast" class="toast hide" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header">
                    <img src="/static/img/modal_logo.webp" alt="logo">
                </div>
                <div class="toast-body">
                    Вы оставили свой запрос, скоро мы свяжемся с Вами!
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'ContactPage'
}
</script>

<style scoped>
.contacts {
    margin: 0 0 116px 0;
}

.contacts .title h2 {
    font-family: Bebas-Neue, Arial, sans-serif;
    font-size: 70px;
    font-weight: 700;
    line-height: 100%;
    color: #FFF;
}

.contacts .title img {
    width: 63px;
    height: 60px;
    -o-object-fit: cover;
    object-fit: cover;
    -o-object-position: center;
    object-position: center;
}

.contacts .section_description {
    font-family: Inter;
    font-size: 18px;
    font-weight: 300;
    color: rgba(255, 255, 255, 0.5);
    margin: 0 0 60px 0;
}

.contacts .contact_row {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    gap: 30px;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-align: start;
    -ms-flex-align: start;
    align-items: flex-start;
}

.contacts .contact_item p {
    font-family: Inter;
    font-size: 16px;
    font-weight: 300;
    line-height: normal;
    letter-spacing: -0.64px;
    color: rgba(255, 255, 255, 0.5);
}

.contacts .contact_item a,
.contacts .contact_item div {
    font-family: Inter;
    font-size: 18px;
    font-weight: 500;
    line-height: normal;
    letter-spacing: -0.72px;
    color: #FFF;
}

.contacts .contact_left {
    max-width: 405px;
}

.contacts .contact_form {
    padding: 40px;
    border-radius: 28px;
    background: #081e36;
}

.contacts .contact_form .form_group p {
    font-family: Inter;
    font-size: 14px;
    font-weight: 400;
    color: #FFF;
    margin: 0 0 8px 0;
}

.contacts .contact_form .form_group input,
.contacts .contact_form .form_group textarea {
    padding: 16px;
    font-size: 16px;
    font-weight: 400;
    width: 100%;
}

.contacts .contact_form .form_group input,
.contacts .contact_form .form_group textarea,
.contacts .contact_form .form_group button {
    border-radius: 32px;
    background: #20344a;
    border: 0;
    outline: 0;
    color: #FFF;
    font-family: Inter;
    line-height: normal;
}

button,
input,
optgroup,
select,
textarea {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
}

contacts .contact_form .form_group label:has(input[type=checkbox]) p {
    margin: 0;
}

.contacts .contact_form .form_group p {
    font-family: Inter;
    font-size: 14px;
    font-weight: 400;
    color: #FFF;
    margin: 0 0 8px 0;
}

.contacts .contact_form .form_group label:has(input[type=checkbox]) p a {
    color: #fd554b;
}

[type=button]:not(:disabled),
[type=reset]:not(:disabled),
[type=submit]:not(:disabled),
button:not(:disabled) {
    cursor: pointer;
}

[type=button],
[type=reset],
[type=submit],
button {
    -webkit-appearance: button;
}

button,
select {
    text-transform: none;
}

button,
input,
optgroup,
select,
textarea {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
}

button {
    border-radius: 0;
}
</style>