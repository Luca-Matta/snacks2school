<template>
  <div
    v-if="isAddChildVisible"
    class="fixed inset-0 flex justify-center items-center z-30 !px-4 md:px-0"
    style="backdrop-filter: blur(50px)"
  >
    <div
      class="bg-white p-8 !rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-full max-w-96 max-h-[500px] overflow-y-auto"
    >
      <h2 class="text-xl text-center font-bold mb-2">Aggiungi un figlio</h2>
      <div class="text-center text-xs mb-4">
        Abbiamo implementato una nuova funzionalità!<br />
        Puoi gestire più figli in un unico account!<br />
        Per effettuare un ordine devi inserire almeno un figlio.
      </div>
      <form @submit.prevent="submitForm">
        <div class="mb-4">
          <label for="first_name" class="block text-xs mb-1">Nome *</label>
          <input
            v-model="firstName"
            type="text"
            id="first_name"
            class="w-full bg-[#f5f5f5] border border-[#e0e0e0]"
            style="border-radius: 5px; padding: 7px"
            required
          />
        </div>
        <div class="mb-4">
          <label for="last_name" class="block text-xs mb-1">Cognome *</label>
          <input
            v-model="lastName"
            type="text"
            id="last_name"
            class="w-full bg-[#f5f5f5] border border-[#e0e0e0]"
            style="border-radius: 5px; padding: 7px"
            required
          />
        </div>
        <div class="mb-3">
          <label class="block text-xs mb-1">Provincia della scuola *</label>
          <select
            v-model="selectedProvince"
            id="selectedProvince"
            name="selectedProvince"
            class="w-full bg-[#f5f5f5] border border-[1.5px] border-[#ffa500] !rounded !px-2 !py-1 cursor-pointer"
            style="border-radius: 5px; padding: 7px"
            @change="fetchSchools"
          >
            <option value="" disabled></option>
            <option
              v-for="province in provinces"
              :key="province.id"
              :value="province.id"
            >
              {{ province.name }}
            </option>
          </select>
        </div>
        <div v-if="selectedProvince" class="mb-3">
          <label class="block text-xs mb-1">Scuola *</label>
          <select
            v-model="selectedSchool"
            id="associatedSchool"
            name="associatedSchool"
            class="w-full bg-[#f5f5f5] border border-[1.5px] border-[#ffa500] !rounded !px-2 !py-1 cursor-pointer"
            @change="fetchClasses"
          >
            <option value="" disabled></option>
            <option
              v-for="school in schoolsByProvince"
              :key="school.id"
              :value="school.id"
            >
              {{ school.name }}
            </option>
          </select>
        </div>
        <div v-if="selectedSchool" class="mb-3">
          <label class="block text-xs mb-1">Classe *</label>
          <select
            v-model="schoolClass"
            id="schoolClass"
            name="schoolClass"
            class="w-full bg-[#f5f5f5] border border-[1.5px] border-[#ffa500] !rounded !px-2 !py-1 cursor-pointer"
            style="border-radius: 5px; padding: 7px"
          >
            <option value="" disabled></option>
            <option
              v-for="schoolClass in classes"
              :key="schoolClass.id"
              :value="schoolClass.id"
            >
              {{ schoolClass.name }}
            </option>
          </select>
        </div>
        <div class="flex justify-end">
          <button
            type="submit"
            class="flex justify-center mx-auto btn bg-[#ffa500] uppercase text-black text-xs shadow-button !py-3 !px-6 !rounded-lg mt-4"
          >
            Aggiungi
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, onMounted } from "vue";
import { checkAuthStatus } from "../utils/auth";
import axios from "axios";

const props = defineProps<{
  isAddChildVisible: boolean;
}>();

const isAuthenticated = ref<boolean>(false);
const firstName = ref<string>("");
const lastName = ref<string>("");
const associatedSchools = ref<string>("");
const provinces = ref([]);
const selectedProvince = ref<string | null>(null);
const schoolsByProvince = ref([]);
const selectedSchool = ref<string | null>(null);
const schoolClass = ref<string>("");
const classes = ref([]);

const emit = defineEmits(["close"]);

const fetchProvinces = async () => {
  try {
    const response = await axios.get("https://www.snacks2school.com/api/provinces/");
    provinces.value = response.data;
  } catch (error) {
    console.error("Error fetching provinces:", error);
  }
};

const fetchSchools = async () => {
  if (!selectedProvince.value) return;
  try {
    const response = await axios.get(
      `https://www.snacks2school.com/api/province/schools/?province=${selectedProvince.value}`
    );
    schoolsByProvince.value = response.data;
  } catch (error) {
    console.error("Error fetching schools:", error);
  }
};

const fetchClasses = async () => {
  if (!selectedSchool.value) return;
  try {
    const response = await axios.get(
      `https://www.snacks2school.com/api/school/classes/?school=${selectedSchool.value}`
    );
    classes.value = response.data;
  } catch (error) {
    console.error("Error fetching classes:", error);
  }
};

const getCsrfToken = async () => {
  const response = await axios.get("https://www.snacks2school.com/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const submitForm = async () => {
  const csrfToken = await getCsrfToken();

  try {
    const response = await axios.post(
      "https://www.snacks2school.com/api/child/create/",
      {
        first_name: firstName.value,
        last_name: lastName.value,
        associated_schools: [selectedSchool.value],
        school_class: schoolClass.value,
      },
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );
    if (response.status >= 200 && response.status < 300) {
      emit("close");
      window.location.reload();
    }
  } catch (error) {
    console.error("Error creating child:", error);
  }
};

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
  fetchProvinces();
});
</script>