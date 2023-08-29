import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
    plugins: [react()],
    resolve: {
        mainFields: [], // To fix an issue with moment-react
    },
    server: {
        watch: {
            usePolling: true
        }
    }
})