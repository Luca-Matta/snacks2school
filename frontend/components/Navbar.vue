<template>
  <header
    class="bg-background/75 backdrop-blur-[8px] border-b-[0.5px] border-gray border-opacity-100 sticky top-0 z-50 mb-8"
  >
    <div
      class="mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl flex items-center justify-between gap-3 h-16"
    >
      <div class="flex items-center gap-1.5">
        <a
          href=""
          class="flex-shrink-0 font-bold text-xl text-gray-900 dark:text-white flex items-end gap-1.5"
          aria-label="Home"
        >
          <img
            src="../assets/icons/extended-logo.svg"
            alt="star"
            class="h-60 w-60"
          />
        </a>
      </div>
      <nav class="flex items-center gap-4">
        <a href="" class="text-yellow hover:text-purple">Store</a>
        <a href="" class="text-yellow hover:text-purple">Merende</a>
        <a href="" class="text-yellow hover:text-purple">Contatti</a>
      </nav>
      <div class="flex items-center gap-3">
        <nuxt-link to="/login">
          <button class="bg-yellow text-black px-4 py-2 rounded-md">
            Accedi
          </button>
        </nuxt-link>
        <button class="border border-black text-black px-4 py-2 rounded-md">
          Registrati
        </button>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts"></script>