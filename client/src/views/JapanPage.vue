<template>

	<div class="china">
		<div class="breadcrumb">
			<div class="breadcrumb-items">
				<a href="/">Главная •</a>
				<a href="/japan">Автомобили из Японии</a>
			</div>
		</div>

		<section class="car-filter">
			<div class="title">
				<h1>Автомобили из Японии</h1>
				<img class="emoji-img" src="../assets/flag2.webp" alt="country-flag">
			</div>

			<div class="filter" style="visibility: visible;">
				<div class="dropdown-filter-select">
					<select class="item" v-model="selectedBrand" @change="onBrandChange">
						<option value="" disabled>Марка авто</option>
						<option v-for="option in brands" :key="option" :value="option">
							{{ option }}
						</option>
					</select>
				</div>
				<div class="two-parts">
					<div class="dropdown-filter-select">
						<select class="item from" v-model="selectedYearFrom">
							<option value="" disabled>Год от</option>
							<option v-for="option in years" :key="option" :value="option">
								{{ option }}
							</option>
						</select>
						<span>|</span>
						<select class="item to" v-model="selectedYearTo">
							<option value="" disabled>до</option>
							<option v-for="option in years" :key="option" :value="option">
								{{ option }}
							</option>
						</select>
					</div>
				</div>
				<div class="two-parts">
					<div class="dropdown-filter-select">
						<select class="item from" v-model="selectedEngineVolumeFrom">
							<option value="" disabled>Объем от,л</option>
							<option v-for="option in engineVolumes" :key="option" :value="option">
								{{ option }}
							</option>
						</select>
						<span>|</span>
						<select class="item to" v-model="selectedEngineVolumeTo">
							<option value="" disabled>до</option>
							<option v-for="option in engineVolumes" :key="option" :value="option">
								{{ option }}
							</option>
						</select>
					</div>
				</div>
				<div class="dropdown-filter-select">
					<select class="item" v-model="selectedDrive">
						<option value="" disabled>Привод</option>
						<option v-for="option in drives" :key="option" :value="option">
							{{ option }}
						</option>
					</select>
				</div>
				<div class="dropdown-filter-select">
					<select class="item" v-model="selectedModel">
						<option value="" disabled>Модель авто</option>
						<option v-for="option in models" :key="option" :value="option">
							{{ option }}
						</option>
					</select>
				</div>
				<div class="two-parts">
					<div class="dropdown-filter-select">
						<select class="item from" v-model="selectedMileageFrom">
							<option value="" disabled>Пробег от,км</option>
							<option v-for="option in mileages" :key="option" :value="option">
								{{ option }}
							</option>
						</select>
						<span>|</span>
						<select class="item to" v-model="selectedMileageTo">
							<option value="" disabled>до</option>
							<option v-for="option in mileages" :key="option" :value="option">
								{{ option }}
							</option>
						</select>
					</div>
				</div>
				<div class="dropdown-filter-select">
					<select class="item" v-model="selectedTransmission">
						<option value="" disabled>Тип КПП</option>
						<option v-for="option in transmissions" :key="option" :value="option">
							{{ option }}
						</option>
					</select>
				</div>
				<div class="dropdown-filter-select">
					<select class="item" v-model="selectedColor">
						<option value="" disabled>Цвет</option>
						<option v-for="option in colors" :key="option" :value="option">
							{{ option }}
						</option>
					</select>
				</div>

				<div class="result">
					<button @click="showAll">Показать</button>
					<a v-if="filtersApplied" href="/china/" @click.prevent="resetDropdowns">Сбросить</a>
				</div>
			</div>
		</section>

		<section class="catalog-car">
			<div class="sort-and-curTraded">
				<select v-model="selectedSorting">
					<option value="" disabled>Сортировка</option>
					<option v-for="(value, key) in sorts" :key="key" :value="key">
						{{ value }}
					</option>
				</select>
				<button>Какие авто торгуются сейчас</button>
			</div>


			<div class="catalog-items">
				<li class="card" v-for="item in items" :key="item.id">
					<router-link :to="{ name: 'CarDetail', params: { id: item.id } }">
						<div class="card-title">
							<h3 class="title-name">{{ item.brand }} {{ item.model }}</h3>
							<p>{{ item.year }} · {{ item.drive }} · {{ item.mileage }} км</p>
						</div>
						<div class="catalog-car-image">
							<img class="car-image" :src="`${mediaUrl}${item.image.split('%2C')[0]}`" alt="Car">
						</div>
						<div class="price-order">
							<h3 class="title-price-order">{{ item.price }} ₽</h3>
							<button class="order-button" @click.prevent='openModal'>Оставить заявку</button>
						</div>
					</router-link>
				</li>
			</div>

			<div class="pagination">
				<div class="catalog-pagination">
					<button :disabled="currentPage === 1" @click="changePage(currentPage - 1)" v-if="currentPage > 1">
						Предыдущее
					</button>

					<span v-for="page in pageNumbers" :key="page">
						<button v-if="page != '...'" :class="{ active: currentPage === page }"
							@click="changePage(page)">
							{{ page }}
						</button>
						<span v-else>...</span>
					</span>

					<button :disabled="currentPage === totalPages" @click="changePage(currentPage + 1)"
						v-if="currentPage < totalPages">
						Следующее
					</button>
				</div>
			</div>
		</section>

		<section class="contacts">
			<div class="contact-content">
				<div class="contact-info">
					<div class="contact-details">
						<h2>Контактная информация 👋</h2>
						<p>Оставьте свою заявку и наш менеджер свяжется с Вами для уточнения деталей</p>
					</div>
					<div class="phone-info">
						<div class="info-item">
							<p>Звонок по России бесплатный</p>
							<a href="tel:+8 (800) 775-67-29">8 800 775-67-29</a>
						</div>
						<div class="info-item">
							<p>WhatsApp</p>
							<a href="https://wa.me/79244202432" target="_blank">+7 (924) 420-24-32</a>
						</div>
						<div class="info-item">
							<p>Офис</p>
							<a>г. Владивосток, ул. Тополевая 6</a>
						</div>
					</div>
				</div>
				<div class="contact-form">
					<div class="form-fields">
						<label>
							<p>Имя</p>
							<input type="text" name="name" placeholder="Введите имя" pattern="^[A-Za-zА-Яа-яЁё\s]+$"
								title="Имя должно содержать только буквы и пробелы." maxlength="20" required
								aria-describedby="id_name_helptext" id="id_name">
						</label>
						<label>
							<p>Телефон</p>
							<input type="tel" name="phone_number" placeholder="+7"
								pattern="^\+7 [0-6,9]\d{2} \d{3} \d{2} \d{2}$"
								title="Формат: &#x27;+7 999 999 99 99&#x27; и номер не должен начинаться с 8 или 7 после кода +7"
								maxlength="16" required aria-describedby="id_phone_number_helptext"
								id="id_phone_number">
						</label>
					</div>
					<div class="message-field">
						<label>
							<p>Уточните свой вопрос</p>
							<textarea name="content" cols="40" rows="10"
								placeholder="Введите текст сообщения, укажите страну, марку и год машины."
								maxlength="200" id="id_content"></textarea>
						</label>
					</div>
					<div class="privacy-policy">
						<label class="privacy-policy-checkbox">
							<input type="checkbox" name="privacy_policy_agreed" required id="id_privacy_policy_agreed"
								checked>
							<p>С <a target="_blank" href="/static/files/tomiko-trade.pdf">правилами политики
									конфиденциальности</a> ознакомлен</p>
						</label>
						<button type="submit" name="submit">Отправить</button>
					</div>
				</div>
			</div>
		</section>

		<section class="socials-media-container">
			<img class="line-img" src="img/line.svg" alt="line">
			<div class="socials-media-background"></div>
			<div class="socials-media-block">
				<h2 class="socials-media-title">
					<span class="social-red-title">Подпишись</span>
					<span class="social-white-title">и не упусти свой автомобиль мечты</span>
				</h2>
				<div class="socials-media">
					<a href="" class="socials-media-link">
						<div class="social-link-background">
							<img src="img/900px-Telegram_Messenger.png" alt="tg-logo">
						</div>
						<div class="social-link-text">
							Телеграм-канал
							<img src="img/frame-9.svg" alt="arrow">
						</div>
					</a>

					<a href="" class="socials-media-link">
						<div class="social-link-background">
							<img src="img/vk-logo-1-1.svg" alt="vk-logo">
						</div>
						<div class="social-link-text">
							VK
							<img src="img/frame-9.svg" alt="arrow">
						</div>
					</a>

					<a href="" class="socials-media-link">
						<div class="social-link-background">
							<img src="img/insta-1.svg" alt="insta-logo">
						</div>
						<div class="social-link-text">
							Instagram
							<img src="img/frame-9.svg" alt="arrow">
						</div>
					</a>
				</div>
			</div>

			<div class="screen-phone-1">
				<img class="phone-back-1" src="img/phone-back-1.svg" alt="back">
				<img class="screen-1" src="img/screen-phone-1.png" alt="screen-phone">
			</div>

			<div class="screen-phone-2">
				<img class="phone-back-2" src="img/phone-back-2.svg" alt="back">
				<img class="screen-2-1" src="img/screen-phone-2.png" alt="screen-phone">
				<img class="screen-2-2" src="img/screen-phone-2.png" alt="screen-phone">
			</div>

			<img class="screen-3" src="img/screen-phone-3.png" alt="screen-phone">
			<img class="social-emoji" src="img/emoji.png" alt="emoji">

			<div class="social-head">
				<img src="img/logo.png" alt="tomiko-trade-logo">
				<div class="social-head-text">
					<span class="social-head-text-1">praviyrul.jp</span>
					<span class="social-head-text-2">г. Владивосток, Приморский край</span>
				</div>
			</div>
		</section>
	</div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';
