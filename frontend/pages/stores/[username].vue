<template>
  <div>
    <Navbar />
    <div class="hero relative text-white pb-6">
      <div class="flex justify-center items-center py-20 md:py-60 px-4">
        <div class="flex flex-col py-8">
          <div class="flex flex-col md:flex-row items-center gap-8">
            <div class="bg-gray-100 h-32 w-32 rounded-xl">
              <img :src="profile_picture" alt="Profile Picture" />
            </div>
            <div class="flex flex-col gap-2 text-center md:text-left">
              <p class="font-bold text-2xl md:text-5xl">
                {{ first_name }} {{ last_name }}
              </p>
              <div>
                <p>{{ location }}</p>
                <p v-html="formattedBio"></p>
              </div>
            </div>
          </div>
          <div
            class="absolute right-0 bottom-6 left-0 py-2"
            style="background-color: rgba(243, 244, 246, 0.6)"
          >
            <div class="flex justify-center items-center">
              <div class="flex gap-12">
                <div>
                  <img
                    src="../../assets/icons/gluten-free.png"
                    alt=""
                    class="h-12 md:h-20 w-12 md:w-20"
                  />
                </div>
                <div>
                  <img
                    src="../../assets/icons/vegan.png"
                    alt=""
                    class="h-12 md:h-20 w-12 md:w-20"
                  />
                </div>
                <div>
                  <img
                    src="../../assets/icons/bio.png"
                    alt=""
                    class="h-12 md:h-20 w-12 md:w-20"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="flex flex-col justify-center items-center max-w-screen-xl mx-auto py-12"
    >
      <div class="flex flex-col justify-center items-center py-8 gap-4">
        <div class="max-w-screen-xl mx-auto">
          <div class="w-full h-auto px-4" autoplay muted>
            <img
              src="../../static/store-menu.png"
              alt="Menu"
              class="bg-center bg-contain bg-no-repeat"
            />
          </div>
        </div>
        <div class="flex flex-wrap justify-center items-center gap-8 py-6">
          <div>
            <div class="flex flex-col justify-center items-center gap-2">
              <div
                class="flex justify-center items-center h-60 w-60 bg-white rounded-xl transition-all duration-200 outline outline-4 outline-brown outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500"
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
const { first_name, last_name, profile_picture, location, bio } = route.query;

const formattedBio = bio ? bio.replace(/\n/g, "<br>") : "";
</script>