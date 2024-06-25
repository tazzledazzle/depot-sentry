// frontend/src/components/NotificationSettings.js

import React, { useState } from 'react';

const NotificationSettings = ({ initialSettings }) => {
    const [settings, setSettings] = useState(initialSettings);

    const handleSave = () => {
        // Save the notification settings
    };

    return (
        <div>
            <h2>Notification Settings</h2>
            <label>
                <input
                    type="checkbox"
                    checked={settings.email}
                    onChange={(e) => setSettings({ ...settings, email: e.target.checked })}
                />
                Email Notifications
            </label>
            <button onClick={handleSave}>Save</button>
        </div>
    );
};

export default NotificationSettings;
