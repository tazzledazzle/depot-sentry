// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import RepoPage from './pages/RepoPage';
import SettingsPage from './pages/SettingsPage';
import CI_CDSettingsPage from './pages/CI_CDSettingsPage';

const App = () => (
    <Router>
        <Header />
        <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/repo/:repoId" component={RepoPage} />
            <Route path="/settings" component={SettingsPage} />
            <Route path="/ci-cd-settings" component={CI_CDSettingsPage} />
        </Switch>
    </Router>
);

export default App;
