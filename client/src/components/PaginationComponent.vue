<template>
    <div v-if="totalPages > 1">
      <button @click="previousPage">Previous</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage">Next</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      currentPage: Number,
      totalPages: Number,
    },
    methods: {
      previousPage() {
        this.$emit('update-page', this.currentPage - 1);
      },
      nextPage() {
        this.$emit('update-page', this.currentPage + 1);
      },
    }
  }
  </script>
  
  <style scoped>
  button {
    margin: 0 5px;
  }
  </style>