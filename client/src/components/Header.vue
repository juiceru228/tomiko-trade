<template>
  <header>
    <nav>
      <ul>
        <div class="header-text">
          <span class="left-text">
          <li><router-link to="/"><img alt="Vue logo" src="../assets/logo.png"></router-link></li>
          <li><router-link to="/china">Авто из Китая</router-link></li>
          <li><router-link to="/japan">Авто из Японии</router-link></li>
          <li><router-link to="/korea">Авто из Кореи</router-link></li></span>
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