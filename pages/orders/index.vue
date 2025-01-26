<template>
  <div>
    <Navbar />
    <div
      class="max-w-screen-xl mx-auto flex flex-col justify-center items-center !py-16 !px-4 gap-12"
    >
      <div class="text-4xl md:text-6xl lg:text-8xl text-center font-bold mb-4">
        <div>
          <span class="text-[#af4135]">Benvenuto</span> nel tuo
          <span class="text-[#a688f9]">gestionale!</span>
        </div>
        <div class="flex justify-center items-center gap-2 md:gap-6">
          <div>
            Visualizza <span class="text-[#bf09bd]">i tuoi ordini</span>
          </div>
          <img
            src="../../assets/icons/orders.png"
            alt="Orders"
            class="h-10 md:h-20 w-10 md:w-20 cursor-pointer"
          />
        </div>
      </div>
    </div>
    <div>
      <div
        class="flex flex-col justify-center max-w-screen-xl mx-auto mb-16 gap-16"
      >
        <div
          v-for="(schools, deliveryDate) in groupedOrders"
          :key="deliveryDate"
          class="flex flex-col justify-center items-center gap-6"
        >
          <div class="flex-col justify-center items-center">
            <div class="flex justify-center items-center gap-2 md:gap-4">
              <img
                src="../../assets/icons/list.png"
                alt="List"
                class="h-6 md:h-10 w-6 md:w-10 cursor-pointer"
              />
              <h2 class="font-bold text-center text-2xl">
                In consegna il {{ deliveryDate }}
              </h2>
            </div>
            <div class="text-center text-xs font-bold max-w-80 mx-auto mt-2">
              Ricorda di inserire nel box la lista con i nomi degli alunni e gli
              snack e le bevande associati.
            </div>
            <div
              class="flex justify-center items-center text-center text-xs font-bold max-w-80 mx-auto -mt-1"
            >
              <div>
                <span class="underline">Te la provvediamo noi!</span> Clicca qui
              </div>
              <span class="text-2xl ml-1">🫶🏽</span>
            </div>
          </div>
          <div
            class="flex justify-center flex-wrap max-w-screen-xl mx-auto gap-12"
          >
            <div
              v-for="(classes, school) in schools"
              :key="school"
              class="bg-white shadow-card !rounded-2xl p-8 outline outline-1 outline-[#af4135] outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 max-w-[350px] md:max-w-96"
            >
              <h3 class="font-bold text-center">{{ school }}</h3>
              <div
                v-for="(items, className) in classes"
                :key="className"
                class="mt-5"
              >
                <h4 class="font-bold text-center">
                  {{ className }}
                </h4>
                <div class="flex flex-col gap-2">
                  <div
                    v-if="
                      Object.keys(items.snack_break.snacks).length > 0 ||
                      Object.keys(items.snack_break.drinks).length > 0
                    "
                  >
                    <h5 class="font-bold text-center text-sm">Merenda</h5>
                    <div
                      v-if="Object.keys(items.snack_break.snacks).length > 0"
                    >
                      <h5 class="font-bold text-sm">Snacks:</h5>
                      <ul>
                        <li
                          v-for="(count, snack) in items.snack_break.snacks"
                          :key="snack"
                          class="text-xs ml-6"
                        >
                          {{ count }} {{ snack }}
                        </li>
                      </ul>
                    </div>
                    <div
                      v-if="Object.keys(items.snack_break.drinks).length > 0"
                    >
                      <h5 class="font-bold text-sm">Drinks:</h5>
                      <ul>
                        <li
                          v-for="(count, drink) in items.snack_break.drinks"
                          :key="drink"
                          class="text-xs ml-6"
                        >
                          {{ count }} {{ drink }}
                        </li>
                      </ul>
                    </div>
                  </div>
                  <div
                    v-if="
                      Object.keys(items.lunch_break.snacks).length > 0 ||
                      Object.keys(items.lunch_break.drinks).length > 0
                    "
                  >
                    <h5 class="font-bold text-center text-sm">Pranzo</h5>
                    <div
                      v-if="Object.keys(items.lunch_break.snacks).length > 0"
                    >
                      <h5 class="font-bold text-sm">Snacks:</h5>
                      <ul>
                        <li
                          v-for="(count, snack) in items.lunch_break.snacks"
                          :key="snack"
                          class="text-xs ml-6"
                        >
                          {{ count }} {{ snack }}
                        </li>
                      </ul>
                    </div>
                    <div
                      v-if="Object.keys(items.lunch_break.drinks).length > 0"
                    >
                      <h5 class="font-bold text-sm">Drinks:</h5>
                      <ul>
                        <li
                          v-for="(count, drink) in items.lunch_break.drinks"
                          :key="drink"
                          class="text-xs ml-6"
                        >
                          {{ count }} {{ drink }}
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="flex flex-col text-xs font-bold mt-4 gap-2">
                  <div
                    class="flex items-center"
                    @click="
                      toggleOrderPrepared(deliveryDate, school, className)
                    "
                  >
                    <img
                      v-if="items.prepared"
                      src="../../assets/icons/checked.png"
                      alt="Checked"
                      class="h-4 w-4 cursor-pointer"
                    />
                    <img
                      v-else
                      src="../../assets/icons/unchecked.png"
                      alt="Unchecked"
                      class="h-4 w-4 cursor-pointer"
                    />
                    <div class="ml-2 cursor-pointer">
                      {{ items.prepared ? "Preparato" : "Non preparato" }}
                    </div>
                  </div>
                  <div
                    class="flex items-center"
                    @click="
                      toggleOrderDelivered(deliveryDate, school, className)
                    "
                  >
                    <img
                      v-if="items.delivered"
                      src="../../assets/icons/checked.png"
                      alt="Checked"
                      class="h-4 w-4 cursor-pointer"
                    />
                    <img
                      v-else
                      src="../../assets/icons/unchecked.png"
                      alt="Unchecked"
                      class="h-4 w-4 cursor-pointer"
                    />
                    <div class="ml-2 cursor-pointer">
                      {{ items.delivered ? "Consegnato" : "Non consegnato" }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
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

const isAuthenticated = ref<boolean>(false);
const currentUserData = ref<Store | null>(null);

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const groupedOrders = ref([]);

const fetchGroupedOrders = async () => {
  try {
    const csrfResponse = await axiosInstance.get("csrf-token/");
    const csrfToken = csrfResponse.data.csrfToken;

    const response = await axiosInstance.get(
      "http://localhost:8000/api/grouped-orders/",
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );

    groupedOrders.value = response.data;
  } catch (error) {
    console.error("Error fetching grouped orders:", error);
  }
};

const toggleOrderPrepared = async (
  deliveryDate: string,
  schoolName: string,
  className: string
) => {
  try {
    const csrfResponse = await axiosInstance.get("csrf-token/");
    const csrfToken = csrfResponse.data.csrfToken;

    const response = await axiosInstance.post(
      "http://localhost:8000/api/toggle-order-prepared-status/",
      {
        delivery_date: deliveryDate,
        school_name: schoolName,
        class_name: className,
      },
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );
  } catch (error) {
    console.error("Error toggling order prepared status:", error);
  } finally {
    window.location.reload();
  }
};

const toggleOrderDelivered = async (
  deliveryDate: string,
  schoolName: string,
  className: string
) => {
  try {
    const csrfResponse = await axiosInstance.get("csrf-token/");
    const csrfToken = csrfResponse.data.csrfToken;

    const response = await axiosInstance.post(
      "http://localhost:8000/api/toggle-order-delivered-status/",
      {
        delivery_date: deliveryDate,
        school_name: schoolName,
        class_name: className,
      },
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );
  } catch (error) {
    console.error("Error toggling order delivered status:", error);
  } finally {
    window.location.reload();
  }
};

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
  fetchGroupedOrders();
});
</script>