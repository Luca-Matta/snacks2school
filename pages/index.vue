<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>Nuxt Ionic</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Nuxt Ionic</ion-title>
        </ion-toolbar>
      </ion-header>
      <div id="container">
        <h1>Nuxt Ionic Module</h1>
        <ion-button router-link="/resources">Get Started</ion-button>
      </div>
    </ion-content>
  </ion-page>
</template>