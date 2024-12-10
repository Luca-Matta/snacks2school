<template>
  <div
    v-if="isVisible"
    class="fixed inset-0 bg-black bg-opacity-70 flex justify-center items-center z-30"
  >
    <div
      class="bg-white p-8 rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-96"
    >
      <h2 class="text-xl text-center font-bold">
        Ordina lo snack del <span class="lowercase">{{ selectedDay }}</span>
      </h2>
      <div v-if="userHasCredit" class="flex justify-center py-4 text-sm">
        Hai {{ currentUser.credit_wallet_amount }}€ sul tuo portafoglio di
        credito
      </div>
      <div
        v-if="!userHasCredit"
        class="flex flex-col justify-center items-center py-4 text-sm text-center gap-4"
      >
        <div>Il tuo portafoglio di credito è vuoto</div>
        <div>
          <button
            @click="chargeCreditWallet"
            class="flex justify-center mx-auto btn bg-yellow uppercase text-black text-xs shadow-button py-3 px-6 rounded-lg"
          >
            Ricaricalo e ordina la tua merenda!
          </button>
        </div>
      </div>
      <div v-if="userHasCredit" class="mb-1 relative">
        <div
          @click="toggleStoresDropdown"
          class="mt-1 flex justify-between w-full px-3 py-2 border-2 border-yellow focus:border-yellow rounded-md cursor-pointer bg-white"
        >
          <span class="text-xs font-bold opacity-80">{{
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
              class="cursor-pointer px-4 py-2 hover:bg-gray-200 text-sm font-bold"
            >
              {{ store.first_name }} {{ store.last_name }}
            </li>
          </ul>
        </div>
      </div>
      <div v-if="userHasCredit && snacks.length" class="mb-1 mt-4 relative">
        <div
          @click="toggleSnacksDropdown"
          class="mt-1 flex justify-between items-center w-full px-3 py-2 border-2 border-yellow focus:border-yellow rounded-md cursor-pointer bg-white"
        >
          <div class="flex items-center gap-2">
            <img
              v-if="selectedSnack"
              :src="selectedSnack.image"
              alt="snack"
              class="bg-center bg-contain bg-no-repeat h-7 w-7"
            />
            <span class="text-xs font-bold opacity-80">{{
              selectedSnack ? selectedSnack.name : "Snacks disponibili..."
            }}</span>
            <span v-if="selectedSnack" class="text-xs opacity-80 mr-2"
              >€{{ selectedSnack.gross_price }}</span
            >
          </div>
          <div>
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
        </div>
        <div
          v-if="snacksDropdownOpen"
          class="absolute mt-1 w-full rounded-md bg-white shadow-card z-20"
        >
          <ul class="max-h-60 overflow-auto">
            <li
              v-for="(snack, index) in snacks"
              :key="index"
              @click="selectSnack(snack)"
              class="flex justify-between items-center cursor-pointer px-4 py-2 hover:bg-gray-200 gap-2"
            >
              <div class="flex gap-2 mr-4">
                <div class="flex justify-center items-center">
                  <img
                    :src="snack.image"
                    alt="snack"
                    class="bg-center bg-contain bg-no-repeat h-7 w-7"
                  />
                </div>
                <div class="text-xs font-bold">
                  {{ snack.name }}
                </div>
              </div>
              <div class="text-xs">€{{ snack.gross_price }}</div>
            </li>
          </ul>
        </div>
      </div>
      <div v-if="userHasCredit" class="flex justify-center gap-2">
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
import { defineProps, defineEmits, onMounted, ref, computed, watch } from "vue";
import { checkAuthStatus, getCurrentUserData } from "../utils/auth";
import axios from "axios";

defineProps({
  isVisible: Boolean,
  selectedDay: String,
});

const emit = defineEmits(["close", "placeOrder"]);

interface Store {
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
  gross_price: number;
  seller: Store;
}

const stores = ref<Store[]>([]);
const snacks = ref<Snack[]>([]);
const selectedStore = ref<Store | null>(null);
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

const fetchSnacks = async (username: string) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/snacks/?username=${username}`
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

const selectStore = (store: Store) => {
  selectedStore.value = store;
  storesDropdownOpen.value = false;
  fetchSnacks(store.username);
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

const currentUser = ref<any>(null);

const userHasCredit = computed(() => {
  return currentUser.value && currentUser.value.credit_wallet_amount > 0;
});

import axiosInstance from "../utils/axiosInstance";

const stripe = ref(null);

const getStripePubKey = async () => {
  const response = await axios.get(
    "http://localhost:8000/api/v1/stripe/stripe-pub-key/"
  );
  console.log("Public key fetched:", response.data);

  const stripePubKey = response.data.publicKey;
  console.log(stripePubKey);
  return stripePubKey;
};

const chargeCreditWallet = async () => {
  try {
    const csrfToken = await axiosInstance.get("csrf-token/");
    const response = await axiosInstance.post(
      "v1/stripe/create-checkout-session/",
      {},
      {
        headers: {
          "X-CSRFToken": csrfToken.data.csrfToken,
        },
        withCredentials: true,
      }
    );
    console.log("Checkout session created:", response);
    return stripe.value.redirectToCheckout({
      sessionId: response.data.sessionId,
    });
  } catch (error) {
    console.error("Error creating checkout session:", error);
  }
};

onMounted(async () => {
  fetchStores();
  currentUser.value = await getCurrentUserData();
  console.log("currentUser:", currentUser.value);
  const stripePubKey = await getStripePubKey();
  stripe.value = Stripe(stripePubKey);
});
</script>