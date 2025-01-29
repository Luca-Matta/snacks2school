<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div>
        <Navbar />
        <div>
          <div class="flex justify-center items-center mx-auto mt-12 gap-6">
            <div
              class="text-4xl md:text-6xl xl:text-8xl xl:text-9xl text-center font-bold mb-4"
            >
              <div>La <span class="text-[#ffa500]"> merenda</span> a</div>
              <div class="flex justify-center items-center gap-2 md:gap-6">
                <div class="flex items-center gap-2 md:gap-6">
                  portata
                  <img
                    src="../assets/icons/desk.png"
                    alt="Desk"
                    class="h-10 md:h-36 w-10 md:w-36 cursor-pointer"
                  />
                  <span class="text-[#a688f9]">di </span
                  ><span class="text-[#bf09bd]">clic</span>
                </div>
              </div>
            </div>
          </div>

          <div
            class="mx-auto text-center font-bold text-sm md:text-lg !px-4 -mt-2 md:mt-4 mb-4"
          >
            Tu ordini. Noi la consegniamo a scuola.
          </div>

          <div class="flex !justify-center !items-center !mx-auto mt-12">
            <div class="swiper-wrapper__inner">
              <ClientOnly>
                <swiper-container
                  class="swiper-cards"
                  :width="240"
                  :slides-per-view="1"
                  :loop="true"
                  effect="cards"
                  :autoplay="{
                    delay: 1000,
                    disableOnInteraction: true,
                  }"
                >
                  <swiper-slide
                    v-for="slide in sellingPoints"
                    :key="`slide-card-${slide.id}`"
                    :class="slide.class"
                  >
                    <div
                      class="swiper-slide-content flex flex-col justify-center items-center"
                    >
                      <img
                        :src="slide.imgSrc"
                        :alt="slide.imgAlt"
                        class="h-9 w-9 mb-2"
                      />
                      <div class="font-bold text-center text-sm">
                        {{ slide.title }}
                      </div>
                      <div class="flex flex-col justify-center items-center">
                        <p
                          class="text-xs"
                          v-for="(text, index) in slide.texts"
                          :key="index"
                        >
                          {{ text }}
                        </p>
                      </div>
                    </div>
                  </swiper-slide>
                </swiper-container>
              </ClientOnly>
            </div>
          </div>

          <div
            class="mx-auto text-center font-bold text-xs md:text-sm opacity-60 !px-4 -mt-2 md:mt-0 mb-6"
          >
            Leggere le card può nuocere gravemente<br />
            al numero di merende che ordini.
          </div>

          <div
            v-if="
              isAuthenticated &&
              currentUser?.value &&
              currentUser.value.is_store
            "
            class="max-w-screen-xl mx-auto flex flex-col justify-center items-center !py-10 md:py-16 mt-4 md:mt-12 !px-4 gap-6 md:gap-10"
          >
            <div
              class="text-2xl md:text-6xl xl:text-8xl text-center font-bold mb-2 md:mb-0"
            >
              <div class="flex justify-center items-center gap-2 md:gap-7">
                <img
                  src="../assets/icons/list.png"
                  alt="Trust"
                  class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
                />
                Vai al <span class="text-[#ffa500]">gestionale</span> e
              </div>
              <div>
                <div class="flex justify-center items-center gap-2 md:gap-7">
                  <div>
                    scopri i <span class="text-[#bf09bd]">nuovi </span>
                    <span class="text-[#a688f9]">ordini </span>
                    <!-- <img
                src="../assets/icons/wheat-sack.png"
                alt="Wheatsack"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer align-middle ml-2 md:ml-7"
              /> -->
                  </div>
                </div>
              </div>
            </div>

            <div
              class="mx-auto text-center font-bold text-xs md:text-sm opacity-60 !px-4 underline"
            >
              <router-link to="/orders">Fai clic qui.</router-link>
            </div>
          </div>

          <hr />

          <div
            class="max-w-screen-xl mx-auto flex flex-col justify-center items-center !px-4 mb-4 md:mb-0 !py-4 md:py-16 mt-6 gap-6 md:gap-10"
          >
            <div
              class="text-2xl md:text-6xl xl:text-8xl text-center font-bold mb-2"
            >
              Rendiamo più
              <span class="text-[#a688f9]">semplice</span><br />
              il <span class="text-[#ffa500]">mestiere</span> più
              <span class="text-[#bf09bd]">difficile:</span><br />
              il
              <span class="text-[#af4135]">genitore</span>
            </div>
            <div
              class="max-w-screen-xl mx-auto flex justify-center items-center !px-4 gap-2"
            >
              <img
                src="../assets/icons/boy_3.png"
                alt="Tomato"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer inline-block align-middle ml-2 md:ml-7"
              />
              <!-- <img
            src="../assets/icons/boy_3.png"
            alt="Tomato"
            class="h-10 md:h-24 w-10 md:w-24 cursor-pointer inline-block align-middle ml-2 md:ml-7"
          /> -->
              <img
                src="../assets/icons/school_bag.png"
                alt="Lettuce"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer inline-block align-middle ml-2 md:ml-7"
              />
              <!-- <img
            src="../assets/icons/girl_2.png"
            alt="Oil"
            class="h-10 md:h-24 w-10 md:w-24 cursor-pointer inline-block align-middle ml-2 md:ml-7"
          /> -->
              <img
                src="../assets/icons/girl.png"
                alt="Oil"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer inline-block align-middle ml-2 md:ml-7"
              />
            </div>

            <div
              class="mx-auto text-center font-bold text-xs md:text-sm opacity-60 !px-4"
            >
              Gestisci la merenda e il pranzo<br />
              di tutti i tuoi figli in un unico account.
              <span v-if="isAuthenticated">
                Vai sul tuo
                <router-link
                  to="/profile"
                  class="!text-black font-bold underline"
                  >profilo</router-link
                >
                per aggiungere i tuoi figli.
              </span>
            </div>
          </div>

          <hr />

          <div
            class="max-w-screen-xl mx-auto flex flex-col justify-center items-center !py-6 !pt-10 !pb-12 md:py-16 !px-4 gap-2 md:gap-12"
          >
            <div
              class="text-2xl md:text-6xl xl:text-8xl text-center font-bold mb-4"
            >
              <div>
                La <span class="text-[#af4135]">merenda</span> che
                <span class="text-[#bf09bd]">cambia</span>,
              </div>
              <div class="flex justify-center items-center gap-2 md:gap-6">
                <div>come <span class="text-[#a688f9]">tuo figlio</span></div>
                <img
                  src="../assets/icons/boy.png"
                  alt="Boy"
                  class="h-10 md:h-20 w-10 md:w-20 cursor-pointer"
                />
              </div>

              <div class="flex justify-center items-center gap-2 md:gap-6">
                <img
                  src="../assets/icons/calendar.png"
                  alt="Calendar"
                  class="h-10 md:h-20 w-10 md:w-20 cursor-pointer"
                />
                <div class="text-[#ffa500]">#snackscalendar</div>
              </div>
            </div>
            <div>
              <Calendar />
            </div>
          </div>

          <hr />

          <div class="pt-2 md:pt-6 pb-10 md:pb-16">
            <div
              class="max-w-screen-xl mx-auto flex flex-col justify-center items-center mt-4 md:mt-12 !px-4 gap-6 md:gap-10"
            >
              <div
                class="text-2xl md:text-6xl xl:text-8xl text-center font-bold mb-2 md:mb-0"
              >
                <div class="flex justify-center items-center gap-2 md:gap-7">
                  <img
                    src="../assets/icons/quality.png"
                    alt="Trust"
                    class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
                  />
                  Ogni <span class="text-[#af4135]">morso</span> è
                </div>
                <div>
                  <div class="flex justify-center items-center gap-2 md:gap-7">
                    <div>
                      <span class="text-[#bf09bd]">gustosissimo,</span>
                      come le nostre
                      <span class="text-[#a688f9]">materie prime</span>
                      <!-- <img
                src="../assets/icons/wheat-sack.png"
                alt="Wheatsack"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer align-middle ml-2 md:ml-7"
              /> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="flex !justify-center !items-center !mx-auto !py-6 mb-6">
              <div class="swiper-wrapper__inner">
                <ClientOnly>
                  <swiper-container
                    v-if="featuredSnacks.length > 0"
                    class="swiper-cards"
                    :width="240"
                    :slides-per-view="1"
                    :loop="true"
                    effect="cards"
                    :autoplay="{
                      delay: 1000,
                      disableOnInteraction: true,
                    }"
                  >
                    <swiper-slide
                      v-for="(snack, index) in featuredSnacks"
                      :key="`slide-snack-card-${snack.id}`"
                      :class="[
                        'flex flex-col justify-center items-center !h-40 !w-60 !rounded-xl p-4 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-1 outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-1',
                        index % 2 === 0
                          ? 'bg-[#ffa500] outline-[#ffa500]'
                          : 'bg-[#a688f9] outline-[#a688f9]',
                      ]"
                      @click="openProductSpecificationSheet(snack)"
                    >
                      <div
                        class="swiper-slide-content flex flex-col justify-center items-center"
                      >
                        <img :src="snack.image" class="h-9 w-9 mb-2" />
                        <div class="font-bold text-center text-sm">
                          {{ snack.name }}
                        </div>
                        <div class="flex flex-col justify-center items-center">
                          <p class="text-xs">
                            {{ snack.gross_price }}
                          </p>
                        </div>
                      </div>
                    </swiper-slide>
                  </swiper-container>
                </ClientOnly>
              </div>
            </div>

            <template>
              <div class="-mt-14 md:mt-6 mb-4">
                <div class="mx-auto">
                  <swiper
                    :slidesPerView="'auto'"
                    :spaceBetween="isMobile ? 0 : 20"
                    :slidesOffsetBefore="isMobile ? 80 : 22.5"
                    :slidesOffsetAfter="0"
                    :centeredSlidesBounds="true"
                    :centeredSlides="false"
                    :pagination="false"
                    :navigation="false"
                    :speed="500"
                    class="!h-[350px] !pb-6"
                  >
                    <swiper-slide
                      v-for="(snack, index) in featuredSnacks"
                      :key="index"
                      class="!h-40 md:!h-60 !w-40 md:!w-60 my-auto mx-5"
                    >
                      <div
                        :class="[
                          'flex flex-col justify-center items-center gap-2 shadow-card hover:shadow-none transition-all duration-500 !rounded-xl h-full w-full p-2 md:p-6 cursor-pointer outline outline-1 outline-offset-4 bg-white outline-[#a688f9]',
                          // index % 2 === 0
                          //   ? 'bg-white outline-[#af4135]'
                          //   : 'bg-[#af4135] outline-[#af4135]',
                        ]"
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
                          <div
                            class="flex flex-col items-center justify-center"
                          >
                            <p
                              class="font-bold text-center text-xs md:text-sm mt-1 md:mt-2"
                            >
                              {{ snack.name }}
                            </p>
                            <!-- <div
                          class="text-xs text-center font-bold !py-1 md:py-2 underline"
                        >
                          Consulta la scheda tecnica
                        </div> -->
                            <p class="text-xs mt-2">{{ snack.gross_price }}€</p>
                          </div>
                          <p class="text-xs opacity-80"></p>
                        </div>
                      </div>
                    </swiper-slide>
                  </swiper>
                </div>
              </div>
            </template>

            <div
              class="mx-auto text-center font-bold text-xs md:text-sm opacity-60 !px-4 -mt-16 md:mt-0"
            >
              Fai clic su un prodotto per consultarne la scheda tecnica:
              proprietà organolettiche e funzionali, ingredienti e allergeni.
            </div>
          </div>

          <ProductSpecificationSheet
            :isProductSpecificationSheetVisible="
              isProductSpecificationSheetVisible
            "
            :selectedItem="selectedItem"
            @openProductSpecificationSheet="openProductSpecificationSheet"
            @close="close"
          />

          <hr />

          <div class="pt-10 md:pt-16 pb-0 md:pb-10">
            <div
              class="max-w-screen-xl mx-auto flex flex-col justify-center items-center mt-2 md:mt-0 !px-4 gap-12 mb-5 md:mb-0"
            >
              <div
                v-if="!isAuthenticated"
                class="text-2xl md:text-6xl xl:text-8xl text-center font-bold mb-2 md:mb-0"
              >
                <div class="flex justify-center items-center gap-2 md:gap-7">
                  <img
                    src="../assets/icons/trust.png"
                    alt="Trust"
                    class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
                  />
                  I nostri <span class="text-[#af4135]">store</span>
                </div>
                <div>
                  <div class="flex justify-center items-center gap-2 md:gap-7">
                    di <span class="text-[#bf09bd]">fiducia</span>
                    <img
                      src="../assets/icons/location.png"
                      alt="Location"
                      class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
                    />
                  </div>
                </div>
              </div>

              <div
                v-if="isAuthenticated"
                class="max-w-screen-xl mx-auto flex flex-col justify-center items-center !px-4 mb-4 md:mb-0"
              >
                <div
                  class="text-2xl md:text-6xl xl:text-8xl text-center font-bold mb-2"
                >
                  <div class="flex justify-center items-center gap-2 md:gap-7">
                    <img
                      src="../assets/icons/trust.png"
                      alt="Trust"
                      class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
                    />
                    <span class="text-[#af4135]">Store</span> che
                    <span class="text-[#ffa500]">consegnano</span>
                  </div>
                  <div>
                    <div
                      class="flex justify-center items-center gap-2 md:gap-7"
                    >
                      nella <span class="text-[#bf09bd]">provincia</span> di
                      <span class="text-[#a688f9]">{{
                        currentUser?.location?.name
                      }}</span>
                      <img
                        src="../assets/icons/location.png"
                        alt="Location"
                        class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="flex !justify-center !items-center !mx-auto !py-4">
              <div class="swiper-wrapper__inner">
                <ClientOnly>
                  <swiper-container
                    v-if="stores.length > 0"
                    class="swiper-cards"
                    :width="240"
                    :slides-per-view="1"
                    :loop="true"
                    effect="cards"
                  >
                    <swiper-slide
                      v-for="store in stores"
                      :key="`slide-card-${store.id}`"
                      class="flex flex-col justify-center items-center !h-40 !w-40 !rounded-xl p-4 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-1 outline-offset-4 outline-[#af4135] cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-1 bg-[#ffffff]"
                    >
                      <div
                        class="swiper-slide-content flex flex-col justify-center items-center"
                      >
                        <img
                          :src="store.profile_picture"
                          class="bg-center bg-contain bg-no-repeat h-24 w-24"
                        />
                        <div
                          class="flex flex-col justify-center items-center mt-2"
                        >
                          <div
                            class="flex items-center justify-center gap-1.5 text-sm"
                          >
                            <p class="font-bold">
                              {{ store.first_name }} {{ store.last_name }}
                            </p>
                            <div
                              class="h-4 w-4 bg-[#ffa500] rounded-full font-bold flex justify-center items-center"
                            >
                              √
                            </div>
                          </div>
                        </div>
                      </div>
                    </swiper-slide>
                  </swiper-container>
                </ClientOnly>
              </div>
            </div>
          </div>

          <hr />

          <div
            class="max-w-screen-xl mx-auto flex flex-col justify-center items-center !py-2 md:py-16 !px-4 my-8"
          >
            <div
              class="text-2xl md:text-6xl xl:text-8xl text-center font-bold mb-2"
            >
              <div class="flex justify-center items-center gap-2 md:gap-7">
                <img
                  src="../assets/icons/referrer.png"
                  alt="Trust"
                  class="h-12 md:h-28 w-12 md:w-28 cursor-pointer"
                />
                Chi <span class="text-[#af4135]">trova</span> un
              </div>
              <div>
                <div class="flex justify-center items-center gap-2 md:gap-7">
                  <div>
                    <span class="text-[#bf09bd]">amico</span>
                    trova un
                    <span class="text-[#a688f9]">tesoro</span>
                    <!-- <img
                src="../assets/icons/wheat-sack.png"
                alt="Wheatsack"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer align-middle ml-2 md:ml-7"
              /> -->
                  </div>
                </div>
              </div>
            </div>

            <div class="flex justify-center mb-2">
              <button
                class="btn bg-[#bf09bd] w-full text-white font-bold uppercase text-xs shadow-button my-4 mb-4 !py-3 !px-6 !rounded-lg outline outline-1 outline-[#bf09bd] outline-offset-4 shadow-lightCard hover:shadow-none transition-all duration-500"
                @click="openReferralExplenation"
              >
                Scopri di più
              </button>
            </div>

            <div
              class="mx-auto text-center font-bold text-xs md:text-sm opacity-60 !px-4"
            >
              Se porti un amico su Snacks2School, riceverai un credito non
              appena lui ricaricherà il suo portafoglio di credito.<br />
              Il numero di amici che puoi portare è illimitato!
            </div>
          </div>

          <ReferralExplenation
            :isReferralExplenationVisible="isReferralExplenationVisible"
            v-if="isReferralExplenationVisible"
            @close="closeReferralExplenation"
          />

          <hr />

          <div
            class="max-w-screen-xl mx-auto flex flex-col justify-center items-center pb-10 md:pb-16 mt-10 md:mt-12 !px-4 gap-6 md:gap-10"
          >
            <div class="text-2xl md:text-6xl xl:text-8xl text-center font-bold">
              <div class="flex justify-center items-center gap-2 md:gap-7">
                <img
                  src="../assets/icons/solution.png"
                  alt="Trust"
                  class="h-10 md:h-24 w-10 md:w-24 cursor-pointer"
                />
                Qualcosa non va?
              </div>
              <div>
                <div class="flex justify-center items-center gap-2 md:gap-7">
                  <div>
                    <span class="text-[#ffa500]">Niente paura!</span>
                    Il nostro
                    <span class="text-[#bf09bd]">customer care</span> è
                    <span class="text-[#a688f9]">sartoriale</span>
                    <!-- <img
                src="../assets/icons/wheat-sack.png"
                alt="Wheatsack"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer align-middle ml-2 md:ml-7"
              /> -->
                  </div>
                </div>
              </div>
            </div>

            <div
              class="max-w-screen-xl mx-auto flex justify-center items-center !px-4 gap-2"
            >
              <img
                src="../assets/icons/headset.png"
                alt="Headset"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer align-middle ml-2 md:ml-7"
              />
              <img
                src="../assets/icons/friendship.png"
                alt="Friendship"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer inline-block align-middle ml-2 md:ml-7"
              />
              <img
                src="../assets/icons/hands.png"
                alt="Hands"
                class="h-10 md:h-24 w-10 md:w-24 cursor-pointer inline-block align-middle ml-2 md:ml-7"
              />
            </div>

            <div class="mx-auto text-center font-bold text-xs md:text-sm !px-4">
              <span class="opacity-60"> Siamo qui per supportarti - </span>
              <a
                href="mailto:snacks2school@gmail.com"
                class="!text-[#a688f9] underline"
              >
                snacks2school@gmail.com
              </a>
            </div>
          </div>

          <Footer />
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { checkAuthStatus, getCurrentUserData } from "../utils/auth";
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/swiper-bundle.css";
import { useNuxtApp } from "#app";
import Navbar from "~/components/Navbar.vue";
import Footer from "~/components/Footer.vue";
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/vue";
import { useSwiper } from "#imports";

