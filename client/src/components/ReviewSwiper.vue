<template>
    <div class="swiper-column">
        <swiper :slides-per-view="4" :space-between="10"
        pagination navigation :loop="false" :preventClicks="true">
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
  }
}
</script>
  
<style scoped>

</style>
  