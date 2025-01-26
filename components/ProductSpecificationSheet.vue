<template>
  <div
    v-if="isProductSpecificationSheetVisible"
    class="fixed inset-0 flex justify-center items-center z-30 !px-4 md:px-0"
    style="backdrop-filter: blur(50px)"
  >
    <div
      class="bg-white p-8 !rounded-3xl outline outline-4 outline-white outline-offset-4 shadow-card w-full max-w-96 max-h-[500px] overflow-y-auto"
    >
      <h2 class="text-xl text-center font-bold mt-2">Scheda tecnica</h2>
      <h6 class="text-center text-xs mx-auto !py-1">
        {{ selectedItem.name }}
      </h6>
      <hr />
      <div class="flex flex-col gap-1">
        <div class="text-center mx-auto font-bold text-sm">
          Proprietà organolettiche e funzionali
        </div>
        <p
          v-html="selectedItem.properties"
          class="text-center text-xs mx-auto"
        ></p>
      </div>
      <hr />
      <h6 class="text-center text-sm font-bold mt-4">Ingredienti</h6>
      <div class="flex flex-col gap-2 mt-3">
        <div
          v-for="(ingredient, index) in selectedItem.ingredients"
          :key="ingredient.name"
        >
          <div class="flex items-center gap-2">
            <div class="flex justify-center items-center">
              <img
                :src="ingredient.image"
                alt="Ingrediente"
                class="bg-center bg-contain bg-no-repeat h-8 w-8"
              />
            </div>
            <div class="text-sm">
              {{ ingredient.name }}
            </div>
          </div>
          <hr v-if="index < selectedItem.ingredients.length - 1" />
        </div>
      </div>
      <hr />
      <h6 class="text-center text-sm font-bold mt-4">Allergeni</h6>
      <div class="flex flex-col gap-2 mt-3">
        <div
          v-for="(allergen, index) in selectedItem.allergens"
          :key="allergen.name"
        >
          <div class="flex items-center gap-2">
            <div class="flex justify-center items-center">
              <img
                :src="allergen.image"
                alt="Allergene"
                class="bg-center bg-contain bg-no-repeat h-8 w-8"
              />
            </div>
            <div class="text-sm">
              {{ allergen.name }}
            </div>
          </div>
          <hr v-if="index < selectedItem.allergens.length - 1" />
        </div>
      </div>
      <hr />
      <h6 class="text-center text-sm font-bold mt-4">
        Può contenere tracce di
      </h6>
      <div class="flex flex-col gap-2 mt-3">
        <div
          v-for="(cross_contaminant, index) in selectedItem.cross_contaminants"
          :key="cross_contaminant.name"
        >
          <div class="flex items-center gap-2">
            <div class="flex justify-center items-center">
              <img
                :src="cross_contaminant.image"
                alt="Contaminante"
                class="bg-center bg-contain bg-no-repeat h-8 w-8"
              />
            </div>
            <div class="text-sm">
              {{ cross_contaminant.name }}
            </div>
          </div>
          <hr v-if="index < selectedItem.cross_contaminants.length - 1" />
        </div>
      </div>
      <hr />
      <!-- <h6 class="text-center text-sm font-bold mt-4">Allergeni</h6> -->
      <button
        @click="$emit('close')"
        class="btn bg-black w-full font-bold text-white uppercase text-xs shadow-button my-4 mt-6 mb-2 !py-3 !px-6 !rounded-lg"
      >
        Chiudi
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { watch } from "vue";

const props = defineProps({
  isProductSpecificationSheetVisible: Boolean,
  selectedItem: Object,
});

const emit = defineEmits(["close"]);

watch(
  () => props.selectedItem,
  (newValue) => {
    console.log("Selected Item:", newValue);
  },
  { immediate: true }
);
</script>