<template>


	<div class="element">
		<h1> Автомобили из Китая</h1>
		<div>
			<select v-model="selectedBrand" @change="onBrandChange">
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
		<select v-model="selectedSorting">
			<option value="" disabled>Сортировка</option>
			<option v-for="(value, key) in sorts" :key="key" :value="key">
				{{ value }}
			</option>
		</select>
		<div v-if="items.length">
			<ul>
				<li v-for="item in items" :key="item.id" class="item">
					<div>{{ item.brand }}</div>
					<div>{{ item.model }} | {{ item.year }} | {{ item.mileage }} км | {{ item.engine_volume }} л</div>
					<div class="image_frame"><img :src="`${mediaUrl}${item.image}`"></div>
				</li>
			</ul>
		</div>
		<div class="overflow-auto">
			<!-- Пагинация -->
			<div class="pagination">
				<button :disabled="currentPage === 1" @click="changePage(1)">
					First
				</button>
				<button :disabled="currentPage === 1" @click="changePage(currentPage - 1)">
					Prev
				</button>
				<span>Page {{ currentPage }} of {{ totalPages }}</span>
				<button :disabled="currentPage === totalPages" @click="changePage(currentPage + 1)">
					Next
				</button>
				<button :disabled="currentPage === totalPages" @click="changePage(totalPages)">
					Last
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
	name: 'ChinaPage',

	data() {
		return {
			COUNTRY: 'Китай',
			brands: [''],
			years: Array.from({ length: 24 }, (_, i) => (i + 2000).toString()),
			engineVolumes: [''],
			drives: ['Передний привод', 'Задний привод', 'Полный'],
			models: [''],
			mileages: ['5000', '15000', '30000', '50000', '100000'],
			transmissions: ['Механика', 'Автомат'],
			colors: ['Черный', 'Бежевый', 'Белый', 'Бордовый', 'Желтый', 'Зеленый', 'Золотой',
				'Коричневый', 'Красный', 'Оранжевый', 'Розовый', 'Серебряный', 'Серый', 'Синий', 'Фиолетовый'],
			items: [],
			sorts: {
				"mileage": "Пробег: по возрастанию",
				"-mileage": "Пробег: по убыванию",
				"price": "Стоимость: по возрастанию",
				"-price": "Стоимость: по убыванию",
				"engine_volume": "Объем: по возрастанию",
				"-engine_volume": "Объем: по убыванию",
				"year": "Год: по возрастанию",
				"-year": "Год: по убыванию"
			},
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
			selectedSorting: '',
			mediaUrl: "http://localhost:8080/media",
			currentPage: ref(1),
			perPage: ref(5),
			rows: ref(50),
		};
	},
	computed: {
		totalPages() {
			return Math.ceil(this.rows / this.perPage);
		}
	},
	mounted() {
		this.fetchData({ country: this.COUNTRY, type: "cars", page: 1 })
			.then(() => this.updateBrands());
	},
	methods: {
		toggleDropdown() {
			this.dropdownVisible = !this.dropdownVisible;
		},
		changePage(page) {
			if (page >= 1 && page <= this.totalPages) {
				this.currentPage = page;
			}
			this.fetchDataWithParam()
		},
		fetchData(params = {}) {

			return axios.get('http://localhost:8080/api/filter/', { params })
				.then(response => {
					this.items = response.data;
					console.log('Fetched data:', this.items);

				}).catch(error => {
					console.error('Error fetchiong data:', error)
					throw error;
				});
		},
		onBrandChange() {
			console.log("Выбранный бренд:", this.selectedBrand);
			this.updateModels(this.selectedBrand);
		},
		updateBrands() {
			this.brands = Array.from(new Set(this.items
				.map(item => item.brand_country?.brand)
				.filter(brand => brand))).sort();
			console.log('Updated brands:', this.brands);
		},
		updateModels(selectedBrand) {
			this.models = Array.from(new Set(this.items
				.map(item => {
					const model = item.model;
					return model && selectedBrand == item.brand_country?.brand ? model : null
				})
				.filter(model => model))).sort();
			console.log('Updated model:', this.model);
		},
		fetchDataWithParam() {
			let params = {
				country: this.COUNTRY,
				type: "cars",
				year_start: this.selectedYearFrom || null,
				year_stop: this.selectedYearTo || null,
				model: this.selectedModel || null,
				transmission: this.selectedTransmission || null,
				engine_volume_start: this.selectedEngineVolumeFrom || null,
				engine_volume_stop: this.selectedEngineVolumeTo || null,
				mileage_start: this.selectedMileageFrom || null,
				mileage_stop: this.selectedMileageTo || null,
				drive: this.selectedDrive || null,
				color: this.selectedColor || null,
				brand: this.selectedBrand || null,
				ordering: this.selectedSorting || null,
				page: this.currentPage || null,
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
				this.selectedColor = '',
				this.selectedSorting = ''
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

.item-list {
	display: flex;
	flex-wrap: wrap;
	gap: 20px;
}

.item {
	width: calc(25% - 20px);
	box-sizing: border-box;
}

.image_frame img {
	width: 322px;
	height: 190px;
}
</style>