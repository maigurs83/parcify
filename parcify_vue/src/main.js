import { createApp } from 'vue';
import VueAxios from 'vue-axios';
import axios from 'axios';
import router from './router/index.js';
import App from './App.vue';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.baseURL = process.env.apiUrl || 'http://127.0.0.1:8000/api/';

const app = createApp(App);

app.use(VueAxios, axios);
app.use(router);

app.mount('#app');