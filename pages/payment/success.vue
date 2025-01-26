<template>
  <div>
    <Navbar />
    <div
      class="flex flex-col justify-center items-center max-w-screen-xl !py-16 mx-auto gap-4"
    >
      <div class="flex justify-center items-center">
        <img
          src="../../assets/icons/charged-wallet.png"
          alt="Safety"
          class="h-20 md:h-24 w-20 md:w-24"
        />
      </div>
      <div class="text-3xl md:text-6xl text-center font-bold">
        Congratulazioni!<br />
        <span class="text-[#bf09bd]">Hai caricato 10€ </span> sul tuo
        <span class="text-[#a688f9]">portafoglio di credito!</span>
      </div>
      <router-link
        to="/"
        class="btn bg-[#ffa500] font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"
        >Ordina una merenda</router-link
      >
    </div>
  </div>
</template>

<script setup lang="ts"></script>