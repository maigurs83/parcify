<template>
  <v-system-bar color="primary">
      <!--<v-btn density="compact" icon="mdi-plus" size="small"></v-btn>-->
      <v-icon icon="mdi-arrow-up-bold-box-outline" class="ms-2"></v-icon>
      <span class="ms-2">{{ this.time }}</span>
  </v-system-bar>
</template>

<script>
export default {
  data() {
    return {
      interval: null,
      time: null
    }
  },
  beforeDestroy() {
    // prevent memory leak
    clearInterval(this.interval)
  },
  created() {
    // update the time every second
    this.interval = setInterval(() => {
      // Concise way to format time according to system locale.
      // In my case this returns "3:48:00 am"
      this.time = Intl.DateTimeFormat(navigator.language, {
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric'
      }).format()
    }, 1000)
  }
}
</script>
