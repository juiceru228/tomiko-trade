<template>

	<div class="korea">
		<div class="breadcrumb">
			<div class="breadcrumb-items">
				<a href="/">Главная •</a>
				<a href="/korea">Автомобили из Кореи</a>
			</div>
		</div>

		<section class="car-filter">
			<div class="title">
				<h1>Автомобили из Кореи</h1>
				<img class="emoji-img" src="../assets/flag2.webp" alt="country-flag">
			</div>

			<div class="filter" style="visibility: visible;">
				<div class="dropdown-filter-select">
					<select class="item" v-model="selectedBrand">
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
					<button @click="fetchDataWithParam">Показать</button>
					<a href="/korea/" style="visibility: hidden;">Сбросить</a>
					<div v-if="items.length">
						<ul>
							<li v-for="item in items" :key="item.id" class="item">
								<div>{{ item.brand }}</div>
								<div>{{ item.model }} | {{ item.year }} | {{ item.mileage }} км | {{ item.engine_volume
									}} л</div>
								<div class="image_frame"><img :src="`${mediaUrl}${item.image}`"></div>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</section>
    
		<section class="catalog-car">
			<div class="catalog">
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
					<div class="card">

						<div class="card-title">
							<h3 class="title-name">{{ item.brand }} {{ item.model }}</h3>
							<p>{{ item.year }} · {{ item.drive }} · {{ item.mileage }}</p>
						</div>
						<div class="catalog-car-image">
							<img class="car-image" src="img/image-26.png" alt="Car">
						</div>
						<div class="price-order">
							<h3 class="title-price-order">{{ car.price }} ₽</h3>
							<button class="order-button">Оставить заявку</button>
						</div>

					</div>
				</div>

				<div class="catalog-pagination">
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
import {ref} from 'vue';

export default {
	name: 'KoreaPage',

	data() {
		return {
			COUNTRY: 'Корея',
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
			mediaUrl: "/media",
			currenPage: ref(1),
			perPage: ref(5),
			rows: ref(50)
		};
	},

	computed: {
		totalPages() {
			return Math.ceil(this.rows / this.perPage);
		}
	},
	mounted() {
		this.fetchData({ country: this.COUNTRY, type: "cars" })
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
			return axios.get('/api/filter/', { params })
				.then(response => {
					this.items = response.data;
					console.log('Fetched data:', this.items);
				}).catch(error => {
					console.error('Error fetching data:', error)
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
			console.log('Updated model:', this.models);
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
				page: this.currenPage,
				items_per_page: this.itemsPerPage
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

<style scoped>
.korea {
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
	align-self: stretch;
	flex-direction: column;
	display: flex;
	gap: 2px;
	padding: 24px 100px 0px;
	position: relative;
	width: 100%;
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
	align-self: stretch;
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 16px;
	padding: 40px 100px 0px;
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
	font-family: Inter;
	font-size: 16px;
	font-weight: 400;
	line-height: 19.36px;
	color: #fd554b;
	height: max-content;
	visibility: hidden;
}

.catalog-car {
	align-self: stretch;
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	position: relative;
	width: 1400px;
	align-items: center;
	gap: 40px;
	justify-content: center;
	padding: 40px 100px 60px;
}

.catalog {
	align-self: stretch;
	display: flex;
	flex: auto;
	flex-direction: column;
	position: relative;
	width: 100%;
	align-items: flex-start;
	gap: 16px;
}

.sort-and-curTraded {
	align-items: center;
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
	cursor: pointer;
	color: #FFFFFF;
	text-align: left;
	justify-content: space-between;
	font-family: "Inter";
	font-weight: 600;
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
}

.catalog-items {
	align-items: center;
	align-self: stretch;
	background-color: transparent;
	display: flex;
	flex: 0 0 auto;
	flex-wrap: wrap;
	gap: 16px 16px;
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
	font-weight: 700;
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

.catalog-pagination {
	align-items: center;
	align-self: flex-end;
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
	padding: 7px 11px;
	position: relative;
	background-color: transparent;
	color: #ffffff;
	font-family: "Inter";
}

.catalog-pagination button:hover {
	background-color: #20344a;
}

.catalog-pagination button.selected {
	background-color: #d51117;
}

.contacts {
	align-self: stretch;
	align-items: center;
	display: flex;
	flex: 0 0 auto;
	position: relative;
	flex-direction: column;
	padding: 80px 100px 100px;
	width: 1400px;
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
	align-items: flex-start;
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

.car-filter {
	align-items: flex-start;
	align-self: stretch;
	display: flex;
	flex: 0 0 auto;
	flex-direction: column;
	gap: 16px;
	padding: 40px 100px 0px;
	position: relative;
	width: 1400px;

}

.socials-media-container {
	align-self: stretch;
	height: 602px;
	width: 1400px;
	position: relative;
	padding: 0px 100px 100px;
}

.line-img {
	height: 87px;
	left: 87px;
	position: relative;
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
	position: absolute;
	top: 176px;
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
	left: 233px;
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
	left: 128px;
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
	left: 16px;
	position: absolute;
	top: -14px;
	width: 480px;
}

.social-emoji {
	height: 84px;
	width: 84px;
	left: 335px;
	position: absolute;
	top: 364px;
	transform: rotate(15.00deg);
}

.social-head {
	align-items: center;
	background-color: #1a2939;
	border-radius: 20px;
	height: 44px;
	width: 291px;
	display: inline-flex;
	gap: 16px;
	left: 95px;
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
	font-weight: 600;
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
