import { create } from 'zustand'

export const useStore = create((set) => ({
    tweets: [],

    addTweetAtTop: (tweet) => set((state) => ({ tweets: [tweet].concat(state.tweets) })),
    addTweet: (tweet) => set((state) => ({ tweets: state.tweets.concat(tweet) })),
    removeAllTweets: () => set({ tweets: [] }),
}))