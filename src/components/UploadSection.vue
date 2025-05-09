<template>
  <section class="section upload">
    <h2>Identify a Care Label Symbol</h2>

    <label class="custom-file-upload">
      <input type="file" @change="onFileChange" accept="image/*" />
      Choose File
    </label>
    <span class="file-name">
      {{ selectedFile ? selectedFile.name : "No file selected" }}
    </span>

    <button @click="sendToServer" :disabled="!selectedFile">
      Analyze Symbol
    </button>
    <p v-if="result">Result: {{ result }}</p>
  </section>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
      result: "",
    };
  },
  methods: {
    onFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    async sendToServer() {
      const formData = new FormData();
      formData.append("file", this.selectedFile);

      try {
        const response = await fetch("http://localhost:5001/predict", {
          method: "POST",
          body: formData,
        });
        const data = await response.json();
        this.result = data.label;
      } catch (error) {
        console.error("Prediction failed:", error);
        this.result = "Error during symbol analysis.";
      }
    },
  },
};
</script>
<style scoped>
.upload {
  height: 100vh;
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding-top: 100px;
  background-color: #fff;
  font-family: "brevia", sans-serif;
}

h2 {
  font-size: 60px;
  font-family: "brevia", sans-serif;
  font-weight: 700;
  color: transparent;
  -webkit-text-stroke: 2px black;
  background: white;
  -webkit-background-clip: text;
  background-clip: text;
  margin-top: -20px;
}

.custom-file-upload {
  display: inline-block;
  padding: 10px 20px;
  background-color: #f0f0f0;
  border: 2px solid #000;
  border-radius: 6px;
  cursor: pointer;
  margin-bottom: 12px;
  font-family: "brevia", sans-serif;
  font-size: 16px;
}

.custom-file-upload input {
  display: none;
}

.file-name {
  font-style: italic;
  color: #555;
  font-family: "brevia", sans-serif;
  margin-bottom: 20px;
}

button {
  font-family: "brevia", sans-serif;
  padding: 10px 24px;
  background-color: black;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s;
}

button:hover:enabled {
  background-color: #333;
}

button[disabled] {
  opacity: 0.5;
  cursor: not-allowed;
}

p {
  margin-top: 24px;
  font-size: 18px;
  font-family: "brevia", sans-serif;
}
</style>
