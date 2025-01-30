<template>
    <div v-if="visible" class="modal-overlay" @click="close">
        <div class="modal-content" @click.stop>
            <img src="../assets/cross.svg" @click="close" class="modal-close" />
            <p class="title">Экономия до <span>30%</span> от рынка авто в наличии</p>
            <img src="../assets/economy.png" class="economy-img">
            <div class="stages__buttons">
                <button class="pill-button" @click="$emit('open-consultation')">Получить консультацию</button>
                <button class="round-button">
                    <img src="../assets/whatsapp.png" alt="WhatsApp" class="icon-whatsapp" />
                </button>
                <button class="round-button">
                    <img src="../assets/telegram.png" alt="Telegram" class="icon-whatsapp" />
                </button>
            </div>
        </div>
    </div>
</template>


<script>
import ModalForm from '../components/ModalForm.vue';
import ValidationForm from '../components/ValidationForm.vue';

export default {
    props: {
        visible: {
            type: Boolean,
        },
    },
    components: {
        ModalForm,
        ValidationForm,
    },
    emits: ['close', 'open-consultation'],
    methods: {
        close() {
            this.$emit('close');
        },
    },
};
</script>

<style scoped>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-content {
    background: #081E36;
    border-radius: 28px;
    width: 899px;
    height: 768px;
    position: relative;
    padding: 24px 40px 40px 40px;
}

.modal-close {
    margin-right: 10px;
    margin-top: 10px;
    color: #fff;
    width: 15.76px;
    height: 15.76px;
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 16px;
    cursor: pointer;
    z-index: 10;
}

.stages__buttons {
    display: flex;
    gap: 12px;
    padding-top: 24px;
    flex-direction: row;
    margin-bottom: 16px;
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

.economy-img {
    width: Hug (819px)px;
    height: Hug (504px)px;
    gap: 20px;
    opacity: 0px;
}

.title {
    padding-top: 12px;
    font-family: 'Inter';
    font-size: 24px;
    text-align: left;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: #FFFFFF;
    text-align: left;
}

.title span {
    font-family: 'Inter';
    font-size: 48px;
    font-weight: 900;
    line-height: 58.09px;
    text-align: left;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: #f8534a;
}

</style>