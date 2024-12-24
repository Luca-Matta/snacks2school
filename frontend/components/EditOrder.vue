<template>
  <div
    v-if="isEditOrderVisible"
    class="fixed inset-0 bg-black bg-opacity-70 flex justify-center items-center z-30"
  >
    <div
      class="bg-white p-8 rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-96"
    >
      <h2 class="text-xl text-center font-bold">
        Modifica l'ordina del
        <span class="lowercase">{{ selectedDay }}</span>
      </h2>
      <div class="flex flex-col justify-center py-4 gap-2">
        <div class="flex flex-col gap-1">
          <div
            v-for="snack in dailyOrderSnacks"
            :key="snack.name"
            class="flex justify-between items-center text-xs font-bold gap-1"
          >
            <div class="flex items-center gap-1">
              <img :src="snack.image" :alt="snack.name" class="h-7 w-7" />
              <div>
                {{ snack.name }}
              </div>
            </div>
            <img
              src="../assets/icons/close.png"
              alt="Close"
              class="h-4 w-4 cursor-pointer"
            />
          </div>
        </div>
        <div class="flex flex-col gap-1">
          <div
            v-for="drink in dailyOrderDrinks"
            :key="drink.name"
            class="flex justify-between items-center text-xs font-bold gap-1"
          >
            <div class="flex items-center gap-1">
              <img :src="drink.image" :alt="drink.name" class="h-7 w-7" />
              <div>
                {{ drink.name }}
              </div>
            </div>
            <img
              src="../assets/icons/close.png"
              alt="Close"
              class="h-4 w-4 cursor-pointer"
            />
          </div>
        </div>
      </div>
      <div
        class="flex justify-center items-center text-center font-bold mt-2 gap-2"
      >
        <div>Vuoi aggiungere qualcosa?</div>
      </div>
      <div
        v-if="userHasCredit"
        class="flex justify-center text-center py-4 text-xs"
      >
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
          class="mt-1 flex justify-between items-center w-full px-3 py-2 border-2 border-yellow focus:border-yellow rounded-md cursor-pointer bg-white gap-2"
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
          </div>
          <div class="flex items-center gap-2">
            <span v-if="selectedSnack" class="text-xs opacity-80 mr-2"
              >€{{ selectedSnack.gross_price }}</span
            >
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
              <div class="flex items-center gap-2 mr-4">
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
      <h6
        v-if="userHasCredit && drinks.length"
        class="text-sm text-center font-bold mt-3"
      >
        Vuoi ordinare una bevanda?
      </h6>
      <div v-if="userHasCredit && drinks.length" class="mb-1 mt-4 relative">
        <div
          @click="toggleDrinksDropdown"
          class="mt-1 flex justify-between items-center w-full px-3 py-2 border-2 border-yellow focus:border-yellow rounded-md cursor-pointer bg-white gap-2"
        >
          <div class="flex items-center gap-2">
            <img
              v-if="selectedDrink"
              :src="selectedDrink.image"
              alt="drink"
              class="bg-center bg-contain bg-no-repeat h-7 w-7"
            />
            <span class="text-xs font-bold opacity-80">{{
              selectedDrink ? selectedDrink.name : "Bevande disponibili..."
            }}</span>
          </div>
          <div class="flex items-center gap-2">
            <span v-if="selectedDrink" class="text-xs opacity-80 mr-2"
              >€{{ selectedDrink.gross_price }}</span
            >
            <svg
              :class="{
                'rotate-180': drinksDropdownOpen,
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
          v-if="drinksDropdownOpen"
          class="absolute mt-1 w-full rounded-md bg-white shadow-card z-20"
        >
          <ul class="max-h-60 overflow-auto">
            <li
              v-for="(drink, index) in drinks"
              :key="index"
              @click="selectDrink(drink)"
              class="flex justify-between items-center cursor-pointer px-4 py-2 hover:bg-gray-200 gap-2"
            >
              <div class="flex items-center gap-2 mr-4">
                <div class="flex justify-center items-center">
                  <img
                    :src="drink.image"
                    alt="drink"
                    class="bg-center bg-contain bg-no-repeat h-7 w-7"
                  />
                </div>
                <div class="text-xs font-bold">
                  {{ drink.name }}
                </div>
              </div>
              <div class="text-xs">€{{ drink.gross_price }}</div>
            </li>
          </ul>
        </div>
      </div>
      <h6
        v-if="selectedSnack || selectedDrink"
        class="text-xs text-center mt-3"
      >
        <span class="text-sm font-bold">Totale:</span> €{{
          total_price.toFixed(2)
        }}
      </h6>
      <div
        v-if="userHasCredit && userHasEnoughCredit"
        class="flex justify-center gap-2"
      >
        <button
          @click="$emit('close')"
          class="btn bg-black w-full font-bold text-white uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
        >
          Annulla
        </button>
        <button
          @click="placeOrder"
          class="btn bg-yellow w-full font-bold uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
        >
          Ordina
        </button>
      </div>
      <div
        v-if="!userHasEnoughCredit && userHasCredit"
        class="flex flex-col justify-center items-center py-4 text-sm text-center gap-4"
      >
        <div class="font-bold underline">
          Non hai abbastanza denaro sul portafoglio di credito per effettuare
          l'acquisto
        </div>
        <div>
          <button
            @click="chargeCreditWallet"
            class="flex justify-center mx-auto btn bg-yellow uppercase text-black text-xs shadow-button py-3 px-6 rounded-lg"
          >
            Ricaricalo e ordina la tua merenda!
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  defineProps,
  defineEmits,
  onMounted,
  ref,
  computed,
  watch,
  watchEffect,
} from "vue";
import { checkAuthStatus, getCurrentUserData } from "../utils/auth";
import axios from "axios";

