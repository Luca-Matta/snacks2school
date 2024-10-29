import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  css: ["@/assets/css/tailwind.css", "@/assets/css/main.css"],

  plugins: ["~/plugins/vue-cal.ts"],

  components: true,

  modules: ["@nuxtjs/tailwindcss"],

  build: {
    postcss: {
      postcssOptions: {
        plugins: {
          tailwindcss: {},
          autoprefixer: {},
        },
      },
    },
  },

  compatibilityDate: "2024-10-29",
});
