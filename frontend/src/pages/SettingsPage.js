// frontend/src/pages/SettingsPage.js

import React from 'react';
import NotificationSettings from '../components/NotificationSettings';

const SettingsPage = () => {
    const initialSettings = {
        email: true
    };

    return (
        <div>
            <h1>Settings</h1>
            <NotificationSettings initialSettings={initialSettings} />
        </div>
    );
};

export default SettingsPage;
