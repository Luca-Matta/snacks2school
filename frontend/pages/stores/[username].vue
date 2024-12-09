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
        <div class="max-w-screen-xl mx-auto">
          <div class="w-full h-auto px-4" autoplay muted>
            <img
              src="../../static/store-menu.png"
              alt="Menu"
              class="bg-center bg-contain bg-no-repeat"
            />
          </div>
        </div>
        <div class="flex flex-wrap justify-center items-center gap-8 py-6">
          <div v-for="snack in singleStoreSnacks" :key="snack">
            <div class="flex flex-col justify-center items-center gap-2">
              <div
                class="flex justify-center items-center h-60 w-60 bg-white rounded-xl transition-all duration-200 outline outline-4 outline-brown outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500"
              >
                <img
                  :src="``"
                  alt="Profile Picture"
                  class="bg-center bg-contain bg-no-repeat h-52 w-52"
                />
              </div>
              <div class="flex flex-col justify-center items-center">
                <div class="flex flex-col items-center justify-center">
                  <p class="font-bold max-w-60 text-center text-sm mt-2">
                    {{ snack.name }}
                  </p>
                  <p>Allergeni</p>
                  <p class="text-sm">{{ snack.price }}€</p>
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
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";

const route = useRoute();
const { first_name, last_name, profile_picture, location, bio } = route.query;
const username = route.params.username;

const formattedBio = bio ? bio.replace(/\n/g, "<br>") : "";

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
  price: number;
  seller: Store;
}

const singleStoreSnacks = ref<Snack[]>([]);

const fetchStoreId = async (username: string) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/stores/?username=${username}`
    );
    if (response.data.length > 0) {
      return response.data[0].id;
    } else {
      console.error("Store not found for username:", username);
      return null;
    }
  } catch (error) {
    console.error("Error fetching store ID:", error);
    return null;
  }
};

const fetchSingleStoreSnacks = async (storeId: number) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/snacks/?store_id=${storeId}`
    );
    singleStoreSnacks.value = response.data;
    console.log("Snacks fetched:", singleStoreSnacks.value);
  } catch (error) {
    console.error("Error fetching snack data:", error);
  }
};

onMounted(async () => {
  if (username) {
    const storeId = await fetchStoreId(username);
    if (storeId) {
      fetchSingleStoreSnacks(storeId);
    }
  } else {
    console.error("Username is not available");
  }
});
</script>