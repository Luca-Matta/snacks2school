<template>
  <div>
    <Navbar />
    <div class="px-4">
      <div
        class="flex flex-col justify-center items-center max-w-screen-xl mx-auto py-16 gap-6"
      >
        <div class="flex justify-center items-center gap-2 md:gap-7">
          <img
            src="../assets/icons/account.png"
            alt="Account"
            class="h-16 md:h-32 w-16 md:w-32 cursor-pointer"
          />
        </div>
        <div class="text-2xl md:text-6xl text-center font-bold">
          <div>
            Ehi {{ currentUser?.first_name }}, benvenuto nel
            <span class="text-[#a688f9]">tuo </span>
            <span class="text-[#bf09bd]">profilo!</span>
          </div>
        </div>
        <div class="flex flex-wrap gap-8">
          <div
            v-for="child in children"
            :key="child.id"
            class="flex flex-col justify-center items-center mx-auto px-4 gap-1 bg-white shadow-card !rounded-xl outline outline-[#bf09bd] outline-offset-4 outline-1 hover:shadow-none transition-all duration-500 max-w-[500px] p-6 mt-6"
          >
            <div class="text-xl font-bold">
              {{ child.first_name }} {{ child.last_name }}
            </div>
            <div v-if="child.associated_schools.length > 1" class="font-bold">
              Scuole
            </div>
            <div v-if="child.associated_schools.length <= 1" class="font-bold">
              Scuola
            </div>

            <div
              v-for="school in child.associated_schools"
              :key="school.id"
              class="text-center text-sm"
            >
              {{ school.name }}
            </div>

            <div
              v-if="child.school_class.name != 'Personale scolastico'"
              class="text-lg font-bold"
            >
              Classe
            </div>
            <div class="text-center text-sm">
              {{ child.school_class.name }}
            </div>

            <div class="flex justify-center items-center">
              <button
                @click="openEditChildProfile"
                class="bg-[#bf09bd] w-full text-white font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
              >
                Modifica
              </button>
            </div>
          </div>
        </div>
        <div
          class="max-w-screen-xl mx-auto flex flex-col justify-center items-center px-4"
        >
          <button
            @click="openAddChild"
            class="bg-[#bf09bd] w-full text-white font-bold uppercase text-xs shadow-button my-4 mb-2 py-3 px-20 !rounded-lg outline outline-1 outline-[#bf09bd] outline-offset-4 shadow-card hover:shadow-none transition-all duration-500"
          >
            Aggiungi un figlio
          </button>
        </div>
        <div
          class="max-w-screen-xl mx-auto flex flex-col justify-center items-center py-10 md:py-16 px-4"
        >
          <div class="text-2xl md:text-6xl text-center font-bold mb-2">
            <div
              class="flex flex-col justify-center items-center gap-2 md:gap-7"
            >
              <img
                src="../assets/icons/referrer.png"
                alt="Trust"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
              />
              <div>Condividi Snacks2School con</div>
            </div>
          </div>

          <div class="flex justify-center gap-6">
            <button
              class="bg-black w-full text-white font-bold uppercase text-xs shadow-button my-4 mb-4 !py-3 !px-6 !rounded-lg outline outline-1 outline-black outline-offset-4 shadow-btn hover:shadow-none transition-all duration-500"
              @click="copyReferralLink('customer')"
            >
              Genitori
            </button>
            <button
              @click="copyReferralLink('school_staff')"
              class="bg-[#a688f9] text-white w-full font-bold uppercase text-xs shadow-button my-4 mb-4 !py-3 !px-6 !rounded-lg outline outline-1 outline-[#a688f9] outline-offset-4 shadow-btn hover:shadow-none transition-all duration-500"
            >
              Personale scolastico
            </button>
          </div>

          <div
            class="mx-auto text-center font-bold text-xs md:text-sm opacity-60 px-4 mt-4"
          >
            Clicca sul pulsante per copiare il link e invialo ad un amico!
            <br />
            Riceverai un credito di 1€ non appena lui ricaricherà il suo
            portafoglio di credito.
          </div>
        </div>
      </div>
    </div>

    <ReferralUserType
      :isReferralUserTypeVisible="isReferralUserTypeVisible"
      :userType="selectedUserType"
      :selectedLink="selectedLink"
      v-if="isReferralUserTypeVisible"
      @close="closeReferralUserType"
    />

    <AddChild :isAddChildVisible="isAddChildVisible" @close="close" />

    <EditChildProfile
      v-if="isEditChildProfileOpen"
      :child-id="selectedChildId"
      @close="isEditChildProfileOpen = false"
    />

    <div
      v-if="isAuthenticated"
      class="max-w-screen-xl mx-auto flex flex-col justify-center items-center pb-16 px-4 gap-6 md:gap-10"
    >
      <div class="text-2xl md:text-6xl text-center font-bold">
        <div class="flex justify-center items-center gap-2 md:gap-7">
          <img
            src="../assets/icons/receipt.png"
            alt="Trust"
            class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
          />
          Visualizza le <span class="text-[#af4135]">ricevute</span>
        </div>
        <div>
          <div class="flex justify-center items-center gap-2 md:gap-7">
            <div>
              dei <span class="text-[#bf09bd]">tuoi </span>
              <span class="text-[#a688f9]">ordini </span>
              <!-- <img
                src="../assets/icons/wheat-sack.png"
                alt="Wheatsack"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer align-middle ml-2 md:ml-7"
              /> -->
            </div>
          </div>
        </div>
      </div>

      <div
        class="mx-auto text-center font-bold text-xs md:text-sm opacity-60 px-4 underline"
      >
        <router-link to="/orders/receipts">Fai clic qui.</router-link>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import {
  checkAuthStatus,
  getCurrentUserData,
  getChildrenForCurrentUser,
} from "../utils/auth";

