import React, { useState } from "react";
import axiosAPI from '../api/axiosAPI';
import {toastr} from 'react-redux-toastr'

export default props => {
    const [username, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");

    const handleLogin = (evt) => {
        evt.preventDefault();

        axiosAPI.post('auth', {
            username: username,
            password: password
        })
            .then(response => {
                localStorage.setItem('access_token', response.data.access_token);
                window.location.href = "/dashboard.html"
            })
            .catch(error => {
                console.log(error.response);
                if(error.response.status == 401)
                    toastr.warning('Info', "Username or password are incorrect")
            })
            .finally(() => {
                // always executed
            });
    }

    const handleNewUser = (evt) => {
        evt.preventDefault();

        axiosAPI.post('user', {
            username: username,
            password: password,
            email: email
        })
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error.response);
                toastr.error('Error !', error.response.data.message)
            })
            .finally(() => {
                // always executed
            });
    }

    return (
        <div>
            <form onSubmit={handleLogin}>
                <div>
                    <div>
                        <label>
                            Username:
                            <input type="text" value={username} onChange={e => setUserName(e.target.value)} />
                        </label>
                    </div>
                    <div>
                        <label>
                            Password:
                            <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                        </label>
                    </div>
                </div>
                <input type="submit" value="Login" />
            </form>
            <form onSubmit={handleNewUser}>
                <div>
                    <label>
                        Username:
                        <input type="text" value={username} onChange={e => setUserName(e.target.value)} />
                    </label>
                </div>
                <div>
                    <label>
                        Password:
                        <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                    </label>
                </div>
                <div>
                    <label>
                        Email:
                        <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
                    </label>
                </div>
                <input type="submit" value="Create User" />
            </form>
        </div>
    );
}