<template>
	<div id="app">
		<Header />
    <main>
      <router-view />
      <img alt="Vue logo" src="./assets/logo.png">
      <PaginationComponent
        :current-page="currentPage"
        :total-pages="totalPages"
        @update-page="handlePageChange"
      />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import PaginationComponent from './components/PaginationComponent.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    PaginationComponent
  },
  data() {
    return {
      currentPage: 1,
      totalPages: 1
    };
  },
  methods: {
    handlePageChange(newPage) {
      this.currentPage = newPage;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  background-color: #023e8a;
  margin-top: 60px;
}
main {
  min-height: calc(100vh - 120px);
}
</style>
