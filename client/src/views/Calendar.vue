<template>
    <div class="calendar-page">
        <div class="calendar-title-area">
            <h1>Calendar Title Will Go Here</h1>
        </div>
        <div class="calendar-body">
            <h2>{{state.monthName}}</h2>
        </div>
    </div>
</template>

<script>
import { onBeforeMount, reactive } from 'vue'
export default {
    name: "Calendar",
    setup() {
        const state = reactive({
            day: 0,
            weekday: 0,
            month: 0,
            dayCount: 0,
            monthName: ''
        })

        function getNumOfDays() {
            if ([0, 2, 4, 6, 7, 9, 11].includes(state.month)) {
                state.dayCount = 31
            } else if (state.month === 1) {
                if  (Date.getFullYear() % 4 === 0) {
                    state.dayCount = 29
                } else {
                    state.dayCount = 28
                }
            } else {
                state.dayCount = 30
            }
        }

        function setDate() {
            const date = new Date()
            state.day = date.getDate()
            state.weekday = date.getDay()
            state.month = date.getMonth()

            const monthObj = {
                0: 'January',
                1: 'February',
                2: 'March',
                3: 'April',
                4: 'May',
                5: 'June',
                6: 'July',
                7: 'August',
                8: 'September',
                9: 'October',
                10: 'November',
                11: 'December'
            }

            state.monthName = monthObj[state.month]

        }

        onBeforeMount(() => {
            setDate()
            getNumOfDays()
        })

        return {
            state
        }
    }
}
</script>

<style scoped>

</style>