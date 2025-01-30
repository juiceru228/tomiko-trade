<template>
  <div class="container">
      <div class="review-card">
        <div class="item_left">
          <div class="avatar" :style="{ backgroundColor: avatarColor }">
            {{ initials }}
          </div>
          <div class="review-content">
            <h3 class="review-name">{{ truncatedName }}</h3>
          </div>
        </div>
        <div class="item_right">
          <div class="ostatok">
            <div class="stars">
                <span v-for="star in stars" :key="star" class="star">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
                    <path d="M7.27995 1.91196C7.60141 1.36008 8.39875 1.36008 8.72015 1.91196L10.5835 5.11112L14.2019 5.89466C14.8261 6.02983 15.0725 6.7881 14.6469 7.26436L12.1801 10.0251L12.5531 13.7085C12.6174 14.3439 11.9724 14.8126 11.3879 14.555L8.00008 13.0621L4.61219 14.555C4.02774 14.8126 3.38271 14.3439 3.44705 13.7085L3.81999 10.0251L1.35323 7.26436C0.92768 6.7881 1.17406 6.02983 1.79827 5.89466L5.41664 5.11112L7.27995 1.91196Z" fill="#F5B300"></path>
                  </svg>
                </span>
                <span v-for="star in remainingStars" :key="star" class="star empty">
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g clip-path="url(#clip0_75_311)">
                  <path d="M7.27995 1.91196C7.60141 1.36008 8.39875 1.36008 8.72015 1.91196L10.5835 5.11112L14.2019 5.89466C14.8261 6.02983 15.0725 6.7881 14.6469 7.26436L12.1801 10.0251L12.5531 13.7085C12.6174 14.3439 11.9724 14.8126 11.3879 14.555L8.00008 13.0621L4.61219 14.555C4.02774 14.8126 3.38271 14.3439 3.44705 13.7085L3.81999 10.0251L1.35323 7.26436C0.92768 6.7881 1.17406 6.02983 1.79827 5.89466L5.41664 5.11112L7.27995 1.91196Z" fill="white" fill-opacity="0.1"/>
                  </g>
                  <defs>
                  <clipPath id="clip0_75_311">
                  <rect width="16" height="16" fill="white"/>
                  </clipPath>
                  </defs>
                  </svg>
                </span>
            </div>
          </div>  
          <p class="review-text">{{ date}}</p>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  props: {
    name: String,
    review: String,
    rating: Number,
    date: String,
    avatarColor: {
      type: String,
      default: '#A84CA8'
    }
  },
  computed: {
    initials() {
      return this.name.split(' ').map(word => word.charAt(0)).join('').toUpperCase();
    },
    stars() {
      return Array.from({ length: Math.floor(this.rating) }, (_, i) => i + 1);
    },
    remainingStars() {
      return Array.from({ length: 5 - Math.floor(this.rating) }, (_, i) => i + 1);
    },
    truncatedName() {
      return this.name.length > 15 ? this.name.substring(0, 15) + '...' : this.name;
    }
  }
}
</script>

<style scoped>
.container .item_left {
    display: flex;
    align-items: center;
    gap: 16px;
}

.container .item_right {
    display: flex;
    align-items: flex-start;
    -ms-flex-direction: column;
    flex-direction: column;
    gap: 8px;
}

.review-card {
    display: flex;
    gap: 16px;
    margin-bottom: 10px;
    align-items: center;
    padding: 16px 24px;
    border-radius: 16px;
    background: #081e36;
    max-width: 340px;
}

.avatar {
  font-size: 22px;
    font-weight: 500;
    line-height: 70px;
    color: #fff;
    display: flex;
    align-items: center;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    -o-object-fit: cover;
    object-fit: cover;
    -o-object-position: center;
    object-position: center;
    flex-shrink: 0;
    justify-content: center;
}

.review-content {
  margin-left: 15px;
  font-family: Inter;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 24px;
  color: #FFF;
}

.review-name {
  font-family: Inter;
  font-size: 16px;
  font-style: normal;
  font-weight: 500;
  line-height: 24px;
  color: #FFF;
}

.stars {
  color: gold;
  display: flex;
  align-items: center;
  gap: 4px;
}

.star.empty {
  color: lightgray;
}

.review-text {
  font-family: Inter;
  font-size: 14px;
  font-weight: 300;
  line-height: 20px;
  color: rgba(255, 255, 255, 0.5);
  white-space: nowrap;
}


.container, .container-lg, .container-md, .container-sm, .container-xl {
    max-width: 1424px;
    margin: 0 auto;
}
@media (min-width: 992px) {
    .container, .container-lg, .container-md, .container-sm {
        max-width: 960px;
    }
}
@media (min-width: 768px) {
    .container, .container-md, .container-sm {
        max-width: 720px;
    }
}
@media (min-width: 576px) {
    .container, .container-sm {
        max-width: 540px;
    }
}
.container, .container-fluid, .container-lg, .container-md, .container-sm, .container-xl, .container-xxl {
    width: 100%;
    padding-right: var(--bs-gutter-x, .75rem);
    padding-left: var(--bs-gutter-x, .75rem);
    margin-left: auto;
    margin-left: auto;
    margin-right: auto;
    position: relative;
    overflow: hidden;
    list-style: none;
    padding: 0;
    z-index: 1;
    display: block;
    flex-wrap: wrap;
    flex-direction: column;
    transform: translate3d(0px, 0px, 0px);
}

.ostatok {
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    gap: 4px;
}

.comments .section_top {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: end;
    -ms-flex-align: end;
    align-items: flex-end;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    margin: 0 0 40px 0;
}

.comments .title h2 {
    font-family: Bebas-Neue, Arial, sans-serif;
    font-size: 70px;
    font-weight: 700;
    line-height: 70px;
    text-align: left;
    color: #fff;
    display: flex;
    align-items: center;
}

.comments .title h2 img {
    margin-left: 24px;
    margin-right: 13px;
    aspect-ratio: 1 / 1;
    width: 48px;
    height: 48px;
}
img, svg {
    vertical-align: middle;
}

.comments .comment_links {
    display: flex;
    align-items: center;
    gap: 24px;
}

.comments .comment_links a {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: Inter;
    font-size: 16px;
    font-style: normal;
    font-weight: 400;
    color: rgba(255, 255, 255, 0.5);
}
</style>
 