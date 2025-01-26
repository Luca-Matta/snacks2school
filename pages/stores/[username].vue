<template>
  <div>
    <Navbar />
    <div class="hero relative text-white pb-6">
      <div class="flex justify-center items-center py-20 md:py-60 px-4">
        <div class="flex flex-col py-8">
          <div class="flex flex-col md:flex-row items-center gap-8">
            <div class="bg-gray-100 h-32 w-32 !rounded-xl">
              <img
                :src="profile_picture"
                alt="Profile Picture"
                class="outline outline-1 outline-white outline-offset-4 !rounded-xl"
              />
            </div>
            <div class="flex flex-col gap-2 text-center md:text-left">
              <p class="font-bold text-2xl md:text-5xl">
                {{ first_name }} {{ last_name }}
              </p>
              <div>
                <p>{{ address }}</p>
                <p v-html="formattedBio"></p>
              </div>
            </div>
          </div>
          <div
            class="absolute right-0 bottom-6 left-0 py-2"
            style="background-color: rgba(243, 244, 246, 0.6)"
          >
            <div class="flex justify-center items-center">
              <div class="flex gap-12">
                <!-- <div>
                  <img
                    src="../../assets/icons/gluten-free.png"
                    alt=""
                    class="h-12 md:h-20 w-12 md:w-20"
                  />
                </div> -->
                <div>
                  <img
                    src="../../assets/icons/vegan.png"
                    alt=""
                    class="h-12 md:h-20 w-12 md:w-20"
                  />
                </div>
                <div>
                  <img
                    src="../../assets/icons/bio.png"
                    alt=""
                    class="h-12 md:h-20 w-12 md:w-20"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      class="max-w-screen-xl mx-auto flex flex-col justify-center items-center pt-12 md:pt-24 px-4 gap-6 md:gap-10"
    >
      <div class="text-2xl md:text-5xl text-center font-bold">
        La <span class="text-[#af4135]">bontà</span> ha
        <span class="text-[#a688f9]">una </span>
        <span class="text-[#bf09bd]">storia</span>
      </div>
      <!-- <div class="text-3xl md:text-5xl text-center font-bold">
        Una <span class="text-[#af4135]">storia</span> di autenticità e tradizione
        <span class="text-[#a688f9]">dal </span>
        <span class="text-[#bf09bd]">1933</span>
      </div> -->

      <div class="mx-auto text-center text-xs md:text-base px-4 -mt-2">
        <span class="font-bold"
          >Una storia di autenticità e tradizione dal 1933.</span
        ><br />
        Il <span class="font-bold">Panificio Drago</span> nasce a Massa, in Via
        Francesco Torta 114, nel lontano 1933, grazie alla
        <span class="font-bold">visione</span> e al
        <span class="font-bold">duro lavoro</span> del fondatore Domenico Drago.
        Da allora, generazione dopo generazione,
        <span class="font-bold"
          >la nostra famiglia ha mantenuto vivo il sogno di offrire un pane
          autentico</span
        >, fatto con ingredienti di qualità e lavorato a mano, secondo metodi
        tradizionali. La nostra sede storica è sempre stata qui, in Via Torta,
        un luogo che custodisce memorie e profumi di un tempo passato, ma che
        guarda al futuro con innovazione e passione. Sin dall'inizio, la
        filosofia del Panificio Drago è stata chiara: artigianalità, qualità e
        genuinità. Ogni giorno portiamo avanti
        <span class="font-bold">la tradizione del "fatto a mano"</span>,
        utilizzando esclusivamente ingredienti selezionati e lievito madre, che
        garantisce
        <span class="font-bold"
          >un pane dal sapore unico, altamente digeribile e privo di
          conservanti.</span
        >
        Grazie al nostro impegno costante nella ricerca della massima qualità,
        abbiamo ottenuto la <span class="font-bold">Certificazione IFS</span>,
        che garantisce ai nostri clienti prodotti sicuri e di eccellenza. Per
        noi, la trasparenza e il rispetto degli standard qualitativi sono
        fondamentali, perché crediamo che chi sceglie il nostro pane meriti il
        meglio.
      </div>
    </div>

    <div
      class="max-w-screen-xl mx-auto flex flex-col justify-center items-center pt-12 px-4"
    >
      <div class="flex justify-center items-center gap-2 md:gap-7">
        <img
          src="../../assets/icons/dough-proofing.png"
          alt="Trust"
          class="h-8 md:h-16 w-8 md:w-16 cursor-pointer"
        />
      </div>
      <div class="flex flex-col gap-6 md:gap-10">
        <div class="text-2xl md:text-5xl text-center font-bold">
          Lievito madre <br />
          Il <span class="text-[#af4135]">cuore</span> del
          <span class="text-[#a688f9]">nostro </span>
          <span class="text-[#bf09bd]">pane</span>
        </div>
        <div class="mx-auto text-center text-xs md:text-base px-4 -mt-2">
          <div class="max-w-60 md:max-w-full text-center mx-auto">
            <span class="font-bold"
              >Il lievito madre è il protagonista assoluto della nostra
              produzione.</span
            >
          </div>
          Si tratta di un impasto composto da farina e acqua, fermentato
          naturalmente grazie alla presenza di batteri lattici e lieviti
          naturali. Questo processo garantisce numerosi benefici:
          <span class="font-bold">alta digeribilità</span> grazie alla
          fermentazione lenta e naturale.
          <span class="font-bold"
            >Assenza di conservanti e additivi artificiali</span
          >, per un prodotto autentico e genuino.
          <span class="font-bold">Indice glicemico più basso</span> rispetto al
          pane prodotto con lieviti industriali, rendendolo adatto anche a chi
          deve monitorare la glicemia. Ricchezza di nutrienti, come
          <span class="font-bold">antiossidanti</span>,
          <span class="font-bold">vitamine</span> e
          <span class="font-bold">minerali essenziali</span> quali calcio, zinco
          e ferro. Usare il lievito madre non è solo una scelta di qualità, ma
          un <span class="font-bold">ritorno alle origini</span>, un modo per
          riscoprire il sapore autentico del
          <span class="font-bold">pane di una volta</span>.
        </div>
      </div>
    </div>

    <div
      class="max-w-screen-xl mx-auto flex flex-col justify-center items-center pt-12 px-4"
    >
      <div class="flex justify-center items-center gap-2 md:gap-7">
        <img
          src="../../assets/icons/ham.png"
          alt="Ham"
          class="h-8 md:h-16 w-8 md:w-16 cursor-pointer inline-block align-middle ml-2 md:ml-7"
        />
      </div>
      <div>
        <div class="hidden md:flex flex-col gap-4">
          <div class="text-2xl md:text-5xl text-center font-bold mt-2">
            Salumi da... <span class="text-[#bf09bd]">"La Bottega di Adò"</span>
          </div>
          <div class="mx-auto text-center font-bold text-sm px-4">
            L'eccellenza della materia prima.
          </div>
        </div>
        <div class="flex flex-col gap-2 md:hidden">
          <div class="text-2xl md:text-5xl text-center font-bold">
            Salumi da... <br />
            <span class="text-[#bf09bd]">"La Bottega di Adò"</span>
          </div>
          <div class="mx-auto text-center font-bold text-xs px-4">
            L'eccellenza della materia prima.
          </div>
        </div>
      </div>
    </div>

    <!-- <div
      class="max-w-screen-xl mx-auto flex flex-col justify-center items-center pt-6 md:pt-12 px-4 gap-6"
    >
      <div class="text-2xl md:text-5xl text-center font-bold">
        I nostri <span class="text-[#af4135]">impasti</span>
      </div>
      <div class="flex gap-4">
        <div class="flex flex-col gap-2">
          <div class="flex justify-center items-center gap-2 md:gap-7">
            <img
              src="../../assets/icons/crostaccio-dough.png"
              alt="Trust"
              class="h-8 md:h-20 w-8 md:w-20 cursor-pointer"
            />
          </div>
          <div class="mx-auto text-center font-bold text-xs md:text-sm px-4">
            Crostaccio
          </div>
        </div>
        <div class="flex flex-col gap-2">
          <div class="flex justify-center items-center gap-2 md:gap-7">
            <img
              src="../../assets/icons/curcuma-chia-dough.png"
              alt="Trust"
              class="h-8 md:h-20 w-8 md:w-20 cursor-pointer"
            />
          </div>
          <div class="mx-auto text-center font-bold text-xs md:text-sm px-4">
            Curcuma e chia
          </div>
        </div>
        <div class="flex flex-col gap-2">
          <div class="flex justify-center items-center gap-2 md:gap-7">
            <img
              src="../../assets/icons/grano-arso-dough.png"
              alt="Trust"
              class="h-8 md:h-20 w-8 md:w-20 cursor-pointer"
            />
          </div>
          <div class="mx-auto text-center font-bold text-xs md:text-sm px-4">
            Grano arso
          </div>
        </div>
      </div>
    </div> -->

    <div
      class="flex flex-col justify-center items-center max-w-screen-xl mx-auto py-6 md:py-12"
    >
      <div class="flex flex-col justify-center items-center py-8 gap-4">
        <div
          class="flex flex-col justify-center items-center max-w-screen-xl mx-auto"
        >
          <!-- <div class="w-full h-auto px-4" autoplay muted>
            <img
              src="../../static/store-menu.png"
              alt="Menu"
              class="bg-center bg-contain bg-no-repeat"
            />
          </div> -->
          <h1 class="font-bold text-center text-2xl md:text-5xl mb-2">
            Catalogo / <span class="text-[#af4135]">Merende</span>
          </h1>
        </div>
        <div
          class="flex flex-wrap justify-center items-center gap-8 md:gap-12 py-6"
        >
          <div v-for="snack in singleStoreSnacks" :key="snack">
            <div
              class="flex flex-col justify-center items-center gap-2 bg-white shadow-card hover:shadow-none transition-all duration-500 !rounded-xl h-48 md:h-64 w-40 md:w-60 p-2 md:p-6 cursor-pointer outline outline-1 outline-[#af4135] outline-offset-4"
              @click="openProductSpecificationSheet(snack)"
            >
              <div class="flex justify-center items-center">
                <img
                  :src="snack.image"
                  alt="snack"
                  class="bg-center bg-contain bg-no-repeat h-8 md:h-16 w-8 md:w-16"
                />
              </div>
              <div class="flex flex-col justify-center items-center">
                <div class="flex flex-col items-center justify-center">
                  <p
                    class="font-bold text-center text-xs md:text-sm mt-1 md:mt-2"
                  >
                    {{ snack.name }}
                  </p>
                  <!-- <div class="flex gap-1">
                    <div
                      v-for="(ingredient, index) in snack.ingredients"
                      :key="index"
                      class="py-2"
                    >
                      <img
                        :src="ingredient.image"
                        :alt="ingredient.name"
                        :title="ingredient.name"
                        class="bg-center bg-contain bg-no-repeat h-4 md:h-6 w-4 md:w-6"
                      />
                    </div>
                  </div> -->
                  <div
                    class="text-xs text-center font-bold py-1 md:py-2 underline"
                  >
                    Consulta la scheda tecnica
                  </div>
                  <p class="text-xs mt-1 md:mt-0">{{ snack.gross_price }}€</p>
                </div>
                <p class="text-xs opacity-80"></p>
              </div>
            </div>
          </div>
        </div>

        <h1 class="font-bold text-center text-2xl md:text-5xl mt-12 mb-2">
          Catalogo / <span class="text-[#af4135]">Bevande</span>
        </h1>
        <div
          class="flex flex-wrap justify-center items-center gap-8 md:gap-12 py-6"
        >
          <div v-for="drink in singleStoreDrinks" :key="drink">
            <div
              class="flex flex-col justify-center items-center gap-2 bg-white shadow-card hover:shadow-none transition-all duration-500 !rounded-xl h-48 md:h-64 w-40 md:w-60 p-6 cursor-pointer outline outline-1 outline-[#af4135] outline-offset-4"
            >
              <div class="flex justify-center items-center">
                <img
                  :src="drink.image"
                  alt="snack"
                  class="bg-center bg-contain bg-no-repeat h-8 md:h-16 w-8 md:w-16"
                />
              </div>
              <div class="flex flex-col justify-center items-center">
                <div class="flex flex-col items-center justify-center">
                  <p
                    class="font-bold text-center text-xs md:text-sm mt-1 md:mt-2"
                  >
                    {{ drink.name }}
                  </p>
                  <!-- <div class="flex gap-1">
                    <div
                      v-for="(ingredient, index) in snack.ingredients"
                      :key="index"
                      class="py-2"
                    >
                      <img
                        :src="ingredient.image"
                        :alt="ingredient.name"
                        :title="ingredient.name"
                        class="bg-center bg-contain bg-no-repeat h-6 w-6"
                      />
                    </div>
                  </div> -->
                  <p class="text-xs mt-1 md:mt-2">{{ drink.gross_price }}€</p>
                </div>
                <p class="text-xs opacity-80"></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <ProductSpecificationSheet
      :isProductSpecificationSheetVisible="isProductSpecificationSheetVisible"
      :selectedItem="selectedItem"
      @openProductSpecificationSheet="openProductSpecificationSheet"
      @close="close"
    />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const state = router.options.history.state;
