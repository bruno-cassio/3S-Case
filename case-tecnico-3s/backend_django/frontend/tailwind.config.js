/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#0d1117",
        secondary: "#161b22",
        accent: "#58a6ff",
        text: "#c9d1d9",
        border: "#30363d"
      },
    },
  },
  darkMode: 'class',
  plugins: [],
}
