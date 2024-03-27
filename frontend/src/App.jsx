import React from 'react'
import { Routes, Route } from 'react-router-dom'

import './App.css'
import LandingPage from './stores/pages/LandingPage'
import MobilePage from './stores/pages/MobilePage'
import CompPage from './stores/pages/CompPage'
import WatchPage from './stores/pages/WatchPage'
import AcPage from './stores/pages/AcPage'
import MobileSingle from './stores/singles/MobileSingle'
import UserCart from './stores/UserCart'
import ComputerSingle from './stores/singles/ComputerSingle'
import AcSingle from './stores/singles/AcSingle'
import WatchSingle from './stores/singles/WatchSingle'
import Login from './stores/components/Login'
import Signup from './stores/components/Signup'
import Actual from './stores/components/Actual'
import Order from './stores/components/Order'

const App = () => {
  return (
    <div>
      <Routes>
        <Route path='/' element={<LandingPage />} />
        {/* <Route path= '/kitchen' element = {<KitchenPage />} /> */}
        <Route path='/mobiles' element={<MobilePage />} />
        <Route path='/computers' element={<CompPage />} />
        <Route path='/watch' element={<WatchPage />} />
        <Route path='/ac' element={<AcPage />} />
        <Route path='/mobiles/:id' element={<MobileSingle />} />
        <Route path='/cart' element={<UserCart />} />
        <Route path='/ac/:id' element={<AcSingle />} />
        <Route path='/computers/:id' element={<ComputerSingle />} />
        <Route path='/watch/:id' element={<WatchSingle />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path='/actual' element={<Actual />} />
        <Route path='/order' element={<Order />} />
      </Routes>
    </div>
  )
}

export default App