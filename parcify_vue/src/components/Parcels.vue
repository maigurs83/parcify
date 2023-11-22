<template>
  <v-container class="fill-height">
    <v-responsive class="align-top text-left fill-height">
      <v-card title="Parcel Orders" style="background-color:transparent;">
        <v-data-table-server v-model:items-per-page="parcelsData.itemsPerPage" :headers="parcelsData.headers"
          :items-length="parcelsData.totalItems" :items="parcelsData.serverItems" :loading="parcelsData.loading"
          item-value="name" @update:options="getParcelsData">
        </v-data-table-server>
      </v-card>
      <v-card title="Parcel Lockers" style="background-color:transparent;">
        <v-data-iterator :items="lockersData.serverItems" item-value="id">
          <template v-slot:default="{ items }">
            <v-row>
              <v-col v-for="item in items" :key="item.raw.id" cols="12" sm="8" md="4">
                <v-card>
                  <v-card-title class="d-flex align-center">
                    <h3>{{ (item.raw.status=='Closed') ? '(!)' : '' }}</h3> <h4>{{ item.raw.city }}: {{ item.raw.address }}</h4>
                  </v-card-title>

                  <v-card-text>
                    <h5>{{ item.raw.sizes }}</h5>
                    {{ item.raw.status }}
                  </v-card-text>

                  <v-divider></v-divider>

                  <div class="d-flex justify-center ga-2 pa-2">
                    <v-data-iterator :items="item.raw.lockers" item-value="id">
                      <template v-slot:default="{ items }">
                        <v-chip v-for="item in items" :key="item.raw.id" variant="flat"
                          :color="`${(item.raw.empty === true) ? 'green' : 'red'}`">{{ item.raw.size }}</v-chip>
                      </template>
                    </v-data-iterator>
                  </div>
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

export default {
  name: "Parcels",
  mounted() {
    this.getLockersData(1, 10, null);
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
    async getLockersData({ page, itemsPerPage, sortBy }) {
      this.lockersData.loading = true;
      const requestOptions = {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        //body: JSON.stringify({ title: 'React POST Request Example' })
      };
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
    }
  })
}
</script>
