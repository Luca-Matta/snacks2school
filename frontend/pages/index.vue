<template>
  <div class="overflow-x-hidden">
    <Navbar />
    <div
      class="flex justify-center items-center max-w-screen-xl mx-auto mt-12 gap-6"
    >
      <div class="text-5xl md:text-6xl lg:text-9xl text-center font-bold mb-4">
        <div>La <span class="text-yellow"> merenda</span> a</div>
        <div class="flex justify-center items-center gap-2 md:gap-6">
          <div class="flex items-center gap-2 md:gap-6">
            portata
            <img
              src="../assets/icons/desk.png"
              alt="Desk"
              class="h-10 md:h-36 w-10 md:w-36 cursor-pointer"
            />
            <span class="text-purple">di </span
            ><span class="text-pink">click</span>
          </div>
        </div>
      </div>
      <!-- <div class="text-4xl md:text-6xl lg:text-9xl text-center font-bold mb-4">
        <div class="flex justify-center items-center">
          <div class="mr-8">
            <img
              src="../assets/icons/food-box.png"
              alt="Box"
              class="h-10 md:h-32 w-10 md:w-32 cursor-pointer"
            />
          </div>
          <div>La <span class="text-yellow"> merenda</span> a</div>
        </div>
        <div class="flex justify-center items-center gap-2 md:gap-6">
          <div class="flex items-center gap-6">
            portata
            <img
              src="../assets/icons/desk.png"
              alt="Desk"
              class="h-10 md:h-32 w-10 md:w-32 cursor-pointer"
            />
            <span class="text-purple">di </span
            ><span class="text-pink">click</span>
          </div>
        </div>
      </div> -->
    </div>

    <template>
      <div class="xl:hidden max-w-screen-xl flex justify-center">
        <div class="mx-auto">
          <swiper
            :slidesPerView="5"
            :centeredSlides="true"
            :pagination="false"
            :navigation="false"
            :speed="500"
            class="h-[350px] max-w-screen-xl"
          >
            <swiper-slide
              v-for="(slide, index) in sellingPoints"
              :key="index"
              class="!h-60 !w-60 my-auto mx-5"
            >
              <div :class="slide.class" class="swiper-slide-content">
                <img
                  :src="slide.imgSrc"
                  :alt="slide.imgAlt"
                  :class="slide.imgClass"
                  class="swiper-slide-image"
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
            </swiper-slide>
          </swiper>
        </div>
      </div>
    </template>

    <div
      class="hidden xl:flex justify-center items-center py-16 px-4 gap-12 mx-auto overflow-hidden"
    >
      <div
        class="flex flex-col justify-center items-center bg-yellow h-64 w-64 rounded-xl p-4 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <img src="../assets/icons/health.png" alt="Health" class="h-12 w-12" />
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
          src="../assets/icons/sleeping-mask.png"
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
          src="../assets/icons/calendar.png"
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
        <img
          src="../assets/icons/credit-card.png"
          alt="Cash"
          class="h-12 w-12"
        />
        <div class="font-bold">Risparmio con gusto</div>
        <p class="text-sm">
          Prezzi più bassi rispetto al dettaglio e alle merende industriali.
        </p>
      </div>
      <div
        class="flex flex-col justify-center items-center bg-yellow h-64 w-64 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2"
      >
        <img src="../assets/icons/girl.png" alt="Safety" class="h-12 w-12" />
        <div class="font-bold">Al sicuro</div>
        <p class="text-sm">
          Tuo figlio non attraverserà più la strada né gestirà soldi per
          comprare la merenda.<br />Più sicurezza per lui, più serenità per te.
        </p>
      </div>
    </div>

    <div
      class="max-w-screen-xl mx-auto flex flex-col justify-center items-center py-6 md:py-16 mt-4 md:mt-0 px-4 gap-2 md:gap-12"
    >
      <div class="text-3xl md:text-6xl lg:text-8xl text-center font-bold mb-4">
        <div>
          La <span class="text-brown">merenda</span> che
          <span class="text-pink">cambia</span>,
        </div>
        <div class="flex justify-center items-center gap-2 md:gap-6">
          <div>come <span class="text-purple">tuo figlio</span></div>
          <img
            src="../assets/icons/boy.png"
            alt="Boy"
            class="h-10 md:h-20 w-10 md:w-20 cursor-pointer"
          />
        </div>

        <div class="flex justify-center items-center gap-2 md:gap-6">
          <img
            src="../assets/icons/calendar.png"
            alt="Calendar"
            class="h-10 md:h-20 w-10 md:w-20 cursor-pointer"
          />
          <div class="text-yellow">#snackscalendar</div>
        </div>
      </div>
      <div>
        <Calendar />
      </div>
    </div>
    <div class="pb-12">
      <div
        class="max-w-screen-xl mx-auto flex flex-col justify-center items-center py-10 md:py-16 mt-2 md:mt-0 mb-8 md:mb-0 px-4 gap-12"
      >
        <div
          class="text-3xl md:text-6xl lg:text-8xl text-center font-bold mb-2 md:mb-0"
        >
          <div class="flex justify-center items-center gap-2 md:gap-7">
            <img
              src="../assets/icons/trust.png"
              alt="Trust"
              class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
            />
            Migliori <span class="text-brown">store</span>
          </div>
          <div>
            <div class="flex justify-center items-center gap-2 md:gap-7">
              nella <span class="text-pink">tua zona</span>
              <img
                src="../assets/icons/location.png"
                alt="Location"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
              />
            </div>
          </div>
        </div>
      </div>
      <div>
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
                    address: store.address,
                    bio: store.bio,
                  },
                }"
              >
                <div
                  class="flex justify-center items-center h-60 w-60 bg-white rounded-xl transition-all duration-200 outline outline-5 outline-brown outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500"
                >
                  <img
                    :src="`${store.profile_picture}`"
                    alt="Profile Picture"
                    class="bg-center bg-contain bg-no-repeat h-52 w-52"
                  />
                </div>
              </nuxt-link>
              <div class="flex flex-col justify-center items-center mt-2">
                <div class="flex items-center justify-center gap-1.5">
                  <p class="font-bold">
                    {{ store.first_name }} {{ store.last_name }}
                  </p>
                  <div
                    class="h-4 w-4 bg-yellow rounded-full font-bold flex justify-center items-center"
                  >
                    √
                  </div>
                </div>
                <p class="text-xs opacity-80">{{ store.address }}</p>
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
                      address: slide.address,
                      bio: slide.bio,
                    },
                  }"
                >
                  <div
                    class="flex justify-center items-center h-56 w-56 bg-white rounded-xl transition-all duration-200 outline outline-5 outline-pink outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500"
                  >
                    <img
                      :src="`${slide.profile_picture}`"
                      alt="Profile Picture"
                      class="bg-center bg-contain bg-no-repeat h-52 w-52"
                    />
                  </div>
                </nuxt-link>
                <div class="flex flex-col justify-center items-center mt-2">
                  <div class="flex items-center justify-center gap-1.5">
                    <p class="font-bold">
                      {{ slide.first_name }} {{ slide.last_name }}
                    </p>
                    <!-- <img
                      src="../assets/icons/review.svg"
                      alt="star"
                      class="h-6 w-6"
                    /> -->
                    <div
                      class="h-4 w-4 bg-yellow rounded-full font-bold flex justify-center items-center"
                    >
                      √
                    </div>
                  </div>
                  <p class="text-xs opacity-80">{{ slide.address }}</p>
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
import { useRouter } from "vue-router";
import axios from "axios";
import { checkAuthStatus } from "../utils/auth";
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/swiper-bundle.css";

