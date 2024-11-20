<template>
  <header
    class="bg-background/75 backdrop-blur-[8px] border-b-[0.5px] border-gray border-opacity-100 sticky top-0 z-50"
  >
    <div
      class="mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl flex items-center justify-between gap-3 h-16"
    >
      <div class="flex items-center gap-1.5">
        <nuxt-link
          to="/"
          class="flex-shrink-0 font-bold text-xl text-gray-900 dark:text-white flex items-end gap-1.5"
          aria-label="Home"
        >
          <img
            src="../assets/icons/extended-logo.svg"
            alt="star"
            class="h-60 w-60"
          />
        </nuxt-link>
      </div>
      <nav class="hidden md:flex items-center gap-4">
        <nuxt-link to="/stores" class="text-pink font-bold">Store</nuxt-link>
        <nuxt-link to="/stores" class="text-purple font-bold">Store</nuxt-link>
        <nuxt-link to="/stores" class="text-yellow font-bold"
          >Contatti</nuxt-link
        >
      </nav>
      <div v-if="isAuthenticated">
        <!-- <img
          :src="`${currentUser?.profile_picture}`"
          alt="Profile Picture"
          class="bg-center bg-contain bg-no-repeat h-52 w-52"
        /> -->
        <div>
          Ciao <span>{{ currentUser?.first_name }}</span>
        </div>
      </div>
      <div v-else class="flex items-center gap-3">
        <nuxt-link to="/login">
          <button class="btn bg-yellow text-white px-4 py-2 rounded-md">
            Accedi
          </button>
        </nuxt-link>
        <nuxt-link to="/signup">
          <button class="btn bg-black text-white px-4 py-2 rounded-md">
            Registrati
          </button>
        </nuxt-link>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { checkAuthStatus, getCurrentUserData } from "../utils/auth";

const isAuthenticated = ref<boolean>(false);
const currentUser = ref<any>(null);

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
  if (isAuthenticated.value) {
    currentUser.value = await getCurrentUserData();
    console.log("currentUser:", currentUser.value); // Debugging log
  }
});
</script>