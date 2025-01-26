export default {
  css: ["~/assets/css/tailwind.css", "@/assets/css/main.css"],

  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  },

  modules: ["@nuxtjs/ionic", "@nuxtjs/device"],
  compatibilityDate: "2025-01-26",
};
