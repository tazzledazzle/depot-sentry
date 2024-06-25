// frontend/src/pages/RepoPage.js

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import RepoDetails from '../components/RepoDetails';
import { fetchRepoDetails } from '../services/api';

const RepoPage = () => {
    const { repoId } = useParams();
    const [repo, setRepo] = useState(null);

    useEffect(() => {
        fetchRepoDetails(repoId).then(data => setRepo(data));
    }, [repoId]);

    if (!repo) return <div>Loading...</div>;

    return (
        <div>
            <h1>Repo Details</h1>
            <RepoDetails repo={repo} />
        </div>
    );
};

export default RepoPage;
