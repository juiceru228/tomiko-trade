<template>
	<div id="app">
		<Header />
    <main>
      <div>
        <router-view />
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
  }
}
</script>

<style>
*{
  color: white;
  padding:0;
  margin:0;
  text-align: center;
  justify-content: center;
}

/*Эти руты очень удобно в будущем, можно вписать все нужные цвета
потом очень легко настраивать разные элементы */
:root {
    --primary-color: #0D2F68;
    --secondary-color: #D51117;
    --hover-color: #feb47b;
    --hover-bg-color: #ff7e5f;
    --background-color: #011224;
    --card-bg-color: #081E36;
    --bs-blue: #0d6efd;
    --bs-indigo: #6610f2;
    --bs-purple: #6f42c1;
    --bs-pink: #d63384;
    --bs-red: #dc3545;
    --bs-orange: #fd7e14;
    --bs-yellow: #ffc107;
    --bs-green: #198754;
    --bs-teal: #20c997;
    --bs-cyan: #0dcaf0;
    --bs-white: #fff;
    --bs-gray: #6c757d;
    --bs-gray-dark: #343a40;
    --bs-primary: #0d6efd;
    --bs-secondary: #6c757d;
    --bs-success: #198754;
    --bs-info: #0dcaf0;
    --bs-warning: #ffc107;
    --bs-danger: #dc3545;
    --bs-light: #f8f9fa;
    --bs-dark: #212529;
    --swiper-theme-color: #007aff;
    --swiper-navigation-size: 44px;
    --bs-font-sans-serif: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    --bs-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    --bs-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));
}

  /*Для изображения*/
  img {
    height: 50px;
  }

  /*Тут общие css*/
  #app {
    background-color: #011224;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    flex-direction: column;
  }
  
  main {
    min-height: calc(100vh - 120px);
  }

  .h1 {
    clear: both;
  }

  .p {
    clear: both;
  }
  
  h3 {
    margin: 40px 0 0;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    display: inline-block;
    margin: 0 10px;
  }
  
  a {
    color: #42b983;
  }

  nav ul {
    list-style-type: none;
    padding: 0;
  }
  nav ul li {
    display: inline;
    margin-right: 15px;
  }
  nav ul li a {
    color: white;
    text-decoration: none;
  }
  nav ul li a:hover {
    text-decoration: underline;
  }
  
</style>