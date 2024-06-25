// frontend/src/services/ci_cd_service.js

const triggerPipeline = async (repoName, ciCdType) => {
    const response = await fetch('/api/ci_cd/trigger', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ repo_name: repoName, ci_cd_type: ciCdType }),
});
return response.json();
};

export { triggerPipeline };
