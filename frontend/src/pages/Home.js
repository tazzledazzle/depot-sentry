// frontend/src/pages/Home.js

import React, { useEffect, useState } from 'react';
import RepoList from '../components/RepoList';
import { fetchRepos } from '../services/api';

const Home = () => {
    const [repos, setRepos] = useState([]);

    useEffect(() => {
        fetchRepos().then(data => setRepos(data));
    }, []);

    return (
        <div>
            <h1>Home</h1>
            <RepoList repos={repos} />
        </div>
    );
};

export default Home;