import ModalForm from '../components/ModalForm.vue';
import ValidationForm from '../components/ValidationForm.vue';
import { reactive } from 'vue';
export default {
	name: 'JapanPage',
	components: {
		ModalForm,
		ValidationForm,
	},
	data() {
		return {
			COUNTRY: 'Япония',
			brands: [],
			years: Array.from({ length: 24 }, (_, i) => (i + 2000).toString()),
			engineVolumes: [],
			drives: ['Передний привод', 'Задний привод', 'Полный'],
			models: [],
			mileages: ['5000', '15000', '30000', '50000', '100000'],
			transmissions: ['Механика', 'Автомат'],
			colors: ['Черный', 'Бежевый', 'Белый', 'Бордовый', 'Желтый', 'Зеленый', 'Золотой',
				'Коричневый', 'Красный', 'Оранжевый', 'Розовый', 'Серебряный', 'Серый', 'Синий', 'Фиолетовый'],
			items: [],
			allItems: [],
			brands_models: [],
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
			form: reactive({
				name: '',
				phone_number: '',
				description: '',
				isAgreed: false
			}),
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
			mediaUrl: "/media",
			filtersApplied: false,
			currentPage: 1,
			perPage: ref(12),
			rows: 0,
			isModalVisible: false,
		};
	},

	computed: {
		totalPages() {
			return Math.ceil(this.rows / this.perPage);
		},
		pageNumbers() {
			const pages = [];
			const total = this.totalPages;
			const current = this.currentPage;

			//первая страница
			if (total > 1) {
				pages.push(1);
			}

			let start = Math.max(2, current - 2);
			let end = Math.min(total - 1, current + 2);

			if (start > 2) {
				pages.push('...');
			}

			for (let i = start; i <= end; i++) {
				pages.push(i);
			}

			if (end < total - 1) {
				pages.push('...');
			}

			//последняя страница
			if (total > 1) {
				pages.push(total);
			}

			return pages;
		}
	},
	mounted() {
		this.fetchData({ country: this.COUNTRY, type: "cars", page: this.currentPage })
		this.fetchModels({ country: this.COUNTRY, type: "cars_models" })
			.then(() => this.updateBrands());
	},
	methods: {
		changePage(page) {
			if (page >= 1 && page <= this.totalPages()) {
				this.currentPage = page;
			}
		},
		toggleDropdown() {
			this.dropdownVisible = !this.dropdownVisible;
		},

		changePage(page) {
			if (page >= 1 && page <= this.totalPages) {
				this.currentPage = page;
				this.fetchDataWithParam();
			}
		},
		fetchData(params = {}) {
			return axios.get('/api/filter/', { params })
				.then(response => {
					this.items = response.data;
					console.log('Fetched data:', this.items.length);
				}).catch(error => {
					console.error('Error fetching data:', error)
					throw error;
				});
		},
		fetchDataAll(params = {}) {
			return axios.get('/api/filter/', { params })
				.then(response => {
					this.allItems = response.data;
					console.log('Fetched data:', this.allItems.length);
				}).catch(error => {
					console.error('Error fetching data:', error)
					throw error;
				});
		},
		fetchModels(params = {}) {
			return axios.get('/api/filter/', { params })
				.then(response => {
					this.brands_models = response.data;
					console.log('Fetched models:', this.brands_models, this.brands_models.length);
					this.rows = this.brands_models.length;
				}).catch(error => {
					console.error('Error fetching models:', error)
					throw error;
				});
		},
		onBrandChange() {
			console.log("Выбранный бренд:", this.selectedBrand);
			this.selectedModel = '';
			this.updateModels(this.selectedBrand);
		},
		updateBrands() {
			this.brands = Array.from(new Set(this.brands_models
				.map(item => item.brand)
				.filter(brand => brand))).sort();
			console.log('Updated brands:', this.brands);
		},
		updateModels(selectedBrand) {
			this.models = Array.from(new Set(this.brands_models
				.map(item => {
					const model = item.model;
					return model && selectedBrand == item.brand ? model : null
				})
				.filter(model => model))).sort();
			console.log('Updated model:', this.models);
		},
		async showAll() {
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
			};
			this.currentPage = 1;
			await this.fetchDataAll(params);
			this.rows = this.allItems.length;
			console.log(this.rows, this.allItems.length)

			this.fetchDataWithParam();
		},
		fetchDataWithParam() {
			this.filtersApplied = true;

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
		openModal() {
			this.isModalVisible = true;
		},
		closeModal() {
			this.isModalVisible = false;
		},
		updateForm(newForm) {
			this.form = newForm;
		},
		handleFormSubmit(formData) {
			console.log('Форма успешно отправлена!', formData);
			alert('Форма успешно отправлена!');
			this.isModalVisible = false;
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
				this.selectedSorting = '',
				this.currentPage = 1;
			this.filtersApplied = false,
				this.fetchDataWithParam()

		}
	},
};
</script>

