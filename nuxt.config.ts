export default {
  css: ["~/assets/css/tailwind.css"],
  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  },
  modules: ["@nuxtjs/ionic"],
};
