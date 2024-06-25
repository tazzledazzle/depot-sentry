// frontend/src/pages/CI_CDSettingsPage.js

import React, { useState } from 'react';
import { triggerPipeline } from '../services/ci_cd_service';

const CI_CDSettingsPage = () => {
    const [repoName, setRepoName] = useState('');
    const [ciCdType, setCiCdType] = useState('');

    const handleTriggerPipeline = async () => {
        const result = await triggerPipeline(repoName, ciCdType);
        console.log(result);
    };

    return (
        <div>
            <h1>CI/CD Settings</h1>
            <input
                type="text"
                value={repoName}
                onChange={(e) => setRepoName(e.target.value)}
                placeholder="Repository Name"
            />
            <select value={ciCdType} onChange={(e) => setCiCdType(e.target.value)}>
                <option value="">Select CI/CD Type</option>
                <option value="jenkins">Jenkins</option>
                <option value="github_actions">GitHub Actions</option>
                <option value="circleci">CircleCI</option>
            </select>
            <button onClick={handleTriggerPipeline}>Trigger Pipeline</button>
        </div>
    );
};

export default CI_CDSettingsPage;
