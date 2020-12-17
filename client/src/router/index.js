import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/Home.vue')
    },
    {
        path: '/calendar/:code',
        name: "Calendar",
        component: () => import('../views/Calendar.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
