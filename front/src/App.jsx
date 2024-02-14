import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Login from "./pages/Login";
import Main from './pages/Main'
import Logout from './components/Logout';
import Navigate from './components/Navigate'
import Register from './pages/Register'
import Spend_form from './components/Spend_form'
function App() {
  return (
    <BrowserRouter>
        <Navigate/>
        <Routes>
          <Route path="/" element={<Main/>}/>
          <Route path="/spend_created" element={<Spend_form/>}/>
          <Route path="/login" element={<Login/>}/>
          <Route path="/logout" element={<Logout/>}/>
          <Route path="/register" element={<Register/>}/>
        </Routes>
      </BrowserRouter>
  
  )
}

export default App
