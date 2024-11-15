import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  css: [
    "@/assets/css/tailwind.css",
    "@/assets/css/main.css",
    "@fortawesome/fontawesome-free/css/all.min.css",
  ],

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

  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap",
        },
      ],
    },
  },
});
