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
  padding:0;
  margin:0;
  text-align: center;
  justify-content: center;
}

/*Тут header*/
.header {
    background-color: rgba(0, 0, 0, 0)e;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    width: 80%;
    text-align: left;
    position: relative;
    margin: 0 auto;
  }

  /*Тут тут настройки для header, почему вторые, потому что без неё могут быть ошибки*/
  .header-text {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 80%;
    margin: 0 auto; 
  }
  
  /*Тут левая часть header*/
  .left-text {
    margin-right: auto;
  }
  
  /*Тут правая часть header*/
  .right-text {
    margin-left: auto;
  }

  /*Тут футер*/
  footer {
    background-color: #081E36;
    color: white;
    text-align: center;
    padding: 10px;
    position: relative;
    bottom: 0;
    width: 100%;
  }

  /* Тут css кнопки */
  .gradient-button {
    background: linear-gradient(to right, #0D2F68, #D51117);
    border: none;
    color: white;
    padding: 15px 30px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 50px;
    transition: background 0.3s ease;
  }
  
  .gradient-button:hover {
    background: linear-gradient(to right, #feb47b, #ff7e5f);
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

  /*настройки разных элементов и классов*/
  .element {
    color: white;
    background-image: url(./assets/back1.png);
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-color: #011224;
    height: auto;
    min-height: 600px;
    width: 100%;
  }
  
  .hello {
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-image: url(./assets/back1.png);
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-color: #011224;
    height: auto;
    min-height: 600px;
    width: 100%;
  }
  
  .content {
    color: white;
    background-color: #011224;
    min-height: 400px;
    height: auto;
    width: 100%;
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