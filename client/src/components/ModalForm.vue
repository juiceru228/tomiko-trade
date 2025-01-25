<template>
    <div v-if="visible" class="modal-overlay" @click="close">
        <div class="modal-content" @click.stop>
            <img src="../assets/cross.svg" @click="close" class="modal-close" />
            <slot></slot>
        </div>

    </div>
</template>

<script>
export default {
    props: {
        visible: {
            type: Boolean,
            default: false,
        },
    },
    emits: ['close'],
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
    width: 640px;
    height: 598px;
    position: relative;
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
</style>