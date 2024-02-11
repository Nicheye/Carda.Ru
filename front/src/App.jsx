import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Login from "./components/Login";
import Home from './components/Home1';
import Logout from './components/Logout';
import Navigate from './components/Navigate'
import Register from './components/Register'
function App() {
 

  return (
    <BrowserRouter>
        <Navigate/>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/login" element={<Login/>}/>
          <Route path="/logout" element={<Logout/>}/>
          <Route path="/register" element={<Register/>}/>
        </Routes>
      </BrowserRouter>
  
  )
}

export default App