interface School {
  id: number;
  name: string;
}

const isAuthenticated = ref<boolean>(false);
const currentUser = ref<any>(null);
const associatedSchools = ref<School[]>([]);
const selectedProvince = ref<any>(null);
const isEditChildProfileOpen = ref(false);
const children = ref<any[]>([]);
const selectedChildId = ref(null);
const isAddChildVisible = ref(false);
const isReferralUserTypeVisible = ref(false);
const selectedUserType = ref<"customer" | "school_staff">("customer");

const close = () => {
  isAddChildVisible.value = false;
};

let selectedLink = ref("");

const openEditChildProfile = (childId) => {
  selectedChildId.value = childId;
  isEditChildProfileOpen.value = true;
};

const openAddChild = () => {
  isAddChildVisible.value = true;
};

const userHasCredit = computed(() => {
  return currentUser.value && currentUser.value.credit_wallet_amount > 0;
});

const openReferralUserType = (userType: "customer" | "school_staff") => {
  isReferralUserTypeVisible.value = true;
  selectedUserType.value = userType;
};

const closeReferralUserType = () => {
  isReferralUserTypeVisible.value = false;
};

const copyReferralLink = async (type: "customer" | "school_staff") => {
  let link = "";
  if (type === "customer") {
    link = currentUser.value.referral_link_customer;
    selectedLink = currentUser.value.referral_link_customer;
  } else if (type === "school_staff") {
    link = currentUser.value.referral_link_school_staff;
    selectedLink = currentUser.value.referral_link_school_staff;
  }

  try {
    await navigator.clipboard.writeText(link);
    openReferralUserType(type);
  } catch (err) {
    console.error("Failed to copy: ", err);
  }
};

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
  currentUser.value = await getCurrentUserData();
  if (currentUser.value) {
    associatedSchools.value = currentUser.value.associated_schools;
    selectedProvince.value = currentUser.value.location.name;
    children.value = await getChildrenForCurrentUser();
  }
});
</script>