<style scoped>
.china {
	align-items: center;
	background-color: #011224;
	display: flex;
	flex-direction: column;
	justify-content: center;
	min-width: 1600px;
	overflow: hidden;
	position: relative;
	top: 0px;
}

.breadcrumb {
	align-items: flex-start;
	flex-direction: column;
	display: flex;
	gap: 2px;
	padding: 24px 100px 0px;
	position: relative;
	width: 1600px;
}

.breadcrumb-items {
	align-items: flex-start;
	display: inline-flex;
	position: relative;
}

.breadcrumb a {
	font-family: "Inter", Helvetica;
	font-weight: 400;
	color: #ffffff80;
	font-size: 14px;
}

.car-filter {
	align-items: flex-start;
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 16px;
	padding: 40px 0px 0px;
	position: relative;
	width: 1400px;
}

.title {
	align-items: flex-start;
	display: inline-flex;
	gap: 12px;
	position: relative;
}

h1 {
	text-align: left;
	margin-top: -1.00px;
	color: #ffffff;
	font-family: 'Bebas Neue', sans-serif;
	font-size: 40px;
	font-weight: 400;
}

.emoji-img {
	height: 34px;
	width: 34px;
	object-fit: cover;
}

.filter {
	grid-template-columns: 1fr 1fr 1fr 1fr;
	background-color: #081E36;
	border-radius: 24px;
	padding: 24px;
	display: grid;
	gap: 12px;
}

