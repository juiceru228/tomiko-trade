<template>
    <div class="logos_brand">
      <div class="logo-carousel" ref="marquee">
        <div class="marquee">
          <div class="marquee-inner" ref="marqueeInner" :style="{ transform: 'translateX(' + translateX + 'px)' }">
            <button v-for="(logo, index) in logos" :key="index" @click="openQuestionnaireForm()">
              <img loading="lazy" :src="logo.src" :alt="logo.alt">
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script>
export default {
    name: "LentaFunc",
    data() {
      return {
        logos: [
          { src: require('../assets/brand1.webp'), alt: 'Logo 1' },
          { src: require('../assets/brand2.webp'), alt: 'Logo 2' },
          { src: require('../assets/brand3.webp'), alt: 'Logo 3' },
          { src: require('../assets/brand4.webp'), alt: 'Logo 4' },
          { src: require('../assets/brand5.webp'), alt: 'Logo 5' },
          { src: require('../assets/brand6.webp'), alt: 'Logo 6' },
          { src: require('../assets/brand7.webp'), alt: 'Logo 7' },
          { src: require('../assets/brand8.webp'), alt: 'Logo 8' },
          { src: require('../assets/brand9.webp'), alt: 'Logo 9' },
          { src: require('../assets/brand10.webp'), alt: 'Logo 10' },
          { src: require('../assets/brand11.webp'), alt: 'Logo 11' },
          { src: require('../assets/brand12.webp'), alt: 'Logo 12' },
          { src: require('../assets/brand13.webp'), alt: 'Logo 13' },
          { src: require('../assets/brand1.webp'), alt: 'Logo 1' },
          { src: require('../assets/brand2.webp'), alt: 'Logo 2' },
          { src: require('../assets/brand3.webp'), alt: 'Logo 3' },
          { src: require('../assets/brand4.webp'), alt: 'Logo 4' },
          { src: require('../assets/brand5.webp'), alt: 'Logo 5' },
          { src: require('../assets/brand6.webp'), alt: 'Logo 6' },
          { src: require('../assets/brand7.webp'), alt: 'Logo 7' },
          { src: require('../assets/brand8.webp'), alt: 'Logo 8' },
          { src: require('../assets/brand9.webp'), alt: 'Logo 9' },
          { src: require('../assets/brand10.webp'), alt: 'Logo 10' },
          { src: require('../assets/brand11.webp'), alt: 'Logo 11' },
          { src: require('../assets/brand12.webp'), alt: 'Logo 12' },
          { src: require('../assets/brand13.webp'), alt: 'Logo 13' },
          { src: require('../assets/brand1.webp'), alt: 'Logo 1' },
          { src: require('../assets/brand2.webp'), alt: 'Logo 2' },
          { src: require('../assets/brand3.webp'), alt: 'Logo 3' },
          { src: require('../assets/brand4.webp'), alt: 'Logo 4' },
          { src: require('../assets/brand5.webp'), alt: 'Logo 5' },
          { src: require('../assets/brand6.webp'), alt: 'Logo 6' },
          { src: require('../assets/brand7.webp'), alt: 'Logo 7' },
          { src: require('../assets/brand8.webp'), alt: 'Logo 8' },
          { src: require('../assets/brand9.webp'), alt: 'Logo 9' },
          { src: require('../assets/brand10.webp'), alt: 'Logo 10' },
          { src: require('../assets/brand11.webp'), alt: 'Logo 11' },
          { src: require('../assets/brand12.webp'), alt: 'Logo 12' },
          { src: require('../assets/brand13.webp'), alt: 'Logo 13' },
        ],
        translateX: 0,
        animationSpeed: 2,
        animationFrameId: null,
      };
    },
    methods: {
      openQuestionnaireForm() {
        console.log('Открыть анкету');
      },
      startAnimation() {
        const totalWidth = this.$refs.marqueeInner.scrollWidth;
        const containerWidth = this.$refs.marquee.offsetWidth;
  
        const animate = () => {
          this.translateX -= this.animationSpeed;
          if (Math.abs(this.translateX) >= totalWidth) {
            this.translateX = containerWidth;
          }
  
          this.animationFrameId = requestAnimationFrame(animate);
        };
  
        animate();
      },
      stopAnimation() {
        cancelAnimationFrame(this.animationFrameId);
      },
    },
    mounted() {
      this.startAnimation();
    },
    beforeUnmount() {
      this.stopAnimation();
    },
  };
</script>

<style scoped>     
.logos_brand {
    background-color: #011224;
    margin-bottom: 52px;
    overflow: hidden;
    width: 2400px;
    max-width: 2000px;
}

.logos_brand .logo-carousel {
    max-width: 2000px;
    width: 2400px;
    overflow: hidden;
    padding: 10px 0;
}

div {
    display: block;
    unicode-bidi: isolate;
}

element.style {
    max-width: 2000px;
    margin-right: 0px;
    float: left;
    display: inline-flex;
    width: 2400px;
    margin-left: 0px;
}

.marquee img {
    -webkit-transition: -webkit-transform .3s ease;
    transition: -webkit-transform .3s ease;
    transition: transform .3s ease;
    transition: transform .3s ease, -webkit-transform .3s ease;
    width: 100px;
    height: 100px;
}

img, svg {
    vertical-align: middle;
}

button, select {
    text-transform: none;
}
button, input, optgroup, select, textarea {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
}
button {
    border-radius: 0;
}

.logo-carousel {
    position: relative;
    white-space: nowrap;
}
      
.marquee {
    display: flex;
    align-items: center;
}
      
.marquee-inner {
    display: flex;
    transition: transform linear;
}
</style>