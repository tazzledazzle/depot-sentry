// frontend/src/components/Header.js

import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => (
    <header>
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/settings">Settings</Link></li>
                <li><Link to="/ci-cd-settings">CI/CD Settings</Link></li>
            </ul>
        </nav>
    </header>
);

export default Header;
