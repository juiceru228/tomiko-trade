<template>
  <header>
    <nav>
      <ul>
        <div class="header-text">
          <span class="left-text">
          <li><router-link to="/"><img alt="Vue logo" src="../assets/logo.png"></router-link></li>
          <li><router-link to="/china">Авто из Китая</router-link></li>
          <li><router-link to="/japan">Авто из Японии</router-link></li>
          <li><router-link to="/korea">Авто из Кореи</router-link></li>
          <li><router-link to="/contact">Контакты</router-link></li></span>
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

<style>
/*Тут header*/
.header {
    background-color: rgba(0, 0, 0, 0)e;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    width: 80%;
    text-align: left;
    position: relative;
    margin: 0 auto;
  }

  /*Тут тут настройки для header, почему вторые, потому что без неё могут быть ошибки*/
  .header-text {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 80%;
    margin: 0 auto; 
  }
  
  /*Тут левая часть header*/
  .left-text {
    margin-right: auto;
  }
  
  /*Тут правая часть header*/
  .right-text {
    margin-left: auto;
  }
  
</style>