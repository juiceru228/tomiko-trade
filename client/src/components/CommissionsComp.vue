<template>
    <div class="container">
        <div class="commissions">
            <h1>КОМИССИ</h1>
            <img src="../assets/commissions.png" alt="Комоссии" class="commissions-img">
            <p>У нас доступна оплата депозита частями</p>
            <div class="button">
                <button class="pill-button">
                    Подробнее тут
                    <img src="../assets/arrow.png" class="arrow-icon">
                </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "CommissionsComp"
}
</script>

<style scoped>
.container {
    background-color: #081E36;
    gap: 40px;
    display: flex;
    align-items: center;
}

.commissions {
    padding-top: 50px;
    padding-bottom: 50px;
}

h1 {
    font-family: 'Bebas Neue';
    font-size: 70px;
    text-align: center;
    gap: 8px;
}

.commissions-img {
    width: 455px;
    height: 180px;
    gap: 16px;
    margin-top: 40px;
    margin-bottom: 40px;
}

p {
    font-family: 'Inter';
    font-size: 18px;
    color: #FFFFFF;
    margin-bottom: 22px;
}

.button {
    margin-left: auto;
    margin-right: auto;
}

.pill-button {
    background: linear-gradient(94.98deg, #0d2f68 0%, #d51117 100%);
    color: white;
    padding: 24px 40px 24px 40px;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 12px;
    margin-left: auto;
    margin-right: auto;
}

.arrow-icon {
    width: 13.5px;
    height: 13.5px;
    top: 5.25px;
    left: 5.25px;
    gap: 0px;
    opacity: 0px;
}
</style>