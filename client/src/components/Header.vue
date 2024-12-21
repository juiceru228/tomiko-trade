<template>
  <header>
    <nav>
      <ul>
        <div class="header-text">
          <span class="left-text">
          <li><router-link to="/"><img alt="Vue logo" src="../assets/logo.png"></router-link></li>
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