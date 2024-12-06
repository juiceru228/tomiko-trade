import { createApp } from 'vue'
import App from './App.vue'
import axios from './axios';

export default {
  data() {
    return {
      posts: []
    };
  },
  created() {
    axios.get('/posts')  // Использование базового URL "/api"
      .then(response => {
        this.posts = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
}

createApp(App).mount('#app')
