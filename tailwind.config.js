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
        black: "#141727",
        dark: "#020420",
        gray: {
          100: "#f8f9fa",
          200: "#f5f5f5",
          300: "#e0e0e0",
          400: "#888",
        },
        pink: "#bf09bd",
        purple: "#a688f9",
        yellow: "#ffa500",
        brown: "#af4135",
      },
      boxShadow: {
        btn: "0 20px 27px 10px rgba(0, 0, 0, 0.20)",
        lightCard: "0 20px 27px 0 rgba(0, 0, 0, 0.15)",
        card: "0 20px 27px 10px rgba(0, 0, 0, 0.25)",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
