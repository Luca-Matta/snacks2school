<template>
  <div>
    <div
      class="flex flex-wrap gap-2 justify-center md:gap-8 max-w-screen-xl mx-auto py-6 text-gray text-xs md:text-sm !leading-none"
    >
      <div class="flex gap-4">
        <div>© 2025 Snacks2School</div>
        <div>
          <a
            href="https://www.iubenda.com/privacy-policy/12347527"
            title="Privacy Policy"
            >Privacy Policy</a
          >
        </div>
        <div>
          <a
            href="https://www.iubenda.com/termini-e-condizioni/12347527"
            title="Termini e Condizioni"
            >Termini e Condizioni</a
          >
        </div>
      </div>
      <div>
        Icons by various authors from
        <a href="https://www.flaticon.com/" title="Flaticon">Flaticon</a> and
        <a href="https://www.freepik.com" title="Freepik">Freepik</a>
        <span @click="showAttributions = true" class="cursor-pointer">
          [Details]</span
        >
      </div>
    </div>

    <div
      v-if="showAttributions"
      class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center px-4"
    >
      <div class="bg-white p-6 !rounded-lg max-w-lg w-full">
        <h2 class="text-xl mb-4">Icons Attributions</h2>
        <ul class="list-disc pl-5">
          <li>
            Icons made by
            <a href="https://www.freepik.com" title="Freepik">Freepik</a>
            from
            <a href="https://www.freepik.com/" title="Freepik"
              >www.freepik.com</a
            >
          </li>
          <li>
            Icons made by
            <a href="https://www.flaticon.com" title="Flaticon">Flaticon</a>
            from
            <a href="https://www.flaticon.com/" title="Flaticon"
              >www.flaticon.com</a
            >
          </li>
          <!-- Add more attributions as needed -->
        </ul>
        <button
          @click="showAttributions = false"
          class="mt-4 bg-[#ffa500] text-black px-4 py-2 !rounded-md"
        >
          Close
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";

const showAttributions = ref(false);

onMounted(() => {
  const script = document.createElement("script");
  script.src = "https://cdn.iubenda.com/iubenda.js";
  script.async = true;
  document.body.appendChild(script);
});
</script>