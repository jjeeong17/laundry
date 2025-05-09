<template>
  <div class="dot-nav">
    <div
      v-for="(section, index) in sections"
      :key="index"
      :class="['dot', { active: section === currentSection }]"
      @click="scrollTo(section)"
    ></div>
  </div>
</template>

<script>
export default {
  props: ["currentSection"],
  data() {
    return {
      sections: ["intro", "label", "need", "upload", "weigh", "wash", "end"],
    };
  },
  methods: {
    scrollTo(sectionId) {
      const el = document.getElementById(sectionId);
      if (el) el.scrollIntoView({ behavior: "smooth" });
    },
  },
};
</script>

<style scoped>
.dot-nav {
  position: fixed;
  top: 50%;
  right: 24px;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: #bbb;
  cursor: pointer;
  transition: background-color 0.3s;
}
.dot.active {
  background-color: #f9c300; /* 강조 색상 */
}
</style>
