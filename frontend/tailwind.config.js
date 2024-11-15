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
        gray: {
          100: "#f8f9fa",
          200: "#f5f5f5",
          300: "#e0e0e0",
        },
        pink: "#bf09bd",
        purple: "#a688f9",
        yellow: "#ffa500",
      },
      boxShadow: {
        card: "0 20px 27px 0 rgba(0, 0, 0, 0.05)",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
