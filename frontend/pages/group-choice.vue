<template>
  <div class="flex justify-center items-center bg-gray-200 h-[100vh]">
    <div class="flex flex-col justify-center items-center">
      <img src="../assets/icons/logo.svg" alt="star" class="h-32 w-32" />
      <div class="text-4xl md:text-5xl font-bold">Snacks2School</div>
      <p class="max-w-96 text-center py-4 px-4">
        La merenda a portata di click
      </p>
      <div
        class="bg-white rounded-3xl shadow-card w-[330px] md:w-auto md:min-w-96 p-6 mt-12"
      >
        <div class="text-2xl text-center font-semibold">
          A quale gruppo appartieni?
        </div>
        <hr class="mt-6 mb-4" />
        <div
          class="flex flex-col md:flex-row justify-center items-center w-full md:gap-2"
        >
          <nuxt-link to="/signup-customer" class="w-full md:w-auto">
            <button
              class="btn bg-yellow w-full md:w-auto font-bold uppercase text-xs shadow-button my-2 md:my-4 mb-2 py-3 px-6 rounded-lg"
            >
              Studenti | Genitori
            </button>
          </nuxt-link>
          <nuxt-link to="/signup-school-staff" class="w-full md:w-auto">
            <button
              class="btn bg-black w-full md:w-auto font-bold text-white uppercase text-xs shadow-button my-2 md:my-4 mb-2 py-3 px-6 rounded-lg"
            >
              Personale scolastico
            </button>
          </nuxt-link>
        </div>
        <p class="text-sm mt-3 mb-0 text-center text-lead">
          Hai già un account?
          <nuxt-link to="/login" class="font-bold">Accedi</nuxt-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>