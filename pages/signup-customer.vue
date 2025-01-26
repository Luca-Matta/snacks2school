<template>
  <div class="flex justify-center items-center bg-gray-200 h-full pb-16">
    <div class="flex flex-col justify-center items-center">
      <img src="../assets/icons/logo.svg" alt="star" class="h-32 w-32" />
      <div class="text-4xl md:text-5xl font-bold">Snacks2School</div>
      <p class="max-w-96 text-center py-4">La merenda a portata di clic</p>
      <div
        class="bg-white !rounded-3xl shadow-card w-[335px] md:w-auto md:min-w-96 p-6 mt-6 md:mt-12"
      >
        <div class="text-2xl font-semibold">Registrati</div>
        <!-- <p class="text-sm opacity-80 mt-2">
          Unisciti agli utenti di Snacks2School
        </p> -->
        <p class="text-sm opacity-80 mt-2">
          Unisciti ai {{ userCount }} utenti di Snacks2School
        </p>
        <hr class="mt-6 mb-4" />
        <form class="mb-3" @submit.prevent="handleSignup">
          <div class="mb-3">
            <label class="block text-xs mb-1">Email *</label>
            <input
              v-model="email"
              id="email"
              name="email"
              type="text"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
          </div>
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
          <!-- <div class="mb-3">
            <label class="block text-xs mb-1">Nome dello studente *</label>
            <input
              v-model="studentFirstName"
              id="studentFirstName"
              name="studentFirstName"
              type="text"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
          </div>
          <div class="mb-3">
            <label class="block text-xs mb-1">Cognome dello studente *</label>
            <input
              v-model="studentLastName"
              id="studentLastName"
              name="studentLastName"
              type="text"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
          </div> -->
          <div class="mb-3">
            <label class="block text-xs mb-1">Nome genitore *</label>
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
            <label class="block text-xs mb-1">Cognome genitore *</label>
            <input
              v-model="lastName"
              id="lastName"
              name="lastName"
              type="text"
              class="w-full bg-gray-200 border border-gray-300"
              style="border-radius: 5px; padding: 7px"
            />
          </div>
          <!-- <div class="mb-3">
            <label class="block text-xs mb-1">Provincia della scuola *</label>
            <select
              v-model="selectedProvince"
              id="selectedProvince"
              name="selectedProvince"
              class="w-full bg-gray-200 border border-[1.5px] border-[#ffa500] !rounded px-2 py-1 cursor-pointer"
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
              class="w-full bg-gray-200 border border-[1.5px] border-[#ffa500] !rounded px-2 py-1 cursor-pointer"
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
              class="w-full bg-gray-200 border border-[1.5px] border-[#ffa500] !rounded px-2 py-1 cursor-pointer"
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
          </div> -->
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
              Facendo clic su "Registrati" accetti i nostri
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
              class="btn bg-[#ffa500] w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
            >
              Registrati
            </button>
          </div>

          <p class="text-sm mt-3 mb-0 text-lead">
            Hai già un account?
            <router-link to="/login" class="font-bold">Accedi</router-link>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

const passwordFieldType = ref<string>("password");
const email = ref<string>("");
const username = ref<string>("");
// const studentFirstName = ref<string>("");
// const studentLastName = ref<string>("");
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
const selectedSchool = ref<string | null>(null);
const classes = ref([]);
const route = useRoute();
const referralUsername = route.query.ref || "";

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

const userCount = ref<number>(0);

const fetchUserCount = async () => {
  try {
    const response = await fetch("http://localhost:8000/api/user-count/");
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    userCount.value = data.user_count;
  } catch (error) {
    console.error("Error fetching user count:", error);
  }
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

import axiosInstance from "../utils/axiosInstance";

const handleLogin = async () => {
  try {
    const csrfResponse = await axiosInstance.get("csrf-token/");
    const csrfToken = csrfResponse.data.csrfToken;

    const response = await axiosInstance.post(
      "login/",
      {
        username: username.value,
        password: password.value,
      },
      {
        headers: {
          "X-CSRFToken": csrfToken,
        },
        withCredentials: true,
      }
    );

    if (response.data.token) {
      localStorage.setItem("token", response.data.token);
      window.location.href = "/";
    }
  } catch (error) {
    console.error("Login failed:", error);
  }
};

const handleSignup = async () => {
  try {
    if (password.value !== confirmPassword.value) {
      console.error("Passwords do not match");
      return;
    }

    const csrfToken = await getCsrfToken();
    const payload = {
      email: email.value,
      username: username.value,
      // student_first_name: studentFirstName.value,
      // student_last_name: studentLastName.value,
      first_name: firstName.value,
      // first_name: firstName.value ? firstName.value : studentFirstName.value,
      last_name: lastName.value,
      // last_name: lastName.value ? lastName.value : studentLastName.value,
      // location: selectedProvince.value,
      // associated_schools: [selectedSchool.value],
      // school_class: schoolClass.value,
      password: password.value,
      confirm_password: confirmPassword.value,
    };

    let signupUrl = "http://localhost:8000/api/signup/customer/";
    if (referralUsername) {
      signupUrl += `?ref=${referralUsername}`;
    }

    const response = await axios.post(signupUrl, payload, {
      headers: {
        "X-CSRFToken": csrfToken,
      },
      withCredentials: true,
    });

    if (response.data.token) {
      document.cookie = `token=${response.data.token}`;
      await handleLogin();
    } else {
      console.error("No token received");
    }
  } catch (error) {
    console.error("Signup failed:", error);
  }
};

onMounted(() => {
  fetchUserCount();
  fetchProvinces();
});
</script>