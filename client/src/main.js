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
import CarDetail from './views/CarDetail.vue';
const routes = [
	{path: '/', component:MainPage},
	{path: '/china', component:ChinaPage},
	{path: '/korea', component:KoreaPage},
	{path: '/japan', component:JapanPage},
  {path: '/car/:id', name: 'CarDetail', component:CarDetail}
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