.dropdown-filter-select {
	display: flex;
	justify-content: center;
	width: max-content;
	position: relative;
}

.two-parts {
	display: flex;
	justify-content: center;
	height: max-content;
	width: max-content;
}

.item {
	width: 329px;
	height: 51px;
	padding: 16px;
	border-radius: 32px;
	background: #20344a;
	outline: 0;
	cursor: pointer;
	color: #FFFFFF80;
	border: 0;
	text-align: left;
	display: flex;
	align-items: center;
	justify-content: space-between;
	outline: 0;
}

.from {
	width: 158px;
	border-radius: 32px 0 0 32px;
}

.to {
	width: 158px;
	border-radius: 0 32px 32px 0;
}

.dropdown-filter-select span {
	background: #20344a;
	color: #ffffff40;
	font-size: 20px;
	width: 4px;
	display: flex;
	align-items: center;
	padding-bottom: 4px;
}

.result {
	display: flex;
	gap: 20px;
	align-items: center;
	padding-top: 12px;
}

.result button {
	width: 190px;
	height: 44px;
	border-radius: 30px;
	background: #FFFFFF1A;
	font-family: Inter;
	font-size: 14px;
	font-weight: 600;
	line-height: 19.6px;
	color: #fff;
	display: flex;
	justify-content: center;
	align-items: center;
	border: 0;
	outline: 0;
}

