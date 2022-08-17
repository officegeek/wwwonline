module.exports = {
  content: ["./layouts/**/*.html", "./content/**/*.md"],
  // safelist: ["bg-blue-50"],
  darkMode: "class",
  media: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        "muted": "#F6F5F1",
      },
      fontFamily: {
        sans: "'Euclid Circular B',-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif",
        serif: ["PT Serif", "serif"],
      },
    },
  },
  plugins: [
    require("@tailwindcss/aspect-ratio"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
  ],
};
