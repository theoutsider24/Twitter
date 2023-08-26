import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { ChakraProvider } from "@chakra-ui/react";
import { Button, ButtonGroup } from "@chakra-ui/react";
import { useStore } from "./store";
import { useEffect } from "react";
import axios from "axios";
import { Input, InputGroup, InputRightAddon } from "@chakra-ui/react";

const LogoutButton = () => {
    const { logout } = useAuth0();

    return (
        <Button onClick={() => logout({ logoutParams: { returnTo: window.location.origin } })}>
            Log Out
        </Button>
    );
};

const LoginButton = () => {
    const { loginWithRedirect } = useAuth0();

    return <Button onClick={() => loginWithRedirect()}>Log In</Button>;
};

const TweetList = () => {
    const tweets = useStore((state) => state.tweets);
    return (
        <ul>
            {tweets.map((tweet) => (
                <li key={tweet.id}>{tweet.text}</li>
            ))}
        </ul>
    );
};

const TweetInput = () => {
    const [tweet, setTweet] = React.useState("");
    const handleChange = (event) => setTweet(event.target.value);

    const submitTweet = () => {
        axios.post("http://localhost:8000/tweets", { text: tweet });
    };

    return (
        <>
            <InputGroup>
                <Input value={tweet} onChange={handleChange}></Input>
                <InputRightAddon>
                    <Button onClick={submitTweet}>Submit</Button>
                </InputRightAddon>
            </InputGroup>
        </>
    );
};

function App() {
    const addTweet = useStore((state) => state.addTweet);
    const removeAllTweets = useStore((state) => state.removeAllTweets);
    useEffect(() => {
        axios.get("http://localhost:8000/tweets").then((res) => {
            removeAllTweets();
            res.data.forEach((tweet) => {
                addTweet(tweet);
            });
        });
    }, []);
    return (
        <ChakraProvider>
            <LoginButton />
            <LogoutButton />
            <TweetList />
            <TweetInput />
        </ChakraProvider>
    );
}

export default App;
