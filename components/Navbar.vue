<template>
  <header
    class="bg-background/75 backdrop-blur-[8px] border-b-[0.5px] border-gray border-opacity-100 sticky top-0 z-50"
  >
    <div
      class="mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl flex items-center justify-between gap-3 h-16"
    >
      <div class="flex items-center gap-1.5">
        <router-link
          to="/"
          class="flex-shrink-0 font-bold text-xl text-gray-900 dark:text-white flex items-end gap-1.5"
          aria-label="Home"
        >
          <img src="../assets/icons/logo.svg" alt="star" class="h-28 w-28" />
        </router-link>
      </div>
      <div v-if="currentUser">
        <!-- <img
          :src="`${currentUser?.profile_picture}`"
          alt="Profile Picture"
          class="bg-center bg-contain bg-no-repeat h-52 w-52"
        /> -->
        <div class="flex items-center space-x-2">
          <span>Ehi {{ currentUser?.first_name }}</span>
          <div class="relative">
            <button @click="toggleDropdown" class="flex items-center space-x-1">
              <svg
                :class="{
                  'rotate-180': dropdownOpen,
                  'transition-transform': true,
                }"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                class="w-5 h-5 text-gray-700"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                />
              </svg>
            </button>
            <div
              v-if="dropdownOpen"
              class="absolute right-0 mt-2 w-36 bg-white border border-gray-200 !rounded-md shadow-lg flex flex-col gap-1"
            >
              <router-link
                to="/profile"
                class="block w-full text-left px-4 pt-2 text-gray-700 hover:bg-gray-100"
                >Il mio profilo</router-link
              >
              <button
                @click.prevent="handleLogout"
                class="block w-full text-left px-4 pb-2 text-gray-700 hover:bg-gray-100"
              >
                Esci
              </button>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="flex items-center gap-3">
        <router-link to="/login">
          <button class="btn bg-[#ffa500] px-4 py-2 !rounded-md">Accedi</button>
        </router-link>
        <router-link to="/group-choice">
          <button class="btn bg-black text-white px-4 py-2 !rounded-md">
            Registrati
          </button>
        </router-link>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import {
  checkAuthStatus,
  getCurrentUserData,
  deleteCookie,
} from "../utils/auth";
import axios from "axios";
import { useRouter } from "vue-router";

const isAuthenticated = ref<boolean>(false);
const currentUser = ref<any>(null);
const router = useRouter();

const dropdownOpen = ref(false);

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value;
};

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const handleLogout = async () => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await axios.post("http://localhost:8000/api/logout/", {
      headers: {
        "X-CSRFToken": csrfToken,
      },
      withCredentials: true,
    });
    if (response.status === 200) {
      localStorage.removeItem("token");
      isAuthenticated.value = false;
      currentUser.value = null;
      router.push("/login");
    }
  } catch (error) {
    console.error("Logout failed:", error);
  }
};

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
  currentUser.value = await getCurrentUserData();
});
</script>