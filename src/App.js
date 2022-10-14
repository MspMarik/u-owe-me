import logo from "./logo.svg";
import "./App.css";
import Home from "./components/Home";
// import Login from "./components/Login";
// import Signup from "./components/Signup";
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import React, { useContext, useState, useEffect, useRef } from "react";

function App() {
    return (
        <Router>
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h1>U Owe Me</h1>
                </header>
                <br />
                <br />
                <div className="App-Body">
                    <Routes>
                        <Route exact path="/" element={<Home />} />
                        {/* <Route exact path="/login" element={<Login />} />
                        <Route exact path="/signup" element={<Signup />} /> */}
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;
