import React, { useState, useEffect, useRef, useContext } from "react";
import "bootstrap/dist/css/bootstrap.css";
import Card from "react-bootstrap/Card";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { Navigate } from "react-router-dom";
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import Home from "./Home";
import logo from "../logo.svg";
import "../App.css";
const Login = () => {
    const [loading, setLoading] = useState(true);
    const [content, setContent] = useState(undefined);
    const [currentUser, setCurrentUser] = useState();
    const [validated, setValidated] = useState(false);
    let navigate = useNavigate();
    let card = null;

    useEffect(() => {
        setLoading(true);
        setLoading(false);
    }, []);

    async function handleSubmit(event) {
        const form = event.currentTarget;
        if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
        } else {
            event.preventDefault();
            event.stopPropagation();
            setValidated(true);
            let username = form.elements.loginUser.value;
            // let password = form.elements.loginPass.value;
            // try {
            //     await doSignInWithEmailAndPassword(username, password);
            // } catch (error) {
            //     alert(error);
            // }
            setCurrentUser(username);
            // return <Navigate to="/" />;
            // navigate("/");
            return <Home user={username} />;
        }
    }

    if (currentUser) {
        // return <Navigate to="/" user={currentUser} />;
        navigate("/", { user: { currentUser } });
    }
    if (loading) {
        return (
            <div>
                <h2>Loading....</h2>
            </div>
        );
    } else {
        return (
            <div className="container align-self-center card-container">
                <Link className="signuponloginpagelink mb-4" to="/signup">
                    Don't have an account? Click here to sign up!
                </Link>
                <Card className="card-shadow">
                    <Card.Header>
                        <h2>Login</h2>
                    </Card.Header>
                    <Form className="p-3 text-start" noValidate validated={validated} onSubmit={handleSubmit}>
                        <Form.Group className="mb-3" controlId="loginUser">
                            <Form.Label className="form-label">Username</Form.Label>
                            <Form.Control name="loginUser" type="text" placeholder="Username" required />
                        </Form.Group>

                        {/* <Form.Group className="mb-3" controlId="loginPass">
                            <Form.Label>Password</Form.Label>
                            <Form.Control name="loginPass" type="password" placeholder="Password" required />
                        </Form.Group> */}
                        <Button variant="primary" type="submit" className="save-button">
                            Submit
                        </Button>
                    </Form>
                </Card>
            </div>
        );
    }
};

export default Login;
