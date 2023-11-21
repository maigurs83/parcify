import { createWebHashHistory, createRouter } from "vue-router";

import NotFoundView from "@/views/NotFound.vue";
import ParcelsView from "@/views/ParcelsView.vue";
import ParcelView from "@/views/ParcelView.vue";

const routes = [
        {
            path: '/parcels',
            conponent: ParcelsView
        },
        {
            path: '/parcels/:id',
            conponent: ParcelView
        },
        {
            path: '/:catchAll(.*)',
            component: NotFoundView
        }
    ];

const router = createRouter({
    history: createWebHashHistory(),
    base: process.env.BASE_URL,
    routes: routes
});

export default router