<template>
	<h1>Список тестовый</h1>

	<div>
			{{ items }}
	</div>
</template>

<script>
	import axios from 'axios';

	export default {
		name: 'ChinaPage',
		data(){
			return {
				items: [],
			};
		},
		methods: {
			fetchData(params = {}){

				axios.get('http://localhost:8080/api/filter/', {params}).then(response => {
					this.items = response.data;
					console.log('Fetched data:', response.data);
			}).catch(error => {
				console.error('Error fetchiong data:', error)
			});
		},
	},
		created(){
			console.log('Запрос отправлен к API...');
			this.fetchData({country: 'Китай', type: 'cars', year: '2023'});
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
