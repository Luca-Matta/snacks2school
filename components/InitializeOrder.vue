<template>
  <div
    v-if="isInitializeOrderVisible"
    class="fixed inset-0 flex justify-center items-center z-30 px-4 md:px-0"
    style="backdrop-filter: blur(50px)"
  >
    <div
      ref="modalContainer"
      class="bg-white p-8 !rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-full max-w-96 max-h-[500px] overflow-y-auto"
    >
      <h2 class="text-xl text-center font-bold">
        Ordina lo snack del <span class="lowercase">{{ selectedDay }}</span>
      </h2>
      <div
        v-if="userHasCredit"
        class="flex justify-center items-center text-center py-4 text-xs gap-2 font-bold"
      >
        <img
          src="../assets/icons/credit-card.png"
          alt="Card"
          class="h-6 w-6 cursor-pointer"
        />
        <div>
          Hai {{ currentUser.credit_wallet_amount }}€ sul tuo portafoglio di
          credito
        </div>
      </div>
      <div
        v-if="!userHasCredit"
        class="flex flex-col justify-center items-center py-4 text-sm text-center gap-4"
      >
        <div
          class="flex justify-center items-center text-center py-4 text-xs gap-2 font-bold"
        >
          <img
            src="../assets/icons/no-money.png"
            alt="Card"
            class="h-9 w-9 cursor-pointer"
          />
          <div>Il tuo portafoglio di credito è vuoto</div>
        </div>
        <div>
          <button
            @click="chargeCreditWallet"
            class="flex justify-center mx-auto btn bg-[#ffa500] uppercase text-black text-xs shadow-button !py-3 !px-6 !rounded-lg"
          >
            Ricaricalo e ordina la tua merenda!
          </button>
        </div>
      </div>
      <div v-if="isOrderEditable && userHasCredit">
        <div class="text-center text-xs font-bold mb-2">
          L'ordine è per merenda o per pranzo?
        </div>

        <div class="relative mb-4">
          <div
            @click="toggleMealTypeDropdown"
            class="mt-1 flex justify-between w-full px-3 py-2 border-2 border-[#ffa500] focus:border-[#ffa500] !rounded-md cursor-pointer bg-white"
          >
            <span class="text-xs font-bold opacity-80">{{
              selectedMealType
            }}</span>
            <svg
              :class="{
                'rotate-180': mealTypeDropdownOpen,
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
            v-if="mealTypeDropdownOpen"
            class="absolute mt-1 w-full !rounded-md bg-white shadow-card z-10"
          >
            <ul class="max-h-60 overflow-auto">
              <li
                @click="selectMealType('Merenda')"
                class="cursor-pointer px-4 py-2 hover:bg-gray-200 text-sm font-bold"
              >
                Merenda
              </li>
              <li
                @click="selectMealType('Pranzo')"
                class="cursor-pointer px-4 py-2 hover:bg-gray-200 text-sm font-bold"
              >
                Pranzo
              </li>
            </ul>
          </div>
        </div>

        <div
          v-if="children.length > 1"
          class="text-center text-xs font-bold mb-2"
        >
          Per chi desideri ordinare?
        </div>
        <div class="relative mb-4" v-if="children.length > 1">
          <div
            @click="toggleChildrenDropdown"
            class="mt-1 flex justify-between w-full px-3 py-2 border-2 border-[#ffa500] focus:border-[#ffa500] !rounded-md cursor-pointer bg-white"
          >
            <span class="text-xs font-bold opacity-80">
              {{
                selectedChild
                  ? `${selectedChild.first_name} ${selectedChild.last_name}`
                  : "Seleziona..."
              }}
            </span>
            <svg
              :class="{
                'rotate-180': childrenDropdownOpen,
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
            v-if="childrenDropdownOpen"
            class="absolute mt-1 w-full !rounded-md bg-white shadow-card z-10"
          >
            <ul class="max-h-60 overflow-auto">
              <li
                v-for="(child, index) in children"
                :key="index"
                @click="selectChild(child)"
                class="cursor-pointer px-4 py-2 hover:bg-gray-200 text-sm font-bold"
              >
                {{ child.first_name }} {{ child.last_name }}
              </li>
            </ul>
          </div>
        </div>

        <div
          class="text-center text-xs font-bold mb-2"
          v-if="selectedChild && selectedChild.associated_schools.length > 1"
        >
          In quale scuola vuoi ricevere l'ordine?
        </div>
        <div
          class="relative mb-4"
          v-if="selectedChild && selectedChild.associated_schools.length > 1"
        >
          <div
            @click="toggleSchoolsDropdown"
            class="mt-1 flex justify-between w-full px-3 py-2 border-2 border-[#ffa500] focus:border-[#ffa500] !rounded-md cursor-pointer bg-white"
          >
            <span class="text-xs font-bold opacity-80">{{
              selectedSchool
                ? getSchoolName(selectedSchool)
                : "Scegli la scuola..."
            }}</span>
            <svg
              :class="{
                'rotate-180': schoolsDropdownOpen,
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
            v-if="schoolsDropdownOpen"
            class="absolute mt-1 w-full !rounded-md bg-white shadow-card z-10"
          >
            <ul class="max-h-60 overflow-auto">
              <li
                v-for="(school, index) in selectedChild?.associated_schools"
                :key="index"
                @click="selectSchool(school)"
                class="cursor-pointer px-4 py-2 hover:bg-gray-200 text-sm font-bold"
              >
                {{ school.name }}
              </li>
            </ul>
          </div>
        </div>
        <div v-if="userHasCredit" class="mb-1 relative">
          <div
            @click="toggleStoresDropdown"
            class="mt-1 flex justify-between w-full px-3 py-2 border-2 border-[#ffa500] focus:border-[#ffa500] !rounded-md cursor-pointer bg-white"
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
            class="absolute mt-1 w-full !rounded-md bg-white shadow-card z-10"
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
            class="mt-1 flex justify-between items-center w-full px-3 py-2 border-2 border-[#ffa500] focus:border-[#ffa500] !rounded-md cursor-pointer bg-white gap-2"
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
            class="absolute mt-1 w-full !rounded-md bg-white shadow-card z-20"
          >
            <ul class="max-h-60 overflow-auto">
              <li
                v-for="(snack, index) in snacks"
                :key="index"
                @click="selectSnack(snack)"
                class="flex justify-between items-center cursor-pointer px-4 py-2 hover:bg-gray-200 gap-2"
              >
                <div class="flex justify-center items-center flex-shrink-0">
                  <img
                    :src="snack.image"
                    alt="snack"
                    class="bg-center bg-contain bg-no-repeat !h-7 !w-7"
                  />
                </div>
                <div class="text-xs font-bold flex-1 ml-1">
                  {{ snack.name }}
                </div>
                <div class="text-xs flex-shrink-0">
                  €{{ snack.gross_price }}
                </div>
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
            class="mt-1 flex justify-between items-center w-full px-3 py-2 border-2 border-[#ffa500] focus:border-[#ffa500] !rounded-md cursor-pointer bg-white gap-2"
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
            class="absolute mt-1 w-full !rounded-md bg-white shadow-card z-20"
          >
            <ul class="max-h-44 overflow-auto">
              <li
                v-for="(drink, index) in drinks"
                :key="index"
                @click="selectDrink(drink)"
                class="flex justify-between items-center cursor-pointer px-4 py-2 hover:bg-gray-200 gap-2"
              >
                <div class="flex justify-center items-center flex-shrink-0">
                  <img
                    :src="drink.image"
                    alt="drink"
                    class="bg-center bg-contain bg-no-repeat !h-7 !w-7"
                  />
                </div>
                <div class="text-xs font-bold flex-1 ml-1">
                  {{ drink.name }}
                </div>
                <div class="text-xs flex-shrink-0">
                  €{{ drink.gross_price }}
                </div>
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
      </div>
      <div
        v-if="userHasCredit"
        class="text-center text-xs opacity-80 underline mt-2"
      >
        L'ordine può essere effettuato e modificato fino alle 13:30 del giorno
        precedente alla data di consegna.
      </div>
      <div
        v-if="userHasCredit && userHasEnoughCredit && isOrderEditable"
        class="flex justify-center gap-2"
      >
        <button
          @click="$emit('close')"
          class="btn bg-black w-full font-bold text-white uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
        >
          Annulla
        </button>
        <button
          @click="placeOrder"
          class="btn bg-[#ffa500] w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
        >
          Ordina
        </button>
      </div>
      <div
        v-if="!userHasEnoughCredit && userHasCredit"
        class="flex flex-col justify-center items-center pb-4 text-sm text-center gap-4"
      >
        <div
          class="flex flex-col justify-center items-center text-center py-4 text-xs font-bold"
        >
          <img
            src="../assets/icons/no-money.png"
            alt="Card"
            class="h-9 w-9 cursor-pointer"
          />
          <div class="font-bold underline">
            Non hai abbastanza denaro sul portafoglio di credito per effettuare
            l'acquisto
          </div>
        </div>
        <div>
          <button
            @click="chargeCreditWallet"
            class="flex justify-center mx-auto btn bg-[#ffa500] uppercase text-black text-xs shadow-button !py-3 !px-6 !rounded-lg"
          >
            Ricaricalo e ordina la tua merenda!
          </button>
        </div>
      </div>
      <button
        v-if="!isOrderEditable"
        @click="$emit('close')"
        class="btn bg-[#ffa500] w-full font-bold text-black uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
      >
        Chiudi
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, onMounted, ref, computed, watch } from "vue";
import {
  checkAuthStatus,
  getCurrentUserData,
  getChildrenForCurrentUser,
} from "../utils/auth";
import axios from "axios";

