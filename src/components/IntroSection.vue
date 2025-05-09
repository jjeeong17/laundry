<template>
  <section class="section">
    <div class="intro-content">
      <h1 class="main-title">
        <span class="text-mask">Ready to become a laundry master?</span>
        <div class="bubble-wrapper">
          <span v-for="i in 20" :key="i" class="bubble"></span>
        </div>
      </h1>
      <p class="subtitle">Let’s learn what those care labels really mean</p>
      <img src="@/assets/intro.svg" alt="Intro Image" class="intro-image" />
    </div>
  </section>
</template>

<script>
export default {
  name: "IntroSection",
};
</script>

<style>
.section {
  width: 100vw;
  height: 100vh;
  scroll-snap-align: start;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ffffff;
}

.intro-content {
  text-align: center;
  position: relative;
}

.main-title {
  position: relative;
  display: inline-block;
  font-size: 70px;
  font-family: "brevia", sans-serif;
  font-weight: 700;
  color: transparent;
  -webkit-text-stroke: 2px black;
  background: white;
  -webkit-background-clip: text;
  background-clip: text;
  overflow: hidden;
  height: 80px;
  margin-top: 90px;
}

.text-mask {
  position: relative;
  z-index: 2;
}

.bubble-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 1;
}

.bubble {
  position: absolute;
  border-radius: 50%;
  border: 2px solid #77d0e9;
  background-color: transparent;
  opacity: 0;
  animation: fall 3s linear infinite;
  animation-fill-mode: forwards;
  top: -30px;
}

.bubble:nth-child(1) {
  left: 5%;
  width: 24px;
  height: 24px;
  animation-delay: 0s;
}
.bubble:nth-child(2) {
  left: 12%;
  width: 30px;
  height: 30px;
  animation-delay: 0.2s;
}
.bubble:nth-child(3) {
  left: 20%;
  width: 28px;
  height: 28px;
  animation-delay: 0.4s;
}
.bubble:nth-child(4) {
  left: 28%;
  width: 26px;
  height: 26px;
  animation-delay: 0.6s;
}
.bubble:nth-child(5) {
  left: 35%;
  width: 32px;
  height: 32px;
  animation-delay: 0.8s;
}
.bubble:nth-child(6) {
  left: 42%;
  width: 20px;
  height: 20px;
  animation-delay: 1s;
}
.bubble:nth-child(7) {
  left: 50%;
  width: 36px;
  height: 36px;
  animation-delay: 1.2s;
}
.bubble:nth-child(8) {
  left: 57%;
  width: 24px;
  height: 24px;
  animation-delay: 1.4s;
}
.bubble:nth-child(9) {
  left: 64%;
  width: 30px;
  height: 30px;
  animation-delay: 1.6s;
}
.bubble:nth-child(10) {
  left: 71%;
  width: 22px;
  height: 22px;
  animation-delay: 1.8s;
}
.bubble:nth-child(11) {
  left: 78%;
  width: 28px;
  height: 28px;
  animation-delay: 2s;
}
.bubble:nth-child(12) {
  left: 85%;
  width: 34px;
  height: 34px;
  animation-delay: 2.2s;
}
.bubble:nth-child(13) {
  left: 92%;
  width: 25px;
  height: 25px;
  animation-delay: 2.4s;
}
.bubble:nth-child(14) {
  left: 3%;
  width: 27px;
  height: 27px;
  animation-delay: 2.6s;
}
.bubble:nth-child(15) {
  left: 17%;
  width: 29px;
  height: 29px;
  animation-delay: 2.8s;
}
.bubble:nth-child(16) {
  left: 31%;
  width: 33px;
  height: 33px;
  animation-delay: 3s;
}
.bubble:nth-child(17) {
  left: 46%;
  width: 30px;
  height: 30px;
  animation-delay: 3.2s;
}
.bubble:nth-child(18) {
  left: 61%;
  width: 24px;
  height: 24px;
  animation-delay: 3.4s;
}
.bubble:nth-child(19) {
  left: 75%;
  width: 26px;
  height: 26px;
  animation-delay: 3.6s;
}
.bubble:nth-child(20) {
  left: 88%;
  width: 35px;
  height: 35px;
  animation-delay: 3.8s;
}

/* 필요한 만큼 더 추가 가능 */

@keyframes fall {
  0% {
    transform: translateY(0) scale(1);
    opacity: 0.9;
  }
  70% {
    opacity: 0.9;
    transform: translateY(105px) scale(0.85); /* 150px의 70% */
  }
  100% {
    transform: translateY(150px) scale(0.8);
    opacity: 0;
  }
}

.subtitle {
  font-size: 20px;
  margin-bottom: 30px;
  font-family: "brevia", sans-serif;
  font-weight: 400;
  margin-top: -50px;
}

.intro-image {
  width: 500px;
  max-width: 80%;
  margin-top: 50px;
}
</style>
