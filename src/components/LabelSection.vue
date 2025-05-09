<template>
  <section class="section">
    <h2 class="title">Let’s Figure Out the Labels</h2>

    <div class="filter">
      <button
        v-for="cat in categories"
        :key="cat"
        :class="[
          'filter-button',
          cat.toLowerCase(),
          { active: selectedCategory === cat },
        ]"
        @click="selectedCategory = cat"
      >
        {{ cat }}
      </button>
    </div>

    <div class="grid">
      <div
        v-for="symbol in filteredSymbols"
        :key="symbol.file"
        class="icon"
        :class="symbol.category.toLowerCase()"
        :data-tooltip="symbol.label"
      >
        <img
          :src="require(`@/assets/label/${symbol.file}`)"
          :alt="symbol.label"
        />
      </div>
    </div>
  </section>
</template>

<script>
import symbolData from "@/assets/data/symbols.js";

export default {
  name: "LabelSection",
  data() {
    return {
      selectedCategory: "All",
      categories: [
        "All",
        "Washing",
        "Bleaching",
        "Ironing",
        "Drying",
        "Cleaning",
        "Etc",
      ],
      symbols: symbolData,
    };
  },
  computed: {
    filteredSymbols() {
      if (this.selectedCategory === "All") {
        return this.symbols;
      }
      return this.symbols.filter(
        (symbol) =>
          symbol.category.toLowerCase() === this.selectedCategory.toLowerCase()
      );
    },
  },
};
</script>

<style>
.section {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 30px 40px 40px 40px;
  box-sizing: border-box;
  scroll-snap-align: start;
  overflow: hidden;
}

.title {
  margin-top: 20px; /* 원하는 높이만큼 조절 */
  margin-bottom: 8px;
  font-size: 55px;
  text-align: center;
  font-family: "brevia", sans-serif;
  font-weight: 700;
  color: transparent;
  -webkit-text-stroke: 2px black;
  background: white;
  -webkit-background-clip: text;
  background-clip: text;
}

.filter {
  margin-bottom: 10px; /* 💡 필터와 그 아래 grid 사이 간격 */
}

.grid {
  flex: 1;
  overflow-y: auto;
  padding-right: 10px;
  display: flex;
  flex-wrap: wrap;
  gap: 30px 40px;
}

.filter {
  margin-bottom: 20px;
}

.filter-button {
  margin-right: 25px;
  margin-top: 20px;
  margin-bottom: 20px;
  padding: 8px 14px;
  border: none;
  border-radius: 6px;
  background: #ededed;
  cursor: pointer;
  transition: 0.2s;
  font-weight: bold;
  font-size: 18px; /* ✨ 텍스트 크게! */
  font-family: "brevia", sans-serif; /* ✨ 글꼴도 적용 */
}

.filter-button.active {
  color: #000;
}

/* 선택된 버튼 색상 */
.filter-button.active.all {
  background: #333;
  color: #fff;
}
.filter-button.active.washing {
  background: #faedcb;
}
.filter-button.active.bleaching {
  background: #c9e4df;
}
.filter-button.active.ironing {
  background: #c5def2;
}
.filter-button.active.drying {
  background: #dacdf0;
}
.filter-button.active.cleaning {
  background: #f2c6df;
}
.filter-button.active.etc {
  background: #f8d9c3;
}

.grid {
  display: flex;
  flex-wrap: wrap;
  gap: 40px 50px; /* 세로 40px, 가로 50px */
  justify-items: center; /* 개별 아이콘을 셀 안에서 가운데 정렬 */
  grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
  margin-left: 60px;
}

.icon {
  position: relative;
  width: 80px;
  height: 90px;
  border: 8px solid #ededed; /* 테두리 더 두껍게 */
  border-radius: 10px;
  transition: border-color 0.3s;
}

.icon img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

/* 설명 tooltip */
.icon::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: -40px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.75);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
  font-size: 15px; /* ✨ tooltip 글자 크기 */
  font-family: "brevia", sans-serif; /* ✨ 글꼴도 적용 */
}

.icon:hover::after {
  opacity: 1;
}

/* ✨ hover 시 category별 테두리 색상 */
.icon.washing:hover {
  border-color: #faedcb;
}
.icon.bleaching:hover {
  border-color: #c9e4df;
}
.icon.ironing:hover {
  border-color: #c5def2;
}
.icon.drying:hover {
  border-color: #dacdf0;
}
.icon.cleaning:hover {
  border-color: #f2c6df;
}
.icon.etc:hover {
  border-color: #f8d9c3;
}
</style>
