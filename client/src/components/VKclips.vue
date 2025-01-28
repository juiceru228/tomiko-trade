<template>
    <section class="clips">
        <p>
            <a name="clips" style="scroll-margin-top: 150px;"></a>
            <a name="clips2" style="scroll-margin-top: 720px;"></a>
        </p>
        <div class="container">
            <div class="section_top">
                <div class="title">
                    <h2><img src="../assets/clip_logo.svg" alt="Клипы">Клипы</h2>
                </div>
                <a href="https://vk.com/tomiko_trade" target="_blank" class="clips_link d-none d-sm-flex">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
                        <g clip-path="url(#clip0_11_1091)">
                            <mask id="mask0_11_1091" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0"
                                width="24" height="24">
                                <path d="M23.8815 0H0.119141V24H23.8815V0Z" fill="white" />
                            </mask>
                            <g mask="url(#mask0_11_1091)">
                                <path
                                    d="M0.119141 11.52C0.119141 6.08942 0.119141 3.37414 1.7895 1.68707C3.45987 0 6.14827 0 11.5251 0H12.4756C17.8524 0 20.5408 0 22.2112 1.68707C23.8815 3.37414 23.8815 6.08942 23.8815 11.52V12.48C23.8815 17.9106 23.8815 20.6259 22.2112 22.3129C20.5408 24 17.8524 24 12.4756 24H11.5251C6.14827 24 3.45987 24 1.7895 22.3129C0.119141 20.6259 0.119141 17.9106 0.119141 12.48V11.52Z"
                                    fill="white" />
                                <path
                                    d="M12.7626 17.2908C7.34671 17.2908 4.25763 13.5408 4.12891 7.30078H6.84179C6.93089 11.8808 8.93085 13.8208 10.515 14.2208V7.30078H13.0695V11.2507C14.6339 11.0808 16.2773 9.28078 16.8317 7.30078H19.3863C18.9605 9.74079 17.1783 11.5408 15.911 12.2808C17.1783 12.8808 19.2081 14.4508 19.9804 17.2908H17.1684C16.5645 15.3908 15.0596 13.9208 13.0695 13.7208V17.2908H12.7626Z"
                                    fill="#B02F3F" />
                            </g>
                        </g>
                        <defs>
                            <clipPath id="clip0_11_1091">
                                <rect width="24" height="24" fill="white" />
                            </clipPath>
                        </defs>
                    </svg>
                    Подписаться
                </a>
            </div>
            <div class="clips_swiper swiper">
                <div class="swiper-wrapper">
                    <div class="swiper-wrapper">
                    <swiper :modules="modules" :slides-per-view="10" :space-between="10" 
                    navigation :pagination="{ clickable: true }" 
                    @swiper="onSwiper" @slideChange="onSlideChange" :loop="true">
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[1]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[0]?.items[1]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[2]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[2]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[3]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[3]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[4]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[4]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[5]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[5]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[6]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[6]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[7]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[7]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[8]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[8]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[9]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[9]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[10]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[10]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[11]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[11]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[12]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[12]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[12]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[12]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[13]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[13]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[14]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[14]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[15]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[15]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[16]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[16]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[17]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[17]?.image[4]?.url }" />
                        </SwiperSlide>
                        <SwiperSlide v-for="(clip, index) in clips" :key="index">
                            <img :src="clip[0]?.items[18]?.image[4]?.url || placeholder" @error="onImageError"
                                :class="{ 'is-placeholder': !clip[1]?.items[18]?.image[4]?.url }" />
                        </SwiperSlide>
                    </swiper>
                    </div>

                </div>
            </div>
            <a href="https://vk.com/tomiko_trade" target="_blank" class="clips_link d-flex d-sm-none">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 25 25" fill="none">
                    <g clip-path="url(#clip0_11_1691)">
                        <mask id="mask0_11_1691" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0"
                            width="25" height="25">
                            <path d="M24.3825 0.496582H0.620117V24.4966H24.3825V0.496582Z" fill="white" />
                        </mask>
                        <g mask="url(#mask0_11_1691)">
                            <path
                                d="M0.620117 12.0166C0.620117 6.58601 0.620117 3.87072 2.29048 2.18365C3.96085 0.496582 6.64925 0.496582 12.0261 0.496582H12.9766C18.3534 0.496582 21.0418 0.496582 22.7121 2.18365C24.3825 3.87072 24.3825 6.58601 24.3825 12.0166V12.9766C24.3825 18.4072 24.3825 21.1224 22.7121 22.8095C21.0418 24.4966 18.3534 24.4966 12.9766 24.4966H12.0261C6.64925 24.4966 3.96085 24.4966 2.29048 22.8095C0.620117 21.1224 0.620117 18.4072 0.620117 12.9766V12.0166Z"
                                fill="white" />
                            <path
                                d="M13.2635 17.7874C7.84769 17.7874 4.7586 14.0374 4.62988 7.79736H7.34276C7.43187 12.3774 9.43183 14.3173 11.016 14.7174V7.79736H13.5705V11.7473C15.1349 11.5773 16.7782 9.77736 17.3327 7.79736H19.8872C19.4615 10.2374 17.6793 12.0373 16.412 12.7773C17.6793 13.3773 19.7091 14.9473 20.4814 17.7874H17.6694C17.0654 15.8874 15.5606 14.4174 13.5705 14.2173V17.7874H13.2635Z"
                                fill="#B02F3F" />
                        </g>
                    </g>
                    <defs>
                        <clipPath id="clip0_11_1691">
                            <rect width="24" height="24" fill="white" transform="translate(0.500977 0.496582)" />
                        </clipPath>
                    </defs>
                </svg>
                Подписаться
            </a>
        </div>
    </section>