const props = defineProps<{
  isInitializeOrderVisible: boolean;
  selectedDay: string;
  selectedDate: string;
}>();

const emit = defineEmits(["close", "openInitializeOrder"]);

const isOrderEditable = computed(() => {
  const now = new Date();
  const cutoffTime = new Date(props.selectedDate);
  cutoffTime.setDate(cutoffTime.getDate() - 1);
  cutoffTime.setHours(13, 30, 0, 0);

  return now < cutoffTime;
});

watch(
  () => props.selectedDate,
  (newDate) => {
    console.log("Selected date:", newDate);
    if (!isOrderEditable.value) {
      console.log(
        "Cannot modify order after 13:30 the day before the delivery date."
      );
    }
  }
);

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

const stores = ref<Store[]>([]);
const snacks = ref<Snack[]>([]);
const drinks = ref<Drink[]>([]);
const selectedStore = ref<Store | null>(null);
const storesDropdownOpen = ref(false);
const snacksDropdownOpen = ref(false);
const drinksDropdownOpen = ref(false);
const schoolsDropdownOpen = ref(false);
const mealTypeDropdownOpen = ref(false);
const selectedMealType = ref("Merenda");
const childrenDropdownOpen = ref(false);
const children = ref<any[]>([]);
const selectedChild = ref(null);

