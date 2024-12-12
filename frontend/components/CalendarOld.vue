<template>
  <div>
    <div>{{ calendarData }}</div>
    <div class="hidden md:flex flex-wrap justify-center items-center gap-8">
      <div
        v-for="(content, day) in days"
        :key="day"
        class="flex flex-col justify-center items-center gap-3"
      >
        <div class="text-xl font-bold">{{ day }}</div>
        <div
          class="flex flex-col justify-center items-center text-center h-40 w-40 rounded-xl outline outline-4 outline-brown outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 cursor-pointer"
          :class="content.snacks || content.drinks ? 'bg-brown' : 'bg-gray-100'"
          @click="open(day)"
        >
          <div v-if="content.snacks" class="svg-icon">
            <img
              :src="content.snacks.image"
              :alt="content.snacks.name"
              class="h-16 w-16"
            />
          </div>
          <div v-if="content.drinks" class="svg-icon">
            <img
              :src="content.drinks.image"
              :alt="content.drinks.name"
              class="h-16 w-16"
            />
          </div>
          <div v-else class="font-bold">Nessuna merenda</div>
          <div
            v-if="!content.snacks && !content.drinks"
            class="text-brown font-bold"
          >
            Ordina ora
          </div>
        </div>
      </div>
    </div>

    <!-- <div class="md:hidden -mt-8">
      <Slider :slides="calendarSlides">
        <template #default="{ slide }">
          <div class="flex flex-col justify-center items-center gap-3">
            <div class="text-xl font-bold">{{ slide.title }}</div>
            <div :class="slide.class" @click="open(slide.title)">
              <div v-if="slide.imgSrc" class="svg-icon">
                <img
                  :src="slide.imgSrc"
                  :alt="slide.imgAlt"
                  :class="slide.imgClass"
                />
              </div>
              <div v-else class="font-bold">{{ slide.texts[0] }}</div>
              <div v-if="!slide.imgSrc" class="text-brown font-bold">
                {{ slide.texts[1] }}
              </div>
            </div>
          </div>
        </template>
      </Slider>
    </div> -->

    <PlaceOrder
      :isVisible="isVisible"
      :selectedDay="selectedDay"
      @close="close"
      @placeOrder="handleOrder"
    />
  </div>
</template>


<script setup lang="ts">
import { ref, onMounted } from "vue";
import Slider from "@/components/Slider.vue";
import PlaceOrder from "@/components/PlaceOrder.vue";
import { checkAuthStatus, getCurrentUserData } from "../utils/auth";
import axios from "axios";

const days = ref({
  LUNEDÌ: { snacks: null, drinks: null },
  MARTEDÌ: { snacks: null, drinks: null },
  MERCOLEDÌ: { snacks: null, drinks: null },
  GIOVEDÌ: { snacks: null, drinks: null },
  VENERDÌ: { snacks: null, drinks: null },
  SABATO: { snacks: null, drinks: null },
});

const currentUser = ref<any>(null);
const calendarData = ref<any>(null);
const isVisible = ref(false);
const selectedDay = ref("");

const getCsrfToken = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/csrf-token/", {
      withCredentials: true,
    });
    return response.data.csrfToken;
  } catch (error) {
    console.error("Error fetching CSRF token:", error);
    throw error;
  }
};

const fetchUserCalendar = async () => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await axios.get(
      "http://localhost:8000/api/calendar/week/",
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );

    if (response.data && response.data.week_days) {
      calendarData.value = response.data.week_days;
      console.log("Calendar data:", calendarData.value);

      for (const day of calendarData.value) {
        const dayName = new Date(day.date)
          .toLocaleDateString("it-IT", { weekday: "long" })
          .toUpperCase();

        days.value[dayName] = {
          snacks: day.snacks.length > 0 ? day.snacks[0] : null,
          drinks: day.drinks.length > 0 ? day.drinks[0] : null,
        };
      }
    } else {
      console.error("No calendar data found in the response.");
    }
  } catch (error) {
    console.error("Error fetching user calendar:", error);
  }
};

const open = (day: string) => {
  selectedDay.value = day;
  isVisible.value = true;
};

const close = () => {
  isVisible.value = false;
  selectedDay.value = "";
};

const handleOrder = (day: string) => {
  console.log(`Placing order for ${day}`);
  close();
};

onMounted(async () => {
  currentUser.value = await getCurrentUserData();
  fetchUserCalendar();
});
</script>