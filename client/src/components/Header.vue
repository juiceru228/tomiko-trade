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
          <li><router-link to="/contacts">Контакты</router-link></li>
          <li><router-link to=""> Акции</router-link></li></span>
          <span class="right-text">8 (800) 500-49-46
          <li><router-link to="/promotions"><img alt="Vue logo" src="../assets/cta_button1.svg"></router-link></li>
          </span>
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

<style scoped>
/*Тут header*/
.header {
    background-color: #011224;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    width: 100%;
    text-align: left;
    position: fixed;
    top: 0;
    z-index: 3;
  }

  /*Тут тут настройки для header, почему вторые, потому что без неё могут быть ошибки*/
  .header-text {
    background-color: #011224;
    display: flex;
    justify-content: space-between;
    padding: 10px 20px;
    align-items: center;
    width: 100%;
    margin: 0 auto; 
    position: fixed;
    top: 0;
    z-index: 3;
  }
  
  /*Тут левая часть header*/
  .left-text {
    margin-right: auto;
    font-size: 16px;
    font-weight: 600;
    line-height: 19.36px;
  }
  
  /*Тут правая часть header*/
  .right-text {
    margin-left: auto;
    font-size: 24px;
    font-weight: 700;
    line-height: 24px;
  }
  
  /* */
  .h1 {
    clear: both;
  }

/*Тут левая часть header*/
.left-text {
  margin-right: auto;
  font-size: 16px;
  font-weight: 600;
  line-height: 19.36px;
}

/*Тут правая часть header*/
.right-text {
  margin-left: auto;
  font-size: 24px;
  font-weight: 700;
  line-height: 24px;
}

/* */
.h1 {
  clear: both;
}

.p {
  clear: both;
}

h3 {
  margin: 40px 0 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
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

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}


dl,
ol,
ul {
  margin-top: 0;
  margin-bottom: 1rem;
}

img, svg {
    vertical-align: middle;
    aspect-ratio: 1 / 1;
    height: 80px;
    width: 80px;

}

header .right-text img {
  width: 36px;
  height: 36px;
  aspect-ratio: 1 / 1;
}
</style>