const props = defineProps({
  isEditOrderVisible: Boolean,
  selectedDay: String,
  selectedDate: String,
});

const getImageUrl = (path) => {
  const baseUrl = "http://localhost:8000";
  return `${baseUrl}${path}`;
};

watch(
  () => props.selectedDate,
  (newDate) => {
    console.log("Selected date:", newDate);
  }
);

const emit = defineEmits(["close", "openEditOrder"]);

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

interface Drink {
  id: number;
  name: string;
  date: string;
  gross_price: number;
  seller: Store;
}

interface DailyOrderData {
  snacks: Snack[];
  drinks: Drink[];
}

const stores = ref<Store[]>([]);
const snacks = ref<Snack[]>([]);
const drinks = ref<Drink[]>([]);
const selectedStore = ref<Store | null>(null);
const storesDropdownOpen = ref(false);
const snacksDropdownOpen = ref(false);
const drinksDropdownOpen = ref(false);

const dailyOrderData = ref<DailyOrderData | null>(null);
const dailyOrderSnacks = ref<string>("");
const dailyOrderDrinks = ref<string>("");

const fetchDailyOrder = async (date: string) => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await axios.get(
      `http://localhost:8000/api/orders-by-day/`,
      {
        params: { selected_day: date },
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );

    dailyOrderData.value = response.data;
    dailyOrderSnacks.value = dailyOrderData.value.snacks;
    dailyOrderDrinks.value = dailyOrderData.value.drinks;
  } catch (error) {
    console.error("Error fetching day data:", error);
  }
};

const normalizeDate = (date: string) => {
  const parsedDate = new Date(date);
  const year = parsedDate.getFullYear();
  const month = String(parsedDate.getMonth() + 1).padStart(2, "0");
  const day = String(parsedDate.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
};

watch(
  [() => props.isEditOrderVisible, () => props.selectedDate],
  async ([isVisible, date]) => {
    if (isVisible && date) {
      dailyOrderData.value = null;
      const normalizedDate = normalizeDate(date);
      await fetchDailyOrder(normalizedDate);
    } else {
      dailyOrderData.value = null;
    }
  },
  { immediate: true }
);

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

const fetchDrinks = async (username: string) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/drinks/?username=${username}`
    );
    drinks.value = response.data;
    console.log("Drinks fetched:", drinks.value);
  } catch (error) {
    console.error("Error fetching drink data:", error);
  }
};

const toggleStoresDropdown = () => {
  storesDropdownOpen.value = !storesDropdownOpen.value;
};

const selectStore = (store: Store) => {
  selectedStore.value = store;
  storesDropdownOpen.value = false;
  fetchSnacks(store.username);
  fetchDrinks(store.username);
};

const toggleSnacksDropdown = () => {
  snacksDropdownOpen.value = !snacksDropdownOpen.value;
};

const toggleDrinksDropdown = () => {
  drinksDropdownOpen.value = !drinksDropdownOpen.value;
};

const selectedSnack = ref<Snack | null>(null);
const selectedDrink = ref<Drink | null>(null);
const selectSnack = (snack: Snack) => {
  selectedSnack.value = snack;
  snacksDropdownOpen.value = false;
  drinksDropdownOpen.value = false;
};

const selectDrink = (drink: Drink) => {
  selectedDrink.value = drink;
  drinksDropdownOpen.value = false;
  snacksDropdownOpen.value = false;
};

const total_price = computed(() => {
  let price = 0;
  if (selectedSnack.value) {
    price += parseFloat(selectedSnack.value.gross_price);
  }
  if (selectedDrink.value) {
    price += parseFloat(selectedDrink.value.gross_price);
  }
  return price;
});

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const placeOrder = async () => {
  if (!selectedStore.value || (!selectedSnack.value && !selectedDrink.value)) {
    console.error("Store, Snack, and Drink must be selected");
    return;
  }
  const csrfToken = await getCsrfToken();

  try {
    const payload = {
      seller_id: selectedStore.value.id,
      selected_date: props.selectedDate,
      total_price: total_price.value.toFixed(2),
      school: currentUser.value.associated_school,
      school_class: currentUser.value.school_class,
    };

    if (selectedSnack.value) {
      payload.snack_id = selectedSnack.value.id;
    }

    if (selectedDrink.value) {
      payload.drink_id = selectedDrink.value.id;
    }

    const response = await axios.post(
      "http://localhost:8000/api/create-order/",
      payload,
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );
    console.log("Order placed:", response.data);
  } catch (error) {
    console.error("Error placing order:", error);
  } finally {
    emit("close");
    window.location.reload();
  }
};

const currentUser = ref<any>(null);

const userHasCredit = computed(() => {
  return currentUser.value && currentUser.value.credit_wallet_amount > 0;
});

const userHasEnoughCredit = computed(() => {
  return (
    (selectedSnack.value ? parseFloat(selectedSnack.value.gross_price) : 0) +
      (selectedDrink.value ? parseFloat(selectedDrink.value.gross_price) : 0) <=
    currentUser.value.credit_wallet_amount
  );
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
  currentUser.value = await getCurrentUserData();
  fetchStores();
  fetchUserCalendar();
  console.log("currentUser:", currentUser.value);
  const stripePubKey = await getStripePubKey();
  stripe.value = Stripe(stripePubKey);
});
</script>