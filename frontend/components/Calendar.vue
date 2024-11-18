<template>
  <div class="flex flex-wrap justify-center items-center gap-5">
    <div
      v-for="(content, day) in days"
      :key="day"
      class="flex flex-col justify-center items-center gap-2"
    >
      <div class="text-xl font-bold">{{ day }}</div>
      <div
        class="flex flex-col justify-center items-center text-center h-40 w-40 border border-4 border-yellow rounded-xl"
      >
        <div v-if="content" class="svg-icon">
          <img :src="hamburgerIcon" alt="Hamburger Icon" class="h-16 w-16" />
        </div>
        <div v-else class="font-bold">Nessuna merenda</div>
        <div v-if="!content" class="text-yellow font-bold">Ordina ora</div>
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