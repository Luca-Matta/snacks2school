<template>
  <div class="slider__container">
    <!-- <button @click="prevSlide">
      <img src="../assets/icons/left-arrow.svg" alt="" class="h-6 w-6" />
    </button> -->
    <swiper
      :slides-per-view="1.5"
      :space-between="0"
      :centered-slides="true"
      pagination
      @init="onSliderInit"
      :speed="500"
    >
      <swiper-slide v-for="(slide, index) in slides" :key="index">
        <slot :slide="slide" :index="index"></slot>
      </swiper-slide>
    </swiper>
    <!-- <div class="flex justify-center items-center border border-[#ffa500]">
      <button @click="nextSlide">
        <img src="../assets/icons/next-arrow.svg" alt="" class="h-6 w-6" />
      </button>
    </div> -->
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide, useSwiper } from "swiper/vue";
import "swiper/swiper-bundle.css";

import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";

const props = defineProps({
  slides: {
    type: Array,
    required: true,
  },
});

// const swiperSlider = ref();
// const prevSlide = () => {
//   swiperSlider.value.slidePrev();
// };
// const nextSlide = () => {
//   swiperSlider.value.slideNext();
// };
const onSliderInit = (swiper) => {
  const centeredSlideIndex = Math.floor(props.slides.length / 2);
  swiper.slideTo(centeredSlideIndex, 0);
};
</script>

<style scoped>
.slider__container {
  width: 100%;
  height: 100%;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  display: flex;
  justify-content: center;
  align-items: center;
  height: auto;
  padding: 55px 0px;
}
</style>