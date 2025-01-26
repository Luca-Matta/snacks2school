import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  css: ["~/assets/css/tailwind.css", "@/assets/css/main.css"],

  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  },

  vite: {
    plugins: [tailwindcss()],
  },

  modules: ["@nuxtjs/ionic", "@nuxtjs/device", "nuxt-swiper"],
  compatibilityDate: "2025-01-26",
});