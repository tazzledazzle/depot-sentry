// frontend/src/services/auth.js

export const login = async (username, password) => {
    const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });
    return response.json();
};

export const logout = async () => {
    const response = await fetch('/api/logout', {
        method: 'POST',
    });
    return response.json();
};
