<template>
    <h1>The user is some.</h1>
</template>

<script>

export default {
    name: "ParcelsView",
    created() {
        this.getMainData();
    },
    computed: {},
    methods: {
        async getMainData() {
            await this.axios.get('parcels', {})
                .then(res => { this.items = res.data; })
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