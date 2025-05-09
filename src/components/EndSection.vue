<template>
  <section class="section">
    <h2 class="title">Wash Me Right</h2>
    <div class="fabric-care-grid">
      <!-- Fabric list -->
      <div class="fabric-list">
        <div
          v-for="(data, fabric) in fabricData"
          :key="fabric"
          class="fabric-button"
          :style="{
            backgroundColor:
              selectedFabric === fabric
                ? fabricColors[fabric]
                : fabricColors[fabric] + '88',
          }"
          @click="selectFabric(fabric)"
        >
          {{ fabric }}
        </div>
      </div>

      <!-- Care method buttons -->
      <div class="care-options">
        <div
          v-for="method in allMethods"
          :key="method"
          class="care-box"
          :style="getMethodStyle(method)"
        >
          {{ method }}
        </div>
      </div>
    </div>

    <!-- Note -->
    <div class="note-box" v-if="selectedFabric">
      <strong>Note:</strong> {{ fabricData[selectedFabric].note }}
    </div>
  </section>
</template>

<script>
export default {
  name: "FabricCareView",
  data() {
    return {
      selectedFabric: null,
      fabricData: {
        Cotton: {
          wash: ["Hot wash", "Warm wash", "Cold wash"],
          dry: ["Low heat dry", "Medium heat dry", "High heat dry"],
          note: "Shrinks in hot water; pre-shrink if needed",
        },
        Linen: {
          wash: ["Cold wash", "Hand wash"],
          dry: ["Air dry", "Low heat dry"],
          note: "Avoid high heat to prevent shrinking",
        },
        Wool: {
          wash: ["Cold wash", "Hand wash", "No wash"],
          dry: ["Air dry", "Low heat dry"],
          note: "Can felt/shrink in hot water; wool cycle preferred",
        },
        Silk: {
          wash: ["Cold wash", "Hand wash"],
          dry: ["Air dry"],
          note: "Use mesh bag; avoid direct sun",
        },
        Rayon: {
          wash: ["Cold wash", "Hand wash"],
          dry: ["Air dry"],
          note: "Fragile when wet; may shrink",
        },
        Nylon: {
          wash: ["Warm wash", "Cold wash"],
          dry: ["Low heat dry", "Air dry"],
          note: "Quick-drying; low heat preferred",
        },
        Polyester: {
          wash: ["Warm wash", "Cold wash"],
          dry: ["Low heat dry", "Medium heat dry"],
          note: "Wrinkle-resistant, durable",
        },
        Spandex: {
          wash: ["Cold wash", "Hand wash"],
          dry: ["Air dry", "Low heat dry"],
          note: "Avoid fabric softener; stretches easily",
        },
        Leather: {
          wash: ["No wash", "Spot clean"],
          dry: ["Air dry"],
          note: "Use leather cleaner only",
        },
        Suede: {
          wash: ["No wash", "Spot clean"],
          dry: ["Air dry"],
          note: "Brush gently; never submerge",
        },
      },
      fabricColors: {
        Cotton: "#b5ddf9",
        Linen: "#1f78b4",
        Wool: "#a0d996",
        Silk: "#33a12c",
        Rayon: "#ffc9c3",
        Nylon: "#f97391",
        Polyester: "#ffff9a",
        Spandex: "#febf70",
        Leather: "#ff7f01",
        Suede: "#cab2d6",
      },
    };
  },
  computed: {
    allMethods() {
      const methods = new Set();
      for (const fabric in this.fabricData) {
        this.fabricData[fabric].wash.forEach((m) => methods.add(m));
        this.fabricData[fabric].dry.forEach((m) => methods.add(m));
      }
      return Array.from(methods);
    },
  },
  methods: {
    selectFabric(fabric) {
      this.selectedFabric = fabric;
    },
    getMethodStyle(method) {
      const isUsed =
        this.selectedFabric &&
        (this.fabricData[this.selectedFabric].wash.includes(method) ||
          this.fabricData[this.selectedFabric].dry.includes(method));
      return {
        backgroundColor: isUsed
          ? this.fabricColors[this.selectedFabric]
          : "white",
        border: "1px solid #333",
      };
    },
  },
};
</script>

<style scoped>
.section {
  padding: 40px;
  background-color: white;
}

.title {
  margin-top: 10px; /* 원하는 높이만큼 조절 */
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

.fabric-care-grid {
  display: flex;
  gap: 60px;
  margin-top: 40px;
}

.fabric-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.fabric-button {
  width: 120px; /* 고정 너비 */
  height: 70px; /* 고정 높이 (정사각형) */
  padding: 0; /* 내부 여백 제거 */
  font-size: 20px;
  line-height: 1.3; /* 줄 간격 조절 */
  color: black;
  font-weight: 600;
  text-align: center; /* 가운데 정렬 */
  font-family: "brevia", sans-serif;
  cursor: pointer;
  border-radius: 8px;
  display: flex;
  align-items: center; /* 수직 가운데 정렬 */
  justify-content: center; /* 수평 가운데 정렬 */
  margin-left: -300px;
}

.care-options {
  display: grid;
  grid-template-columns: repeat(3, auto);
  gap: 40px;
  align-content: flex-start;
  margin-top: 40px;
}

.care-box {
  width: 150px;
  height: 120px; /* ✅ 정사각형 */
  display: flex; /* ✅ 텍스트 중앙 정렬 */
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: 500;
  font-family: "brevia", sans-serif;
  text-align: center;
  border-radius: 8px;
  cursor: default;
  transition: background-color 0.3s ease;
  padding: 10px; /* 🔄 적당한 내부 여백 유지 */
  box-sizing: border-box; /* ✅ padding 포함한 사이즈 유지 */
}

.note-box {
  margin-top: -90px;
  margin-left: 60px; /* ➡️ 오른쪽으로 살짝 이동 */
  background: white; /* 오타 수정: #white ❌ → white ✅ */
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-family: "brevia", sans-serif;
  max-width: 600px;
}
</style>
