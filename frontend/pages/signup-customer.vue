<template>
  <div class="flex justify-center items-center bg-gray-200 h-[100vh]">
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
          <div class="mb-3 relative">
            <label class="block text-xs mb-1"> Password *</label>
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
            <label class="block text-xs mb-1"> Conferma password *</label>
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
              class="btn bg-yellow w-full font-bold text-white uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
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
import { ref } from "vue";
import axios from "axios";

const passwordFieldType = ref<string>("password");
const username = ref<string>("");
const password = ref<string>("");

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

const handleSignup = async () => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await axios.post(
      "http://localhost:8000/api/signup/",
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
    console.log("Signup successful:", response.data);

    if (response.data.token) {
      document.cookie = `token=${response.data.token}`;
      window.location.href = "/";
    }
  } catch (error) {
    console.error("Signup failed:", error);
  }
};
</script>