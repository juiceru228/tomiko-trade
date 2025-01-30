<template>
    <div class="logos_brand logos_brand2">
            <div class="">
                <div class="logo-carousel">
                        <div class='marquee2'>
                                <div style="display: inline-flex">
                                        <a href="" class="red-line">Денежное вознаграждение за рекомендацию</a>
                                        <span class="red-line">|</span>
                                        <a href="" class="red-line">Оплата депозита двумя частями</a>
                                        <span class="red-line">|</span>
                                        <a href="" class="red-line">Система лояльности для оптовых заказов</a>
                                        <span class="red-line">|</span>     
                                </div>
                                <div style="display: inline-flex">      
                                        <a href="" class="red-line">Денежное вознаграждение за рекомендацию</a>
                                        <span class="red-line">|</span>
                                        <a href="" class="red-line">Оплата депозита двумя частями</a>
                                        <span class="red-line">|</span>
                                        <a href="" class="red-line">Система лояльности для оптовых заказов</a>
                                        <span class="red-line">|</span>
                                </div>
                                <div style="display: inline-flex">
                                        <a href="" class="red-line">Денежное вознаграждение за рекомендацию</a>
                                        <span class="red-line">|</span>                               
                                        <a href="" class="red-line">Оплата депозита двумя частями</a>
                                        <span class="">|</span>                                
                                        <a href="" class="red-line">Система лояльности для оптовых заказов</a>
                                        <span class="red-line">|</span>                                
                                </div>
                                
                                <div style="display: inline-flex">                                
                                        <a href="" class="red-line">Денежное вознаграждение за рекомендацию</a>
                                        <span class="red-line">|</span>                                
                                        <a href="" class="red-line">Оплата депозита двумя частями</a>
                                        <span class="red-line">|</span>                                
                                        <a href="" class="red-line">Система лояльности для оптовых заказов</a>
                                        <span class="red-line">|</span>                                
                                </div>
                                
                                <div style="display: inline-flex">                                
                                        <a href="" class="red-line">Денежное вознаграждение за рекомендацию</a>
                                        <span class="red-line">|</span>                                
                                        <a href="" class="red-line">Оплата депозита двумя частями</a>
                                        <span class="red-line">|</span>                                
                                        <a href="" class="red-line">Система лояльности для оптовых заказов</a>
                                        <span class="red-line">|</span>                                
                                </div>
                                
                                <div style="display: inline-flex">                                
                                        <a href="" class="red-line">Денежное вознаграждение за рекомендацию</a>
                                        <span class="red-line">|</span>                                
                                        <a href="" class="red-line">Оплата депозита двумя частями</a>
                                        <span class="red-line">|</span>                                
                                        <a href="" class="red-line">Система лояльности для оптовых заказов</a>
                                        <span class="red-line">|</span>                               
                                </div>                       
                        </div>
                </div>
            </div>
        </div>
</template>

<script>
export default {
        name: "CatuselL",
}
</script>

<style scoped>
.logos_brand2 {
        max-width: 2000px;
        margin-bottom: -10px;
}
.logos_brand .logo-carousel {
        max-width: 2000px;
        width: 100%;
        overflow: hidden;
        padding: 10px 0;
}

.marquee2 {
        max-width: 1800px;
        animation: scrolling 30s linear infinite;
        white-space: nowrap;
        display: inline-block;
        will-change: transform;
}

.marquee2 div {
        background-color: #d51117;
}

@keyframes scrolling {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(-100%);
    }
  }


span.red-line {
        width: 40px;
        justify-content: center;
        color: #FFFFFF66;
        font-weight: 400;
}
.red-line, .blue-line {
        cursor: pointer;
}
.red-line {
        height: 40px;
        background-color: #d51117;
        color: white;
        font-size: 16px;
        font-weight: 600;
        line-height: 24px;
        text-align: left;
        display: flex;
        align-items: center;
}

span.red-line {
        width: 40px;
        justify-content: center;
        color: #FFFFFF66;
        font-weight: 400;
}
</style>