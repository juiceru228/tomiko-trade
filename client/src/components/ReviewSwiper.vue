<template>
    <div class="swiper-column">
        <swiper :modules="modules" :slides-per-view="4" :space-between="10" 
          navigation :pagination="{ clickable: true }" 
          @swiper="onSwiper" @slideChange="onSlideChange" :loop="true">
        <swiper-slide v-for="review in reviews" :key="review.id">
            <ReviewCard 
            :name="review.user.name"
            :rating="review.rating"
            :date="formatDate(review.date_created)"
            :avatarColor="'#8A2BE2'" />
        </swiper-slide>
        </swiper>
    </div>
</template>
  
<script>
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Navigation, Pagination, A11y } from 'swiper/modules';
  import 'swiper/css/navigation';
  import 'swiper/css/pagination';
  import 'swiper/swiper-bundle.css';
  import ReviewCard from './ReviewCard.vue';
  
  export default {
    name: `ReviewSwiper`,
    components: {
      Swiper,
      SwiperSlide,
      ReviewCard
    },
    
    data() {
      return {
        reviews: []
      };
    },
    async mounted() {
      await this.fetchReviews();
    },
    methods: {
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('ru-RU', options);
    }
  },
  mounted() {
    fetch('http://localhost:8080/api/reviews/')
      .then(response => response.json())
      .then(data => {
        this.reviews = data.reviews;
      });
  },
  setup() {
        const onSwiper = (swiper) => {
            console.log(swiper);
        };
        const onSlideChange = () => {
            console.log('slide change');
        };
        return {
            onSwiper,
            onSlideChange,
            modules: [Navigation, Pagination, A11y],
        };
    },
  
}
</script>
  
<style scoped>

</style>
  