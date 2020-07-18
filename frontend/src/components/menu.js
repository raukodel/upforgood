import React, { useState } from 'react';
import style from '../layout/menu.css';

export default props => {
    const [access_token, setAccessToken] = useState("");

    // componentDidMount() {
    //     setAccessToken(localStorage.getItem('access_token'))
    //     console.log(access_token)
    // }

    return (
        <ul className={style.Menu}>
            <li><a href="/index.html">Home</a></li>
            <li><a href="/products/product-1.html">Product</a></li>
            <li><a href="/contact.html">Contact</a></li>
        </ul>
    );

}