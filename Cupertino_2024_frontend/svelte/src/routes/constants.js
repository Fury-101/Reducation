import { readable } from 'svelte/store';

export const frontendPort = readable('5173');
export const apiPort = readable('5000');