<template>
  <div>
    <Navbar />
    <div class="py-12">
      <div
        class="flex flex-col justify-center max-w-screen-xl mx-auto py-16 gap-16"
      >
        <div
          v-for="(schools, deliveryDate) in groupedOrders"
          :key="deliveryDate"
          class="flex flex-col justify-center items-center gap-6"
        >
          <h2 class="font-bold text-center text-xl">
            Ordini da consegnare il {{ deliveryDate }}
          </h2>
          <div
            class="flex justify-center flex-wrap max-w-screen-xl mx-auto gap-12"
          >
            <div
              v-for="(classes, school) in schools"
              :key="school"
              class="bg-white shadow-card rounded-2xl p-8 outline outline-4 outline-yellow outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 max-w-[350px] md:max-w-96"
            >
              <h3 class="font-bold text-center">{{ school }}</h3>
              <div
                v-for="(items, className) in classes"
                :key="className"
                class="mt-6"
              >
                <h4 class="font-bold text-center">{{ className }}</h4>
                <div class="flex flex-col gap-2">
                  <div>
                    <h5 class="font-bold text-sm">Snacks:</h5>
                    <ul>
                      <li
                        v-for="(count, snack) in items.snacks"
                        :key="snack"
                        class="text-xs ml-6"
                      >
                        {{ count }} {{ snack }}
                      </li>
                    </ul>
                  </div>
                  <div>
                    <h5 class="font-bold text-sm">Drinks:</h5>
                    <ul>
                      <li
                        v-for="(count, drink) in items.drinks"
                        :key="drink"
                        class="text-xs ml-6"
                      >
                        {{ count }} {{ drink }}
                      </li>
                    </ul>
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
    console.log("Grouped orders fetched:", groupedOrders.value);
  } catch (error) {
    console.error("Error fetching grouped orders:", error);
  }
};

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
  fetchGroupedOrders();
});
</script>