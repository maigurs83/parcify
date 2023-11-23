<template>
  <v-container class="fill-height">
    <v-responsive class="align-top text-left fill-height">
      <v-card flat class="mb-2 pa-2">
        <v-card-title class="d-flex align-center pe-2">
          <v-card-text><h2>Parcel Orders</h2></v-card-text>
          <v-spacer></v-spacer>
          <ParcelWindow :visible="showParcelWindow" :lockersData="lockersData.serverItems" @close="showParcelWindow=false" />
          <v-btn color="accent" large @click.stop="showParcelWindow=true">Add New</v-btn>
        </v-card-title>
        <v-data-table-server v-model:items-per-page="parcelsData.itemsPerPage" :headers="parcelsData.headers"
          :items-length="parcelsData.totalItems" :items="parcelsData.serverItems" :loading="parcelsData.loading"
          item-value="name" @update:options="getParcelsData">
        </v-data-table-server>
      </v-card>
      <v-card flat class="mt-2 pa-2">
        <v-card-title class="d-flex align-center pe-2">
          <v-card-text><h2>Parcel Lockers</h2></v-card-text>
        </v-card-title>
        <v-data-iterator :items="lockersData.serverItems" item-value="id">
          <template v-slot:default="{ items }">
            <v-row>
              <v-col v-for="item in items" :key="item.raw.id" cols="16" xs="16" sm="6" md="4" lg="4" xl="2">
                <v-card variant="tonal" color="primary">
                  <v-card-title class="d-flex align-center">
                    <h4>{{ (item.raw.status=='Closed') ? `(${ item.raw.status }):` : '' }} {{ item.raw.city }}</h4>
                  </v-card-title>

                  <v-card-subtitle class="d-flex align-center">
                    <h5>{{ item.raw.address }}</h5>
                  </v-card-subtitle>

                  <v-card-text>
                    <h5>{{ item.raw.sizes }}</h5>
                  </v-card-text>

                  <v-card-actions class="d-flex justify-center ga-2 pa-2">
                    <v-data-iterator :items="item.raw.lockers" item-value="id">
                      <template v-slot:default="{ items }">
                        <v-chip v-for="item in items" :key="item.raw.id" variant="flat"
                          :color="`${(item.raw.empty === true) ? 'green' : 'red'}`">{{ item.raw.size }}</v-chip>
                      </template>
                    </v-data-iterator>
                  </v-card-actions>
                </v-card>
              </v-col>
            </v-row>
          </template>
        </v-data-iterator>
      </v-card>
    </v-responsive>
  </v-container>
</template>

<script>
import ParcelWindow from './ParcelWindow.vue'

export default {
  name: "Parcels.Main",
  mounted() {
    this.getLockersData();
  },
  methods: {
    async getParcelsData({ page, itemsPerPage, sortBy }) {
      this.parcelsData.loading = true;
      const requestOptions = {};
      await fetch('http://localhost:8000/api/parcels/', requestOptions)
        .then(response => response.json())
        .then(data => {
          this.parcelsData.serverItems = data.results;
          this.parcelsData.totalItems = data.count;
        })
        .catch(errors => console.error(errors))
        .finally(() => { this.parcelsData.loading = false });
    },
    async getLockersData() {
      this.lockersData.loading = true;
      const requestOptions = {};
      await fetch('http://localhost:8000/api/parcel_lockers/', requestOptions)
        .then(response => response.json())
        .then(data => {
          this.lockersData.serverItems = data.results;
          this.lockersData.totalItems = data.count;
        })
        .catch(errors => console.error(errors))
        .finally(() => { this.lockersData.loading = false });
    }
  },
  data: () => ({
    parcelsData: {
      itemsPerPage: 10,
      headers: [
        { title: '#', key: 'id', align: 'start', sortable: false },
        { title: 'Sender', key: 'sender', align: 'end' },
        { title: 'Receiver', key: 'receiver', align: 'end' },
        { title: 'Size', key: 'size', align: 'end' },
        { title: 'PlacedOn', key: 'placedOn', align: 'end' },
        { title: 'UpdatedOn', key: 'updatedOn', align: 'end' },
        { title: 'Status', key: 'status', align: 'end' },
        { title: 'Locker', key: 'locker', align: 'end' },
      ],
      serverItems: [],
      loading: true,
      totalItems: 0
    },
    lockersData: {
      itemsPerPage: 10,
      serverItems: [],
      loading: true,
      totalItems: 0
    },
    showParcelWindow: false
  }),
  components: {
    ParcelWindow
  }
}
</script>