.result a {
	font-family: "Inter";
	font-size: 16px;
	font-weight: 400;
	line-height: 19.36px;
	color: #fd554b;
	height: max-content;
}

.catalog-car {
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	position: relative;
	width: 1600px;
	gap: 40px;
	justify-content: center;
	padding: 40px 100px 60px;
	align-items: center;
}

.sort-and-curTraded {
	align-items: center;
	align-self: flex-start;
	background-color: transparent;
	display: inline-flex;
	flex: 0 0 auto;
	gap: 16px;
	position: relative;
}

.sort-and-curTraded select {
	width: 205px;
	height: 44px;
	border-radius: 30px;
	display: flex;
	align-items: center;
	padding: 12px 16px;
	position: relative;
	background-color: #ffffff1a;
	background: #20344a;
	cursor: pointer;
	color: #FFFFFF;
	text-align: left;
	justify-content: space-between;
	font-family: "Inter";
	font-weight: 600;
	font-size: 14px;
	border: 0;
}

.sort-and-curTraded button {
	align-items: center;
	width: 248px;
	height: 44px;
	border-radius: 30px;
	display: inline-flex;
	flex: 0 0 auto;
	align-items: center;
	padding: 12px 16px;
	position: relative;
	background-color: #d51117;
	justify-content: center;
	color: #fff;
	font-family: "Inter";
	font-weight: 600;
	font-size: 14px;
}

.catalog-items {
	align-items: center;
	background-color: transparent;
	display: flex;
	flex: 0 0 auto;
	flex-wrap: wrap;
	gap: 16px;
	position: relative;
	width: 100%;
}

.card {
	align-items: flex-start;
	background-color: #081E36;
	border-radius: 24px;
	display: flex;
	flex-direction: column;
	gap: 16px;
	overflow: hidden;
	padding: 16px 8px;
	position: relative;
	justify-content: center;
	height: 347px;
	width: 338px;
}

.card-title {
	align-items: flex-start;
	flex-direction: column;
	gap: 8px;
	display: flex;
	padding: 0px 8px;
	position: relative;
	width: 322px;
}

.title-name {
	align-self: stretch;
	position: relative;
	text-align: left;
	color: #ffffff;
	font-family: "Bebas Neue", sans-serif;
	font-size: 24px;
	font-weight: 400;
}

.card-title p {
	align-self: stretch;
	position: relative;
	text-align: left;
	color: #ffffff80;
	font-family: "Inter", sans-serif;
	font-size: 14px;
	font-weight: 700;
}

.catalog-car-image {
	align-items: center;
	flex-direction: column;
	display: flex;
	overflow: hidden;
	height: 190px;
	position: relative;
	width: 100%;
}

.car-image {
	border-radius: 16px;
	position: absolute;
	object-fit: cover;
	width: 322px;
	height: 190px;
}

.price-order {
	margin-top: 10px;
	align-items: center;
	display: flex;
	justify-content: space-between;
	align-self: stretch;
	padding: 0px 8px;
	position: relative;
	width: 322px;
}

.title-price-order {
	letter-spacing: 0.00px;
	position: relative;
	text-align: right;
	white-space: nowrap;
	width: fit-content;
	color: #ffffff;
	font-family: "Bebas Neue", sans-serif;
	font-size: 24px;
	font-weight: 400;
}

.order-button {
	height: 44px;
	width: 149px;
	align-items: center;
	border-radius: 30px;
	gap: 12px;
	padding: 12px 16px;
	position: relative;
	background: #FFFFFF1A;
	display: inline-flex;
	justify-content: center;
	text-align: center;
	color: #ffffff;
	font-family: "Inter";
	font-size: 14px;
	font-weight: 600;
}

.order-button:hover {
	background-color: #d51117;
}

.pagination {
	display: flex;
	justify-content: flex-end;
	width: 100%;
}

.catalog-pagination {
	align-items: center;
	position: relative;
	background-color: #1a2939;
	border-radius: 52px;
	display: inline-flex;
	gap: 2px;
	justify-content: center;
	padding: 4px;
}

.catalog-pagination button {
	align-items: center;
	border-radius: 48px;
	display: inline-flex;
	flex-direction: column;
	gap: 10px;
	justify-content: center;
	height: 31px;
	min-width: 31px;
	position: relative;
	background-color: transparent;
	color: #ffffff;
	font-family: "Inter";
}

