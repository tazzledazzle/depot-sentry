// frontend/src/components/RepoDetails.js

import React from 'react';

const RepoDetails = ({ repo }) => (
    <div>
        <h2>{repo.name}</h2>
        <p>{repo.description}</p>
        <p>Stars: {repo.stars}</p>
    </div>
);

export default RepoDetails;
