<template>
  <HelloPage/>
  <swiperRelevant/>
  <LentaFunc/>
  <EtapPage/>
  <AboutUs/>
  <CaruselFuncL/>
  <CaruselFuncR/>
  <ReviewSwiper/>
  <VKclipsPage/>
  <subcribe/>
  <contacts/>
</template>

<script>
import VKclipsPage from '../components/VKclips.vue';
import contacts from '@/components/ContactsPage.vue';
import subcribe from '@/components/subcribe.vue';
import swiperRelevant from '@/components/SwiperCars.vue';
import AboutUs from '@/components/AboutUs.vue';
import LentaFunc from '@/components/LentaFunc.vue';
import CaruselFuncL from '@/components/CaruselFuncL.vue';
import CaruselFuncR from '@/components/CaruselFuncR.vue';
import ReviewSwiper from '@/components/ReviewSwiper.vue';
import EtapPage from '../components/EtapPage.vue';
import HelloPage from '../components/HelloPage.vue';
export default {
  name: 'MainPage',
  components: {
    VKclipsPage,
    contacts,
    subcribe,
    swiperRelevant,
    AboutUs,
    LentaFunc,
    CaruselFuncL,
    CaruselFuncR,
    ReviewSwiper,
    EtapPage,
    HelloPage,
  }
};
</script>

<style scoped>
</style>