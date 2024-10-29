module.exports = {
  content: [
    "./components/**/*.{vue,js,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  darkMode: "media",
  theme: {
    extend: {
      colors: {
        dark: "#020420",
        gray: "#f5f5f5",
        pink: "#bf09bd",
        purple: "#a688f9",
        yellow: "#facc15",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
