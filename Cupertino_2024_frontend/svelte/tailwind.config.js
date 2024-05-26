/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      opacity: {
        '87': '.87',
        '60': '.60',
        '38': '.38'
      },
      width: {
        '260': '260px',
      }
    },
  },
  plugins: [],
}

