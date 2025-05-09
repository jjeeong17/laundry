<template>
  <section class="section">
    <!-- 타이틀 분리 -->
    <div class="title-container">
      <h2 class="title">Weigh It Right</h2>
    </div>

    <!-- 콘텐츠 분리 -->
    <div class="content">
      <div class="load-selector">
        <!-- 왼쪽: 세탁 바구니 선택 -->
        <div class="baskets">
          <div
            v-for="load in loads"
            :key="load.label"
            class="basket"
            @mouseenter="selectedLoad = load"
            @mouseleave="selectedLoad = null"
          >
            <img :src="load.image" :alt="load.label" />
            <p>{{ load.label }} ({{ load.weight }} lbs)</p>
          </div>
        </div>

        <!-- 오른쪽: 의류 아이템 -->
        <div class="clothing-items">
          <div v-for="item in clothing" :key="item.name" class="clothing">
            <img :src="item.image" :alt="item.name" />
            <div
              class="bubble"
              v-if="
                selectedLoad &&
                selectedLoad.counts &&
                selectedLoad.counts[item.name] !== undefined
              "
            >
              {{ selectedLoad.counts[item.name] }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "WeighSection",
  data() {
    return {
      selectedLoad: null,
      loads: [
        {
          label: "Medium Load",
          weight: 6,
          image: require("@/assets/img/medium.svg"),
          counts: {
            Sock: 1,
            Under: 3,
            Short: 6,
            Long: 1,
            Skirt: 2,
            Jean: 3,
            Shirt: 1,
          },
        },
        {
          label: "Large Load",
          weight: 11,
          image: require("@/assets/img/large.svg"),
          counts: {
            Sock: 6,
            Under: 4,
            Short: 12,
            Long: 1,
            Skirt: 3,
            Jean: 5,
            Shirt: 1,
          },
        },
        {
          label: "Heavy Load",
          weight: 21,
          image: require("@/assets/img/heavy.svg"),
          counts: {
            Sock: 12,
            Under: 6,
            Short: 12,
            Long: 7,
            Skirt: 6,
            Jean: 6,
            Shirt: 8,
          },
        },
      ],
      clothing: [
        { name: "Sock", image: require("@/assets/img/sock.svg") },
        { name: "Under", image: require("@/assets/img/under.svg") },
        { name: "Short", image: require("@/assets/img/short.svg") },
        { name: "Long", image: require("@/assets/img/long.svg") },
        { name: "Skirt", image: require("@/assets/img/skirt.svg") },
        { name: "Jean", image: require("@/assets/img/jean.svg") },
        { name: "Shirt", image: require("@/assets/img/shirt.svg") },
      ],
    };
  },
};
</script>

<style scoped>
.section {
  height: 100vh;
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  padding-top: 40px;
}

.title-container {
  text-align: center;
  margin-bottom: 40px;
}

.title {
  font-size: 60px;
  font-family: "brevia", sans-serif;
  font-weight: 700;
  color: transparent;
  -webkit-text-stroke: 2px black;
  background: white;
  -webkit-background-clip: text;
  background-clip: text;
}

.content {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 100%;
  padding-left: 80px;
  margin-left: 900px;
  margin-top: 90px;
  margin-right: 30px;
}

.load-selector {
  display: flex;
  gap: 240px;
  justify-content: space-between;
  align-items: flex-start;
}

.baskets {
  display: flex;
  flex-direction: column;
  gap: 50px;
}

.basket img {
  width: 190px;
}

.basket p {
  font-family: "brevia", sans-serif;
  text-align: center;
}

.clothing-items {
  display: grid;
  grid-template-columns: repeat(3, 100px);
  grid-gap: 40px;
  position: relative;
  overflow: visible;
}

.clothing {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.clothing img {
  width: 150px;
  height: auto;
}

.bubble {
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%);
  background: white;
  border: 2px solid black;
  border-radius: 8px;
  padding: 4px 8px;
  font-size: 14px;
  font-weight: bold;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  z-index: 10;
}

.bubble::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-width: 6px;
  border-style: solid;
  border-color: white transparent transparent transparent;
}
</style>