.catalog-pagination button:hover {
	background-color: #20344a;
}

.catalog-pagination button.active {
	background-color: #d51117;
}

.contacts {
	align-items: center;
	display: flex;
	flex: 0 0 auto;
	position: relative;
	flex-direction: column;
	padding: 80px 100px 100px;
	width: 1600px;
}

.contact-content {
	align-items: flex-start;
	display: inline-flex;
	flex: 0 0 auto;
	gap: 367px;
	position: relative;
	width: 100%;
}

.contact-info {
	align-items: flex-start;
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 60px;
	position: relative;
	width: 393px;
}

.contact-details {
	align-items: flex-start;
	align-self: stretch;
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 12px;
	position: relative;
	width: 100%;
}

.contact-details h2 {
	position: relative;
	align-items: stretch;
	text-align: left;
	color: #ffffff;
	font-family: "Bebas Neue";
	font-size: 60px;
	font-weight: 500;
}

.contact-info p {
	align-items: stretch;
	color: #ffffff80;
	font-family: "Inter";
	font-size: 18px;
	font-weight: 400;
	position: relative;
	text-align: left;
}

.phone-info {
	align-items: flex-start;
	display: inline-flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 16px;
	position: relative;
}

.info-item {
	align-items: flex-start;
	flex-direction: column;
	gap: 8px;
	min-width: 256px;
	overflow: hidden;
	position: relative;
	display: inline-flex;
}

.info-item a {
	text-align: left;
	position: relative;
	width: fit-content;
	color: #ffffff;
	font-family: "Inter";
	font-size: 18px;
	font-weight: 500;
}

.contact-form {
	align-items: flex-start;
	background-color: #081E36;
	border-radius: 28px;
	display: flex;
	flex-direction: column;
	gap: 24px;
	padding: 40px;
	position: relative;
	width: 640px;
}

.form-fields {
	align-items: flex-start;
	align-self: stretch;
	display: flex;
	gap: 16px;
	height: 76px;
	position: relative;
	width: 100%;
}

.form-fields label {
	align-items: flex-start;
	display: flex;
	flex: 1;
	flex-direction: column;
	flex-grow: 1;
	gap: 8px;
	overflow: hidden;
	position: relative;
}

.contact-form p {
	text-align: left;
	position: relative;
	align-self: stretch;
	color: #ffffff;
	font-family: "Inter";
	font-size: 14px;
	font-weight: 400;
}

.form-fields input {
	align-items: flex-start;
	background-color: #20344a;
	display: flex;
	gap: 10px;
	overflow: hidden;
	position: relative;
	align-self: stretch;
	border-radius: 32px;
	flex: 0 0 auto;
	padding: 16px;
	width: 100%;
	border: 0;
	color: #ffffff80;
	font-family: "Inter";
	font-size: 16px;
	font-weight: 400;
	text-align: left;
}

.message-field label {
	align-items: flex-start;
	align-self: stretch;
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 8px;
	overflow: hidden;
	position: relative;
	width: 100%;
}

.message-field textarea {
	align-self: stretch;
	background-color: #20344a;
	border-radius: 16px;
	height: 101px;
	overflow: hidden;
	position: relative;
	width: 560px;
	border: 0;
}

.message-field textarea::placeholder {
	text-align: left;
	height: auto;
	left: 16px;
	position: absolute;
	top: 15px;
	width: 442px;
	color: #ffffff80;
	font-family: "inter";
	font-size: 16px;
	font-weight: 400;
}

.privacy-policy {
	align-items: stretch;
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 24px;
	justify-content: center;
	position: relative;
	width: 100%;
}

.privacy-policy-checkbox {
	align-items: center;
	display: flex;
	flex: 0 0 auto;
	gap: 12px;
	position: relative;
	width: 100%;
}

.privacy-policy-checkbox input {
	border-radius: 8px;
	height: 24px;
	width: 24px;
}

.privacy-policy-checkbox p {
	position: relative;
	text-align: left;
	font-family: "Inter";
	font-size: 14px;
	font-weight: 400;
	color: #ffffff;
	top: 6px;
}

.privacy-policy-checkbox a {
	color: #fd554b;
}

.privacy-policy button {
	align-items: center;
	align-self: stretch;
	background-color: #20344a;
	border-radius: 60px;
	display: flex;
	flex: 0 0 auto;
	gap: 12px;
	justify-content: center;
	padding: 24px 40px;
	position: relative;
	color: #ffffff;
	font-family: "Inter";
	font-size: 18px;
	font-weight: 600;
	text-align: left;
	width: 560px;
}