const { $device } = useNuxtApp();
const isMobile = ref<boolean>($device.isMobile);

interface Store {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  location: string;
  address: string;
  profile_picture: string;
  bio: string;
}

const isAuthenticated = ref<boolean>(false);
const currentUser = ref<any>(null);

const stores = ref<Store[]>([]);

import healthIcon from "@/assets/icons/health.png";
import comfortIcon from "@/assets/icons/sleeping-mask.png";
import calendarIcon from "@/assets/icons/calendar.png";
import qualityIcon from "@/assets/icons/quality.png";
import safetyIcon from "@/assets/icons/credit-card.png";

const sellingPoints = [
  {
    class:
      "flex flex-col justify-center items-center bg-[#ffa500] !h-40 !w-60 !rounded-xl p-4 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-1 outline-[#ffa500] outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-1",
    imgSrc: healthIcon,
    imgAlt: "Health",
    imgClass: "h-8 w-8",
    title: "Salute e tutela",
    texts: ["Trasparenza sugli ingredienti.", "Allergeni sempre in evidenza."],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-[#a688f9] !h-40 !w-60 !rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-1 outline-[#a688f9] outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-1",
    imgSrc: qualityIcon,
    imgAlt: "Comfort",
    imgClass: "h-7 w-7",
    title: "Gustosissimo",
    texts: [
      "Materie prime di qualità elevatissima. Ogni morso è gustosissimo.",
    ],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-[#ffa500] !h-40 !w-60 !rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-1 outline-[#ffa500] outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-1",
    imgSrc: calendarIcon,
    imgAlt: "Calendar",
    imgClass: "h-7 w-7",
    title: "Snacks Calendar",
    texts: [
      "Ogni giorno uno snack diverso. Una dieta varia e sana è fondamentale per la salute di tuo figlio.",
    ],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-[#a688f9] !h-40 !w-60 !rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-1 outline-[#a688f9] outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-1",
    imgSrc: comfortIcon,
    imgAlt: "Cash",
    imgClass: "h-9 w-9",
    title: "Comodità",
    texts: [
      "Di' addio alle mattinate frenetiche. Ordina comodamente dal tuo divano.",
    ],
  },
  {
    class:
      "flex flex-col justify-center items-center bg-[#ffa500] !h-40 !w-60 !rounded-xl p-4 lg:p-8 text-center cursor-pointer shadow-card transition-all duration-500 outline outline-1 outline-[#ffa500] outline-offset-4 cursor-pointer shadow-card hover:shadow-none transition-all duration-500 gap-1",
    imgSrc: safetyIcon,
    imgAlt: "Safety",
    imgClass: "h-7 w-7",
    title: "Risparmio",
    texts: [
      "Prezzi più bassi rispetto al dettaglio e alle merende industriali.",
    ],
  },
];

const getCsrfToken = async () => {
  const response = await axios.get("http://localhost:8000/api/csrf-token/", {
    withCredentials: true,
  });
  return response.data.csrfToken;
};

const stripe = ref(null);

const getStripePubKey = async () => {
  const response = await axios.get(
    "http://localhost:8000/api/v1/stripe/stripe-pub-key/"
  );

  const stripePubKey = response.data.publicKey;
  return stripePubKey;
};

import axiosInstance from "../utils/axiosInstance";
import ReferralExplenation from "~/components/ReferralExplenation.vue";

const chargeCreditWallet = async () => {
  try {
    const csrfToken = await axiosInstance.get("csrf-token/");
    const response = await axiosInstance.post(
      "v1/stripe/create-checkout-session/",
      {},
      {
        headers: {
          "X-CSRFToken": csrfToken.data.csrfToken,
        },
        withCredentials: true,
      }
    );
    return stripe.value.redirectToCheckout({
      sessionId: response.data.sessionId,
    });
  } catch (error) {
    console.error("Error creating checkout session:", error);
  }
};

const router = useRouter();

const navigateToStore = (store: Store) => {
  router.push({
    name: "stores-username",
    params: { username: store.username },
    state: {
      id: store.id,
      first_name: store.first_name,
      last_name: store.last_name,
      profile_picture: store.profile_picture,
      location: store.location,
      address: store.address,
      bio: store.bio,
    },
  });
};

const groupedOrders = ref([]);

const isReferralExplenationVisible = ref(false);

const openReferralExplenation = () => {
  isReferralExplenationVisible.value = true;
};

const closeReferralExplenation = () => {
  isReferralExplenationVisible.value = false;
};

const featuredSnacks = ref([]);

const isProductSpecificationSheetVisible = ref<boolean>(false);
const selectedItem = ref<any>(null);

const openProductSpecificationSheet = (item: any) => {
  selectedItem.value = item;
  isProductSpecificationSheetVisible.value = true;
};

const close = () => {
  isProductSpecificationSheetVisible.value = false;
};

watch(isProductSpecificationSheetVisible, (newValue) => {
  if (newValue) {
    document.body.style.overflow = "hidden";
  } else {
    document.body.style.overflow = "";
  }
});

onMounted(async () => {
  isAuthenticated.value = await checkAuthStatus();
  currentUser.value = await getCurrentUserData();

  featuredSnacks.value = (
    await axios.get("http://localhost:8000/api/featured-snacks/")
  ).data;

  stores.value = (await axios.get("http://localhost:8000/api/stores/")).data;

  const stripePubKey = await getStripePubKey();
  stripe.value = Stripe(stripePubKey);

  // try {
  //   const response = await axios.get("http://localhost:8000/api/stores/");
  //   stores.value = response.data;
  // } catch (error) {
  //   console.error("Error fetching user data:", error);
  // }
});
</script>

<style>
swiper-slide {
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-wrapper {
  display: flex;
  flex-direction: column;
}

.swiper-wrapper h2 {
  font-size: 1.5rem;
  font-weight: bold;
  margin-top: 0;
  margin-bottom: 1rem;
}

/* .swiper-wrapper__inner {
  border: 1px solid #eaeaea;
  background-color: #f5f5f5;
  padding: 1rem;
  border-radius: 8px;
} */

.swiper-cards {
  width: 240px;
  height: 240px;
}
.swiper-cards swiper-slide {
  border-radius: 6px;
}
</style>