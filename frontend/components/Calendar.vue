<template>
  <div class="flex flex-wrap justify-center items-center gap-8">
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
</template>

<script setup lang="ts">
import hamburgerIcon from "../assets/icons/hamburger.svg";

const days = {
  LUNEDÌ: null,
  MARTEDÌ: "hamburger",
  MERCOLEDÌ: null,
  GIOVEDÌ: "hamburger",
  VENERDÌ: null,
  SABATO: "hamburger",
};
</script>