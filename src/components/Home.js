import React, { useState, useEffect, useRef, useContext } from "react";
import "bootstrap/dist/css/bootstrap.css";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import ListGroup from "react-bootstrap/ListGroup";
import Form from "react-bootstrap/Form";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import { Navigate } from "react-router-dom";
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import logo from "../logo.svg";
import "../App.css";
const Home = (props) => {
    const [loading, setLoading] = useState(true);
    const [content, setContent] = useState(undefined);
    const [currentUser, setCurrentUser] = useState();
    const [validated, setValidated] = useState(false);
    let navigate = useNavigate();
    let card = null;
    let userBlock = null;

    useEffect(() => {
        setLoading(true);
        // if (!currentUser) {
        //     navigate("/login");
        // }
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
            // return <Home user={username} />;
        }
    }

    if (loading) {
        return (
            <div>
                <h2>Loading....</h2>
            </div>
        );
    } else {
        if (currentUser) {
            userBlock = (
                <Card className="card-shadow">
                    <Card.Header>
                        <h2>Hello {currentUser}</h2>
                    </Card.Header>
                    <Card.Body>
                        <Button variant="primary" onClick={() => setCurrentUser(undefined)} className="save-button">
                            Logout
                        </Button>
                    </Card.Body>
                </Card>
            );
        } else {
            userBlock = (
                <Card className="card-shadow">
                    <Card.Header>
                        <h2>Login</h2>
                    </Card.Header>
                    <Form className="p-3 text-start" noValidate validated={validated} onSubmit={handleSubmit}>
                        <Form.Group className="mb-3" controlId="loginUser">
                            <Form.Label className="form-label">Username</Form.Label>
                            <Form.Control name="loginUser" type="text" placeholder="Username" required />
                        </Form.Group>
                        <Button variant="primary" type="submit" className="save-button">
                            Submit
                        </Button>
                    </Form>
                </Card>
            );
        }
        return (
            <div className="container align-self-center card-container">
                {userBlock}
                <br />
                <Card className="card-shadow">
                    <Card.Img variant="top" src={logo} />
                    <Card.Body>
                        <Card.Title id="name">{content && content.name}</Card.Title>
                        <ListGroup variant="flush" className="float-center">
                            <ListGroup.Item>
                                <Card.Text>
                                    <div className="d-flex justify-content-between">
                                        <Card.Text id="age">{content && content.age}</Card.Text>
                                        <Card.Text id="gender">{content && content.gender}</Card.Text>
                                    </div>
                                </Card.Text>
                                <Card.Text id="bio">{content && content.bio}</Card.Text>
                            </ListGroup.Item>
                            <ListGroup.Item id="ld-likes">
                                <Card.Text className="fw-bold">Likes</Card.Text>
                                {content && content.likes}
                            </ListGroup.Item>
                            <ListGroup.Item id="ld-likes">
                                <Card.Text className="fw-bold">Dislikes</Card.Text>
                                {content && content.dlikes}
                            </ListGroup.Item>
                        </ListGroup>
                    </Card.Body>
                </Card>
            </div>
        );
    }
};

export default Home;
