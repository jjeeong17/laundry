<template>
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">Laundry Symbols by Clothing Type</h2>
    </div>
    <div class="symbol-groups">
      <div
        v-for="(groupSymbols, groupName) in groupedSymbols"
        :key="groupName"
        class="group-bubble"
      >
        <h3 class="group-title">{{ groupName }}</h3>
        <div class="symbol-bubble">
          <div
            v-for="symbol in groupSymbols"
            :key="symbol.file"
            :class="['circle-icon', getCategoryClass(groupName)]"
            v-intersect="'enter-bounce'"
          >
            <img
              :src="require(`@/assets/label/${symbol.file}`)"
              :alt="symbol.label"
            />
            <span class="tooltip">{{ symbol.label }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import symbolData from "@/assets/data/symbols_with_groups.json";

export default {
  name: "GroupBubbleView",
  computed: {
    groupedSymbols() {
      const grouped = {};
      for (const symbol of symbolData) {
        if (!Array.isArray(symbol.group)) continue;
        for (const g of symbol.group) {
          if (!grouped[g]) grouped[g] = [];
          grouped[g].push(symbol);
        }
      }
      return grouped;
    },
  },
  methods: {
    getCategoryClass(groupName) {
      const map = {
        "T-Shirts / Sweatshirts": "border-pink",
        "Underwear / Socks": "border-orange",
        "Sweaters / Knitwear": "border-blue",
        "Jeans / Pants": "border-green",
        "Dress Shirts / Blouses": "border-purple",
        "Activewear / Sportswear": "border-yellow",
        "Jackets / Coats": "border-lightyellow",
      };
      return map[groupName] || "border-default";
    },
  },
  directives: {
    intersect: {
      mounted(el, binding) {
        const observer = new IntersectionObserver(
          ([entry]) => {
            if (entry.isIntersecting) {
              el.classList.add(binding.value);
              observer.unobserve(el);
            }
          },
          { threshold: 0.2 }
        );
        observer.observe(el);
      },
    },
  },
};
</script>

<style scoped>
.section {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 170px 40px 40px;
  background-color: white;
  overflow: visible;
}

/* 타이틀만 따로 분리 */
.section-header {
  margin-bottom: 40px;
}

.section-title {
  font-size: 55px;
  text-align: center;
  font-family: "brevia", sans-serif;
  font-weight: 700;
  color: transparent;
  -webkit-text-stroke: 2px black;
  background: white;
  -webkit-background-clip: text;
  background-clip: text;
  margin-top: -90px;
}

.symbol-groups {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  justify-content: center;
  overflow: visible;
}

.group-bubble {
  background: #fff;
  border: 4px solid #ccc;
  border-radius: 50%;
  padding: 20px;
  width: 300px;
  height: 300px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: visible;
}

.group-title {
  position: absolute;
  top: -30px;
  font-size: 20px;
  font-family: "brevia", sans-serif;
  font-weight: 700;
}

.symbol-bubble {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  align-items: center;
  overflow: visible;
}

.circle-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 2px solid #ccc;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  position: relative;
  z-index: 1;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  opacity: 0;
}

.circle-icon:hover {
  transform: scale(1.1) translateY(-3px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.circle-icon img {
  width: 80%;
  height: 80%;
  object-fit: contain;
}

.tooltip {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 8px;
  background: rgba(0, 0, 0, 0.85);
  color: white;
  padding: 6px 10px;
  border-radius: 4px;
  font-size: 12px;
  white-space: normal;
  max-width: 200px;
  text-align: center;
  z-index: 9999;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
}

.circle-icon:hover .tooltip {
  opacity: 1;
}

.enter-bounce {
  animation: dropIn 0.6s ease-out forwards;
}

@keyframes dropIn {
  0% {
    transform: translateY(-60px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Border color overrides */
.border-pink {
  border-color: #f8b2bc !important;
}
.border-orange {
  border-color: #fcb49a !important;
}
.border-blue {
  border-color: #a6c6e9 !important;
}
.border-purple {
  border-color: #b3b4d9 !important;
}
.border-green {
  border-color: #9dc8b9 !important;
}
.border-default {
  border-color: #ccc !important;
}
.border-yellow {
  border-color: #e6eda0 !important;
}
.border-lightyellow {
  border-color: #fae1a7 !important;
}
</style>
