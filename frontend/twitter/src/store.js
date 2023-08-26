import { create } from 'zustand'

export const useStore = create((set) => ({
    tweets: [],
    addTweet: (tweet) => set((state) => ({ tweets: state.tweets.concat(tweet) })),
    removeAllTweets: () => set({ tweets: [] }),
}))