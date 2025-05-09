<template>
  <div class="app">
    <DotNav :currentSection="currentSection" />
    <section id="intro" class="section" @mouseenter="setSection('intro')">
      <Intro />
    </section>
    <section id="label" class="section" @mouseenter="setSection('label')">
      <Label />
    </section>
    <section id="need" class="section" @mouseenter="setSection('need')">
      <Need />
    </section>
    <section id="upload" class="section" @mouseenter="setSection('upload')">
      <Upload />
    </section>
    <section id="weigh" class="section" @mouseenter="setSection('weigh')">
      <Weigh />
    </section>
    <section id="wash" class="section" @mouseenter="setSection('wash')">
      <Wash />
    </section>
    <section id="end" class="section" @mouseenter="setSection('end')">
      <End />
    </section>
  </div>
</template>

<script>
import DotNav from "./components/DotNav.vue";
import Intro from "./components/IntroSection.vue";
import Label from "./components/LabelSection.vue";
import Need from "./components/NeedSection.vue";
import Upload from "./components/UploadSection.vue";
import Weigh from "./components/WeighSection.vue";
import Wash from "./components/WashSection.vue";
import End from "./components/EndSection.vue";

export default {
  components: { DotNav, Intro, Label, Need, Upload, Weigh, Wash, End },
  data() {
    return {
      currentSection: "intro",
    };
  },
  methods: {
    setSection(sectionName) {
      this.currentSection = sectionName;
    },
  },
};
</script>

<style>
.app {
  scroll-snap-type: y mandatory;
  overflow-y: scroll;
  height: 100vh;
}
.section {
  scroll-snap-align: start;
  height: 100vh;
}
</style>
