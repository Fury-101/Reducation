<script>
    let shown = true;
</script>

<div hidden={!shown}>
    <div class='w-260 flex flex-col justify-center items-end'>
        <div class='absolute'>
            <button type='button' on:click={(e)=>{shown = !shown;}}>
                <svg class='w-6 h-9' preserveAspectRatio="none" data-slot="icon" fill="none" stroke-width="4" stroke="white" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5 8.25 12l7.5-7.5"></path>
                </svg>
            </button>
        </div>
        <nav class="flex h-screen flex-col bg-neutral-900 w-full px-3 pt-1/4">
            <a href='/' class='flex items-center gap-2 text-left hover:bg-neutral-800 rounded-md text-white text-sm p-2' >Start a new course 
                <svg class='w-6 h-6 inline-block' data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10"></path>
                </svg>
            </a>
            <span class='px-2 text-white/38 text-xs text-center'> History </span>
            {#each ['AP Calculus AB', 'Machine Learning', 'Financial Literacy', 'Quantum Mechanics', 'AP United States History'] as course}
                <a href='/course/{course}' type='button' class='flex items-center gap-2 text-left hover:bg-neutral-800 rounded-md text-white text-sm p-2' >{course}</a>
            {/each}
        </nav>
    </div> 
</div>
<div hidden={shown}>
    <div class='flex flex-col justify-center items-center h-screen absolute z-10'>
        <button type='button' on:click={(e)=>{shown = !shown;}}>
            <svg class='w-6 h-9' preserveAspectRatio="none" data-slot="icon" fill="none" stroke-width="4" stroke="white" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5"></path>
            </svg>
        </button>
    </div>
</div>