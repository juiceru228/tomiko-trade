<template>
  <div>
		<h1>Список тестовый</h1>
		<ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>
	import axios from 'axios';

	export default {
		data(){
			return {
				items: [],
			};
		},
		created(){
		axios.get('http://localhost:8080/api/parking').then(response => {
			this.items = response.data;
		}).catch(error => {
			console.error('Error fetchiong data:', error)
		});
	},
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
