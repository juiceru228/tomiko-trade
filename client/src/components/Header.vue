<template>
  <header>
    <nav>
      <ul>
        <li><router-link to="/">Главная страница</router-link></li>
        <li><router-link to="/china">Китай</router-link></li>
        <li><router-link to="/japan">Японий</router-link></li>
        <li><router-link to="/korea">Корея</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader'
}
</script>

<style scoped>
header {
  background-color: #03045e;
  color: white;
  padding: 10px;
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