function toggleMealTypeDropdown() {
  mealTypeDropdownOpen.value = !mealTypeDropdownOpen.value;
}

function selectMealType(mealType: string) {
  selectedMealType.value = mealType;
  mealTypeDropdownOpen.value = false;
}

const toggleSchoolsDropdown = () => {
  schoolsDropdownOpen.value = !schoolsDropdownOpen.value;
};

const toggleChildrenDropdown = () => {
  childrenDropdownOpen.value = !childrenDropdownOpen.value;
};

const selectSchool = (school: School) => {
  selectedSchool.value = school.id;
  schoolsDropdownOpen.value = false;
};

const getSchoolName = (schoolId) => {
  if (!selectedChild.value) return "Scegli la scuola...";
  const school = selectedChild.value.associated_schools.find(
    (s) => s.id === schoolId
  );
  return school ? school.name : "";
};

const fetchStores = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/stores/");
    stores.value = response.data;
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

const selectChild = (child) => {
  selectedChild.value = child;
  childrenDropdownOpen.value = false;
  if (child.associated_schools.length > 0) {
    selectedSchool.value = child.associated_schools[0].id;
  } else {
    selectedSchool.value = null;
  }
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

interface School {
  id: number;
  name: string;
}

const currentUser = ref<any>(null);
const associatedSchools = ref<School[]>([]);
const selectedSchool = ref<number | null>(null);

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
      school: selectedSchool.value,
      is_snack_break: selectedMealType.value === "Merenda",
      is_lunch_break: selectedMealType.value === "Pranzo",
      child_first_name: selectedChild.value.first_name,
      child_last_name: selectedChild.value.last_name,
      school_class: selectedChild.value.school_class,
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
  } catch (error) {
    console.error("Error placing order:", error);
  } finally {
    emit("close");
    window.location.reload();
  }
};

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

  const stripePubKey = response.data.publicKey;
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
    return stripe.value.redirectToCheckout({
      sessionId: response.data.sessionId,
    });
  } catch (error) {
    console.error("Error creating checkout session:", error);
  }
};

// const modalContainer = ref(null);

// const updateModalOverflow = () => {
//   if (modalContainer.value) {
//     modalContainer.value.style.overflow =
//       snacksDropdownOpen.value ||
//       drinksDropdownOpen.value ||
//       storesDropdownOpen.value
//         ? "visible"
//         : "auto";
//   }
// };

// watch(snacksDropdownOpen, updateModalOverflow);
// watch(drinksDropdownOpen, updateModalOverflow);
// watch(storesDropdownOpen, updateModalOverflow);

onMounted(async () => {
  fetchStores();
  currentUser.value = await getCurrentUserData();
  if (currentUser.value) {
    associatedSchools.value = currentUser.value.associated_schools;
    children.value = await getChildrenForCurrentUser();
    if (children.value.length > 0) {
      selectedChild.value = children.value[0];
      if (selectedChild.value.associated_schools.length > 0) {
        selectedSchool.value = selectedChild.value.associated_schools[0].id;
      }
    }
  }
  const stripePubKey = await getStripePubKey();
  stripe.value = Stripe(stripePubKey);
});
</script>