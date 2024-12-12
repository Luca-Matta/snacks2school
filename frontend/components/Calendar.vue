<template>
  <div>
    <div class="hidden md:flex flex-wrap justify-center items-center gap-8">
      <div v-for="(dayData, dayName) in days" :key="dayName">
        <h3 class="text-xl font-bold mb-3 text-center">{{ dayName }}</h3>
        <div
          class="flex flex-col justify-center items-center text-center h-40 w-40 rounded-xl outline outline-4 outline-brown outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 cursor-pointer"
          @click="open(dayName, dayData.date)"
        >
          <div
            v-if="dayData.snacks.length === 0 && dayData.drinks.length === 0"
          >
            <p class="font-bold">Nessuna merenda</p>
            <p class="text-brown font-bold">Ordina ora</p>
          </div>
          <div v-else class="flex flex-col justify-center items-center gap-2">
            <div
              v-if="dayData.snacks.length > 0"
              class="flex justify-center items-center"
            >
              <div v-for="snack in dayData.snacks" :key="snack.id">
                <img
                  :src="getImageUrl(snack.image)"
                  :alt="snack.name"
                  class="h-7 w-7"
                />
              </div>
            </div>
            <div
              v-if="dayData.drinks.length > 0"
              class="flex justify-center items-center"
            >
              <div v-for="drink in dayData.drinks" :key="drink.id">
                <img
                  :src="getImageUrl(drink.image)"
                  :alt="drink.name"
                  class="h-7 w-7"
                />
              </div>
            </div>
            <div class="text-xs mt-1">Vuoi cambiare qualcosa?</div>
          </div>
        </div>
      </div>
    </div>

    <PlaceOrder
      :isVisible="isVisible"
      :selectedDay="selectedDay"
      :selectedDate="selectedDate"
      @close="close"
      @placeOrder="handleOrder"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

const days = ref({
  LUNEDÌ: { date: "", snacks: [], drinks: [] },
  MARTEDÌ: { date: "", snacks: [], drinks: [] },
  MERCOLEDÌ: { date: "", snacks: [], drinks: [] },
  GIOVEDÌ: { date: "", snacks: [], drinks: [] },
  VENERDÌ: { date: "", snacks: [], drinks: [] },
  SABATO: { date: "", snacks: [], drinks: [] },
});

const currentUser = ref<any>(null);
const calendarData = ref<any>(null);
const selectedDay = ref<string>("");
const selectedDate = ref<string>("");
const isVisible = ref<boolean>(false);

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

    console.log("API response:", response);
    console.log("API response data:", response.data);

    if (response.data && response.data.days) {
      calendarData.value = response.data.days;
      console.log("Fetched calendar data:", calendarData.value);

      for (const day of calendarData.value) {
        const date = new Date(day.date);
        const dayName = date
          .toLocaleDateString("it-IT", { weekday: "long" })
          .toUpperCase();

        days.value[dayName] = {
          date: day.date,
          snacks: day.snacks,
          drinks: day.drinks,
        };
      }
    } else {
      console.error("No calendar data found in the response.");
    }
  } catch (error) {
    console.error("Error fetching user calendar:", error);
  }
};

const getImageUrl = (path) => {
  const baseUrl = "http://localhost:8000";
  return `${baseUrl}${path}`;
};

const open = (day: string, date: string) => {
  selectedDay.value = day;
  selectedDate.value = date;
  isVisible.value = true;
};

const close = () => {
  isVisible.value = false;
  selectedDay.value = "";
  selectedDate.value = "";
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