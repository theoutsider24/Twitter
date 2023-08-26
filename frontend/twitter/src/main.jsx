import React from "react";
import { createRoot } from "react-dom/client";
import { Auth0Provider } from "@auth0/auth0-react";
import App from "./App";

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
