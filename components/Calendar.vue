<template>
  <div class="calendar-container">
    <vue-cal
      :events="events"
      :time="false"
      :view="view"
      :start-date="startDate"
      :locale="locale"
      :formats="formats"
      :disable-views="['years', 'year', 'month']"
      @event-click="onEventClick"
      @event-create="onEventCreate"
      class="w-[1000px] max-w-screen-lg mx-auto"
    >
      <template v-slot:day="{ day }">
        <div class="vuecal__cell">
          <div class="vuecal__flex vuecal__cell-content">
            <!-- Displaying the message directly -->
            <div class="custom-message">Nessuna merenda ordinata</div>
          </div>
        </div>
      </template>
    </vue-cal>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { format, startOfWeek } from "date-fns";
import { it } from "date-fns/locale";

const events = ref([
  {
    id: 1,
    start: "2023-10-01 10:00",
    end: "2023-10-01 12:00",
    title: "Event 1",
  },
  {
    id: 2,
    start: "2023-10-02 14:00",
    end: "2023-10-02 16:00",
    title: "Event 2",
  },
]);

const view = ref("week");
const startDate = ref(
  format(startOfWeek(new Date(), { weekStartsOn: 1 }), "yyyy-MM-dd")
);
const locale = ref(it);
const formats = ref({
  title: "dddd D MMMM YYYY",
  weekdays: "dddd",
});

const onEventClick = (event: any) => {
  console.log("Event clicked:", event);
};

const onEventCreate = (event: any) => {
  console.log("Event created:", event);
};
</script>

<style scoped>
.vuecal__cell {
  background-color: #f0f0f0; /* Background for the day cell */
}

.vuecal__header {
  background-color: #6a0dad; /* Header background color */
  color: white; /* Header text color */
}

.custom-message {
  font-size: 1em; /* Font size for the message */
  color: #666; /* Message color */
  text-align: center; /* Center text */
  padding: 10px; /* Padding for the message */
}

.event {
  background-color: #ffeb3b; /* Event background color */
  padding: 5px; /* Padding for event items */
  margin: 5px; /* Margin for event items */
  border-radius: 5px; /* Rounded corners for events */
}
</style>
