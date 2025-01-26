<template>
  <div
    class="fixed inset-0 flex justify-center items-center z-30 !px-4 md:px-0"
    style="backdrop-filter: blur(50px)"
  >
    <div
      class="bg-white p-8 !rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-full max-w-96 max-h-[500px] overflow-y-auto"
    >
      <h2 class="text-xl text-center font-bold">Modifica le informazioni di</h2>
      <form class="flex flex-col mt-3" @submit.prevent="">
        <div class="mb-3">
          <label class="block text-center text-xs font-bold mb-2">
            Provincia della scuola *</label
          >
          <select
            v-model="selectedProvince"
            id="selectedProvince"
            name="selectedProvince"
            class="w-full bg-[#f5f5f5] border border-[1.5px] border-[#bf09bd] !rounded !px-2 !py-1 cursor-pointer"
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
          <label class="block text-center text-xs font-bold mb-2"
            >Scuola *</label
          >
          <select
            v-model="selectedSchool"
            id="associatedSchool"
            name="associatedSchool"
            class="w-full bg-[#f5f5f5] border border-[1.5px] border-[#bf09bd] !rounded !px-2 !py-1 cursor-pointer"
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
          <label class="block text-center text-xs font-bold mb-2"
            >Classe *
          </label>
          <select
            v-model="schoolClass"
            id="schoolClass"
            name="schoolClass"
            class="w-full bg-[#f5f5f5] border border-[1.5px] border-[#bf09bd] !rounded !px-2 !py-1 cursor-pointer"
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
        <div class="flex flex-col md:flex-row gap-2">
          <button
            @click="$emit('close')"
            class="btn bg-black w-full font-bold text-white uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
          >
            Annulla
          </button>
          <button
            @click="editChildProfile"
            class="btn bg-[#bf09bd] text-white w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
          >
            Salva
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import axios from "axios";

const props = defineProps({
  childId: {
    type: Number,
    required: true,
  },
});

const schoolsDropdownOpen = ref(false);
const selectedProvince = ref<string | null>(null);
const provinces = ref([]);
const schoolsByProvince = ref([]);
const selectedSchool = ref<string | null>(null);
const schoolClass = ref<string>("");
const classes = ref([]);

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const fetchProvinces = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/provinces/");
    provinces.value = response.data;
  } catch (error) {
    console.error("Error fetching provinces:", error);
  }
};

const fetchSchools = async () => {
  if (!selectedProvince.value) return;
  try {
    const response = await axios.get(
      `http://localhost:8000/api/province/schools/?province=${selectedProvince.value}`
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
      `http://localhost:8000/api/school/classes/?school=${selectedSchool.value}`
    );
    classes.value = response.data;
  } catch (error) {
    console.error("Error fetching classes:", error);
  }
};

const toggleSchoolsDropdown = () => {
  schoolsDropdownOpen.value = !schoolsDropdownOpen.value;
};

const editChildProfile = async () => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await axios.post(
      `http://localhost:8000/api/children/${props.childId}/edit/`,
      {
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
  } catch (error) {
    console.error("Error updating child profile:", error);
  }
};

onMounted(async () => {
  fetchProvinces();
  const response = await axios.get(
    `http://localhost:8000/api/children/${props.childId}`
  );
  const childData = response.data;
  selectedSchool.value = childData.associated_schools[0];
  schoolClass.value = childData.school_class;
});
</script>