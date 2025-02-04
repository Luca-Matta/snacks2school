<template>
  <div>
    <div class="flex flex-wrap justify-center items-center gap-8 mt-4 md:mt-0">
      <div v-for="(dayData, dayName) in days" :key="dayName">
        <h3 class="text-sm font-bold text-center">
          {{ dayName }}
        </h3>
        <div class="text-center text-xs font-bold mb-3">
          {{ dayData.date }}
        </div>
        <div
          class="flex flex-col justify-center items-center text-center h-20 xl:h-40 w-20 xl:w-40 !rounded-xl outline outline-1 outline-[#af4135] outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 cursor-pointer"
          @click="
            isAuthenticated
              ? children?.length > 0
                ? dayData?.snacks?.length === 0 && dayData?.drinks?.length === 0
                  ? initializeOrder(dayName, dayData.date)
                  : editOrder(dayName, dayData.date)
                : openAddChild()
              : redirectToLogin()
          "
        >
          <div
            v-if="dayData.snacks.length === 0 && dayData.drinks.length === 0"
            class="text-xs"
          >
            <p class="font-bold">Nessuna merenda</p>
            <p class="text-[#af4135] font-bold">Ordina ora</p>
          </div>
          <div v-else class="flex flex-col justify-center items-center gap-2">
            <div
              v-if="dayData.snacks.length > 0"
              class="flex justify-center items-center"
            >
              <div v-for="snack in dayData.snacks" :key="snack.id">
                <img
                  :src="fixImageUrl(snack.image)"
                  :alt="snack.name"
                  class="h-5 md:h-7 w-5 md:w-7"
                />
              </div>
            </div>
            <div
              v-if="dayData.drinks.length > 0"
              class="flex justify-center items-center"
            >
              <div v-for="drink in dayData.drinks" :key="drink.id">
                <img
                  :src="fixImageUrl(drink.image)"
                  :alt="drink.name"
                  class="h-5 md:h-7 w-5 md:w-7"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      class="hidden md:block mx-auto text-center mt-12 font-bold text-sm opacity-60"
    >
      Il calendario della prossima settimana diventa disponibile dalla
      mezzanotte tra venerdì e sabato.
      <br />
      L'ordine può essere effettuato e modificato entro le 13:30 del giorno
      precedente alla data di consegna.
      <br />
      Ricorda di fare in anticipo l'ordine per lunedì!
    </div>
    <div
      class="block md:hidden mx-auto text-center mt-12 font-bold text-xs opacity-60"
    >
      Il calendario della prossima settimana diventa disponibile dalla
      mezzanotte tra venerdì e sabato. L'ordine può essere effettuato e
      modificato entro le 13:30 del giorno precedente alla data di consegna.
      Ricorda di fare in anticipo l'ordine per lunedì!
    </div>

    <AddChild :isAddChildVisible="isAddChildVisible" @close="close" />

    <InitializeOrder
      :isInitializeOrderVisible="isInitializeOrderVisible"
      :selectedDay="selectedDay"
      :selectedDate="selectedDate"
      @close="close"
      @openInitializeOrder="openInitializeOrder"
    />

    <EditOrder
      :isEditOrderVisible="isEditOrderVisible"
      :selectedDay="selectedDay"
      :selectedDate="selectedDate"
      @close="close"
      @openEditOrder="openEditOrder"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
import axios from "axios";
import {
  checkAuthStatus,
  getCurrentUserData,
  getChildrenForCurrentUser,
} from "../utils/auth";
import { useRouter } from "nuxt/app";

const router = useRouter();

const redirectToLogin = () => {
  router.push("/login");
};

const fixImageUrl = (url) => {
  if (!url) return ""; // Handle cases where image is missing
  if (url.startsWith("http")) return url; // If already absolute, return as is
  return `https://www.snacks2school.com${url}`; // Prepend base URL
};

const days = ref({
  LUNEDÌ: { date: "", snacks: [], drinks: [] },
  MARTEDÌ: { date: "", snacks: [], drinks: [] },
  MERCOLEDÌ: { date: "", snacks: [], drinks: [] },
  GIOVEDÌ: { date: "", snacks: [], drinks: [] },
  VENERDÌ: { date: "", snacks: [], drinks: [] },
  SABATO: { date: "", snacks: [], drinks: [] },
});

const isAuthenticated = ref<boolean>(false);
const currentUser = ref<any>(null);
const children = ref<any[]>([]);
const calendarData = ref<any>(null);
const selectedDay = ref<string>("");
const selectedDate = ref<string>("");
const isAddChildVisible = ref<boolean>(false);
const isInitializeOrderVisible = ref<boolean>(false);
const isEditOrderVisible = ref<boolean>(false);

const getCsrfToken = async () => {
  try {
    const response = await axios.get(
      "https://www.snacks2school.com/api/csrf-token/",
      {
        withCredentials: true,
      }
    );
    return response.data.csrfToken;
  } catch (error) {
    console.error("Error fetching CSRF token:", error);
    throw error;
  }
};

const fetchUserCalendar = async () => {
  try {
    const token = localStorage.getItem("authToken");

    if (!token) {
      console.error("No auth token found.");
      return;
    }

    const response = await axios.get(
      "https://www.snacks2school.com/api/calendar/week/",
      {
        headers: {
          Authorization: `Token ${token}`,
        },
        withCredentials: true,
      }
    );

    if (response.data && response.data.days) {
      calendarData.value = response.data.days;

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

const openAddChild = () => {
  isAddChildVisible.value = true;
};

const initializeOrder = (day: string, date: string) => {
  selectedDay.value = day;
  selectedDate.value = date;
  isInitializeOrderVisible.value = true;
};

const editOrder = (day: string, date: string) => {
  selectedDay.value = day;
  selectedDate.value = date;
  isEditOrderVisible.value = true;
};

const close = () => {
  isInitializeOrderVisible.value = false;
  isEditOrderVisible.value = false;
  isAddChildVisible.value = false;
  selectedDay.value = "";
  selectedDate.value = "";
};

const openInitializeOrder = (day: string) => {
  close();
};

const openEditOrder = (day: string) => {
  close();
};

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
  currentUser.value = await getCurrentUserData();
  children.value = await getChildrenForCurrentUser();
  fetchUserCalendar();
  watch(isInitializeOrderVisible, (newValue) => {
    if (newValue) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "auto";
    }
  });
  watch(isEditOrderVisible, (newValue) => {
    if (newValue) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "auto";
    }
  });
});
</script>