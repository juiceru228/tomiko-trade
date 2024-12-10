/* eslint-disable */
import { createApp } from 'vue'
import App from './App.vue'
import axios from './axios';
import {createRouter, createWebHistory} from 'vue-router';

import MainPage from './views/MainPage.vue'
import ChinaPage from './views/ChinaPage.vue'
import KoreaPage from './views/KoreaPage.vue'
import JapanPage from './views/JapanPage.vue'

const routes = [
	{path: '/', component:MainPage},
	{path: '/china', component:ChinaPage},
	{path: '/korea', component:KoreaPage},
	{path: '/japan', component:JapanPage},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default {
  data() {
    return {
      posts: [],
      currentPage: 1,
      totalPages: 1,
    };
  },
  created() {
    axios.get('/posts?page=' + this.currentPage) 
      .then(response => {
        this.posts = response.data;
        this.totalPages = Math.ceil(response.headers['X-Total-Count'] / 10);
      })
      .catch(error => {
        console.error(error);
      });
  }
}

createApp(App).use(router).mount('#app');
