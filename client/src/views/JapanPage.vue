<template>
	<h1>Список японовёдер</h1>

	<div>
		<div>
			<select v-model="selectedBrand">
				<option value="" disabled>Марка авто</option>
				<option v-for="option in brands" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedYearFrom">
				<option value="" disabled>Год от</option>
				<option v-for="option in years" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedYearTo">
				<option value="" disabled>Год до</option>
				<option v-for="option in years" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedEngineVolumeFrom">
				<option value="" disabled>Объем от</option>
				<option v-for="option in engineVolumes" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedEngineVolumeTo">
				<option value="" disabled>Объем до</option>
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
			<select v-model="selectedMileageFrom">
				<option value="" disabled>Пробег от</option>
				<option v-for="option in mileages" :key="option" :value="option">
					{{ option }}
				</option>
			</select>
			<select v-model="selectedMileageTo">
				<option value="" disabled>Пробег до</option>
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
		</div>

	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'JapanPage',
	data() {
		return {
			brands: [''],
			years: Array.from({ length: 24 }, (_, i) => (i + 2000).toString()),
			engineVolumes: [''],
			drives: ['Передний привод', 'Задний привод', 'Полный'],
			models: [''],
			mileages: ['5000', '15000', '30000', '50000', '100000'],
			transmissions: ['Механика', 'Автомат'],
			colors: ['Бежевый', 'Белый', 'Бордовый', 'Желтый', 'Зеленый', 'Золотой', 'Коричневый', 'Красный', 'Оранжевый', 'Розовый', 'Серебряный', 'Серый', 'Синий', 'Фиолетовый'],
			items: [],
			selectedBrand: '',
			selectedYearFrom: '',
			selectedYearTo: '',
			selectedEngineVolumeFrom: '',
			selectedEngineVolumeTo: '',
			selectedDrive: '',
			selectedModel: '',
			selectedMileageFrom: '',
			selectedMileageTo: '',
			selectedTransmission: '',
			selectedColor: '',
		};
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
				country: "Япония",
				type: "cars",
				year_start: this.selectedYearFrom || null,
				year_stop: this.selectedYearTo || null,
				model: this.selectedModel || null,
				transmission: this.selectedTransmission || null,
				engine_volumeFrom: this.selectedEngineVolume || null,
				engine_volumeTo: this.selectedEngineVolume || null,
				mileageFrom: this.selectedMileageFrom || null,
				mileageTo: this.selectedMileageTo || null,
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
		resetDropdowns() {
			this.selectedBrand = '',
				this.selectedYearFrom = '',
				this.selectedYearTo = '',
				this.selectedEngineVolumeFrom = '',
				this.selectedEngineVolumeTo = '',
				this.selectedDrive = '',
				this.selectedModel = '',
				this.selectedMileageFrom = '',
				this.selectedMileageTo = '',
				this.selectedTransmission = '',
				this.selectedColor = ''
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
