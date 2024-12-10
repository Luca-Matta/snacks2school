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
        <div
          class="flex flex-col justify-center items-center max-w-screen-xl mx-auto"
        >
          <!-- <div class="w-full h-auto px-4" autoplay muted>
            <img
              src="../../static/store-menu.png"
              alt="Menu"
              class="bg-center bg-contain bg-no-repeat"
            />
          </div> -->
          <h1 class="font-bold text-5xl mb-2">
            Catalogo / <span class="text-brown">Merende</span>
          </h1>
        </div>
        <div class="flex flex-wrap justify-center items-center gap-12 py-6">
          <div v-for="snack in singleStoreSnacks" :key="snack">
            <div
              class="flex flex-col justify-center items-center gap-2 bg-white shadow-card hover:shadow-none transition-all duration-500 rounded-xl h-64 w-60 p-6 cursor-pointer outline outline-2 outline-brown outline-offset-4"
            >
              <div class="flex justify-center items-center">
                <img
                  :src="snack.image"
                  alt="snack"
                  class="bg-center bg-contain bg-no-repeat h-20 w-20"
                />
              </div>
              <div class="flex flex-col justify-center items-center">
                <div class="flex flex-col items-center justify-center">
                  <p class="font-bold text-center text-sm mt-2">
                    {{ snack.name }}
                  </p>
                  <div class="flex gap-1">
                    <div
                      v-for="(ingredient, index) in snack.ingredients"
                      :key="index"
                      class="py-2"
                    >
                      <img
                        :src="ingredient.image"
                        :alt="ingredient.name"
                        :title="ingredient.name"
                        class="bg-center bg-contain bg-no-repeat h-6 w-6"
                      />
                    </div>
                  </div>
                  <p>Allergeni</p>
                  <p class="text-sm">{{ snack.gross_price }}€</p>
                </div>
                <p class="text-xs opacity-80"></p>
              </div>
            </div>
          </div>
        </div>

        <h1 class="font-bold text-5xl mt-12 mb-2">
          Catalogo / <span class="text-brown">Bevande</span>
        </h1>
        <div class="flex flex-wrap justify-center items-center gap-12 py-6">
          <div v-for="drink in singleStoreDrinks" :key="drink">
            <div
              class="flex flex-col justify-center items-center gap-2 bg-white shadow-card hover:shadow-none transition-all duration-500 rounded-xl h-64 w-60 p-6 cursor-pointer outline outline-2 outline-brown outline-offset-4"
            >
              <div class="flex justify-center items-center">
                <img
                  :src="drink.image"
                  alt="snack"
                  class="bg-center bg-contain bg-no-repeat h-20 w-20"
                />
              </div>
              <div class="flex flex-col justify-center items-center">
                <div class="flex flex-col items-center justify-center">
                  <p class="font-bold text-center text-sm mt-2">
                    {{ drink.name }}
                  </p>
                  <!-- <div class="flex gap-1">
                    <div
                      v-for="(ingredient, index) in snack.ingredients"
                      :key="index"
                      class="py-2"
                    >
                      <img
                        :src="ingredient.image"
                        :alt="ingredient.name"
                        :title="ingredient.name"
                        class="bg-center bg-contain bg-no-repeat h-6 w-6"
                      />
                    </div>
                  </div> -->
                  <p class="text-sm">{{ drink.gross_price }}€</p>
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
import { useRoute, useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const state = router.options.history.state;
const { first_name, last_name, profile_picture, location, bio } = route.query;
const username = route.params.username;

const formattedBio = bio ? bio.replace(/\n/g, "<br>") : "";

interface Store {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  location: string;
  // profile_picture: string;
  bio: string;
}

interface Ingredient {
  name: string;
  image: string;
}

interface Snack {
  id: number;
  name: string;
  date: string;
  price: number;
  image: string;
  ingredients: Ingredient[];
  seller: Store;
}

interface Drink {
  id: number;
  name: string;
  date: string;
  price: number;
  image: string;
  ingredients: Ingredient[];
  seller: Store;
}

const singleStoreSnacks = ref<Snack[]>([]);
const singleStoreDrinks = ref<Drink[]>([]);

const fetchSingleStoreSnacks = async (username: string) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/snacks/?username=${username}`
    );
    singleStoreSnacks.value = response.data;
    console.log("Snacks fetched:", singleStoreSnacks.value);
  } catch (error) {
    console.error("Error fetching snack data:", error);
  }
};

const fetchSingleStoreDrinks = async (username: string) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/drinks/?username=${username}`
    );
    singleStoreDrinks.value = response.data;
    console.log("Snacks fetched:", singleStoreDrinks.value);
  } catch (error) {
    console.error("Error fetching snack data:", error);
  }
};

onMounted(async () => {
  if (username) {
    fetchSingleStoreSnacks(username);
    fetchSingleStoreDrinks(username);
  } else {
    console.error("Username is not available");
  }
});
</script>