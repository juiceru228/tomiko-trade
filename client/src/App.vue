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