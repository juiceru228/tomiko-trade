<template>
	<h1>Список китаевёдер</h1>

	<div>
		<div>
			<select v-model="selectedBrand">
				<option value="" disabled>Марка авто</option>
				<option v-for="option in brands" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedYear">
				<option value="" disabled>Год</option>
				<option v-for="option in years" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedEngineVolume">
				<option value="" disabled>Объем</option>
				<option v-for="option in engineVolumes" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedDrive">
				<option value="" disabled>Привод</option>
				<option v-for="option in drives" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedModel">
				<option value="" disabled>Модель авто</option>
				<option v-for="option in models" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedMileage">
				<option value="" disabled>Пробег</option>
				<option v-for="option in mileages" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedTransmission">
				<option value="" disabled>Тип КПП</option>
				<option v-for="option in transmissions" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedColor">
				<option value="" disabled>Цвет</option>
				<option v-for="option in colors" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
		</div>
		<button @click="fetchDataWithParam">Запросить данные</button>
		<button @click="resetDropdowns">Сбросить значения</button>
		<div v-if="items.length">
			<ul>
				<li v-for="item in items" :key="item.id">
					<div>{{ item.brand }}</div>
					<div>{{ item.model }} | {{ item.year }} | {{ item.mileage }} км | {{ item.engine_volume }} л</div>
				</li>
			</ul>
  
		<PaginationComponent
			:current-page="currentPage"
			:total-pages="totalPages"
			@update-page="onUpdatePage"
		/>
		</div>

	</div>
</template>

<script>
import axios from 'axios';
import PaginationComponent from '../components/PaginationComponent.vue';

export default {
	name: 'ChinaPage',
	components: {
		PaginationComponent,
	},
	data() {
		return {
			brands: [''],
			years: ['2020', '2021', '2022'],
			engineVolumes: [''],
			drives: ['Передний привод', 'Задний привод'],
			models: [''],
			mileages: [''],
			transmissions: ['Механика', 'Автомат'],
			colors: ['Черный', 'Белый'],
			items: [],
		currentPage: 1,
		totalPages: 1,
			selectedBrand: '',
			selectedYear: '',
			selectedEngineVolume: '',
			selectedDrive: '',
			selectedModel: '',
			selectedMileage: '',
			selectedTransmission: '',
			selectedColor: '',
		};
	},
	computed: {
		filters() {
			return {
				country: "Китай",
				type: "cars",
				year: this.selectedYear || null,
				model: this.selectedModel || null,
				transmission: this.selectedTransmission || null,
				engine_volume: this.selectedEngineVolume || null,
				drive: this.selectedDrive || null,
				color: this.selectedColor || null,
				brand: this.selectedBrand || null,
			};
		},
	},
	methods: {
		toggleDropdown() {
			this.dropdownVisible = !this.dropdownVisible;
		},
		fetchData(params = {}) {

			axios.get('http://localhost:8080/api/filter/', { params }).then(response => {
				this.items = response.data;
				console.log('Fetched data:', response.data);
			}).catch(error => {
				console.error('Error fetchiong data:', error)
			});
		},
		fetchDataWithParam() {
			let params = {
				country: "Китай",
				type: "cars",
				year: this.selectedYear || null,
				model: this.selectedModel || null,
				transmission: this.selectedTransmission || null,
				engine_volume: this.selectedEngineVolume || null,
				drive: this.selectedDrive || null,
				color: this.selectedColor || null,
				brand: this.selectedBrand || null
			};
			Object.keys(params).forEach(key => {
				if (params[key] === null) {
				delete params[key];
				}
			});
			this.fetchData(params);
		},
		onUpdatePage(newPage) {
			this.currentPage = newPage;
			this.fetchDataWithParam();
	  	},
		resetDropdowns() {
			this.selectedYear = '';
			this.selectedBrand = '';
			this.selectedColor = '';
			this.selectedDrive = '';
			this.selectedMileage = '';
			this.selectedModel = '';
			this.selectedTransmission = '';
			this.selectedEngineVolume = '';
		}
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
