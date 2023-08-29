import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { CardFooter, CardHeader, ChakraProvider } from "@chakra-ui/react";
import { Button } from "@chakra-ui/react";
import { useStore } from "./store";
import { useEffect } from "react";
import axios from "axios";
import { Input, InputGroup, InputRightAddon } from "@chakra-ui/react";
import { Card, CardBody, Text, Collapse } from "@chakra-ui/react";
import Moment from "react-moment";

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
                <Tweet tweet={tweet} key={tweet.created_date} />
            ))}
        </ul>
    );
};

const Tweet = ({ tweet }) => {
    const [rendered, setRendered] = React.useState(false);
    useEffect(() => {
        setInterval(() => {
            setRendered(true);
        }, 10);
    }, []);
    return (
        <Collapse in={rendered}>
            <Card bg="teal.500" color="white" m={1}>
                <CardHeader>
                    <Text>{tweet.author_id}</Text>
                </CardHeader>
                <CardBody>
                    <Text>{tweet.text}</Text>
                </CardBody>
                <CardFooter>
                    <Moment fromNow interval={30000} utc>
                        {tweet.created_date}
                    </Moment>
                </CardFooter>
            </Card>
        </Collapse>
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
    const addTweetAtTop = useStore((state) => state.addTweetAtTop);
    const removeAllTweets = useStore((state) => state.removeAllTweets);

    const socket = new WebSocket("ws://127.0.0.1:8001/ws");

    socket.addEventListener("message", (event) => {
        addTweetAtTop(JSON.parse(event.data));
    });

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
