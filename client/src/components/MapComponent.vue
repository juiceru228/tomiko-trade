<template>
  <div id="map" style="width: 100%; height: 400px;"></div>
</template>

<script>
import DG from '2gis-maps'
export default {
  name: 'MapComponent',
  mounted() {
    const script = document.createElement('script');
    script.src = 'https://maps.api.2gis.ru/2.0/loader.js';
    script.onload = () => {
      DG.then(() => {
        const map = DG.map('map', {
          center: [43.124913, 131.905167],
          zoom: 15
        }).marker([43.124913, 131.905167]).addTo(map).bindPopup("I'm there!!!");
      });
    };
    document.head.appendChild(script);
  }
};
</script>

<style scoped>
#map {
  display: flex; 
  justify-content: center; 
  align-items: center;
  margin: auto; 
  max-width: 80%;
  height: 400px;
  border-radius: 50px;
}
</style>