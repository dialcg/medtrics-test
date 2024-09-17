<template>
  <div id="app">
    <main>
      <SessionsPage />
    </main>
  </div>
</template>

<script>
import SessionsPage from './components/SessionsPage.vue';

export default {
  name: 'App',
  components: {
    SessionsPage
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
