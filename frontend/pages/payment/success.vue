<template>
  <div>
    <Navbar />
    <div
      class="flex flex-col justify-center items-center max-w-screen-xl py-16 mx-auto gap-4"
    >
      <h1 class="font-bold text-3xl">
        Congratualazioni! Hai caricato 20€ sul tuo portafoglio di credito!
      </h1>
      <nuxt-link
        to="/"
        class="btn bg-yellow font-bold text-white uppercase text-xs shadow-button my-4 mb-2 py-3 px-6 rounded-lg"
        >Ordina una merenda</nuxt-link
      >
    </div>
  </div>
</template>

<script setup lang="ts"></script>