.socials-media-container {
	display: flex;
	height: 702px;
	width: 1600px;
	position: relative;
	padding: 0px 100px 100px;
}

.line-img {
	height: 87px;
	left: 140px;
	position: absolute;
	top: 515px;
	width: 1300px;
}

.socials-media-background {
	background-color: #081E36;
	border-radius: 28px;
	height: 476px;
	position: absolute;
	top: 102px;
	width: 1400px;
}

.socials-media-block {
	align-items: flex-start;
	display: inline-flex;
	flex-direction: column;
	gap: 32px;
	left: 665px;
	position: relative;
	top: 174px;
}

.socials-media-title {
	font-family: "Bebas Neue";
	font-size: 70px;
	font-weight: 400;
	position: relative;
	text-align: left;
	width: 595px;
}

.social-red-title {
	color: #fd554b;
}

.social-white-title {
	color: #ffffff;
}

.socials-media {
	flex: 0 0 auto;
	position: relative;
	align-items: flex-start;
	display: inline-flex;
	flex-direction: column;
	gap: 12px;
}

.socials-media-link {
	align-items: center;
	background-color: #081E36;
	border-radius: 16px;
	display: inline-flex;
	flex: 0 0 auto;
	gap: 24px;
	position: relative;
}

.social-link-background {
	align-items: center;
	background-color: #ffffff33;
	border-radius: 12px;
	padding: 10px;
}

.social-link-background img {
	height: 24px;
	width: 24px;
}

.social-link-text {
	align-items: center;
	gap: 8px;
	position: relative;
	display: inline-flex;
	flex: 0 0 auto;
	text-align: left;
	color: #ffffff;
	font-family: "Inter";
	font-size: 24px;
	font-weight: 400;
}

.screen-phone-1 {
	position: absolute;
	height: 466px;
	width: 224px;
	left: 330px;
	top: 46px;
}

.phone-back-1 {
	position: absolute;
	height: 494px;
	left: -54px;
	top: -16px;
	width: 335px;
}

.screen-1 {
	height: 491px;
	left: -58px;
	position: absolute;
	top: -9px;
	width: 331px;
}

.screen-phone-2 {
	position: absolute;
	height: 533px;
	left: 228px;
	width: 256px;
	top: 0px;
}

.phone-back-2 {
	position: absolute;
	height: 693PX;
	left: -40px;
	top: -20px;
	width: 416px;
}

.screen-2-1 {
	position: absolute;
	height: 312px;
	left: 9px;
	top: 10px;
	width: 238px;
}

.screen-2-2 {
	position: absolute;
	height: 312px;
	left: 9px;
	width: 238px;
	top: 212px;
}

.screen-3 {
	height: 568px;
	left: 116px;
	position: absolute;
	top: -14px;
	width: 480px;
}

.social-emoji {
	height: 84px;
	width: 84px;
	left: 435px;
	position: absolute;
	top: 364px;
	transform: rotate(15.00deg);
}

.social-head {
	align-items: center;
	background-color: #1a2939;
	border-radius: 20px;
	height: 60px;
	width: 319px;
	display: inline-flex;
	gap: 16px;
	left: 195px;
	padding: 8px 16px 8px 12px;
	position: absolute;
	top: 63px;
}

.social-head img {
	height: 44px;
	width: 44px;
}

.social-head-text {
	align-items: flex-start;
	display: inline-flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 7px;
	position: relative;
}

.social-head-text span {
	align-self: stretch;
	color: #ffffff;
	font-family: "Inter";
	position: relative;
	text-align: left;
}

.social-head-text-1 {
	font-size: 16px;
	font-weight: 500;
}

.social-head-text-2 {
	font-size: 14px;
	font-weight: 400;
}

p,
h1,
h2,
h3 {
	margin: 0;
	padding: 0;
}

a {
	text-decoration: none;
}

button {
	border: 0;
}

@font-face {
	font-family: "Bebas Neue";
	src: url('../assets/fonts/BebasNeue.ttf') format('truetype');
	font-weight: normal;
	font-style: normal;
}

@font-face {
	font-family: "Inter";
	src: url('../assets/fonts/Inter.ttf') format('truetype');
	font-weight: normal;
	font-style: normal;
}
</style>
