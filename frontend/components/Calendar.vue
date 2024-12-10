<template>
  <div>
    <div class="hidden md:flex flex-wrap justify-center items-center gap-8">
      <div
        v-for="(content, day) in days"
        :key="day"
        class="flex flex-col justify-center items-center gap-3"
      >
        <div class="text-xl font-bold">{{ day }}</div>
        <div
          class="flex flex-col justify-center items-center text-center h-40 w-40 rounded-xl outline outline-4 outline-brown outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 cursor-pointer"
          :class="content ? 'bg-brown' : 'bg-gray-100'"
          @click="open(day)"
        >
          <div v-if="content" class="svg-icon">
            <img :src="hamburgerIcon" alt="Hamburger Icon" class="h-16 w-16" />
          </div>
          <div v-else class="font-bold">Nessuna merenda</div>
          <div v-if="!content" class="text-brown font-bold">Ordina ora</div>
        </div>
      </div>
    </div>

    <div class="md:hidden -mt-8">
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
    </div>

    <!-- PlaceOrder Modal -->
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
  LUNEDÌ: null,
  MARTEDÌ: null,
  MERCOLEDÌ: null,
  GIOVEDÌ: null,
  VENERDÌ: null,
  SABATO: null,
});

const currentUser = ref<any>(null);
const calendarSlides = ref([]);
const isVisible = ref(false);
const selectedDay = ref("");

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const fetchUserCalendar = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/api/user/calendar/"
    );
    const calendarData = response.data.snacks_for_week;
    console.log("Fetched calendar data:", calendarData);
    for (const [date, snacks] of Object.entries(calendarData)) {
      const dayName = new Date(date)
        .toLocaleDateString("it-IT", { weekday: "long" })
        .toUpperCase();
      days.value[dayName] = snacks.length > 0 ? "hamburger" : null;
    }
    console.log("Processed days object:", days.value);
    updateCalendarSlides();
  } catch (error) {
    console.error("Error fetching user calendar:", error);
  }
};

const updateCalendarSlides = () => {
  calendarSlides.value = Object.entries(days.value).map(([day, content]) => ({
    class:
      "flex flex-col justify-center items-center text-center h-56 w-56 rounded-xl outline outline-4 outline-brown outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 cursor-pointer " +
      (content ? "bg-brown" : "bg-gray-100"),
    imgSrc: content ? hamburgerIcon : "",
    imgAlt: content ? "Hamburger Icon" : "",
    imgClass: "h-16 w-16",
    title: day,
    texts: content ? [] : ["Nessuna merenda", "Ordina ora"],
  }));
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
