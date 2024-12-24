<template>
    <div>
      <div class="hello">
        <h1>автомобиль вашей мечты здесь</h1>
        <p1>Прозрачное ценообразование с подробным
        <br>разъяснением затрат на каждом этапе</p1>
        <br><button class="gradient-button">Расчитать стоимость</button>
      </div>
      <div class="content">
        <h1>Йоу, надо примерно так ещё сделать</h1>
        <p1>Тут нужны картинки разных авто</p1>
      </div>
      <iframe loading="lazy" src="https://vk.com/video_ext.php?oid=499628829&id=456239017&hash=08167ba3a6aa1892&__ref=vk.admin_android&api_hash=173506549679f8e7117113cc6111_GM2DINZRGM2TGOI" width="640" height="360" frameborder="0" allowfullscreen></iframe>    </div>
</template>

<script>
export default {
  name: 'MainPage',
};
</script>


<style>
/* Тут css кнопки */
.gradient-button {
    background: linear-gradient(to right, #0D2F68, #D51117);
    border: none;
    color: white;
    padding: 15px 30px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 50px;
    transition: background 0.3s ease;
  }
  
  .gradient-button:hover {
    background: linear-gradient(to right, #feb47b, #ff7e5f);
  }

  .hello {
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-image: url(../assets/back1.png);
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-color: #011224;
    height: auto;
    min-height: 600px;
    width: 100%;
  }
  
  .content {
    color: white;
    background-color: #011224;
    min-height: 400px;
    height: auto;
    width: 100%;
  }
</style>