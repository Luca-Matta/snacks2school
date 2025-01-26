<template>
  <div>
    <Navbar />
    <div
      class="flex flex-col justify-center items-center max-w-screen-xl mx-auto py-16"
    >
      <div class="text-4xl md:text-6xl lg:text-8xl text-center font-bold mb-4">
        <div>Ecco le <span class="text-[#ffa500]">ricevute</span></div>
        <div class="flex justify-center items-center gap-2 md:gap-6">
          <div>
            dei <span class="text-[#a688f9]">tuoi </span>
            <span class="text-[#bf09bd]">ordini</span>
          </div>
          <img
            src="../../assets/icons/receipt.png"
            alt="Receipt"
            class="h-10 md:h-20 w-10 md:w-20 cursor-pointer"
          />
        </div>
      </div>
      <div class="flex justify-center flex-wrap gap-8 py-16 px-6">
        <div v-for="receipt in receipts" :key="receipt.id">
          <div
            class="bg-white shadow-card !rounded-2xl p-8 outline outline-1 outline-[#af4135] outline-offset-4 shadow-card hover:shadow-none transition-all duration-500 h-full w-full md:w-[480px]"
          >
            <div class="flex flex-col justify-center items-center">
              <div class="font-bold">
                {{ receipt.seller.first_name }}
                {{ receipt.seller.last_name }}
              </div>
              <div class="text-xs">
                {{ receipt.seller.address }}
              </div>
            </div>
            <div class="text-sm mt-2">
              <div class="flex gap-1">
                <div class="font-bold">Data dell'ordine:</div>
                <div>
                  {{ receipt.order_date }}
                </div>
              </div>
              <div class="flex gap-1">
                <div class="font-bold">Data della consegna:</div>
                <div>
                  {{ receipt.delivery_date }}
                </div>
              </div>
              <div class="flex gap-1">
                <div class="font-bold">Acquirente:</div>
                <div>
                  {{ receipt.customer.first_name }}
                  {{ receipt.customer.last_name }}
                </div>
              </div>
              <div v-if="receipt.snack" class="flex gap-2">
                <div class="font-bold">Snack:</div>
                <div class="flex">
                  {{ receipt.snack.name }} | {{ receipt.snack.gross_price }}€
                </div>
              </div>
              <div v-if="receipt.drink" class="flex gap-2">
                <div class="font-bold">Bevanda:</div>
                <div class="flex">
                  {{ receipt.drink.name }} | {{ receipt.drink.gross_price }}€
                </div>
              </div>
              <div class="flex gap-1">
                <div class="font-bold">Totale ordine:</div>
                <div>{{ receipt.total_price }}€</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";

const getImageUrl = (path) => {
  const baseUrl = "http://localhost:8000";
  return `${baseUrl}${path}`;
};

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const receipts = ref<any>(null);

const fetchReceipts = async () => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await axios.get("http://localhost:8000/api/receipts", {
      headers: {
        "X-CSRFToken": csrfToken,
      },
      withCredentials: true,
    });

    if (response.data) {
      receipts.value = response.data;
    }
  } catch (error) {
    console.error("Error fetching receipts:", error);
  }
};

onMounted(async () => {
  fetchReceipts();
});
</script>