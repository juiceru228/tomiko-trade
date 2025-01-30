<template>
  <div class="comments">
    <p>
      <a name="reviews" style="scroll-margin-top: 150px;"></a>
      <a name="reviews2" style="scroll-margin-top: 720px;"></a>
    </p>
    <div class="container">
      <div class="section_top">
        <div class="title">
          <h2>Отзывы <img loading="lazy" src="../assets/star2.webp" alt="Звездочка">4.5</h2>
        </div>
        <div class="comment_links">
          <a href="https://2gis.ru/vladivostok/firm/70000001067259118/tab/reviews" target="_blank">
            2ГИС
            <img loading="lazy" src="../assets/arr_link.svg" alt="Стрелка">
          </a>

          <a href="https://www.vl.ru/pravyj-rul-avto-iz-yaponii" target="_blank">
            VL справочник
            <img loading="lazy" src="../assets/arr_link.svg" alt="Стрелка">
          </a>

          <a href="https://yandex.ru/maps/org/pravy_rul/114125692870/reviews/?ll=131.886877%2C43.098752&amp;tab=reviews&amp;z=15"
            target="_blank">
            Яндекс карты
            <img loading="lazy" src="../assets/arr_link.svg" alt="Стрелка">
          </a>
        </div>
      </div>
      <div class="swiper-column">
        <swiper :modules="modules" :slides-per-view="4" :loop="true" :space-between="10">
          <swiper-slide v-for="(pair, index) in groupedReviews" :key="index">
            <ReviewCard v-for="review in pair" :key="review.id" :name="review.user.name" :rating="review.rating"
              :date="formatDate(review.date_created)" :avatarColor="'#A84CA8'" />
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation, Pagination, A11y } from 'swiper/modules';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/swiper-bundle.css';
import ReviewCard from './ReviewCard.vue';
import axios from 'axios';
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
  computed: {
    groupedReviews() {
      const pairs = [];
      for (let i = 0; i < this.reviews.length; i += 2) {
        pairs.push(this.reviews.slice(i, i + 2));
      }
      return pairs;
    }
  },

  methods: {
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(dateString).toLocaleDateString('ru-RU', options);
    },

    async fetchReviews() {
      this.loading = true;
      try {
        const response = await axios.get('/api/reviews/');
        this.reviews = response.data.reviews;
        console.log('reviews', this.reviews);
      } catch (error) {
        this.error = 'Error fetching reviews';
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
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
.comments .section_top {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: end;
  -ms-flex-align: end;
  align-items: flex-end;
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  margin: 0 0 40px 0;
}

.comments .comment_links {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  gap: 24px;
}

.comments .comment_links a {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  gap: 8px;
  font-family: Inter;
  font-size: 16px;
  font-style: normal;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.5);
}

.comments .title h2 {
  font-family: Bebas-Neue, Arial, sans-serif;
  font-size: 70px;
  font-weight: 700;
  line-height: 70px;
  text-align: left;
  color: #fff;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.comments .title h2 img {
  margin-left: 24px;
  margin-right: 13px;
  aspect-ratio: 1 / 1;
  width: 48px;
  height: 48px;
}

img,
svg {
  vertical-align: middle;
}
</style>