<template>
  <div>
    <Navbar />
    <div class="max-w-screen-xl mx-auto pb-8">
      <video class="w-full h-auto px-4" autoplay muted>
        <source src="../../static/home-header.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
    <div
      class="flex flex-col justify-center items-center max-w-screen-xl mx-auto py-16"
    >
      <div class="flex flex-col justify-center items-center">
        <img :src="profile_picture" alt="Profile Picture" />
        <p class="font-bold">{{ first_name }} {{ last_name }}</p>
        <p>{{ location }}</p>
      </div>
      <div class="flex flex-col justify-center items-center py-16">
        <h2 class="text-4xl font-bold">Catalogo</h2>
        <div class="flex flex-wrap justify-center items-center gap-8 py-6">
          <div>
            <div class="flex flex-col justify-center items-center gap-2">
              <div
                class="flex justify-center items-center h-60 w-60 bg-white rounded-xl transition-all duration-200 outline-none outline-0 outline-offset-0 hover:outline hover:outline-4 hover:outline-yellow hover:outline-offset-4 cursor-pointer shadow-card"
              >
                <img
                  :src="``"
                  alt="Profile Picture"
                  class="bg-center bg-contain bg-no-repeat h-52 w-52"
                />
              </div>
              <div class="flex flex-col justify-center items-center">
                <div class="flex items-center justify-center gap-1">
                  <p class="font-bold">Prodotto 1</p>
                  <img
                    src="../../assets/icons/review.svg"
                    alt="star"
                    class="h-6 w-6"
                  />
                </div>
                <p class="text-xs opacity-80"></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from "vue-router";

const route = useRoute();
const { first_name, last_name, profile_picture, location } = route.query;
</script>