interface Store {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  location: string;
  address: string;
  profile_picture: string;
  bio: string;
}

const isAuthenticated = ref<boolean>(false);
const currentUserData = ref<Store | null>(null);

const stores = ref<Store[]>([]);

import healthIcon from "@/assets/icons/health.png";
import comfortIcon from "@/assets/icons/sleeping-mask.png";
import calendarIcon from "@/assets/icons/calendar.png";
import cashIcon from "@/assets/icons/credit-card.png";
import safetyIcon from "@/assets/icons/girl.png";

const sellingPoints = [
  {
    class:
      "flex flex-col justify-center items-center bg-yellow h-60 w-60 rounded-xl p-4 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
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
      "flex flex-col justify-center items-center bg-purple h-60 w-60 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-purple outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
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
      "flex flex-col justify-center items-center bg-yellow h-60 w-60 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
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
      "flex flex-col justify-center items-center bg-purple h-60 w-60 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-purple outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
    imgSrc: cashIcon,
    imgAlt: "Cash",
    imgClass: "h-12 w-12",
    title: "Risparmia con gusto",
    texts: [
      "Prezzi più bassi rispetto al dettaglio e alle merende industriali.",
    ],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-yellow h-60 w-60 rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-4 outline-yellow outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-2",
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

const router = useRouter();

const navigateToStore = (store: Store) => {
  router.push({
    name: "stores-username",
    params: { username: store.username },
    state: {
      id: store.id,
      first_name: store.first_name,
      last_name: store.last_name,
      profile_picture: store.profile_picture,
      location: store.location,
      address: store.address,
      bio: store.bio,
    },
  });
};

const groupedOrders = ref([]);

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