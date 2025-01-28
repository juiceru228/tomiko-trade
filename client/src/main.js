/* eslint-disable */
import { createApp } from 'vue'
import App from './App.vue'
import axios from './axios';
import {createRouter, createWebHistory} from 'vue-router';
// main.js/ts
import {createBootstrap} from 'bootstrap-vue-next'

// Add the necessary CSS
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

import MainPage from './views/MainPage.vue'
import ChinaPage from './views/ChinaPage.vue'
import KoreaPage from './views/KoreaPage.vue'
import JapanPage from './views/JapanPage.vue'
import CarDetail from './views/CarDetail.vue'
import ContactPage from './views/ContactPage.vue'
import NotFound from './views/NotFound.vue'
import SwiperCars from './components/SwiperCars.vue'
import AboutUs from './views/AboutUs.vue'
import PromotionsComponent from './views/Promotions.vue';
const routes = [
	{path: '/', component:MainPage},
	{path: '/china', component:ChinaPage},
	{path: '/korea', component:KoreaPage},
	{path: '/japan', component:JapanPage},
  {path: '/car/:id', name: 'CarDetail', component:CarDetail},
  {path: '/contacts', component:ContactPage},
  {path: '/:pathMatch(.*)*', name: 'NotFound', component:NotFound},
  {path: '/ayaya', component:SwiperCars},
  {path: '/about', component:AboutUs},
  {path: '/promotions', component:PromotionsComponent}
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default {
  data() {
    return {
      posts: []
    };
  },
  created() {
    axios.get('/posts') 
      .then(response => {
        this.posts = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
}

createApp(App).use(router).mount('#app');
