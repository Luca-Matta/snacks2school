<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div class="flex justify-center items-center bg-[#f5f5f5] h-[100vh]">
        <div class="flex flex-col justify-center items-center !px-4">
          <img src="../assets/icons/logo.svg" alt="star" class="h-32 w-32" />
          <div class="text-4xl md:text-5xl font-bold">Snacks2School</div>
          <p class="max-w-96 text-center !py-4">
            La merenda a portata di click
          </p>
          <div
            class="bg-white !rounded-3xl shadow-card w-[335px] md:w-auto md:min-w-96 p-6 mt-6 md:mt-12"
          >
            <div class="text-2xl font-semibold">Accedi</div>
            <p class="text-sm opacity-80 mt-2">Compra la tua merenda</p>
            <hr class="mt-6 mb-4" />
            <form class="mb-3" @submit.prevent="handleLogin">
              <div class="mb-3">
                <label class="block text-xs mb-1" for="username"
                  >Nome utente</label
                >
                <input
                  v-model="username"
                  id="username"
                  name="username"
                  type="text"
                  class="w-full !bg-[#f5f5f5] !border !border-[#e0e0e0]"
                  style="border-radius: 5px; padding: 7px"
                  autocomplete="username"
                />
              </div>
              <div class="mb-3 relative">
                <label class="block text-xs mb-1" for="password">
                  Password
                </label>
                <input
                  v-model="password"
                  id="password"
                  name="password"
                  :type="passwordFieldType"
                  class="w-full bg-[#f5f5f5] border border-[#e0e0e0]"
                  style="border-radius: 5px; padding: 7px"
                  autocomplete="current-password"
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
              <div class="text-center">
                <button
                  type="submit"
                  class="btn bg-[#ffa500] w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
                >
                  Accedi
                </button>
              </div>

              <p class="text-sm mt-3 mb-0 text-lead">
                Non hai un account?
                <router-link to="/group-choice" class="font-bold !text-black"
                  >Registrati</router-link
                >
              </p>
            </form>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/vue";

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
</script>