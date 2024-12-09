<template>
  <div>
    <Navbar />
    <div class="max-w-screen-xl mx-auto pb-8 mt-8">
      <video class="w-full h-full px-4" autoplay muted>
        <source src="../static/home-header.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
    <div class="md:hidden -mt-12">
      <Slider :slides="sellingPoints">
        <template #default="{ slide }">
          <div :class="slide.class">
            <img
              :src="slide.imgSrc"
              :alt="slide.imgAlt"
              :class="slide.imgClass"
            />
            <div class="font-bold text-center">{{ slide.title }}</div>
            <div class="flex flex-col justify-center items-center">
              <p
                class="text-sm"
                v-for="(text, index) in slide.texts"
                :key="index"
              >
                {{ text }}
              </p>
            </div>
          </div>
        </template>
      </Slider>
    </div>

    <div
      class="hidden md:flex justify-center items-center py-16 px-4 gap-12 mx-auto overflow-hidden"
    >
      <div
        class="flex flex-col justify-center items-center bg-yellow h-64 w-64 rounded-xl p-4 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <img src="../assets/icons/health.svg" alt="Health" class="h-12 w-12" />
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
        <img
          src="../assets/icons/comfort.svg"
          alt="Comfort"
          class="h-14 w-14"
        />
        <div class="font-bold">Comodità</div>
        <div class="flex flex-col justify-center items-center">
          <p class="text-sm">
            Di' addio alle mattinate frenetiche. Ordina comodamente dal tuo
            divano.
          </p>
        </div>
      </div>

      <div
        class="flex flex-col justify-center items-center bg-yellow h-80 w-80 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <img
          src="../assets/icons/calendar.svg"
          alt="Calendar"
          class="h-12 w-12"
        />
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
        <img src="../assets/icons/cash.svg" alt="Cash" class="h-12 w-12" />
        <div class="font-bold">Risparmio con gusto</div>
        <p class="text-sm">
          Prezzi più bassi rispetto alle merende industriali.
        </p>
      </div>
      <div
        class="flex flex-col justify-center items-center bg-yellow h-64 w-64 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <img src="../assets/icons/safety.svg" alt="Safety" class="h-12 w-12" />
        <div class="font-bold">Zero rischi / Al sicuro</div>
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
    <div class="py-12 mb-4">
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
      <div class="-mt-12 md:-mt-32">
        <div
          class="hidden md:flex flex-wrap justify-center items-center gap-8 lg:p-8"
        >
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
                    bio: store.bio,
                  },
                }"
              >
                <div
                  class="flex justify-center items-center h-60 w-60 bg-white rounded-xl transition-all duration-200 outline outline-4 outline-brown outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500"
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

        <div class="md:hidden -mt-24 md:-mt-8">
          <Slider :slides="stores">
            <template #default="{ slide }">
              <div class="flex flex-col justify-center items-center gap-2">
                <nuxt-link
                  :to="{
                    name: 'stores-username',
                    params: { username: slide.username },
                    query: {
                      first_name: slide.first_name,
                      last_name: slide.last_name,
                      profile_picture: slide.profile_picture,
                      location: slide.location,
                      bio: slide.bio,
                    },
                  }"
                >
                  <div
                    class="flex justify-center items-center h-56 w-56 bg-white rounded-xl transition-all duration-200 outline outline-4 outline-brown outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500"
                  >
                    <img
                      :src="`${slide.profile_picture}`"
                      alt="Profile Picture"
                      class="bg-center bg-contain bg-no-repeat h-52 w-52"
                    />
                  </div>
                </nuxt-link>
                <div class="flex flex-col justify-center items-center mt-2">
                  <div class="flex items-center justify-center gap-1">
                    <p class="font-bold">
                      {{ slide.first_name }} {{ slide.last_name }}
                    </p>
                    <img
                      src="../assets/icons/review.svg"
                      alt="star"
                      class="h-6 w-6"
                    />
                  </div>
                  <p class="text-xs opacity-80">{{ slide.location }}</p>
                </div>
              </div>
            </template>
          </Slider>
        </div>
      </div>
    </div>
    <Footer />
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
  bio: string;
}

const isAuthenticated = ref<boolean>(false);
const currentUserData = ref<User | null>(null);

const stores = ref<User[]>([]);

import healthIcon from "@/assets/icons/health.svg";
import comfortIcon from "@/assets/icons/comfort.svg";
import calendarIcon from "@/assets/icons/calendar.svg";
import cashIcon from "@/assets/icons/cash.svg";
import safetyIcon from "@/assets/icons/safety.svg";

const sellingPoints = [
  {
    class:
      "flex flex-col justify-center items-center bg-yellow h-56 w-56 rounded-xl p-4 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
    imgSrc: healthIcon,
    imgAlt: "Health",
    imgClass: "h-12 w-12",
    title: "Salute e tutela",
    texts: [
      "Trasparenza sugli ingredienti.",
      "Allergeni sempre in evidenza.",
      "Proposte vegane e gluten free.",
    ],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-purple h-56 w-56 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-purple outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
    imgSrc: comfortIcon,
    imgAlt: "Comfort",
    imgClass: "h-14 w-14",
    title: "Comodità",
    texts: [
      "Di' addio alle mattinate frenetiche. Ordina comodamente dal tuo divano.",
    ],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-yellow h-56 w-56 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
    imgSrc: calendarIcon,
    imgAlt: "Calendar",
    imgClass: "h-12 w-12",
    title: "Snacks Calendar",
    texts: [
      "Ogni giorno uno snack diverso.",
      "Una dieta varia e sana è fondamentale per la salute di tuo figlio.",
    ],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-purple h-56 w-56 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-purple outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
    imgSrc: cashIcon,
    imgAlt: "Cash",
    imgClass: "h-12 w-12",
    title: "Risparmia con gusto",
    texts: ["Prezzi più bassi rispetto alle merende industriali."],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-yellow h-56 w-56 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
    imgSrc: safetyIcon,
    imgAlt: "Safety",
    imgClass: "h-12 w-12",
    title: "Zero rischi",
    texts: [
      "Tuo figlio non attraverserà più la strada né gestirà soldi per comprare la merenda.",
      "Più sicurezza per lui, più serenità per te.",
    ],
  },
];

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

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

import axiosInstance from "../utils/axiosInstance";

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
  isAuthenticated.value = await checkAuthStatus();

  const stripePubKey = await getStripePubKey();
  stripe.value = Stripe(stripePubKey);

  try {
    const response = await axios.get("http://localhost:8000/api/stores/");
    stores.value = response.data;
    console.log("Users fetched:", stores.value);
  } catch (error) {
    console.error("Error fetching user data:", error);
  }
});
</script>