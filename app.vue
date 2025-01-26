<template>
  <ion-app>
    <ion-router-outlet />
  </ion-app>
</template>

<style>
.shadow-btn {
  box-shadow: 0 20px 27px 10px rgba(0, 0, 0, 0.2);
}
.shadow-card {
  box-shadow: 0 20px 27px 10px rgba(0, 0, 0, 0.25);
}
.shadow-lightCard {
  box-shadow: 0 20px 27px 0 rgba(0, 0, 0, 0.15);
}

body {
  margin: 0;
  padding: 0;
  font-family: "Open Sans", sans-serif;
  color: #141727;
  background-color: #f8f9fa;
}

hr {
  border-top: none !important;
  height: 1px;
  opacity: 0.25;
  display: block;
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  margin-inline-start: auto;
  margin-inline-end: auto;
  unicode-bidi: isolate;
  overflow: hidden;
  background-color: transparent;
  background-image: linear-gradient(
    to right,
    rgba(0, 0, 0, 0),
    rgba(0, 0, 0, 0.4),
    rgba(0, 0, 0, 0)
  );
}

input:focus {
  background-color: #f5f5f5 !important;
  outline: none;
  border: 1px solid #ffa500 !important;
  outline: none;
  /* box-shadow: 0 0 0 1px #8C20F8; */
  box-shadow: 0 0 0 0.2rem rgba(226, 192, 43, 0.25) !important;
}

input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0px 1000px #f5f5f5 inset !important;
  border: 1.5px solid #ffa500 !important;
}

input:valid {
  border: 0.5px solid #ffa500;
  box-shadow: 0 0 0 1px #ffa500;
}

.btn {
  transition: all 0.5s ease;
  position: relative;
  overflow: hidden;
  font-weight: bold;
  z-index: 1;
}

.btn::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, #ff8c00, transparent);
  transition: left 1s;
  z-index: -1;
}

.btn:hover::before {
  left: 100%;
}

.hero {
  background: center / cover no-repeat;
  background-image: linear-gradient(
      180deg,
      rgba(0, 0, 0, 0.75) 0%,
      rgba(0, 0, 0, 0.25) 100%
    ),
    url(../../static/store-hero.png) !important;
}
</style>