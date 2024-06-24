import React, { useState, useEffect } from 'react';
import { getAllRepos } from '../services/api';

const RepoList = ({ user }) => {
    const [repos, setRepos] = useState([]);

    useEffect(() => {
        if (user) {
            getAllRepos(user).then(setRepos);
        }
    }, [user]);

    return (
        <div>
            <h2>Repositories</h2>
            <ul>
                {repos.map((repo) => (
                    <li key={repo.id}>{repo.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default RepoList;
