import React, { useState, useEffect, useRef, useContext } from "react";
import "bootstrap/dist/css/bootstrap.css";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import ListGroup from "react-bootstrap/ListGroup";
import Form from "react-bootstrap/Form";
import Table from "react-bootstrap/Table";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
import { Navigate } from "react-router-dom";
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
// import yamlConvert from "../yaml-convert";
import logo from "../logo.svg";
import yaml from "js-yaml";
import yamlFile from "../charges.yaml";
import "../App.css";

const Home = (props) => {
    const [loading, setLoading] = useState(true);
    const [content, setContent] = useState(undefined);
    const [currentUser, setCurrentUser] = useState();
    const [validated, setValidated] = useState(false);
    let navigate = useNavigate();
    let card = null;
    let userBlock = null;
    let owingBlock = null;
    // let yamlJSON = yamlConvert.get();

    useEffect(() => {
        setLoading(true);
        // if (!currentUser) {
        //     navigate("/login");
        // }
        console.log(yamlFile);
        fetch(yamlFile)
            .then((r) => r.text())
            .then((text) => {
                let jsonedYaml = yaml.load(text);
                console.log(currentUser);
                console.log(jsonedYaml);
                setContent(jsonedYaml);
            });
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

            let username = "";
            for (let i = 0; i < form.elements.loginUser.value.length; i++) {
                if (i == 0) {
                    username += form.elements.loginUser.value.charAt(0).toUpperCase();
                } else {
                    username += form.elements.loginUser.value.charAt(i).toLowerCase();
                }
            }
            if (username == "Mark" || username == "Andrew" || username == "Eric" || username == "Jon") {
                setValidated(true);
                setCurrentUser(username);
            }
            setValidated(false);
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
            let owe = content.users[currentUser].Owe;
            let owed = content.users[currentUser].Owed;
            let oweBlock;
            let owedBlock;

            const buildCard = (arr) => {
                return (
                    <tr>
                        <td>{arr[0]}</td>
                        <td>{arr[1] != "" ? "$" + arr[1] : ""}</td>
                    </tr>
                );
                // return <li>{arr[0] + ": " + "$" + arr[1]}</li>;
            };

            // [key, value]
            oweBlock = Object.entries(owe).map((arr) => {
                return buildCard(arr);
            });
            owedBlock = Object.entries(owed).map((arr) => {
                return buildCard(arr);
            });
            owingBlock = (
                <Card className="card-shadow">
                    <Card.Body>
                        <ListGroup variant="flush" className="float-center">
                            <Card.Title id="name">Owe</Card.Title>
                            <Table striped bordered hover className="tbl">
                                <tbody>{oweBlock}</tbody>
                            </Table>
                        </ListGroup>
                        <hr />
                        <ListGroup variant="flush" className="float-center">
                            <Card.Title id="name">Owed</Card.Title>
                            <Table striped bordered hover className="tbl">
                                <tbody>{owedBlock}</tbody>
                            </Table>
                        </ListGroup>
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
                {owingBlock}
            </div>
        );
    }
};

export default Home;
