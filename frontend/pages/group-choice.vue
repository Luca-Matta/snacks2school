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
        <div class="text-2xl text-center font-semibold">
          A quale gruppo appartieni?
        </div>
        <hr class="mt-6 mb-4" />
        <div class="grid grid-cols-2 gap-2">
          <nuxt-link to="/signup-customer">
            <button
              class="btn bg-yellow w-full font-bold uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
            >
              Cliente
            </button>
          </nuxt-link>
          <nuxt-link to="/signup-store">
            <button
              class="btn bg-black w-full font-bold text-white uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
            >
              Store
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