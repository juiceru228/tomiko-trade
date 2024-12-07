/* eslint-disable */
import { createApp } from 'vue'
import App from './App.vue'
import axios from './axios';
import {createRouter, createWebHistory} from 'vue-router';

import MainPage from './components/MainPage.vue'
import ChinaPage from './components/ChinaPage.vue'
import KoreaPage from './components/KoreaPage.vue'
import JapanPage from './components/JapanPage.vue'

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
