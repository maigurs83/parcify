<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-img height="140" src="@/assets/logo.svg" />
      <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>
      <h1 class="text-h2 font-weight-bold">Parcify Express</h1>
      <div class="py-14" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto"></v-col>
        <v-col cols="auto">
          <v-btn
            color="primary"
            href="./parcels"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            target="_self"
            variant="flat"
          >
            <v-icon
              icon="mdi-package"
              size="large"
              start
            />
            Get Started
          </v-btn>
        </v-col>

        <v-col cols="auto"></v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script setup>
  //
</script>
