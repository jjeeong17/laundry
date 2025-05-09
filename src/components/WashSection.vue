<template>
  <section class="section">
    <h2 class="title">Spin It Right</h2>

    <div class="dial-grid">
      <!-- Washer -->
      <div class="washer-wrapper">
        <img src="@/assets/washer.svg" class="washer-svg" />
        <div
          v-for="(info, label) in washerInfo"
          :key="label"
          class="dial-label"
          :style="washerLabelPositions[label]"
          @click="selectInfo(label, 'washer')"
        >
          {{ label }}
        </div>

        <div
          v-for="(info, label) in temperatureInfo"
          :key="label"
          class="dial-label"
          :style="temperatureLabelPositions[label]"
          @click="selectInfo(label, 'temp')"
        >
          {{ label }}
        </div>
      </div>

      <!-- Dryer -->
      <div class="dryer-wrapper">
        <img src="@/assets/dryer.svg" class="dryer-svg" />
        <div
          v-for="(info, label) in dryerInfo"
          :key="label"
          class="dial-label"
          :style="dryerLabelPositions[label]"
          @click="selectInfo(label, 'dryer')"
        >
          {{ label }}
        </div>
      </div>
    </div>

    <!-- Info Box -->
    <div class="info-box-wide" v-if="selected">
      <h3>{{ selected }}</h3>
      <p v-if="currentInfo.temp">
        <strong>{{ currentInfo.temp }}</strong>
      </p>
      <p>{{ currentInfo.desc }}</p>
    </div>
  </section>
</template>

