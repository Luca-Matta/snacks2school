<template>
  <div
    v-if="isVisible"
    class="fixed inset-0 bg-black bg-opacity-70 flex justify-center items-center"
  >
    <div
      class="bg-white p-8 rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-96"
    >
      <h2 class="text-xl text-center font-bold mb-4">
        Ordina lo snack del <span class="lowercase">{{ selectedDay }}</span>
      </h2>
      <div class="mb-1 relative">
        <div
          @click="toggleStoresDropdown"
          class="mt-1 flex justify-between w-full px-3 py-2 border-2 border-yellow focus:border-yellow rounded-md cursor-pointer bg-white"
        >
          <span class="text-sm opacity-80">{{
            selectedStore
              ? selectedStore.first_name + " " + selectedStore.last_name
              : "Scegli lo store..."
          }}</span>
          <svg
            :class="{
              'rotate-180': storesDropdownOpen,
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
        </div>
        <div
          v-if="storesDropdownOpen"
          class="absolute mt-1 w-full rounded-md bg-white shadow-card z-10"
        >
          <ul class="max-h-60 overflow-auto">
            <li
              v-for="(store, index) in stores"
              :key="index"
              @click="selectStore(store)"
              class="cursor-pointer px-4 py-2 hover:bg-gray-200"
            >
              {{ store.first_name }} {{ store.last_name }}
            </li>
          </ul>
        </div>
      </div>
      <div v-if="snacks.length" class="mb-1 mt-4 relative">
        <div
          @click="toggleSnacksDropdown"
          class="mt-1 flex justify-between w-full px-3 py-2 border-2 border-yellow focus:border-yellow rounded-md cursor-pointer bg-white"
        >
          <span class="text-sm opacity-80">{{
            selectedSnack ? selectedSnack.name : "Snacks disponibili..."
          }}</span>
          <svg
            :class="{
              'rotate-180': snacksDropdownOpen,
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
        </div>
        <div
          v-if="snacksDropdownOpen"
          class="absolute mt-1 w-full rounded-md bg-white shadow-card z-10"
        >
          <ul class="max-h-60 overflow-auto">
            <li
              v-for="(snack, index) in snacks"
              :key="index"
              @click="selectSnack(snack)"
              class="cursor-pointer px-4 py-2 hover:bg-gray-200"
            >
              {{ snack.name }} <span class="text-sm">€{{ snack.price }}</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="flex justify-center gap-2">
        <button
          @click="$emit('close')"
          class="btn bg-black w-full font-bold text-white uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
        >
          Annulla
        </button>
        <button
          @click="placeOrder"
          class="btn bg-yellow w-full font-bold text-white uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
        >
          Ordina
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, onMounted, ref, watch } from "vue";
import axios from "axios";

defineProps({
  isVisible: Boolean,
  selectedDay: String,
});

const emit = defineEmits(["close", "placeOrder"]);

interface User {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  location: string;
  profile_picture: string;
  bio: string;
}

interface Snack {
  id: number;
  name: string;
  date: string;
  seller: User;
}

const stores = ref<User[]>([]);
const snacks = ref<Snack[]>([]);
const selectedStore = ref<User | null>(null);
const storesDropdownOpen = ref(false);
const snacksDropdownOpen = ref(false);

const fetchStores = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/stores/");
    stores.value = response.data;
    console.log("Stores fetched:", stores.value);
  } catch (error) {
    console.error("Error fetching store data:", error);
  }
};

const fetchSnacks = async (storeId: number) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/snacks/?store_id=${storeId}`
    );
    snacks.value = response.data;
    console.log("Snacks fetched:", snacks.value);
  } catch (error) {
    console.error("Error fetching snack data:", error);
  }
};

const toggleStoresDropdown = () => {
  storesDropdownOpen.value = !storesDropdownOpen.value;
};

const selectStore = (store: User) => {
  selectedStore.value = store;
  storesDropdownOpen.value = false;
  fetchSnacks(store.id);
};

const toggleSnacksDropdown = () => {
  snacksDropdownOpen.value = !snacksDropdownOpen.value;
};

const selectedSnack = ref<Snack | null>(null);
const selectSnack = (snack: Snack) => {
  selectedSnack.value = snack;
  snacksDropdownOpen.value = false;
};

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const placeOrder = async () => {
  if (!selectedStore.value || !selectedSnack.value) {
    console.error("Store and Snack must be selected");
    return;
  }
  const csrfToken = await getCsrfToken();
  try {
    const response = await axios.post(
      "http://localhost:8000/api/create-order/",
      {
        seller_id: selectedStore.value.id,
        snack_id: selectedSnack.value.id,
      },
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );
    console.log("Order placed:", response.data);
    emit("close");
  } catch (error) {
    console.error("Error placing order:", error);
  }
};

onMounted(() => {
  fetchStores();
});
</script>