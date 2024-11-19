<template>
  <div>
    <Navbar />
    <div class="max-w-screen-xl mx-auto pb-8">
      <video class="w-full h-auto px-4" autoplay muted>
        <source src="../static/home-header.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
    <div class="flex justify-center items-center py-16 px-4 gap-12 mx-auto">
      <div
        class="flex flex-col justify-center items-center bg-yellow h-64 w-64 rounded-xl p-4 cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <div class="font-bold text-center">Salute e tutela</div>
        <div class="flex flex-col justify-center items-center">
          <p class="text-sm">Trasparenza sugli ingredienti.</p>
          <p class="text-sm">Allergeni sempre in evidenza.</p>
          <p class="text-sm">Proposte vegane e gluten free.</p>
        </div>
      </div>

      <div
        class="flex flex-col justify-center items-center bg-purple h-72 w-72 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-purple outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <div class="font-bold">Comodità</div>
        <div class="flex flex-col justify-center items-center">
          <p class="text-sm">
            Di' addio alle mattinate frenetiche. Ordina comodamente dal tuo
            divano.
          </p>
        </div>
      </div>

      <div
        class="flex flex-col justify-center items-center bg-pink h-80 w-80 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-pink outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <div class="font-bold">
          Snacks Calendar <br />
          La merenda che cambia, <br />
          come tuo figlio
        </div>
        <div class="flex flex-col justify-center items-center">
          <p class="text-sm">
            Ogni giorno uno snack diverso.<br />
            Una dieta varia e sana è fondamentale per la salute di tuo figlio.
          </p>
        </div>
      </div>

      <div
        class="flex flex-col justify-center items-center bg-purple h-72 w-72 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-purple outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <div class="font-bold">Risparmia con gusto</div>
        <p class="text-sm">
          Prezzi più bassi rispetto alle merende industriali.
        </p>
      </div>
      <div
        class="flex flex-col justify-center items-center bg-yellow h-64 w-64 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <div class="font-bold">Zero rischi</div>
        <p class="text-sm">
          Tuo figlio non attraverserà più la strada né gestirà soldi per
          comprare la merenda.<br />Più sicurezza per lui, più serenità per te.
        </p>
      </div>
    </div>
    <div
      class="max-w-screen-xl mx-auto flex flex-col justify-center items-center py-16 px-4 gap-12"
    >
      <!-- <h2 class="text-4xl font-bold">Snacks Calendar</h2> -->
      <div class="max-w-screen-xl mx-auto -mt-16">
        <video class="w-full h-auto px-4" autoplay muted>
          <source src="../static/calendar-header.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div class="-mt-16">
        <Calendar />
      </div>
    </div>
    <div>
      <div
        class="max-w-screen-xl mx-auto flex flex-col justify-center items-center py-16 px-4 gap-12"
      >
        <!-- <h2 class="text-4xl font-bold">Migliori store in zona</h2> -->
        <div class="max-w-screen-xl mx-auto -mt-16">
          <video class="w-full h-auto px-4" autoplay muted>
            <source src="../static/best-stores-header.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      </div>
      <div class="-mt-32">
        <div class="flex flex-wrap justify-center items-center gap-8 lg:p-8">
          <div v-for="store in stores" :key="store.id">
            <div class="flex flex-col justify-center items-center gap-2">
              <nuxt-link
                :to="{
                  name: 'stores-username',
                  params: { username: store.username },
                  query: {
                    first_name: store.first_name,
                    last_name: store.last_name,
                    profile_picture: store.profile_picture,
                    location: store.location,
                  },
                }"
              >
                <div
                  class="flex justify-center items-center h-60 w-60 bg-gray-200 rounded-xl transition-all duration-200 outline outline-4 outline-brown outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500"
                >
                  <img
                    :src="`${store.profile_picture}`"
                    alt="Profile Picture"
                    class="bg-center bg-contain bg-no-repeat h-52 w-52"
                  />
                </div>
              </nuxt-link>
              <div class="flex flex-col justify-center items-center mt-2">
                <div class="flex items-center justify-center gap-1">
                  <p class="font-bold">
                    {{ store.first_name }} {{ store.last_name }}
                  </p>
                  <img
                    src="../assets/icons/review.svg"
                    alt="star"
                    class="h-6 w-6"
                  />
                </div>
                <p class="text-xs opacity-80">{{ store.location }}</p>
              </div>
            </div>
          </div>
        </div>
        <Footer />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
import { checkAuthStatus } from "../utils/auth";

interface User {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  location: string;
  profile_picture: string;
}

const isAuthenticated = ref<boolean>(false);
const currentUserData = ref<User | null>(null);

const stores = ref<User[]>([]);

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();

  try {
    const response = await axios.get("http://localhost:8000/api/stores/");
    stores.value = response.data;
    console.log("Users fetched:", stores.value);
  } catch (error) {
    console.error("Error fetching user data:", error);
  }
});
</script>