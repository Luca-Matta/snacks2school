<template>
  <div
    v-if="isReferralExplenationVisible"
    class="fixed inset-0 flex justify-center items-center z-30 px-4 md:px-0"
    style="backdrop-filter: blur(50px)"
  >
    <div
      class="bg-white p-8 !rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-full max-w-96 max-h-[500px] overflow-y-auto"
    >
      <h2 class="text-xl text-center font-bold mb-2">
        Ricevere credito su Snacks2School
      </h2>
      <div class="text-center text-sm mb-4">
        Se porti un amico su Snacks2School, riceverai un credito di 1€ non
        appena lui ricaricherà il proprio portafoglio di credito. Il numero di
        amici che puoi portare è illimitato! In questo modo potrai ricevere un
        credito significativo per fare i tuoi acquisti!
      </div>
      <div class="text-center text-sm font-bold">Come fare:</div>
      <div class="text-center text-sm">• Vai sul tuo profilo</div>
      <div class="text-center text-sm">
        • Clicca sul relativo pulsante nella sezione "Condividi Snacks2School"
      </div>
      <div class="text-center text-sm">• Invia il link a chi vuoi</div>
      <div class="flex justify-center gap-2">
        <!-- <button
          @click="$emit('close')"
          class="btn bg-black w-full font-bold text-white uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
        >
          Chiudi
        </button> -->
        <router-link :to="isAuthenticated ? '/profile' : '/login'">
          <button
            class="btn bg-[#bf09bd] w-full text-white font-bold uppercase text-xs shadow-button my-4 mb-4 !py-3 !px-6 !rounded-lg outline outline-1 outline-[#bf09bd] outline-offset-4 shadow-btn hover:shadow-none transition-all duration-500 mt-6"
          >
            Profilo
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, onMounted } from "vue";
import { checkAuthStatus } from "../utils/auth";

const props = defineProps<{
  isReferralExplenationVisible: boolean;
}>();

const isAuthenticated = ref<boolean>(false);

const emit = defineEmits(["close"]);

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
});
</script>