<script>
export default {
  name: "WashSection",
  data() {
    return {
      selected: null,
      selectedCategory: null,
      washerInfo: {
        Normal: {
          temp: "Temperature: Warm",
          desc: "For everyday cottons/linens. Warm water, high spin for moderate soil.",
        },
        Colors: {
          temp: "Temperature: Cool",
          desc: "For darks & activewear. Cool water, high spin to protect color.",
        },
        Whites: {
          temp: "Temperature: Hot",
          desc: "Hot water & high spin for whites. Great with bleach for brightening.",
        },
        Delicates: {
          temp: "Temperature: Cool",
          desc: "Cold water, low spin. For silks, undergarments, delicate fabrics.",
        },
        "Bulky/Sheets": {
          temp: "Temperature: Warm",
          desc: "Extra water & low spin for comforters, rugs, jackets, blankets.",
        },
        "Heavy Duty": {
          temp: "Temperature: Hot",
          desc: "Hot water & high spin for towels, jeans, heavy soil.",
        },
        "Perm Press": {
          temp: "Temperature: Warm",
          desc: "Helps reduce wrinkles with spray rinse & slower spin.",
        },
        Wool: {
          temp: "Temperature: Cool",
          desc: "Gentle care for wool with cold water and low spin.",
        },
      },
      temperatureInfo: {
        Hot: {
          temp: "Temperature: 140°F",
          desc: "Deep clean for whites, towels, jeans. May cause shrinking.",
        },
        Warm: {
          temp: "Temperature: 105–120°F",
          desc: "Good for bright colors with moderate soil.",
        },
        Cool: {
          temp: "Temperature: 85–100°F",
          desc: "For colors and activewear. May blend warm water for soil.",
        },
        Cold: {
          temp: "Temperature: 85°F",
          desc: "Best for delicates and darks. Reduces shrinking and fading.",
        },
        "Tap Cold": {
          desc: "Uses home water temp. May auto-adjust if too cold.",
        },
      },
      dryerInfo: {
        "No Heat / Fluff": {
          temp: "Temperature: No heat",
          desc: "Air dry rubber/plastic items like bath mats.",
        },
        "Delicates / Less Dry": {
          temp: "Temperature: Extra Low",
          desc: "Gentle drying for light fabrics and athletic wear.",
        },
        "Normal / Regular": {
          temp: "Temperature: Medium",
          desc: "Auto-senses dryness. Good for everyday items.",
        },
        "More Dry / Very Dry": {
          temp: "Temperature: Medium",
          desc: "For thick items like towels and jeans.",
        },
        "Heavy Duty/Heavy Dry": {
          temp: "Temperature: Medium",
          desc: "Long & hot drying for bulky items like comforters.",
        },
        "Permanent Press": {
          temp: "Temperature: Low",
          desc: "Reduces wrinkles with cool-down. Ideal for synthetics.",
        },
        "Tumble Dry": {
          temp: "Temperature: Varies",
          desc: "General drying with various heat settings. Check care tag.",
        },
        "Steam Dry": {
          temp: "Temperature: Medium",
          desc: "Adds steam to reduce wrinkles. Great for freshening clothes.",
        },
      },
      washerLabelPositions: {
        Normal: { top: "26%", left: "16%" },
        "Heavy Duty": { top: "39.5%", left: "12%" },
        Colors: { top: "53%", left: "14%" },
        Whites: { top: "67%", left: "15.5%" },
        Delicates: { top: "26%", left: "55.5%" },
        Wool: { top: "39.5%", left: "55.5%" },
        "Perm Press": { top: "53%", left: "59%" },
        "Bulky/Sheets": { top: "67%", left: "58.5%" },
      },
      temperatureLabelPositions: {
        Hot: { top: "21.5%", left: "85.5%" },
        Warm: { top: "35.5%", left: "85.5%" },
        Cool: { top: "49%", left: "85.5%" },
        Cold: { top: "62.5%", left: "85.5%" },
        "Tap Cold": { top: "76%", left: "85.5%" },
      },
      dryerLabelPositions: {
        "No Heat / Fluff": { top: "28%", left: "22%" },
        "Delicates / Less Dry": { top: "41.5%", left: "16%" },
        "Normal / Regular": { top: "55%", left: "18%" },
        "More Dry / Very Dry": { top: "68.5%", left: "18%" },
        "Heavy Duty/Heavy Dry": { top: "28%", left: "83%" },
        "Permanent Press": { top: "41.5%", left: "82%" },
        "Tumble Dry": { top: "55%", left: "78%" },
        "Steam Dry": { top: "68.5%", left: "76%" },
      },
    };
  },
  computed: {
    currentInfo() {
      if (!this.selected) return {};
      if (this.selectedCategory === "washer")
        return this.washerInfo[this.selected];
      if (this.selectedCategory === "temp")
        return this.temperatureInfo[this.selected];
      if (this.selectedCategory === "dryer")
        return this.dryerInfo[this.selected];
      return {};
    },
  },
  methods: {
    selectInfo(label, category) {
      this.selected = label;
      this.selectedCategory = category;
    },
  },
};
</script>

<style scoped>
.section {
  scroll-snap-align: start;
  background-color: #fff;
  padding: 40px;
}

.title {
  margin-top: 30px;
  margin-bottom: 8px;
  font-size: 60px;
  font-family: "brevia", sans-serif;
  font-weight: 700;
  color: transparent;
  -webkit-text-stroke: 2px black;
  background: white;
  -webkit-background-clip: text;
  background-clip: text;
}

.dial-grid {
  display: flex;
  gap: 80px;
  justify-content: center;
  position: relative;
  flex-wrap: wrap;
  margin-top: 85px;
}

.washer-wrapper {
  position: relative;
  width: 830px;
}
.dryer-wrapper {
  position: relative;
  width: 690px;
}

.washer-svg,
.dryer-svg {
  width: 100%;
}

.dial-label {
  position: absolute;
  transform: translate(-50%, -50%);
  background: white;
  border: none;
  border-radius: 0;
  padding: 4px 6px;
  font-size: 18px;
  cursor: pointer;
  white-space: nowrap;
  transition: none;
  font-family: "brevia", sans-serif;
  box-shadow: none;
}

.dial-label:hover {
  background: #e3f5ff;
  border-color: #71b9f2;
}

.info-box-wide {
  margin-top: 80px;
  background: white;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 8px;
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  font-family: "brevia", sans-serif;
}
</style>
