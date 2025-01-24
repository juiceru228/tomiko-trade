<template>
  <div class="container">
    <div class="review-card">
      <div class="avatar" :style="{ backgroundColor: avatarColor }">
        {{ initials }}
      </div>
      <div class="review-content">
        <h3 class="review-name">{{ truncatedName }}</h3>
        <div class="stars">
          <span v-for="star in stars" :key="star" class="star">★</span>
          <span v-for="star in remainingStars" :key="star" class="star empty">☆</span>
        </div>
        <p class="review-text">{{ review }}</p>
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
    avatarColor: {
      type: String,
      default: '#8A2BE2'
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
.review-card {
  justify-content:space-between 20;
  display: flex;
  align-items: center;
  max-width: 338px;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  background-color: #081e36;
  margin: 10px;
}

.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 20px;
}

.review-content {
  margin-left: 15px;
}

.review-name {
  font-size: 16px;
  margin-bottom: 5px; 
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.stars {
  color: gold;
}

.star.empty {
  color: lightgray;
}

.review-text {
  margin-top: 10px;
  font-size: 14px;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
  -webkit-line-clamp: 2;
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
    margin-right: auto;
    margin-left: auto;
}
</style>
 