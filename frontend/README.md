# RepoSentry Frontend

This is the frontend for the RepoSentry project, built with React.

## Setup

1. Install dependencies:
    ```bash
    npm install
    ```

2. Run the development server:
    ```bash
    npm start
    ```

3. Build for production:
    ```bash
    npm run build
    ```

## Docker

To build and run the Docker container:

1. Build the Docker image:
    ```bash
    docker build -t reposentry-frontend .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 80:80 reposentry-frontend
    ```

## Available Scripts

In the project directory, you can run:

- `npm start`: Runs the app in the development mode.
- `npm test`: Launches the test runner in the interactive watch mode.
- `npm run build`: Builds the app for production to the `build` folder.

## Learn More

To learn React, check out the [React documentation](https://reactjs.org/).
