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
import "./styles.css";

export default {
  name: 'App',
  components: {
    Header,
    Footer,
  }
}
</script>

<style>
</style>