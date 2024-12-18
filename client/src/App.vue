<template>
	<div id="app">
		<Header />
    <main>
      <div class="element">
        <router-view />
      </div>
    </main>
    <ContentTest />
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