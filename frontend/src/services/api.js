// frontend/src/services/api.js
import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const triggerBuild = (service, repoUrl) => {
    return axios.post(`${API_URL}/trigger_build`, {
        service,
        repo_url: repoUrl,
    });
};

export const getBuildStatus = (service, buildId) => {
    return axios.get(`${API_URL}/build_status/${service}/${buildId}`);
};

export const getLatestBuilds = (service, repoUrl) => {
    return axios.get(`${API_URL}/latest_builds/${service}/${repoUrl}`);
};


const API_BASE_URL = 'http://localhost:5000';

export const getGitHubRepos = async (user) => {
    const response = await axios.get(`${API_BASE_URL}/github/repos`, { params: { user } });
    return response.data;
};

export const getGitLabRepos = async (user) => {
    const response = await axios.get(`${API_BASE_URL}/gitlab/repos`, { params: { user } });
    return response.data;
};

export const getBitbucketRepos = async (user) => {
    const response = await axios.get(`${API_BASE_URL}/bitbucket/repos`, { params: { user } });
    return response.data;
};

export const getAllRepos = async (user) => {
    const response = await axios.get(`${API_BASE_URL}/vcs/repos`, { params: { user } });
    return response.data;
};
