<template>
  <div>
    <div class="hidden md:flex flex-wrap justify-center items-center gap-8">
      <div
        v-for="(content, day) in days"
        :key="day"
        class="flex flex-col justify-center items-center gap-3"
      >
        <div class="text-xl font-bold">{{ day }}</div>
        <div
          class="flex flex-col justify-center items-center text-center h-40 w-40 rounded-xl outline outline-4 outline-brown outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 cursor-pointer"
          :class="content ? 'bg-brown ' : 'bg-gray-100'"
        >
          <div v-if="content" class="svg-icon">
            <img :src="hamburgerIcon" alt="Hamburger Icon" class="h-16 w-16" />
          </div>
          <div v-else class="font-bold">Nessuna merenda</div>
          <div v-if="!content" class="text-brown font-bold">Ordina ora</div>
        </div>
      </div>
    </div>

    <div class="md:hidden -mt-8">
      <Slider :slides="calendarSlides">
        <template #default="{ slide, index }">
          <div class="flex flex-col justify-center items-center gap-3">
            <div class="text-xl font-bold">{{ slide.title }}</div>
            <div :class="slide.class">
              <div v-if="slide.imgSrc" class="svg-icon">
                <img
                  :src="slide.imgSrc"
                  :alt="slide.imgAlt"
                  :class="slide.imgClass"
                />
              </div>
              <div v-else class="font-bold">{{ slide.texts[0] }}</div>
              <div v-if="!slide.imgSrc" class="text-brown font-bold">
                {{ slide.texts[1] }}
              </div>
            </div>
          </div>
        </template>
      </Slider>
    </div>
  </div>
</template>

<script setup lang="ts">
import Slider from "@/components/Slider.vue";
import hamburgerIcon from "../assets/icons/hamburger.svg";

const days = {
  LUNEDÌ: null,
  MARTEDÌ: "hamburger",
  MERCOLEDÌ: null,
  GIOVEDÌ: "hamburger",
  VENERDÌ: null,
  SABATO: "hamburger",
};

const calendarSlides = Object.entries(days).map(([day, content]) => ({
  class:
    "flex flex-col justify-center items-center text-center h-56 w-56 rounded-xl outline outline-4 outline-brown outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 cursor-pointer " +
    (content ? "bg-brown" : "bg-gray-100"),
  imgSrc: content ? hamburgerIcon : "",
  imgAlt: content ? "Hamburger Icon" : "",
  imgClass: "h-16 w-16",
  title: day,
  texts: content ? [] : ["Nessuna merenda", "Ordina ora"],
}));
</script>

<style scoped>
/* Add any additional styles if needed */
</style>