const { first_name, last_name, profile_picture, location, address, bio } =
  route.query;
const username = route.params.username;

const formattedBio = bio ? bio.replace(/\n/g, "<br>") : "";

interface Store {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  location: string;
  address: string;
  // profile_picture: string;
  bio: string;
}

interface Ingredient {
  name: string;
  image: string;
}

interface Snack {
  id: number;
  name: string;
  date: string;
  price: number;
  image: string;
  ingredients: Ingredient[];
  seller: Store;
}

interface Drink {
  id: number;
  name: string;
  date: string;
  price: number;
  image: string;
  ingredients: Ingredient[];
  seller: Store;
}

const singleStoreSnacks = ref<Snack[]>([]);
const singleStoreDrinks = ref<Drink[]>([]);

const fetchSingleStoreSnacks = async (username: string) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/snacks/?username=${username}`
    );
    singleStoreSnacks.value = response.data;
  } catch (error) {
    console.error("Error fetching snack data:", error);
  }
};

const fetchSingleStoreDrinks = async (username: string) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/drinks/?username=${username}`
    );
    singleStoreDrinks.value = response.data;
  } catch (error) {
    console.error("Error fetching snack data:", error);
  }
};

const groupedOrders = ref([]);

const transformData = (data) => {
  const result = {};
  data.forEach((item) => {
    const schoolName = item.school__name;
    const className = item.school_class__name;
    const totalOrders = item.total_orders;

    if (!result[schoolName]) {
      result[schoolName] = [];
    }
    result[schoolName].push({ className, totalOrders });
  });
  return result;
};

const fetchGroupedOrders = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/api/grouped-orders/"
    );
    groupedOrders.value = transformData(response.data);
  } catch (error) {
    console.error("Error fetching grouped orders:", error);
  }
};

const isProductSpecificationSheetVisible = ref<boolean>(false);
const selectedItem = ref<any>(null);

const openProductSpecificationSheet = (item: any) => {
  selectedItem.value = item;
  isProductSpecificationSheetVisible.value = true;
};

const close = () => {
  isProductSpecificationSheetVisible.value = false;
};

onMounted(async () => {
  if (username) {
    fetchSingleStoreSnacks(username);
    fetchSingleStoreDrinks(username);
    fetchGroupedOrders();
  } else {
    console.error("Username is not available");
  }
});
</script>