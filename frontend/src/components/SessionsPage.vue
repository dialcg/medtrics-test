<template>
    <div class="container mt-5">
      <h1 class="mb-4">Medtrics School Session List</h1>
  
      <!-- Filters -->
      <div class="row mb-4">
        <div class="col-md-4 mb-3">
          <label class="form-label">Search by name:</label>
          <input
            v-model="search"
            type="text"
            class="form-control"
            placeholder="Search by session name or location"
          />
        </div>
        <div class="col-md-2 mb-3">
          <label for="courseSelect" class="form-label">Course:</label>
          <select
            v-model="selectedCourse"
            id="courseSelect"
            class="form-select"
          >
            <option value="">All courses</option>
            <option v-for="course in courses" :key="course.id" :value="course.id">
              {{ course.name }}
            </option>
          </select>
        </div>
        <div class="col-md-2 mb-3">
          <label for="dateSelect" class="form-label">Date:</label>
          <input
            v-model="selectedDate"
            type="date"
            id="dateSelect"
            class="form-control"
          />
        </div>
        <div class="col-md-4 mb-3">
          <label for="locationSelect" class="form-label">Location:</label>
          <select
            v-model="selectedLocation"
            id="locationSelect"
            class="form-select"
          >
            <option value="">All locations</option>
            <option v-for="location in locations" :key="location.id" :value="location.id">
              {{ location.name }}
            </option>
          </select>
        </div>
      </div>
  
      <!-- Session List -->
      <ul class="list-group">
        <li
          v-for="session in paginatedSessions"
          :key="session.id"
          class="list-group-item mb-3"
        >
          <div>
            <h5 class="mb-1">{{ session.session.name }}</h5>
            <p class="mb-0"><strong>Date:</strong> {{ session.date }}</p>
            <p class="mb-0"><strong>Location:</strong> {{ session.location.name }}</p>
            <p class="mb-0"><strong>Course:</strong> {{ session.session.course.name }}</p>
          </div>
        </li>
      </ul>
  
      <!-- Pagination -->
      <nav class="mt-4">
        <ul class="pagination justify-content-center">
          <li
            class="page-item"
            :class="{ disabled: currentPage === 1 }"
          >
            <a
              class="page-link"
              href="#"
              @click.prevent="prevPage"
            >Previous</a>
          </li>
          <li
            v-for="page in totalPagesArray"
            :key="page"
            class="page-item"
            :class="{ active: page === currentPage }"
          >
            <a
              class="page-link"
              href="#"
              @click.prevent="goToPage(page)"
            >{{ page }}</a>
          </li>
          <li
            class="page-item"
            :class="{ disabled: currentPage === totalPages }"
          >
            <a
              class="page-link"
              href="#"
              @click.prevent="nextPage"
            >Next</a>
          </li>
        </ul>
      </nav>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        sessions: [],
        courses: [],
        locations: [],
        search: '',
        selectedCourse: '',
        selectedDate: '',
        selectedLocation: '',
        currentPage: 1,
        perPage: 5,
      };
    },
    computed: {
      filteredSessions() {
        return this.sessions.filter(session => {
          return (
            (this.search === '' ||
              session.session.name.toLowerCase().includes(this.search.toLowerCase()) ||
              session.location.name.toLowerCase().includes(this.search.toLowerCase())) &&
            (this.selectedCourse === '' || session.session.course.id === this.selectedCourse) &&
            (this.selectedDate === '' || session.date === this.selectedDate) &&
            (this.selectedLocation === '' || session.location.id === this.selectedLocation)
          );
        });
      },
      totalPages() {
        return Math.ceil(this.filteredSessions.length / this.perPage);
      },
      totalPagesArray() {
        return Array.from({ length: this.totalPages }, (_, i) => i + 1);
      },
      paginatedSessions() {
        const start = (this.currentPage - 1) * this.perPage;
        const end = start + this.perPage;
        return this.filteredSessions.slice(start, end);
      }
    },
    methods: {
      async fetchData() {
        try {
          const sessionsResponse = await axios.get('http://localhost:8000/api/sessions/session-schedules/');
          this.sessions = sessionsResponse.data;
          const coursesResponse = await axios.get('http://localhost:8000/api/courses/');
          this.courses = coursesResponse.data;
          const locationsResponse = await axios.get('http://localhost:8000/api/sessions/locations/');
          this.locations = locationsResponse.data;
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
      prevPage() {
        if (this.currentPage > 1) {
          this.currentPage--;
        }
      },
      nextPage() {
        if (this.currentPage < this.totalPages) {
          this.currentPage++;
        }
      },
      goToPage(page) {
        this.currentPage = page;
      }
    },
    mounted() {
      this.fetchData();
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 1200px;
  }
  
  .pagination {
    font-size: 0.9rem;
  }
  
  .list-group-item {
    border-radius: 0.25rem;
  }

  </style>
  