<template>
  <v-row justify="center">
    <v-dialog v-model="show" persistent width="1024">
      <v-form validate-on="submit lazy" @submit.prevent="submit">
        <v-card>
          <v-card-title>
            <span class="text-h5">Parcel Order</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" sm="6" md="6">
                  <v-text-field v-model="formData.sender" :rules="rules" label="Sender*" hint="Who is sender" persistent-hint
                    required></v-text-field>
                </v-col>
                <v-col cols="12" sm="6" md="6">
                  <v-text-field v-model="formData.receiver" :rules="rules" label="Receiver*" hint="Who is receiver" persistent-hint
                    required></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field v-model="formData.placedOn" label="Placed On" readonly></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field v-model="formData.updatedOn" label="Updated On" readonly></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field v-model="formData.status" label="Status" readonly></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-select v-model="formData.size" :rules="rules" :items="['XS', 'S', 'M', 'L', 'XL']" label="Size*"
                    required></v-select>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-select v-model="formData.locker" :rules="rules" :items="lockersData" :item-props="lockerItemProps"
                    label="Lockers*" required return-object single-line></v-select>
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue-darken-1" variant="text" @click="show = false">
              Close
            </v-btn>
            <v-btn color="blue-darken-1" variant="text" type="submit">
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  props: ['visible', 'lockersData'],
  computed: {
    show: {
      get() {
        return this.visible
      },
      set(value) {
        if (!value) {
          this.$emit('close')
        }
      }
    }
  },
  data: () => ({
    loading: false,
    timeout: null,
    rules: [value => new Promise(resolve => {
          if (value == null || value == '') return resolve('Field value is a must, master.');
          return resolve(true);
      })],
    formData: {
      sender: '',
      receiver: '',
      size: '',
      placedOn: new Date().toDateString(),
      updatedOn: new Date().toDateString(),
      locker: 0,
      status: ''
    }
  }),
  methods: {
    lockerItemProps(item) {
      return {
        title: item.address,
        subtitle: item.city,
        id: item.id
      }
    },
    async submit(event) {
      this.loading = true;
      const results = await event;
      //console.log('ParcelWindow.Validation():', JSON.stringify(results, null, 2));
      if (results.valid){
        const saveParcelResults = await this.saveParcelOrder(this.formData);
        console.log('ParcelWindow.Sumbit():', JSON.stringify(saveParcelResults, null, 2));
      }
      this.loading = false;
    },
    async saveParcelOrder(formData) {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization':'Basic YWRtaW46cGFzc3dvcmQxMjM=' },
        body: JSON.stringify(formData)
      };

      const response = await fetch('http://localhost:8000/api/parcels/', requestOptions)
        .then(response => response.json())
        .catch((error) => console.error(error));

        return new Promise(resolve => {
          if (response.statusCode == '500' || response.statusCode == '403' || response.detail !== null) return resolve(response);
          return resolve(true);
      });
    },
    async validateField(value){
      return new Promise(resolve => {
          if (value == null || value == '') return resolve('Field value is a must, master.');
          return resolve(true);
      })
    }
  }
}
</script>