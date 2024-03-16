require('dotenv').config();
const express = require('express');
const cors = require('cors');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

const app = express();
const PORT = process.env.PORT || 4000;

// Supabase credentials (set these in a .env file — see .env.example)
const supabaseUrl = process.env.SUPABASE_URL;
const supabaseKey = process.env.SUPABASE_KEY;

if (!supabaseUrl || !supabaseKey) {
  console.error('Missing SUPABASE_URL or SUPABASE_KEY. Copy .env.example to .env and fill in your values.');
  process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseKey);

// Middleware
app.use(cors());
app.use(express.json());

// Serve static files from "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve index.html on root "/"
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// === API ROUTES ===

// Patients
app.get('/api/patients', async (req, res) => {
  // TODO: fetch all patients from Supabase and return them
});

app.post('/api/patients', async (req, res) => {
  // TODO: read the required fields from req.body and insert into the patients table
});

// Medications
app.get('/api/medications', async (req, res) => {
  // TODO: fetch all medications from Supabase and return them
});

app.post('/api/medications', async (req, res) => {
  // TODO: read the required fields from req.body and insert into the medications table
});

// Appointments
app.get('/api/appointments', async (req, res) => {
  // TODO: fetch all appointments from Supabase and return them
});

app.post('/api/appointments', async (req, res) => {
  // TODO: read the required fields from req.body and insert into the appointments table
});

// Doctors
app.get('/api/doctors', async (req, res) => {
  // TODO: fetch all doctors from Supabase and return them
});

app.post('/api/doctors', async (req, res) => {
  // TODO: read the required fields from req.body and insert into the doctors table
});

// Consultations
app.get('/api/consultations', async (req, res) => {
  // TODO: fetch all consultations from Supabase and return them
});

app.post('/api/consultations', async (req, res) => {
  // TODO: read the required fields from req.body and insert into the consultations table
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
