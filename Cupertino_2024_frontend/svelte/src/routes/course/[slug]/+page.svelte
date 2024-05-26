<script>
// import { frontendPort, apiPort } from '../../constants.js'
const frontendPort = 5173
const apiPort = 5000
import History from '../../History.svelte'
import { onMount } from 'svelte';
export let data;

console.log(data.slug)

let C = null;
let MCQ = null;
let FRQ = null;
let YT = null;

let a = data.data.d;
C = a['C'];
for (let [name, u] of Object.entries(C)) {
    u.expanded = false;
};
let sbexpanded = []
for (let [name, u] of Object.entries(C)) {
    sbexpanded.push(Array(Object.entries(u).length).fill(false))
}

console.log(a)
MCQ = a['Q_mcq'];
FRQ = a['Q_frq'];
YT = a['YT_vids'];

let loading = false;

function subunitChecker(e, mcq) {
    const formData = new FormData(e.target);
    const data = [...formData];
    let correct = (data[0][1] === mcq.options[mcq.ans])
    
    if (!correct) {
        document.getElementById(mcq.options[mcq.ans].replace(/\W/g, '')).parentNode.style.backgroundColor = "green";
        document.getElementById(data[0][1].replace(/\W/g, '')).parentNode.style.backgroundColor = "red";
    }
    if (correct) {
        document.getElementById(mcq.options[mcq.ans].replace(/\W/g, '')).parentNode.style.backgroundColor = "green";
    }

    return false;
}

async function frqChecker(e, unit) {
    const formData = new FormData(e.target);
    const data = [...formData];
    console.log(data[0][1]);
    console.log(unit);
    let evaluation = await fetch(`http://localhost:5000/grade_frq`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'question': FRQ[unit], 'user_response': data[0][1]})
    });
    evaluation = await evaluation.json();
    evaluation = evaluation.response
    document.getElementById(`p${FRQ[unit].replace(/\W/g, '')}`).innerText = evaluation;

    return false;
}
// console.log(MCQ);
console.log(YT);
// console.log(MCQ['Unit 1: Foundations of American History'][0].mcq[0])

let shown = true;
</script>

<div class='flex flex-row h-full'> 
    <History></History>
    <div class='w-[calc(100vw)] bg-black/25 opacity-100 py-6 px-12'>
        {#if !loading}
            {#each Object.entries(C) as [name, unit], uidx}
                <div class='m-4 p-4 rounded-xl shadow-[0_0_32px_5px_rgba(0,0,0,0.3)]'>
                    <button type='button' class='text-center text-white opacity-87 text-left w-full text-xl' on:click={()=>{unit.expanded = !unit.expanded;}}>{name}</button>
                    <div hidden={!unit.expanded}>
                        {#each Object.entries(unit) as [sbname, subunit], sbidx}
                            {#if (sbname!=='expanded')}
                                <button type='button' class='text-white opacity-87 text-left w-full text-lg' on:click={()=>{sbexpanded[uidx][sbidx] = !sbexpanded[uidx][sbidx];}}>
                                    <svg class='h-4 w-4 inline-block' data-slot="icon" fill="none" stroke-width="1.5" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5"></path>
                                    </svg>
                                    {sbname}</button>
                                    <div hidden={!sbexpanded[uidx][sbidx]}>
                                        <p class='text-white opacity-60 text-md px-4'>{subunit}</p>
                                        {#if (YT[name][sbidx] != null)}
                                            <div class='my-4 flex flex-row justify-center items-center w-full'>
                                                <iframe title='video' width="420" height="315"
                                                    src='{YT[name][sbidx]['videos']}'>
                                                </iframe>
                                            </div>
                                            
                                            <!-- <h>{MCQ[name][sbidx].mcq[0].q}</h>
                                            <p>{JSON.stringify(MCQ[name][sbidx])}</p>
                                                <form on:submit={(e) => subunitChecker(e, MCQ['name']['sbidx'])}> 
                                                    {#each MCQ[name][sbidx].options as opt}
                                                    <div>
                                                        <input id={opt.replace(/\W/g, '')} type="radio" name={mcq.q} value="{opt}" class='z-10'>
                                                        <label for={opt.replace(/\W/g, '')}>{opt}</label>
                                                        <br>
                                                    </div>
                                                    {/each}
                                                    <input type='submit'>
                                                </form> -->
                                        {/if}
                                </div> 
                            {/if}
                        {/each}
                        <div>
                            <form class='flex flex-col justify-center items-center' on:submit={(e) => frqChecker(e, name)}>
                                <label class='text-white opacity-60 mt-2' for="{FRQ[name].replace(/\W/g, '')}">{FRQ[name]}</label>
                                <br>
                                <textarea class='text-white bg-neutral-700 my-4 w-full' id="{FRQ[name].replace(/\W/g, '')}" name='{FRQ[name]}'></textarea>
                                <br>
                                <input class='text-white bg-red-900 rounded-xl p-2' type='submit'>
                            </form>
                            <p class='text-white' id="p{FRQ[name].replace(/\W/g, '')}"></p>
                        </div>
                    </div>
                    <br>
                </div>
            {/each}
        {:else}
                <p>loading data...</p>
        {/if}
    </div>
</div>

<style>
    :global(body) {
        background-color: #2f2f2f;
    }
</style>