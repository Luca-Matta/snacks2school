<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div class="flex justify-center items-center bg-[#f5f5f5] h-[100vh]">
        <div class="flex flex-col justify-center items-center">
          <img src="../assets/icons/logo.svg" alt="star" class="h-32 w-32" />
          <div class="text-4xl md:text-5xl font-bold">Snacks2School</div>
          <p class="max-w-96 text-center !py-4 !px-4">
            La merenda a portata di click
          </p>
          <div
            class="bg-white !rounded-3xl shadow-card w-[330px] md:w-auto md:min-w-96 p-6 mt-12"
          >
            <div class="text-2xl text-center font-semibold">
              A quale gruppo appartieni?
            </div>
            <hr class="mt-6 mb-4" />
            <div
              class="flex flex-col md:flex-row justify-center items-center w-full md:gap-2"
            >
              <router-link to="/signup-customer" class="w-full md:w-auto">
                <button
                  class="btn bg-[#ffa500] w-full md:w-auto font-bold uppercase text-xs shadow-button my-2 md:my-4 mb-2 !py-3 !px-6 !rounded-lg text-black"
                >
                  Studenti | Genitori
                </button>
              </router-link>
              <router-link to="/signup-school-staff" class="w-full md:w-auto">
                <button
                  class="btn bg-black w-full md:w-auto font-bold text-white uppercase text-xs shadow-button my-2 md:my-4 mb-2 !py-3 !px-6 !rounded-lg"
                >
                  Personale scolastico
                </button>
              </router-link>
            </div>
            <p class="text-sm mt-3 mb-0 text-center text-lead">
              Hai già un account?
              <router-link to="/login" class="font-bold !text-black"
                >Accedi</router-link
              >
            </p>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/vue";
</script>