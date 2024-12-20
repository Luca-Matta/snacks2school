<template>
  <div class="flex justify-center items-center bg-gray-200 h-full pb-16">
    <div class="flex flex-col justify-center items-center">
      <img src="../assets/icons/logo.svg" alt="star" class="h-32 w-32" />
      <div class="text-5xl font-bold">Snacks2School</div>
      <p class="max-w-96 text-center py-4">
        L'app per la merenda a scuola che pensa alla salute dei ragazzi e ai
        bisogni dei genitori
      </p>
      <div class="bg-white rounded-3xl shadow-card min-w-96 p-6 mt-12">
        <div class="text-2xl font-semibold">Registrati</div>
        <p class="text-sm opacity-80 mt-2">
          Unisciti ai 1 membri di Snacks2School
        </p>
        <hr class="mt-6 mb-4" />
        <form class="mb-3" @submit.prevent="handleSignup">
          <div class="mb-3">
            <label class="block text-xs mb-1">Nome utente *</label>
            <input
              v-model="username"
              id="username"
              name="username"
              type="text"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
          </div>
          <div class="mb-3">
            <label class="block text-xs mb-1">Nome *</label>
            <input
              v-model="firstName"
              id="firstName"
              name="firstName"
              type="text"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
          </div>
          <div class="mb-3">
            <label class="block text-xs mb-1">Cognome *</label>
            <input
              v-model="lastName"
              id="lastName"
              name="lastName"
              type="text"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
          </div>
          <div class="mb-3">
            <label class="block text-xs mb-1">Provincia *</label>
            <select
              v-model="selectedProvince"
              id="selectedProvince"
              name="selectedProvince"
              class="w-full bg-gray-200 border border-[1.5px] border-yellow rounded px-2 py-1 cursor-pointer"
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
              v-model="associatedSchool"
              id="associatedSchool"
              name="associatedSchool"
              class="w-full bg-gray-200 border border-[1.5px] border-yellow rounded px-2 py-1 cursor-pointer"
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
          <div class="mb-3">
            <label class="block text-xs mb-1">Classe *</label>
            <select
              v-model="schoolClass"
              id="schoolClass"
              name="schoolClass"
              class="w-full bg-gray-200 border border-[1.5px] border-yellow rounded px-2 py-1 cursor-pointer"
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
          <div class="mb-3 relative">
            <label class="block text-xs mb-1">Password *</label>
            <input
              v-model="password"
              id="password"
              name="password"
              :type="passwordFieldType"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
            <i
              :class="
                passwordFieldType === 'password'
                  ? 'fas fa-eye'
                  : 'fas fa-eye-slash'
              "
              class="absolute right-3 top-10 transform -translate-y-1/2 cursor-pointer"
              @click="togglePasswordVisibility"
            ></i>
          </div>
          <div class="mb-3 relative">
            <label class="block text-xs mb-1">Conferma password *</label>
            <input
              v-model="confirmPassword"
              id="confirmPassword"
              name="confirmPassword"
              :type="passwordFieldType"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
            <i
              :class="
                passwordFieldType === 'password'
                  ? 'fas fa-eye'
                  : 'fas fa-eye-slash'
              "
              class="absolute right-3 top-10 transform -translate-y-1/2 cursor-pointer"
              @click="togglePasswordVisibility"
            ></i>
          </div>
          <div class="text-left">
            <label class="text-gray-400 text-xs" for="flexCheckDefault">
              Facendo click su "Registrati" accetti i nostri
              <a
                href=""
                class="iubenda-nostyle iubenda-noiframe iubenda-embed iubenda-noiframe underline text-gray-400"
                title="Termini e Condizioni"
              >
                Termini e condizioni
              </a>
            </label>
          </div>
          <div class="text-center">
            <button
              type="submit"
              class="btn bg-yellow w-full font-bold uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
            >
              Registrati
            </button>
          </div>

          <p class="text-sm mt-3 mb-0 text-lead">
            Hai già un account?
            <nuxt-link to="/login" class="font-bold">Accedi</nuxt-link>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

const passwordFieldType = ref<string>("password");
const username = ref<string>("");
const firstName = ref<string>("");
const lastName = ref<string>("");
const location = ref<string>("");
const associatedSchool = ref<string>("");
const schoolClass = ref<string>("");
const password = ref<string>("");
const confirmPassword = ref<string>("");
const provinces = ref([]);
const selectedProvince = ref<string | null>(null);
const schoolsByProvince = ref([]);
const classes = ref([]);

const togglePasswordVisibility = () => {
  passwordFieldType.value =
    passwordFieldType.value === "password" ? "text" : "password";
};

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
    console.log("Schools:", schoolsByProvince.value);
  } catch (error) {
    console.error("Error fetching schools:", error);
  }
};

const fetchClasses = async () => {
  const response = await axios.get("http://localhost:8000/api/classes/");
  classes.value = response.data;
  console.log("Classes:", classes.value);
};

const handleSignup = async () => {
  try {
    if (password.value !== confirmPassword.value) {
      console.error("Passwords do not match");
      return;
    }

    const csrfToken = await getCsrfToken();
    const payload = {
      username: username.value,
      first_name: firstName.value,
      last_name: lastName.value,
      location: selectedProvince.value,
      associated_school: associatedSchool.value,
      school_class: schoolClass.value,
      password: password.value,
      confirm_password: confirmPassword.value,
    };

    console.log("Signup payload:", payload);

    const response = await axios.post(
      "http://localhost:8000/api/signup/customer/",
      payload,
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );
    console.log("Signup successful:", response.data);

    if (response.data.token) {
      document.cookie = `token=${response.data.token}`;
      window.location.href = "/";
    } else {
      console.error("No token received");
    }
  } catch (error) {
    console.error("Signup failed:", error);
  }
};

onMounted(() => {
  fetchProvinces();
  fetchClasses();
});
</script>