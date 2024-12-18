<template>
  <header>
    <nav>
      <ul>
        <div class="header-text">
          <span class="left-text">
          <img alt="Vue logo" src="../assets/log1.png">
          <li><router-link to="/">Главная страница</router-link></li>
          <li><router-link to="/china">Китай</router-link></li>
          <li><router-link to="/japan">Япония</router-link></li>
          <li><router-link to="/korea">Корея</router-link></li></span>
          <span class="right-text">8 (800) 500-49-46</span>
        </div>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader'
}
</script>