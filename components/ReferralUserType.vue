<template>
  <div
    v-if="isReferralUserTypeVisible"
    class="fixed inset-0 flex justify-center items-center z-30 !px-4 md:px-0"
    style="backdrop-filter: blur(50px)"
  >
    <div
      class="bg-white p-8 !rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-full max-w-96 max-h-[500px] overflow-y-auto"
    >
      <h2 class="text-xl text-center font-bold mb-2">
        Hai copiato il link
        <span class="underline">da inviare ai {{ userType }}</span>
      </h2>
      <div class="text-center text-sm mb-4">
        Non ti resta che inviarlo a tutti i {{ userType }} che vuoi. <br />
        Per ognuno di essi, non appena si sarà registrato e avrà ricaricato il
        proprio portafoglio di credito, riceverai 1€ di credito da spendere su
        Snacks2School!
      </div>
      <div class="flex justify-center gap-2">
        <router-link to="/" class="w-full">
          <button
            class="btn bg-black text-white w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
          >
            Torna alla Home
          </button>
        </router-link>
        <button
          class="btn bg-[#ffa500] w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
          @click="shareLink"
        >
          Condividi
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, onMounted, computed } from "vue";
import { checkAuthStatus } from "../utils/auth";

const props = defineProps<{
  isReferralUserTypeVisible: boolean;
  userType: "customer" | "school_staff";
  selectedLink: string;
}>();

const userType = computed(() => {
  return props.userType === "customer"
    ? "genitori"
    : "membri del personale scolastico";
});

const isAuthenticated = ref<boolean>(false);

const emit = defineEmits(["close"]);

const shareLink = () => {
  const shareData = {
    title: "Snacks2School | La merenda a portata di clic",
    text: "Scopri Snacks2School, l'app che ti permette di ordinare la merenda comodamente dal tuo divano e riceverla a scuola! La qualità dei prodotti è elevatissima, ma i prezzi sono più bassi rispetto al dettaglio e alle merende industriali.",
    url: props.selectedLink,
  };

  if (navigator.share) {
    navigator
      .share(shareData)
      .then(() => console.log("Successful share"))
      .catch((error) => console.log("Error sharing", error));
  } else {
    alert("Web Share API is not supported in your browser.");
  }
};

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
});
</script>