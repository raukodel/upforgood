import React from 'react';
import ReactDOM from 'react-dom';
import Login from 'components/login';
import Message from '../components/message';
import { Provider } from 'react-redux';
import { Store } from '../store';

ReactDOM.render(
    <Provider store={Store}>
        <Login />
        <Message />
    </Provider>,
 document.getElementById('login'));