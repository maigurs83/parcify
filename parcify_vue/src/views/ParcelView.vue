<template>
    <v-container id="parcel-page" fluid pa-0>
    </v-container>
</template>

<script>

export default {
    name: "ParcelView",
        created() {
            this.getMainData();
        },
    computed: {},
    methods: {
        async getMainData() {
            await this.axios.apiClient.getAccounts()
                .then(res => console.log(res.data))
                .catch(errors => console.log(errors.data))
                .finally(() => console.log('Done'));
        }
    },
    data() {
        return {
            search: '',
            headers: [
            {
                filterable: false,
                sortable: false,
                text: this.$t('account.id'),
                value: "id"
            },
            {
                sortable: true,
                text: this.$t('account.name'),
                value: "displayName",
                width: '200'
            },
            {
                filterable: false,
                sortable: false,
                text: this.$t('account.modifiedOn'),
                value: "modifiedOn",
                dataType: "Date"
            },
            {
                filterable: false,
                sortable: false,
                text: this.$t('account.hasOrder'),
                value: "hasOrder",
                dataType: "Boolean"
            },
            {
                filterable: false,
                sortable: false,
                text: "",
                value: "actions"
            }
            ],
            items: []
        }
    }
};
</script>