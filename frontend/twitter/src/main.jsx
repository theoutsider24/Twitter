import React from "react";
import { createRoot } from "react-dom/client";
import { Auth0Provider } from "@auth0/auth0-react";
import App from "./App";
import * as Sentry from "@sentry/react";

Sentry.init({
    dsn: import.meta.env.VITE_SENTRY_DSN,
    integrations: [new Sentry.BrowserTracing({}), new Sentry.Replay()],

    // Set tracesSampleRate to 1.0 to capture 100%
    // of transactions for performance monitoring.
    tracesSampleRate: 1.0,

    // Set `tracePropagationTargets` to control for which URLs distributed tracing should be enabled
    tracePropagationTargets: ["localhost"],

    // Capture Replay for 10% of all sessions,
    // plus for 100% of sessions with an error
    replaysSessionSampleRate: 0.1,
    replaysOnErrorSampleRate: 1.0,
});

const root = createRoot(document.getElementById("root"));

root.render(
    <Auth0Provider
        domain="dev-i2at2bc6kbe15h2w.uk.auth0.com"
        clientId="ilWZ1w7DjkECoWZIqg9S4UzwzBcQoJ9l"
        authorizationParams={{
            redirect_uri: window.location.origin,
            audience: "core",
        }}
    >
        <App />
    </Auth0Provider>
);