</template>

<script>
import { Navigation, Pagination, A11y } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import axios from 'axios';

export default {
    name: 'VKclipsPage',
    components: {
        Swiper,
        SwiperSlide,
    },
    data() {
        return {
            clips: [],
            loading: false,
            error: null,
            placeholder: 'data:image/svg+xml;base64,' + btoa(`
        <svg xmlns="http://www.w3.org/2000/svg" width="405" height="720">
          <rect width="100%" height="100%" fill="#ccc" />
          <text x="50%" y="50%" text-anchor="middle" fill="#666" font-size="24px" dy=".3em">Image not loaded</text>
        </svg>`),
        };
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            this.loading = true;
            try {
                const response = await axios.get('http://localhost:8080/api/clips/');
                this.clips = response.data;
                console.log('CLIPS', this.clips);
            } catch (error) {
                this.error = 'Error fetching vk_clips';
                console.error(error);
            } finally {
                this.loading = false;
            }
        },
        
    },
    setup() {
        const onSwiper = (swiper) => {
            console.log(swiper);
        };
        const onSlideChange = () => {
            console.log('slide change');
        };
        return {
            onSwiper,
            onSlideChange,
            modules: [Navigation, Pagination, A11y],
        };
    },
};
</script>

<style scoped>
.clips {
    padding: 60px 0 100px 0;
    margin: 0 0 80px 0;
    position: relative;
    z-index: 1;
}

.clips::after {
    box-sizing: border-box;
    position: absolute;
    content: "";
    left: 50%;
    top: 48%;
    width: 120%;
    height: 70%;
    background: linear-gradient(95deg, #0d2f68 0, #d51117 100%);
    -webkit-transform: rotate(-3deg) translate(-50%, -62%);
    transform: rotate(-3deg) translate(-50%, -62%);
    -webkit-clip-path: polygon(0 0, 100% 0, 100% 95%, 0 100%);
    clip-path: polygon(0 0, 100% 0, 100% 95%, 0 100%);
    z-index: -1;
}

.clips .clips_swiper .swiper-slide img {
    width: 150px;
    height: 260px;
    border-radius: 16px;
    display: inline-block;
    max-width: 2000px;
}

.swiper-slide img {
    object-fit: cover;
    max-width: 2000px;
}

img,
svg {
    vertical-align: middle;
}

.clips .clips_swiper {
    overflow: visible;
    display: inline-block;
    max-width: 2000px;
}

.swiper-horizontal {
    touch-action: pan-y;
}

.swiper {
    margin-left: auto;
    margin-right: auto;
    position: relative;
    overflow: hidden;
    list-style: none;
    padding: 0;
    z-index: 1;
    display: block;
}

.swiper-wrapper {
    position: relative;
    width: 100%;
    height: 100%;
    z-index: 1;
    display: flex;
    flex-direction: row;
    transition-property: transform;
    transition-timing-function: var(--swiper-wrapper-transition-timing-function, initial);
    box-sizing: content-box;
}

.clips .clips_swiper .swiper-wrapper {
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    max-width: 2000px;
}

.clips .title h2 {
    font-size: 70px;
    font-weight: 700;
    line-height: 70px;
    text-align: left;
    color: #fff;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
}

.clips .clips_link {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.1);
    font-family: Inter;
    font-size: 14px;
    font-weight: 600;
    line-height: 140%;
    color: #FFF;
}

@media (min-width: 576px) {
    .d-sm-flex {
        display: flex !important;
    }
}
.container, .container-lg, .container-md, .container-sm, .container-xl {
    max-width: 100%;
    margin: 0 auto;
}

.clips .section_top {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: end;
    -ms-flex-align: end;
    align-items: flex-end;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    margin: 0 0 24px 0;
}
</style>