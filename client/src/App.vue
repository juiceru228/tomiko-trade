<template>
	<div id="app">
		<nav>
			<router-link to="/">MainPage</router-link>
			<router-link to="/china">ChinaPage</router-link>
			<router-link to="/korea">KoreaPage</router-link>
			<router-link to="/japan">JapanPage</router-link>
		</nav>
		<router-view></router-view>
  </div>
  <img alt="Vue logo" src="./assets/logo.png">
</template>

<script>
/*import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}*/
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
